---
permalink: /blog/
title: "Blog"
excerpt: "{{ cookiecutter.project_name }}"
---

<h2> Blog posts </h2>

{% raw %}
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}
{% endraw %}
