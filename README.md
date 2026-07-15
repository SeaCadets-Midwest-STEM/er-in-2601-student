# ER-IN-2601 Student Companion Site

Student-facing companion website for the **Invention Lab 2026** (ER-IN-2601) Sea Cadets STEM training program.

## Quick Start

### Prerequisites

- [Hugo Extended](https://gohugo.io/installation/) (v0.130.0 or later)
- Any modern web browser

### Local Development

```bash
# Clone the repository
git clone https://github.com/SeaCadets-Midwest-STEM/er-in-2601-student.git
cd er-in-2601-student

# Start the development server
hugo server

# Open in browser
# http://localhost:1313
```

The development server auto-reloads when content or layout files change.

### Build for Production

```bash
hugo --minify
```

The compiled site will be in the `public/` directory.

## Site Structure

```
er-in-2601-student/
├── .github/workflows/
│   └── hugo.yml              # GitHub Actions: build + deploy to Pages
├── content/
│   ├── about/
│   │   └── _index.md         # About page
│   ├── resources/
│   │   └── _index.md         # Student resources page
│   └── schedule/
│       ├── _index.md          # Schedule overview
│       ├── day-01.md          # Day 1: The Translator's Spark
│       ├── day-02.md          # Day 2: Sensory Perception
│       ├── day-03.md          # Day 3: Shaping the Physical World
│       ├── day-04.md          # Day 4: The Connected Hive
│       └── day-05.md          # Day 5: The Horizon and Launch
├── layouts/
│   ├── index.html             # Home page template
│   └── _default/
│       ├── baseof.html        # Base template (header, nav, footer)
│       ├── list.html          # Section listing template
│       └── single.html        # Single page template
├── static/
│   └── css/
│       └── main.css           # All site styles
├── hugo.toml                  # Hugo configuration
└── README.md
```

## GitHub Pages Deployment

This site is automatically deployed to [GitHub Pages](https://pages.github.com/) via GitHub Actions.

- Push to `main` triggers an automatic build and deployment
- The site is published to `https://seacadets-midwest-stem.github.io/er-in-2601-student/`
- Manual deployments can be triggered from the Actions tab

### Enabling GitHub Pages (first-time setup)

1. Go to **Settings** &rarr; **Pages** in the GitHub repository
2. Under **Source**, select **GitHub Actions**
3. The workflow file (`.github/workflows/hugo.yml`) handles the rest

## Content Authoring

All content is written in Markdown. To add a new page:

1. Create a `.md` file in the appropriate `content/` subdirectory
2. Add front matter with `title`, and optionally `date` and `weight`
3. Write Markdown content below the front matter

Example:

```markdown
---
title: "My New Page"
weight: 6
---

Page content goes here in Markdown.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.