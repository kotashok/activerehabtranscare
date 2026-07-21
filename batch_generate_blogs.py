import os
import sys
import re
import datetime
import subprocess

from blog_publisher import ARTICLES_LIBRARY, generate_standalone_html, update_sitemap, apply_internal_linking, generate_cta_box

def run_batch():
    print("============================================================")
    print("      ActiveRehab TransCare - BATCH SEO BLOG GENERATOR")
    print("============================================================")
    
    index_html_path = "index.html"
    with open(index_html_path, "r", encoding="utf-8") as f:
        index_html = f.read()
        
    for idx, article in enumerate(ARTICLES_LIBRARY):
        slug = re.sub(r'[^a-z0-9]+', '-', article["title"].lower()).strip('-')
        date_str = "Jul 21, 2026"
        print(f"\nProcessing [{idx+1}/{len(ARTICLES_LIBRARY)}]: {article['title']}")
        
        # 1. Generate standalone HTML page
        generate_standalone_html(article, date_str)
        
        # 2. Update sitemap.xml
        update_sitemap(slug)
        
        # 3. Replace <button data-article="..."> with <a href="{slug}.html"> in index.html if present
        button_pattern = re.compile(rf'<button[^>]*data-article="{re.escape(slug)}"[^>]*>Read Article</button>', re.IGNORECASE)
        new_link = f'<a href="{slug}.html" class="btn btn-secondary" style="width: 100%; margin-top: 15px; padding: 10px 20px; font-size: 0.95rem; text-align: center;">Read Article</a>'
        index_html = button_pattern.sub(new_link, index_html)

    # Save updated index.html
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("\n[OK] Updated index.html with direct <a href='...'> HTML links for all blog cards.")
    
    # Git commit & push
    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_msg = "feat(seo): generate standalone SEO HTML blog pages with H1-H3 headings, meta tags, image alts, & JSON-LD FAQs"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("\n[OK] Git changes committed and deployed live to GitHub Pages!")
    except Exception as e:
        print(f"[NOTICE] Git output: {e}")

if __name__ == "__main__":
    run_batch()
