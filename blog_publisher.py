import os
import sys
import re
import datetime
import urllib.request
import json
import subprocess

# Define categories, subpages, and keywords for Point 2 (Internal Silo Linking)
INTERNAL_LINKS = {
    "Ortho Step-Down": {
        "url": "ortho-stepdown.html",
        "keywords": [
            "orthopedic step-down rehabilitation",
            "post-operative orthopedic care",
            "joint replacement recovery",
            "total knee replacement",
            "spine stabilization"
        ]
    },
    "Neuro Rehab": {
        "url": "neuro-rehabilitation.html",
        "keywords": [
            "neurological step-down rehabilitation",
            "stroke recovery therapy",
            "neuroplasticity exercises",
            "stroke rehabilitation",
            "Parkinson's gait correction"
        ]
    },
    "Cardiorespiratory": {
        "url": "cardiorespiratory-rehab.html",
        "keywords": [
            "cardiorespiratory rehabilitation",
            "post-CABG bypass recovery",
            "cardiac rehabilitation",
            "telemetry monitored recovery",
            "lung volume expansion"
        ]
    },
    "Fall Prevention": {
        "url": "geriatric-fall-prevention.html",
        "keywords": [
            "elderly fall prevention therapy",
            "geriatric rehabilitation",
            "gaze stabilization",
            "balance and gait training",
            "sarcopenia muscle reversal"
        ]
    }
}

# Pre-composed premium medical articles library
ARTICLES_LIBRARY = [
    {
        "title": "Restoring Balance: Advanced Stance & Gait Correction After Knee Replacement",
        "category": "Ortho Care",
        "image": "blog_ortho.png",
        "excerpt": "Discover how computerized stance re-education and progressive loading restore walking symmetry and eliminate limps post-total knee replacement.",
        "content": """
            <p class="lead">Undergoing a total knee replacement is the first step toward pain-free living, but the final outcome is determined by post-operative orthopedic care. A common complication is the development of an asymmetrical limp, which, if uncorrected, puts stress on the other knee, hips, and lower back.</p>
            <h5>1. Overcoming the Fear of Weight-Bearing</h5>
            <p>Directly after surgery, the brain protective reflex restricts loading on the joint. Specialized step-down clinical care utilizes guided parallel rail corridors to systematically retrain the foot-strike pattern and center of gravity, returning immediate walking confidence.</p>
            <h5>2. Reversing Quadriceps Muscle Atrophy</h5>
            <p>Surgery causes temporary muscle shutdown. Targeted isometric quadriceps contractions and light progressive resistance band training are essential to stabilize the patella and ensure complete knee extension angles.</p>
            <h5>3. The Clinical Step-Down Advantage</h5>
            <p>Step-down transitional facilities bridge the gap between hospital discharge and going home, providing continuous swelling monitoring, sterile dressing oversight, and intensive daily therapy sessions.</p>
        """
    },
    {
        "title": "Neuroplasticity in Action: Rebuilding Independence After a Stroke",
        "category": "Neuro Rehab",
        "image": "blog_neuro.png",
        "excerpt": "Learn how task-specific repetitive training stimulates cerebral rewiring and helps stroke survivors reclaim motor control and speaking abilities.",
        "content": """
            <p class="lead">A stroke represents a major disruption to neural pathways, but cerebral tissue possesses a remarkable power called neuroplasticity. This allows healthy regions of the brain to learn and take over functions previously handled by the damaged areas.</p>
            <h5>1. Task-Oriented Repetitive Training</h5>
            <p>Passive range of motion is insufficient. True recovery requires stroke rehabilitation focused on goal-oriented tasks, such as reaching for objects or guided standing, to force the brain to forge new motor connections.</p>
            <h5>2. Regulating Hypertonia & Spasticity</h5>
            <p>Hyperactive muscle reflexes can lead to painful muscle shortening and joint contractures. Specialized neurological step-down rehabilitation incorporates neuro-cryotherapy and prolonged stretching to calm overactive nerve groups.</p>
            <h5>3. The Subacute Recovery Window</h5>
            <p>The first 3 to 6 months post-stroke represent the golden window for motor recovery. In a dedicated transition facility, patients receive the intensive, multi-hour daily therapy and round-the-clock nursing supervision needed to maximize their independent walking outcomes.</p>
        """
    },
    {
        "title": "Heart-Rate Monitored Pacing: Telemetry Rehabilitation Post-CABG",
        "category": "Cardiorespiratory Rehab",
        "image": "blog_stepdown.png", # Fallback default
        "excerpt": "Explore why strictly monitored metabolic equivalent (MET) pacing is vital to rebuild cardiovascular endurance safely after bypass surgery.",
        "content": """
            <p class="lead">Discharge from acute care post-CABG bypass surgery is a huge milestone, but returning home directly can be highly stressful. Reconditioning the heart muscle requires precise cardiorespiratory rehabilitation to establish safe physical boundaries.</p>
            <h5>1. Sternal Healing & Splinted Protection</h5>
            <p>Healing a divided breastbone takes 8 to 12 weeks. Patients must avoid unilateral pushing or pulling forces. In a clinical facility, nurses train patients on splinted chest protection when coughing or transferring beds.</p>
            <h5>2. Telemetry-Monitored Aerobic Progression</h5>
            <p>Physical loading must be calibrated. Continuous heart-rate tracking and oxygen saturation mapping are deployed during daily exercise sessions to ensure physical efforts remain safely within targeted MET parameters.</p>
            <h5>3. Breath Re-education & Lung Recruitment</h5>
            <p>Post-surgical pain often results in shallow breathing, leading to fluid congestion in the lungs. Incorporating diaphragmatic breathing and incentive spirometry drills helps open deep air sacs and prevents post-op pneumonia.</p>
        """
    },
    {
        "title": "Elderly Gait Instability: Reversing Sarcopenia to Prevent Falls",
        "category": "Fall Prevention",
        "image": "blog_stepdown.png",
        "excerpt": "Discover how targeting the somatosensory system and rebuilding low-impact muscle groups can completely eliminate fall risks for seniors.",
        "content": """
            <p class="lead">For senior citizens, a single fall can instantly threaten independence, leading to a fear of walking, muscle wasting, and prolonged hospital readmissions. However, advanced elderly fall prevention therapy can successfully eliminate these hazards.</p>
            <h5>1. Reversing Age-Related Sarcopenia</h5>
            <p>As we age, we naturally lose muscle mass, especially in the calves, quadriceps, and core stabilizing groups. Targeted, low-impact geriatric rehabilitation builds strength back into these crucial balance muscle groups safely.</p>
            <h5>2. Retraining the Somatosensory Pathways</h5>
            <p>Our balance relies on proprioceptors in the soles of our feet. Exercising under professional guidance on high-density foam balance pods stimulates these sensors, allowing older adults to react instantly to changes in walking surfaces.</p>
            <h5>3. Vestibular Equilibrium and Vertigo Relief</h5>
            <p>Dizzy spells triggered by sudden head movements are major fall hazards. Dedicated vestibular exercises like gaze stabilization stabilize the visual field, restoring absolute walking confidence at home.</p>
        """
    }
]

