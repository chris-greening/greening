---
layout: splash
permalink: /
title: {{ cookiecutter.project_name }}
header:
  overlay_image: /images/image.gif
  cta_label: "<i class='fa fa-download'></i> pip install {{ cookiecutter.project_slug }}"
  cta_url: "https://pypi.org/project/{{ cookiecutter.project_slug }}/"
excerpt: {{ cookiecutter.project_slug }}

feature_row:
  - image_path: images/red.PNG
    image_size: 100px
    alt: ""
    title: "Expressive and consistent syntax"
    excerpt: ""
    url: ""
    btn_label: "Learn More"
  - image_path: images/green.PNG
    alt: ""
    title: "Clear visualizations and animations"
    excerpt: ""
    url: ""
    btn_label: "Learn More"
  - image_path: images/blue.PNG
    alt: "100% free"
    title: "Completely free and open source"
    excerpt: ""
    url: "/license/"
    btn_label: "Learn More"
github:
  - excerpt: '{::nomarkdown}<iframe style="display: inline-block;" src="https://ghbtns.com/github-btn.html?user=mmistakes&repo=minimal-mistakes&type=star&count=true&size=large" frameborder="0" scrolling="0" width="160px" height="30px"></iframe> <iframe style="display: inline-block;" src="https://ghbtns.com/github-btn.html?user=mmistakes&repo=minimal-mistakes&type=fork&count=true&size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>{:/nomarkdown}'
---

{% raw %}
{% include feature_row %}
{% endraw %}

<h2> Recent Blog Posts </h2>

{% raw %}
{% for post in site.posts limit:3 %}
  {% include archive-single.html %}
{% endfor %}
{% endraw %}

[See all blog posts...]({`{` site.url `}`}{`{` site.baseurl `}`}/blog/){: .btn .btn--info}
