import glob
import re

switcher = """<div class="lang-switcher" style="margin-left: 20px; font-size: 0.9rem;">
          <a href="/" style="color:var(--text-muted);">🇺🇸 EN</a> | <a href="/es/" style="color:var(--text-muted);">🇪🇸 ES</a> | <a href="/fr/" style="color:var(--text-muted);">🇫🇷 FR</a> | <a href="/de/" style="color:var(--text-muted);">🇩🇪 DE</a> | <a href="/zh-TW/" style="color:var(--text-muted);">🇹🇼 ZH</a>
        </div>"""

files = glob.glob('**/*.html', recursive=True)
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Simple regex to replace the old lang switcher or add it if missing
    content = re.sub(r'<div class="lang-switcher".*?</div>', switcher, content, flags=re.DOTALL)
    
    with open(f, 'w') as file:
        file.write(content)
