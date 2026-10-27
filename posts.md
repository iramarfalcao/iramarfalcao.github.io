---
layout: default
lang: en
alt: /pt/posts/
title: Articles
description: Articles and notes by Iramar Falcão on software, projects and tools.
permalink: /posts/
---

# Articles

Notes on software, projects, tools and lessons from the work.

<div class="post-list">
  {% for post in site.posts %}
    <article>
      <p class="meta">{{ post.date | date: "%B %-d, %Y" }}</p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    </article>
  {% else %}
    <p>No articles yet.</p>
  {% endfor %}
</div>
