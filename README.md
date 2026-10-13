# Septian Saputra — Portfolio site

Static personal site: profile, portfolio, and CV for Septian Saputra (Product Manager & QA Automation Lead, Jakarta).

| Page | File |
|---|---|
| Profile (with particle intro and optional voice greeting) | `index.html` |
| Portfolio (selected work and PRDs) | `portfolio.html` |
| CV (web version, PDF download) | `cv.html` |
| Downloads | `assets/Septian-Saputra-CV.pdf`, `assets/Septian-Saputra-Portfolio.pdf` |

No build step and no dependencies. Fonts load from Google Fonts. Each page is a single self-contained HTML file; the profile page embeds its photo and greeting audio.

## Run locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Served by GitHub Pages from the `main` branch root (Settings → Pages). Pushing to `main` redeploys the site.
