# Lab Manual Publishing Guide

This site uses Hugo's **draft system** to control when lab manuals become visible to students. All lab manual pages are created with `draft: true` in their frontmatter, which means they will **not appear** in the published GitHub Pages site until explicitly unpublished.

## How It Works

### Draft State (Default)

Every lab manual page includes `draft: true` in its frontmatter:

```yaml
---
title: "Hello Matrix LED"
description: "Program the LED matrix display"
draft: true
---
```

When `draft: true` is set, Hugo excludes the page from all normal builds. The GitHub Pages deployment workflow runs standard `hugo` commands, so **draft pages never appear on the live site**.

### Publishing a Lab Manual

To make a lab manual visible on the live site:

1. **Remove the draft flag** from the page's frontmatter (delete the `draft: true` line or set `draft: false`)
2. **Commit and push** the change to the `main` branch
3. **GitHub Pages** will automatically rebuild and deploy within a few minutes

### Quick Publish Command

To unpublish all lab manuals for a specific day:

```bash
# Example: Publish all Day 1 lab manuals
sed -i 's/^draft: true$//' content/lab-manuals/day-01/_index.md
sed -i 's/^draft: true$//' content/lab-manuals/day-01/hello-matrix.md
sed -i 's/^draft: true$//' content/lab-manuals/day-01/button-input.md
git add content/lab-manuals/day-01/
git commit -m "Publish Day 1 lab manuals"
git push
```

On Windows (PowerShell):

```powershell
# Example: Publish all Day 1 lab manuals
(Get-Content content/lab-manuals/day-01/_index.md) | Where-Object { $_ -notmatch '^draft: true$' } | Set-Content content/lab-manuals/day-01/_index.md
(Get-Content content/lab-manuals/day-01/hello-matrix.md) | Where-Object { $_ -notmatch '^draft: true$' } | Set-Content content/lab-manuals/day-01/hello-matrix.md
(Get-Content content/lab-manuals/day-01/button-input.md) | Where-Object { $_ -notmatch '^draft: true$' } | Set-Content content/lab-manuals/day-01/button-input.md
git add content/lab-manuals/day-01/
git commit -m "Publish Day 1 lab manuals"
git push
```

## Recommended Publishing Schedule

| When | Action |
|------|--------|
| **Before event week** | All lab manuals remain `draft: true` — students cannot see them |
| **Morning of Day 1** (Jul 27) | Unpublish `day-01/` lab manuals |
| **Morning of Day 2** (Jul 28) | Unpublish `day-02/` lab manuals |
| **Morning of Day 3** (Jul 29) | Unpublish `day-03/` lab manuals |
| **Morning of Day 4** (Jul 30) | Unpublish `day-04/` lab manuals |
| **Morning of Day 5** (Jul 31) | Unpublish `day-05/` lab manuals |

## Local Testing

To preview draft content locally during development:

```bash
hugo server --buildDrafts
```

This will show you the site as it would appear with all lab manuals published. Without the `--buildDrafts` flag, `hugo server` mimics the production build and hides drafts.

## Folder Structure

```
content/lab-manuals/
├── _index.md              # Main lab manuals page (draft: true)
├── day-01/
│   ├── _index.md          # Day 1 overview (draft: true)
│   ├── hello-matrix.md    # Hello Matrix lab (draft: true)
│   └── button-input.md    # Button Input lab (draft: true)
├── day-02/
│   ├── _index.md
│   ├── light-sensor-circuit.md
│   ├── potentiometer-analog.md
│   └── hysteresis.md
├── day-03/
│   ├── _index.md
│   ├── ultrasonic-ruler.md
│   └── design-sprint.md
├── day-04/
│   ├── _index.md
│   ├── mqtt-board-to-board.md
│   └── data-collection.md
└── day-05/
    ├── _index.md
    └── capstone-integration.md
```

## Important Notes

- The lab manuals **index page** (`content/lab-manuals/_index.md`) is also set to `draft: true`. Remember to unpublish it on the morning of Day 1 so the `/lab-manuals/` section becomes accessible.
- Schedule pages (e.g., `/schedule/day-01/`) contain direct links to lab manuals. These links will simply return 404 until the lab manual is unpublished — this is expected behavior.
- If you want to hide the lab manual links from schedule pages until publishing day, you could wrap them in Hugo shortcodes or conditionally render them. However, the current simple approach (links that 404 until published) is recommended for clarity and maintainability.