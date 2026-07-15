#!/usr/bin/env python3
"""
Scan content/ for mermaid code blocks, render each to a PNG image
using @mermaid-js/mermaid-cli (mmdc), and save to static/mermaid/.

Filenames are MD5-based hashes of the mermaid source, ensuring
deterministic output: the same diagram always produces the same file.

Additionally, a JSON lookup table (data/mermaid-diagrams.json) is
written so Hugo's render hook can resolve a normalized mermaid
snippet to its pre-rendered PNG filename at build time.

Usage:
    python scripts/generate_mermaid.py [content_dir]

Defaults:
    content_dir  = content/
    output_dir   = static/mermaid/
    data_file    = data/mermaid-diagrams.json
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile


# Regex to match fenced mermaid code blocks
MERMAID_BLOCK_RE = re.compile(
    r"^```mermaid\s*$\s*\n(.*?)^\s*```$",
    re.MULTILINE | re.DOTALL,
)

# Ensure output directories exist
os.makedirs("static/mermaid", exist_ok=True)
os.makedirs("data", exist_ok=True)


def hash_content(source):
    """Return a hex digest for deterministic filenames."""
    return hashlib.md5(source.encode("utf-8")).hexdigest()


def normalize_key(source):
    """Collapse all whitespace to single spaces and strip — matches Hugo's template normalization."""
    return re.sub(r"\s+", " ", source.strip())


def render_mermaid(source, output_path):
    """Render mermaid source to a PNG using mmdc."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".mmd", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(source)
        tmp_path = tmp.name

    try:
        cmd = (
            "npx @mermaid-js/mermaid-cli "
            + f"-i {tmp_path} -o {output_path} -b white"
        )
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            print("  WARNING: mmdc failed:\n{}".format(result.stderr), file=sys.stderr)
            return False
        return True
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print("  WARNING: Could not run mmdc: {}".format(e), file=sys.stderr)
        return False
    finally:
        os.unlink(tmp_path)


def process_file(filepath, lookup):
    """Process a single markdown file. Returns count of diagrams rendered."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    count = 0
    for match in MERMAID_BLOCK_RE.finditer(content):
        mermaid_source = match.group(1).strip()
        if not mermaid_source:
            continue

        filename = "diagram-{}.png".format(hash_content(mermaid_source))
        output_path = os.path.join("static", "mermaid", filename)

        # Populate lookup table: normalized key -> PNG filename
        key = normalize_key(mermaid_source)
        if key not in lookup or not os.path.exists(
            os.path.join("static", "mermaid", lookup[key])
        ):
            lookup[key] = filename

        # Skip if the file already exists and is newer than the source markdown
        if os.path.exists(output_path):
            mtime_output = os.path.getmtime(output_path)
            mtime_source = os.path.getmtime(filepath)
            if mtime_output >= mtime_source:
                print("  (up to date) {} <- {}".format(filename, filepath))
                count += 1
                continue

        print("  Rendering {} <- {}".format(filename, filepath))
        if render_mermaid(mermaid_source, output_path):
            count += 1
        else:
            print("  FAILED to render {}".format(filename), file=sys.stderr)

    return count


def main():
    content_dir = sys.argv[1] if len(sys.argv) > 1 else "content"
    if not os.path.isdir(content_dir):
        print("Error: content directory '{}' not found.".format(content_dir), file=sys.stderr)
        sys.exit(1)

    # lookup: normalized mermaid source -> PNG filename in static/mermaid/
    lookup = {}
    total = 0

    for root, dirs, files in os.walk(content_dir):
        for filename in sorted(files):
            if not filename.endswith((".md", ".mdx")):
                continue
            filepath = os.path.join(root, filename)
            count = process_file(filepath, lookup)
            if count > 0:
                print("{}: {} diagram(s)".format(filepath, count))
            total += count

    # Write JSON lookup table for Hugo render hook
    data_file = "data/mermaid-diagrams.json"
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(lookup, f, indent=2, ensure_ascii=False)
    print("Lookup table: {} ({} entries)".format(data_file, len(lookup)))

    print("\nTotal diagrams rendered (or up to date): {}".format(total))


if __name__ == "__main__":
    main()
