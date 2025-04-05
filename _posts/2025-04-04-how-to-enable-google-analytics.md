```
---
title: "How to Enable Google Analytics Tracking in Your Greening-Deployed Site"
date: 2025-04-04
categories: how-to
---

Want to track visitors to your open-source project site or personal portfolio? Greening makes it easy to wire up **Google Analytics** — no manual editing required.

With just a few lines in your `greening.yaml` config, you can automatically include a Google Analytics tracking ID in your deployed GitHub Pages site.

## 🧠 Why This Is Useful

Traditional static site setups (Jekyll, Hugo, etc.) require you to:
- Manually edit template files or `_config.yml`
- Copy and paste Google scripts
- Hope nothing breaks in the build

**Greening skips all that.** Just provide your tracking tag, and it handles the rest.

## 📈 What You’ll Need

1. A **Google Analytics 4** property
2. The **Measurement ID** (e.g., `G-XXXXXXXXXX`)
3. A Greening project with a configured `greening.yaml`

## ✏️ Step 1: Grab Your Tracking Tag

1. Go to [Google Analytics](https://analytics.google.com/)
2. Select or create a GA4 property
3. Navigate to **Admin → Data Streams → Web**
4. Copy the **Measurement ID** (starts with `G-`)

## 📄 Step 2: Paste It into `greening.yaml`

In your project’s root directory, open or create a `greening.yaml` file and add:

```yaml
google_analytics: G-XXXXXXXXXX
```

Replace `G-XXXXXXXXXX` with your actual tag.

## 🚀 Step 3: Deploy Your Site

Run the following command to generate and publish your GitHub Pages site:

```bash
greening deploy
```

Greening will:
- Render your site using Jekyll and the Minimal Mistakes theme
- Inject your analytics tag automatically
- Push it to the `gh-pages` branch

## ✅ You’re Done!

Visit your site, and you’ll start seeing traffic data appear in your GA4 dashboard — no manual setup, no scripts to mess with.

---

Greening’s mission is to make launching, documenting, and deploying projects **fast, beautiful, and automated**. Adding analytics should never be the bottleneck.

You can follow the project or contribute on GitHub:
👉 https://github.com/chris-greening/greening

