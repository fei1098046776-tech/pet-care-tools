import glob
import os

files = glob.glob('**/*.html', recursive=True)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Fix 1: Change Taiwan flag to China flag
    content = content.replace('🇹🇼', '🇨🇳')
    
    # Fix 2: Fix broken CSS paths in subdirectories
    # If the file is in a subdirectory (like fr/, de/, zh-TW/)
    if '/' in f or '\\' in f:
        # Replace relative css path to one level up if it's currently pointing to the same folder
        content = content.replace('href="css/style.css"', 'href="../css/style.css"')
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fixed CSS paths and updated flags!")
