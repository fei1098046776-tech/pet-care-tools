import glob
import re

footer_en = """<footer class="site-footer">
  <div class="container">
    <div style="margin-bottom: 20px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
      <a href="/about.html" style="color:var(--text-muted); text-decoration:none;">About Us</a>
      <a href="/privacy-policy.html" style="color:var(--text-muted); text-decoration:none;">Privacy Policy</a>
      <a href="/terms-of-service.html" style="color:var(--text-muted); text-decoration:none;">Terms of Service</a>
      <a href="/contact.html" style="color:var(--text-muted); text-decoration:none;">Contact Us</a>
    </div>
    <p>© 2026 PetCalc. Not a substitute for professional veterinary advice.</p>
  </div>
</footer>"""

files = glob.glob('**/*.html', recursive=True)

for f in files:
    # Skip files that already have the new footer (like the legal pages we just created)
    if f in ['privacy-policy.html', 'terms-of-service.html', 'about.html', 'contact.html', 'blog/index.html']:
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Inject Blog into nav
    if 'href="/blog/index.html">Blog</a>' not in content:
        content = content.replace('<div class="lang-switcher"', '<li><a href="/blog/index.html">Blog</a></li>\n        <div class="lang-switcher"')
    
    # 2. Replace the old footer
    # Using regex to match the old footer block
    content = re.sub(r'<footer class="site-footer">.*?</footer>', footer_en, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Injected Blog link and Legal Footer into all pages!")