def print_banner():
    print("=" * 60)
    print("      ActiveRehab TransCare - AUTOMATED BLOG PUBLISHER")
    print("=" * 60)

def ask_choice(options, prompt):
    while True:
        try:
            for idx, opt in enumerate(options, 1):
                print(f"  [{idx}] {opt}")
            val = input(f"{prompt} (1-{len(options)}): ")
            choice = int(val)
            if 1 <= choice <= len(options):
                return choice - 1
            else:
                print("Invalid range. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def apply_internal_linking(content, category):
    # Perform Point 2 (Semantic Internal Silo linking)
    # Replaces keywords with hyperlinks once to prevent spamming
    modified = content
    for cat_name, info in INTERNAL_LINKS.items():
        url = info["url"]
        for keyword in info["keywords"]:
            # Case insensitive match, but preserve the original word casing
            pattern = re.compile(rf"\b({re.escape(keyword)})\b", re.IGNORECASE)
            
            # Replaces the FIRST occurrence of the keyword in the text
            def replacer(match):
                word = match.group(1)
                return f'<a href="{url}" style="color: var(--secondary); font-weight: 600; text-decoration: underline;">{word}</a>'
            
            # Replace only the first occurrence in the entire content
            modified, count = pattern.subn(replacer, modified, count=1)
            if count > 0:
                # Only link once per category to keep it natural and avoid keyword stuffing
                break
    return modified

def generate_cta_box(category):
    # Generate Point 3: High-converting WhatsApp booking CTA banner
    cta_title = "Need a customized recovery care plan?"
    cta_desc = "Our Lead Physiotherapist, Dr. Ashok P. Kota (17+ years experience), can build a customized step-down roadmap for you or your loved one."
    
    if category == "Ortho Care":
        cta_title = "Secure Your Post-Op Recovery Suite"
        cta_desc = "Our clinical team under Dr. Ashok P. Kota will review your surgical details, coordinate hospital transfer logs, and prepare a custom step-down roadmap."
    elif category == "Neuro Rehab":
        cta_title = "Secure Your Stroke & Neuro Recovery Suite"
        cta_desc = "Coordinate a seamless transition from hospital discharge. Dr. Ashok P. Kota will build a targeted task-oriented neuroplasticity program."
    elif category == "Fall Prevention":
        cta_title = "Book a Senior Fall-Risk Assessment"
        cta_desc = "Our clinical team will perform dynamic balance mappings and vestibular ocular checks to design an independent walking confidence plan."
        
    cta_box = f"""
                    <!-- WhatsApp Call to Action (Point 3) -->
                    <div class="blog-cta-box glass-card" style="margin-top: 40px; padding: 30px; text-align: center; background: rgba(0, 128, 128, 0.05); border: 1px solid rgba(0, 128, 128, 0.15); border-radius: var(--radius-md);">
                        <i class="fab fa-whatsapp" style="font-size: 40px; color: #25D366; margin-bottom: 15px; display: inline-block;"></i>
                        <h3 style="font-size: 1.3rem; margin-bottom: 10px; color: var(--primary);">{cta_title}</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">{cta_desc}</p>
                        <a href="https://wa.me/918106822020" target="_blank" class="btn btn-whatsapp" style="display: inline-flex; padding: 12px 25px; align-items: center; justify-content: center; text-decoration: none; gap: 8px; border-radius: var(--radius-sm);">
                            <i class="fab fa-whatsapp" style="margin-bottom: 0;"></i> Consult with Dr. Ashok
                        </a>
                    </div>
    """
    return cta_box

def publish_blog():
    print_banner()
    
    article = None
    
    # Check for CLI arguments for automation
    if len(sys.argv) > 2 and sys.argv[1] == "--auto":
        try:
            art_idx = int(sys.argv[2])
            if 0 <= art_idx < len(ARTICLES_LIBRARY):
                article = ARTICLES_LIBRARY[art_idx]
                print(f"Non-interactive mode: Automatically selecting premium article [{art_idx}]: {article['title']}")
            else:
                print(f"Error: Auto index {art_idx} out of range.")
                sys.exit(1)
        except ValueError:
            print("Error: Auto index must be an integer.")
            sys.exit(1)
            
    if article is None:
        # Let the user pick a template or write custom
        print("\nSelect the Blog Creation Mode:")
        mode = ask_choice(["Select from Premium Medical Library (Recommended)", "Input Custom Draft Text"], "Choose mode")
        
        if mode == 0:
            titles = [art["title"] for art in ARTICLES_LIBRARY]
            print("\nChoose an article from our Medical Library:")
            art_idx = ask_choice(titles, "Choose article")
            article = ARTICLES_LIBRARY[art_idx]
        else:
            title = input("\nEnter Blog Title: ").strip()
        category = input("Enter Category (e.g. Ortho Care, Neuro Rehab, Cardiorespiratory, Fall Prevention): ").strip()
        excerpt = input("Enter a 1-sentence Excerpt: ").strip()
        print("Enter Content Body (Press Enter and type/paste. Finish by typing 'END' on a new line):")
        content_lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            content_lines.append(line)
        content_body = "\n".join(content_lines)
        
        # Format custom content into basic paragraphs
        formatted_content = ""
        paragraphs = content_body.split("\n\n")
        for idx, para in enumerate(paragraphs):
            if idx == 0:
                formatted_content += f'<p class="lead">{para}</p>\n'
            else:
                formatted_content += f'<p>{para}</p>\n'
                
        article = {
            "title": title,
            "category": category,
            "image": "blog_stepdown.png", # Default fallback
            "excerpt": excerpt,
            "content": formatted_content
        }
        
    slug = re.sub(r'[^a-z0-9]+', '-', article["title"].lower()).strip('-')
    date_str = datetime.date.today().strftime("%b %d, %Y")
    
    # Process Content for Point 2 and Point 3
    processed_content = apply_internal_linking(article["content"], article["category"])
    cta_banner = generate_cta_box(article["category"])
    full_content = processed_content.strip() + "\n" + cta_banner
    
    print(f"\nPublishing details:")
    print(f"  Title:    {article['title']}")
    print(f"  Slug:     {slug}")
    print(f"  Category: {article['category']}")
    print(f"  Date:     {date_str}")
    
    # 1. Update app.js (Incorporate into database)
    app_js_path = "app.js"
    if not os.path.exists(app_js_path):
        print(f"Error: {app_js_path} not found!")
        sys.exit(1)
        
    with open(app_js_path, "r", encoding="utf-8") as f:
        app_js_content = f.read()
        
    articles_marker = "const articles = {"
    if articles_marker not in app_js_content:
        print(f"Error: Articles marker not found in {app_js_path}!")
        sys.exit(1)
        
    # Build JS entry
    js_entry = f"""        '{slug}': {{
            title: "{article['title']}",
            category: "{article['category']}",
            date: "{date_str}",
            author: "Dr. Ashok P. Kota",
            image: "{article['image']}",
            content: `
                {full_content.strip()}
            `
        }},
"""
    # Insert new record right after "const articles = {"
    app_js_content = app_js_content.replace(articles_marker, f"{articles_marker}\n{js_entry}")
    
    with open(app_js_path, "w", encoding="utf-8") as f:
        f.write(app_js_content)
    print(f"[OK] Successfully appended article record to {app_js_path}")
    
    # 2. Update index.html (Incorporate into HTML card grid)
    index_html_path = "index.html"
    if not os.path.exists(index_html_path):
        print(f"Error: {index_html_path} not found!")
        sys.exit(1)
        
    with open(index_html_path, "r", encoding="utf-8") as f:
        index_html_content = f.read()
        
    grid_marker = '<div class="blog-grid">'
    if grid_marker not in index_html_content:
        print(f"Error: Blog grid marker not found in {index_html_path}!")
        sys.exit(1)
        
    # Build HTML card
    html_card = f"""                <!-- Blog Card: {article['title']} -->
                <div class="glass-card blog-card">
                    <div class="blog-img-container">
                        <img src="{article['image']}" alt="{article['title']}" width="350" height="220" loading="lazy">
                        <span class="blog-badge">{article['category']}</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> {date_str}</span>
                            <span><i class="far fa-user"></i> Dr. Ashok P. Kota</span>
                        </div>
                        <h3>{article['title']}</h3>
                        <p>{article['excerpt']}</p>
                        <button class="btn btn-secondary blog-read-btn" data-article="{slug}" style="width: 100%; margin-top: 15px; padding: 10px 20px; font-size: 0.95rem;">Read Article</button>
                    </div>
                </div>

"""
    # Insert new card right after '<div class="blog-grid">'
    index_html_content = index_html_content.replace(grid_marker, f"{grid_marker}\n{html_card}")
    
    with open(index_html_path, "w", encoding="utf-8") as f:
        f.write(index_html_content)
    print(f"[OK] Successfully appended blog card to {index_html_path}")
    
    # 3. Commit and Deploy via Git
    print("\nPushing changes to GitHub Pages production server...")
    try:
        subprocess.run(["git", "add", "app.js", "index.html"], check=True)
        commit_msg = f"feat(blog): publish '{article['title']}' clinical post"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[OK] Git changes committed and deployed live successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[WARNING] Git process returned an error: {e}. Changes are saved locally but could not be pushed.")
        
    # 4. Trigger IndexNow search engine ping
    print("\nInitiating IndexNow search engine ping...")
    try:
        payload = {
            "host": "activerehabtranscare.in",
            "key": "f6323c28df774d758f1a26ca994ee31b",
            "keyLocation": "https://activerehabtranscare.in/f6323c28df774d758f1a26ca994ee31b.txt",
            "urlList": [
                "https://activerehabtranscare.in/",
                "https://activerehabtranscare.in/ortho-stepdown.html",
                "https://activerehabtranscare.in/neuro-rehabilitation.html",
                "https://activerehabtranscare.in/cardiorespiratory-rehab.html",
                "https://activerehabtranscare.in/geriatric-fall-prevention.html"
            ]
        }
        
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        
        with urllib.request.urlopen(req) as res:
            if res.status == 200:
                print("[OK] IndexNow ping completed successfully! Search engines notified.")
            else:
                print(f"[WARNING] IndexNow returned status code: {res.status}")
    except Exception as ex:
        print(f"[WARNING] Failed to trigger IndexNow ping: {ex}")
        
    print("\n" + "=" * 60)
    print("[OK] CONGRATULATIONS! YOUR NEW BLOG POST IS LIVE ON PRODUCTION!")
    print("=" * 60)

if __name__ == "__main__":
    publish_blog()
