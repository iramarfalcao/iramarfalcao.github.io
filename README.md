# iramarfalcao.github.io

[![Deploy GitHub Pages](https://github.com/iramarfalcao/iramarfalcao.github.io/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/iramarfalcao/iramarfalcao.github.io/actions/workflows/pages.yml)
![Jekyll](https://img.shields.io/badge/Jekyll-4.4.1-CC0000)
![Ruby](https://img.shields.io/badge/Ruby-3.4-CC342D)

Personal website of Iramar Falcao: portfolio, resume and posts, built with Jekyll and published on GitHub Pages at <https://iramarfalcao.github.io>.

## O que é

The source of the personal site of Iramar Falcao, software engineer and founder of Falcao SL. It is a small Jekyll site with one layout, one stylesheet and hand-written pages, in **Brazilian Portuguese and English**. Portuguese pages live at the root (`/`, `/resume/`, `/projects/`, `/posts/`) and English pages under `/en/`. Each page points to its twin with `alt:` in the front matter, which feeds the PT/EN switch and the `hreflang` tags.

## O que faz

It presents Iramar's work to recruiters, clients and anyone who lands on the Falcao SL products: who he is, what he has built, where he has worked and how to get in touch.

## Funcionalidades

- **Home** (`index.md`, `en/index.md`): hero with the Falcao SL falcon, short bio and a card for S-Clean.
- **Projects** (`projects.md`, `en/projects.md`): featured apps, apps in development (Quick Read, Lira, PocketRocket, SwipeClean, Infinity War, Hortfrut, MeuPosto) and infrastructure/services (Homelab, MyBooks), each linking to its own site.
- **Resume** (`resume.md`, `en/resume.md`): about, experience, skills, education and languages, aligned with the LinkedIn profile, plus a print / save-as-PDF button. The content lives once in `_data/resume.yml` (fields `en` and `pt`) and is rendered by `_includes/resume.html`. Products and their status live in `_data/products.yml`; interface strings in `_data/i18n.yml`.
- **Posts** (`posts.md`, `/posts/`): post list generated from `_posts/`. There is one post so far, "Welcome".
- **Feed and discovery files**: `feed.xml`, `sitemap.xml`, `robots.txt` and `llms.txt` (a plain-text description of the site for language models).
- **Brand assets**: the Falcao SL palette (graphite `#262A2F`, blue `#0096EA`), favicons, hero falcon, footer signature and social preview in `assets/brand/`, regenerated from the Falcao SL brand by `scripts/export-brand.sh`.
- **Deploy**: every push to `main` builds the site and publishes it through `.github/workflows/pages.yml`.

## Como rodar

Requires Ruby 3.4 (see `.ruby-version`) and Bundler 4.0.11 (see `Gemfile.lock`).

```bash
bundle install
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

To regenerate the icons and the social preview (macOS, needs Google Chrome and the `Falcao-SL` repository next to this one):

```bash
zsh scripts/export-brand.sh
```

## O que falta

`design-qa.md` records an open visual QA pass: compare a rendered home page against a 960x960 reference image, then tune spacing, card proportions and text scale. The Jekyll build now works locally with Homebrew Ruby 4.0.7 and Bundler 4.0.15 (the earlier block was Ruby 2.6.10). The redesign of 2026-10-14 moved the site to the Falcao SL palette and an editorial layout, so the 960x960 reference comparison no longer applies. There are no articles in Portuguese yet (the only post, "Welcome", is in English).

## Status nas lojas

Não se aplica: this is a website, not a store app.

## Mais detalhes

- Site settings (title, author, social links, permalink format) are in `_config.yml`.
- The workflow uses `actions/configure-pages`, `ruby/setup-ruby` with `bundler-cache`, `actions/upload-pages-artifact` and `actions/deploy-pages`. It also runs manually through `workflow_dispatch`.
- The repository has no LICENSE file.
