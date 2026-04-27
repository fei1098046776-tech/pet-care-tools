import os
import glob

# Read base English files
with open('dog-chocolate-toxicity-calculator.html', 'r') as f: choc_html = f.read()
with open('cat-calorie-calculator.html', 'r') as f: cal_html = f.read()
with open('dog-age-converter.html', 'r') as f: age_html = f.read()

# French translations
fr_choc = choc_html.replace('Dog Chocolate Toxicity Calculator', 'Calculatrice de Toxicité du Chocolat').replace('Did your dog eat chocolate?', 'Votre chien a-t-il mangé du chocolat?').replace('/index.html', '/fr/index.html')
fr_cal = cal_html.replace('Daily Pet Calorie Calculator', 'Calculatrice de Calories Quotidiennes').replace('Stop guessing how much to feed your pet.', 'Arrêtez de deviner combien nourrir votre animal.').replace('/index.html', '/fr/index.html')
fr_age = age_html.replace('Dog to Human Years Converter', 'Convertisseur d\'Âge de Chien').replace('Stop multiplying by 7!', 'Arrêtez de multiplier par 7!').replace('/index.html', '/fr/index.html')

# German translations
de_choc = choc_html.replace('Dog Chocolate Toxicity Calculator', 'Schokoladenvergiftungs-Rechner').replace('Did your dog eat chocolate?', 'Hat Ihr Hund Schokolade gegessen?').replace('/index.html', '/de/index.html')
de_cal = cal_html.replace('Daily Pet Calorie Calculator', 'Täglicher Kalorienrechner').replace('Stop guessing how much to feed your pet.', 'Hören Sie auf zu raten, wie viel Sie füttern sollen.').replace('/index.html', '/de/index.html')
de_age = age_html.replace('Dog to Human Years Converter', 'Hundealter in Menschenjahre').replace('Stop multiplying by 7!', 'Hören Sie auf, mit 7 zu multiplizieren!').replace('/index.html', '/de/index.html')

# Chinese translations
zh_choc = choc_html.replace('Dog Chocolate Toxicity Calculator', '狗狗巧克力中毒計算機').replace('Did your dog eat chocolate?', '狗狗誤食巧克力了嗎？').replace('/index.html', '/zh-TW/index.html')
zh_cal = cal_html.replace('Daily Pet Calorie Calculator', '寵物每日卡路里計算機').replace('Stop guessing how much to feed your pet.', '不再憑感覺餵食。精準計算所需熱量。').replace('/index.html', '/zh-TW/index.html')
zh_age = age_html.replace('Dog to Human Years Converter', '狗狗真實年齡換算器').replace('Stop multiplying by 7!', '別再乘以7了！計算真實年齡。').replace('/index.html', '/zh-TW/index.html')

# Write files
with open('fr/toxicite-chocolat.html', 'w') as f: f.write(fr_choc)
with open('fr/calories.html', 'w') as f: f.write(fr_cal)
with open('fr/age-chien.html', 'w') as f: f.write(fr_age)

with open('de/schokoladenvergiftung.html', 'w') as f: f.write(de_choc)
with open('de/kalorien.html', 'w') as f: f.write(de_cal)
with open('de/hundealter.html', 'w') as f: f.write(de_age)

with open('zh-TW/chocolate-toxicity.html', 'w') as f: f.write(zh_choc)
with open('zh-TW/calorie.html', 'w') as f: f.write(zh_cal)
with open('zh-TW/dog-age.html', 'w') as f: f.write(zh_age)

print("Generated 9 missing calculators!")
