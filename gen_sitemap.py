import glob
import os

base_url = "https://pet-care-tools.vercel.app"
files = glob.glob("**/*.html", recursive=True)

xml_urls = []
for f in files:
    # Skip drafts
    if f.startswith("drafts/"):
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

with open("sitemap.xml", "w") as f:
    f.write(sitemap)
