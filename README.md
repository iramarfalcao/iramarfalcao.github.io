# iramarfalcao.github.io

[![Deploy GitHub Pages](https://github.com/iramarfalcao/iramarfalcao.github.io/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/iramarfalcao/iramarfalcao.github.io/actions/workflows/pages.yml)
![Jekyll](https://img.shields.io/badge/Jekyll-4.4.1-CC0000)
![Ruby](https://img.shields.io/badge/Ruby-3.4-CC342D)

Personal website of Iramar Falcao: portfolio, resume and posts, built with Jekyll and published on GitHub Pages at <https://iramarfalcao.github.io>.

## O que é

The source of the personal site of Iramar Falcao, software engineer and founder of Falcao SL. It is a small Jekyll site with one layout, one stylesheet and hand-written pages. The text is mostly in Brazilian Portuguese (`lang: pt-BR`).

## O que faz

It presents Iramar's work to recruiters, clients and anyone who lands on the Falcao SL products: who he is, what he has built, where he has worked and how to get in touch.

## Funcionalidades

- **Home** (`index.md`): hero, short bio and cards for S-Clean, HyperEnv and BR Generator.
- **Projects** (`projects.md`, `/projects/`): featured apps, apps in development (Quick Read, Lira, PocketRocket, SwipeClean, Infinity War, Hortfrut, MeuPosto) and infrastructure/services (Homelab, MyBooks), each linking to its own site.
- **Resume** (`resume.md`, `/resume/`): career timeline, own products, skills, education, and a print / save-as-PDF button.
- **Posts** (`posts.md`, `/posts/`): post list generated from `_posts/`. There is one post so far, "Welcome".
- **Feed and discovery files**: `feed.xml`, `sitemap.xml`, `robots.txt` and `llms.txt` (a plain-text description of the site for language models).
- **Brand assets**: favicons and social preview in `assets/brand/`, regenerated from the Falcao SL brand by `scripts/export-brand.sh`.
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

`design-qa.md` records an open visual QA pass: compare a rendered home page against a 960x960 reference image, then tune spacing, card proportions and text scale. It was blocked on that day by the local Ruby (2.6.10) not meeting the Bundler requirement; `.ruby-version` now says 3.4, so the note may be out of date. It also asks whether the visual direction should keep the mono green reference or move to a more conventional editorial look.

## Status nas lojas

Não se aplica: this is a website, not a store app.

## Mais detalhes

- Site settings (title, author, social links, permalink format) are in `_config.yml`.
- The workflow uses `actions/configure-pages`, `ruby/setup-ruby` with `bundler-cache`, `actions/upload-pages-artifact` and `actions/deploy-pages`. It also runs manually through `workflow_dispatch`.
- The repository has no LICENSE file.
