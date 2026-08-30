---
layout: default
title: Projects
description: Apps, systems and infrastructure built by Iramar Falcao — shipped products and work in progress.
permalink: /projects/
---

# Projects

Every project below is a real repository with product documentation, a status
page and, where it applies, its own site under `falcaosl.com`.

## Shipped

<div class="card-grid">
  <article class="card">
    <p class="eyebrow">macOS · Swift / SwiftUI</p>
    <h3>S-Clean</h3>
    <p>Mac cleaner and uninstaller. A catalogue of 98 versioned rules finds cache, leftovers and forgotten installers; the scan ends in a list with full path and size, and nothing is removed without an explicit pick. Everything goes to the Trash. No network requests, no account, 15 languages, widgets and a menu bar item.</p>
    <a href="https://sclean.falcaosl.com">sclean.falcaosl.com</a>
  </article>
  <article class="card">
    <p class="eyebrow">macOS · Swift / SwiftUI · MIT</p>
    <h3>HyperEnv</h3>
    <p>Environment variable manager: one profile per environment inside each project, applied by writing a single generated file that the login shell reads. Each profile carries a risk class — production is red everywhere and the only one that asks for confirmation. Undo restores the previous value of each variable instead of just deleting it.</p>
    <a href="https://github.com/iramarfalcao/hyperenv">Source</a>
  </article>
  <article class="card">
    <p class="eyebrow">Android · iOS · Web · Flutter</p>
    <h3>BR Generator</h3>
    <p>Generator and validator for Brazilian documents used in software testing — CPF, CNPJ (numeric and the new alphanumeric format), RG, CNH and thirty more. Batch generation, export to PDF/CSV/Excel, and an explanation of which rule failed when a document is invalid. Fully offline.</p>
    <a href="https://brgenerator.falcaosl.com">brgenerator.falcaosl.com</a>
  </article>
</div>

## In progress

<div class="card-grid">
  <article class="card">
    <p class="eyebrow">Kotlin Multiplatform</p>
    <h3>Quick Read</h3>
    <p>RSVP ebook reader — one word at a time, adjustable WPM. Imports EPUB, MOBI, PDF and TXT; local-first, with an optional Appwrite account used only for sync. Android and iOS on a shared Kotlin core.</p>
  </article>
  <article class="card">
    <p class="eyebrow">Kotlin Multiplatform + Rust</p>
    <h3>Lira</h3>
    <p>English and French for Portuguese speakers: a six-step daily lesson, an adapted SM-2 spaced repetition engine, phoneme-level pronunciation feedback, and a conversational tutor that works offline and expands through the Claude API. Two Rust services back it — a metered tutor proxy and a 50k-lemma lexicon.</p>
  </article>
  <article class="card">
    <p class="eyebrow">iPadOS · Swift + MLX</p>
    <h3>MiniMLX</h3>
    <p>Quantized MLX models running on M-series iPads: resumable HuggingFace downloads, streaming chat with vision, on-device transcription and speech, and a LAN server exposing both OpenAI-compatible endpoints and the Anthropic Messages API.</p>
  </article>
  <article class="card">
    <p class="eyebrow">Rust · actix-web · HTMX</p>
    <h3>Hortfrut</h3>
    <p>Management system for fresh produce distribution: immutable CEASA price quotes, a catalogue with unit conversion, quotes that surface cost, sale price and margin per item, orders with frozen prices, and delivery checked item by item. Three portals with scoping enforced in SQL.</p>
  </article>
  <article class="card">
    <p class="eyebrow">Rust · PostGIS · KMP</p>
    <h3>MeuPosto</h3>
    <p>Crowdsourced fuel prices with proof: geospatial search, price updates that require an on-site check-in plus a photo of the price board, four anti-fraud layers, OCR of the board, and Bayesian ratings resistant to review bombing.</p>
  </article>
  <article class="card">
    <p class="eyebrow">iOS · Swift + PhotoKit</p>
    <h3>SwipeClean</h3>
    <p>Clear the camera roll by gesture — swipe to keep or discard, with duplicates grouped and a mandatory review screen before anything is actually deleted. Nothing leaves the device.</p>
  </article>
  <article class="card">
    <p class="eyebrow">Flutter</p>
    <h3>Infinity War</h3>
    <p>One-tap infinite runner-shooter: the ship moves on its own, a tap reverses it and fires, one mistake ends the run. Difficulty rises to a studied ceiling; the simulation is separated from the UI and covered by tests.</p>
  </article>
</div>

## Infrastructure

<div class="card-grid">
  <article class="card">
    <p class="eyebrow">Terraform · Ansible · Docker</p>
    <h3>Homelab</h3>
    <p>The whole environment as code: Proxmox nodes, Cloudflare DNS and Tunnel via Terraform, and Ansible playbooks for Coolify, Appwrite, MinIO, PostgreSQL and application deployment. Every app site ships from here on push to main.</p>
  </article>
  <article class="card">
    <p class="eyebrow">Rust</p>
    <h3>MyBooks</h3>
    <p>A Gutenberg mirror with a catalogue and API — the content service behind Quick Read.</p>
  </article>
</div>
