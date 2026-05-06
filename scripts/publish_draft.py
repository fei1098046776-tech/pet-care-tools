import os
import glob
import re
from datetime import datetime

base_url = "https://pet-care-tools.vercel.app"

# Find drafts
drafts = glob.glob('drafts/*.html')
if not drafts:
    print("No drafts to publish.")
    exit(0)

# Pick the first one alphabetically
drafts.sort()
draft_to_publish = drafts[0]
filename = os.path.basename(draft_to_publish)

with open(draft_to_publish, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Title
title_match = re.search(r'<title>(.*?)</title>', content)
title = title_match.group(1).replace(' - PetCalc', '') if title_match else "New Pet Care Article"

# Generate Snippet
today = datetime.now().strftime("%B %d, %Y")
snippet = f"""
    <!-- Auto Published Article -->
    <a href="{filename}" class="article-card">
      <div class="article-img">🐾</div>
      <div class="article-content">
        <div class="article-category">Pet Care</div>
        <h2 class="article-title">{title}</h2>
        <p class="article-excerpt">Discover our latest veterinary-approved guide to keeping your pets happy, healthy, and safe.</p>
        <div class="article-meta">
          <span>By PetCalc Team</span>
          <span>{today}</span>
        </div>
      </div>
    </a>
"""

# Update blog/index.html
with open('blog/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace('<div class="article-grid">', f'<div class="article-grid">\n{snippet}')

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

# Update layout to match other files (using update_layout.py logic if needed, but since the draft already has the proper footer/header, we just move it)
os.rename(draft_to_publish, f'blog/{filename}')
print(f"Successfully published {filename}")

# Update Sitemap
files = glob.glob("**/*.html", recursive=True)
xml_urls = []
for f in files:
    if f.startswith("drafts/") or f.startswith("node_modules/"):
        continue
    url_path = f.replace("index.html", "").strip("/")
    if url_path:
        url_path = "/" + url_path
    else:
        url_path = "/"
    xml_urls.append(f"  <url>\n    <loc>{base_url}{url_path}</loc>\n    <changefreq>weekly</changefreq>\n  </url>")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(xml_urls)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
print("Sitemap updated.")
