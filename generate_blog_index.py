import re

blog_items = """
    <!-- Article 1 -->
    <a href="chocolate-toxicity-guide.html" class="article-card">
      <div class="article-img">🍫🐕</div>
      <div class="article-content">
        <div class="article-category">Emergency Care</div>
        <h2 class="article-title">What To Do If Your Dog Eats Chocolate: A Step-by-Step Guide</h2>
        <p class="article-excerpt">Don't panic. Learn exactly how to assess the situation, use our toxicity calculator, and know when to rush to the emergency vet.</p>
        <div class="article-meta">
          <span>By Dr. Sarah Jenkins</span>
          <span>April 27, 2026</span>
        </div>
      </div>
    </a>

    <!-- Article 2 -->
    <a href="cat-wet-vs-dry-food.html" class="article-card">
      <div class="article-img">🥩🐈</div>
      <div class="article-content">
        <div class="article-category">Nutrition</div>
        <h2 class="article-title">The Ultimate Guide to Cat Nutrition: Wet vs Dry Food</h2>
        <p class="article-excerpt">How many calories does your indoor cat really need? We break down the wet food vs dry food debate and explain Daily Energy Requirements.</p>
        <div class="article-meta">
          <span>By PetCalc Team</span>
          <span>April 26, 2026</span>
        </div>
      </div>
    </a>
    
    <!-- Article 3 -->
    <a href="dog-aging-process.html" class="article-card">
      <div class="article-img">🐕⏳</div>
      <div class="article-content">
        <div class="article-category">Health Insights</div>
        <h2 class="article-title">How Fast Do Dogs Really Age? The Myth of the 7-Year Rule</h2>
        <p class="article-excerpt">The 1 dog year equals 7 human years rule is a myth. Learn the real science behind how fast dogs age based on their breed size.</p>
        <div class="article-meta">
          <span>By PetCalc Team</span>
          <span>April 26, 2026</span>
        </div>
      </div>
    </a>
    
    <!-- Article 4 -->
    <a href="#" class="article-card" style="opacity:0.6">
      <div class="article-img">🍎🥩</div>
      <div class="article-content">
        <div class="article-category">Diet</div>
        <h2 class="article-title">10 Human Foods That Are Completely Safe for Dogs</h2>
        <p class="article-excerpt">Not all human food is bad! Discover which fruits and vegetables make healthy, low-calorie treats for your pup.</p>
        <div class="article-meta">
          <span>Coming Soon</span>
          <span>Pending</span>
        </div>
      </div>
    </a>
    
    <!-- Article 5 -->
    <a href="#" class="article-card" style="opacity:0.6">
      <div class="article-img">🩺🐱</div>
      <div class="article-content">
        <div class="article-category">Cat Health</div>
        <h2 class="article-title">7 Subtle Signs Your Indoor Cat Might Be Sick</h2>
        <p class="article-excerpt">Cats are masters at hiding pain. Learn the subtle behavioral changes that mean it's time to visit the vet.</p>
        <div class="article-meta">
          <span>Coming Soon</span>
          <span>Pending</span>
        </div>
      </div>
    </a>
"""

with open('blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the inner content of article-grid
content = re.sub(r'<div class="article-grid">.*?</div>\n</div>', f'<div class="article-grid">{blog_items}</div>\n</div>', content, flags=re.DOTALL)

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
