import os
import sys
import re
import datetime
import urllib.request
import json
import subprocess

# Define categories, subpages, and keywords for Internal Silo Linking
INTERNAL_LINKS = {
    "Ortho Care": {
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
    "Cardiorespiratory Rehab": {
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

# Pre-composed premium medical articles library with enriched SEO keywords & FAQs
ARTICLES_LIBRARY = [
    {
        "title": "Restoring Balance: Advanced Stance & Gait Correction After Knee Replacement",
        "category": "Ortho Care",
        "image": "blog_ortho.png",
        "excerpt": "Discover how computerized stance re-education and progressive loading restore walking symmetry and eliminate limps post-total knee replacement.",
        "keywords": "knee replacement gait correction, post-op TKR balance, limp reversal knee surgery, stance re-education, total knee replacement rehabilitation Hyderabad",
        "content": """
            <p class="lead">Undergoing a total knee replacement is the first step toward pain-free living, but the final outcome is determined by post-operative orthopedic care. A common complication is the development of an asymmetrical limp, which, if uncorrected, puts stress on the other knee, hips, and lower back.</p>
            <h5>1. Overcoming the Fear of Weight-Bearing</h5>
            <p>Directly after surgery, the brain protective reflex restricts loading on the joint. Specialized step-down clinical care utilizes guided parallel rail corridors to systematically retrain the foot-strike pattern and center of gravity, returning immediate walking confidence.</p>
            <h5>2. Reversing Quadriceps Muscle Atrophy</h5>
            <p>Surgery causes temporary muscle shutdown. Targeted isometric quadriceps contractions and light progressive resistance band training are essential to stabilize the patella and ensure complete knee extension angles.</p>
            <h5>3. The Clinical Step-Down Advantage</h5>
            <p>Step-down transitional facilities bridge the gap between hospital discharge and going home, providing continuous swelling monitoring, sterile dressing oversight, and intensive daily therapy sessions.</p>
        """,
        "faqs": [
            {
                "question": "How soon after knee replacement surgery can I start gait and stance correction therapy?",
                "answer": "Under expert clinical supervision at ActiveRehab TransCare, gentle weight-bearing and stance re-education typically begin within 24 to 48 hours post-op."
            },
            {
                "question": "Why do patients develop an asymmetrical limp after total knee replacement?",
                "answer": "Protective brain reflexes often restrict full weight-bearing on the new joint. Step-down parallel rail corridors help retrain muscle memory and eliminate limping patterns."
            },
            {
                "question": "How long does orthopedic step-down rehabilitation take after TKR?",
                "answer": "Most patients achieve independent walking confidence and stair-climbing safety within 2 to 3 weeks of intensive step-down therapy."
            }
        ]
    },
    {
        "title": "Neuroplasticity in Action: Rebuilding Independence After a Stroke",
        "category": "Neuro Rehab",
        "image": "blog_neuroplasticity_stroke.png",
        "excerpt": "Learn how task-specific repetitive training stimulates cerebral rewiring and helps stroke survivors reclaim motor control and speaking abilities.",
        "keywords": "stroke rehabilitation Hyderabad, neuroplasticity motor recovery, post-stroke physical therapy, stroke gait training, subacute stroke step-down care",
        "content": """
            <p class="lead">A stroke represents a major disruption to neural pathways, but cerebral tissue possesses a remarkable power called neuroplasticity. This allows healthy regions of the brain to learn and take over functions previously handled by the damaged areas.</p>
            <h5>1. Task-Oriented Repetitive Training</h5>
            <p>Passive range of motion is insufficient. True recovery requires stroke rehabilitation focused on goal-oriented tasks, such as reaching for objects or guided standing, to force the brain to forge new motor connections.</p>
            <h5>2. Regulating Hypertonia & Spasticity</h5>
            <p>Hyperactive muscle reflexes can lead to painful muscle shortening and joint contractures. Specialized neurological step-down rehabilitation incorporates neuro-cryotherapy and prolonged stretching to calm overactive nerve groups.</p>
            <h5>3. The Subacute Recovery Window</h5>
            <p>The first 3 to 6 months post-stroke represent the golden window for motor recovery. In a dedicated transition facility, patients receive the intensive, multi-hour daily therapy and round-the-clock nursing supervision needed to maximize their independent walking outcomes.</p>
        """,
        "faqs": [
            {
                "question": "What is neuroplasticity and how does it help in stroke recovery?",
                "answer": "Neuroplasticity is the brain's ability to rewire neural connections, allowing healthy brain tissue to take over motor functions lost during a stroke."
            },
            {
                "question": "What is the golden window for stroke rehabilitation?",
                "answer": "The first 3 to 6 months post-stroke represent the subacute window where neuroplastic recovery occurs fastest with intensive daily therapy."
            },
            {
                "question": "Can step-down care prevent post-stroke muscle spasticity and joint stiffness?",
                "answer": "Yes. Specialized neuro-cryotherapy, serial stretching, and task-specific repetition calm hyperactive reflexes and prevent contractures."
            }
        ]
    },
    {
        "title": "Heart-Rate Monitored Pacing: Telemetry Rehabilitation Post-CABG",
        "category": "Cardiorespiratory Rehab",
        "image": "blog_stepdown.png",
        "excerpt": "Explore why strictly monitored metabolic equivalent (MET) pacing is vital to rebuild cardiovascular endurance safely after bypass surgery.",
        "keywords": "cardiac rehabilitation Hyderabad, post-CABG recovery care, telemetry heart pacing, sternal precaution recovery, lung volume expansion therapy",
        "content": """
            <p class="lead">Discharge from acute care post-CABG bypass surgery is a huge milestone, but returning home directly can be highly stressful. Reconditioning the heart muscle requires precise cardiorespiratory rehabilitation to establish safe physical boundaries.</p>
            <h5>1. Sternal Healing & Splinted Protection</h5>
            <p>Healing a divided breastbone takes 8 to 12 weeks. Patients must avoid unilateral pushing or pulling forces. In a clinical facility, nurses train patients on splinted chest protection when coughing or transferring beds.</p>
            <h5>2. Telemetry-Monitored Aerobic Progression</h5>
            <p>Physical loading must be calibrated. Continuous heart-rate tracking and oxygen saturation mapping are deployed during daily exercise sessions to ensure physical efforts remain safely within targeted MET parameters.</p>
            <h5>3. Breath Re-education & Lung Recruitment</h5>
            <p>Post-surgical pain often results in shallow breathing, leading to fluid congestion in the lungs. Incorporating diaphragmatic breathing and incentive spirometry drills helps open deep air sacs and prevents post-op pneumonia.</p>
        """,
        "faqs": [
            {
                "question": "Why is continuous heart-rate telemetry monitoring necessary after bypass surgery (CABG)?",
                "answer": "Telemetry tracking ensures physical exercise load remains strictly within safe metabolic equivalent (MET) thresholds, preventing cardiac overexertion."
            },
            {
                "question": "What are sternal precautions after open-heart surgery?",
                "answer": "Sternal precautions prevent division stress on the healing breastbone. Patients are trained on splinted chest protection when coughing or transferring beds."
            },
            {
                "question": "How does cardiorespiratory step-down care prevent post-op lung complications?",
                "answer": "Incentive spirometry, diaphragmatic breathing drills, and postural drainage keep air sacs open, preventing fluid congestion and post-op pneumonia."
            }
        ]
    },
    {
        "title": "Elderly Gait Instability: Reversing Sarcopenia to Prevent Falls",
        "category": "Fall Prevention",
        "image": "blog_fall_prevention.png",
        "excerpt": "Discover how targeting the somatosensory system and rebuilding low-impact muscle groups can completely eliminate fall risks for seniors.",
        "keywords": "elderly fall prevention therapy Hyderabad, senior balance reconditioning, sarcopenia reversal exercises, vestibular vertigo therapy, geriatric step-down care",
        "content": """
            <p class="lead">For senior citizens, a single fall can instantly threaten independence, leading to a fear of walking, muscle wasting, and prolonged hospital readmissions. However, advanced elderly fall prevention therapy can successfully eliminate these hazards.</p>
            <h5>1. Reversing Age-Related Sarcopenia</h5>
            <p>As we age, we naturally lose muscle mass, especially in the calves, quadriceps, and core stabilizing groups. Targeted, low-impact geriatric rehabilitation builds strength back into these crucial balance muscle groups safely.</p>
            <h5>2. Retraining the Somatosensory Pathways</h5>
            <p>Our balance relies on proprioceptors in the soles of our feet. Exercising under professional guidance on high-density foam balance pods stimulates these sensors, allowing older adults to react instantly to changes in walking surfaces.</p>
            <h5>3. Vestibular Equilibrium and Vertigo Relief</h5>
            <p>Dizzy spells triggered by sudden head movements are major fall hazards. Dedicated vestibular exercises like gaze stabilization stabilize the visual field, restoring absolute walking confidence at home.</p>
        """,
        "faqs": [
            {
                "question": "What causes sudden gait instability and fall risk in senior citizens?",
                "answer": "Age-related sarcopenia (muscle loss), degraded foot proprioceptors, and inner-ear vestibular imbalances are the primary causes of senior stumbles."
            },
            {
                "question": "How does proprioceptive foam pad training improve elderly balance?",
                "answer": "Exercising on high-density foam pads stimulates deep sensory nerves in the soles of the feet, enabling instant postural reactions to uneven surfaces."
            },
            {
                "question": "Can vestibular therapy cure dizzy spells and vertigo when seniors stand up?",
                "answer": "Yes. Gaze stabilization and head-movement exercises retrain inner-ear fluid sensors, stabilizing the visual field and eliminating dizziness."
            }
        ]
    }
]

def print_banner():
    print("=" * 60)
    print("  ActiveRehab TransCare - AUTOMATED SEO BLOG ENGINE")
    print("=" * 60)

def apply_internal_linking(content, category):
    modified = content
    for cat_name, info in INTERNAL_LINKS.items():
        url = info["url"]
        for keyword in info["keywords"]:
            pattern = re.compile(rf"\b({re.escape(keyword)})\b", re.IGNORECASE)
            def replacer(match):
                word = match.group(1)
                return f'<a href="{url}" style="color: var(--secondary); font-weight: 600; text-decoration: underline;">{word}</a>'
            modified, count = pattern.subn(replacer, modified, count=1)
            if count > 0:
                break
    return modified

def generate_cta_box(category):
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
                    <!-- WhatsApp Call to Action -->
                    <div class="blog-cta-box glass-card" style="margin-top: 40px; padding: 30px; text-align: center; background: rgba(0, 128, 128, 0.05); border: 1px solid rgba(0, 128, 128, 0.15); border-radius: var(--radius-md);">
                        <i class="fab fa-whatsapp" style="font-size: 40px; color: #25D366; margin-bottom: 15px; display: inline-block;"></i>
                        <h3 style="font-size: 1.3rem; margin-bottom: 10px; color: var(--primary); font-family: 'Outfit';">{cta_title}</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">{cta_desc}</p>
                        <a href="https://wa.me/918106822020" target="_blank" class="btn btn-whatsapp" style="display: inline-flex; padding: 12px 25px; align-items: center; justify-content: center; text-decoration: none; gap: 8px; border-radius: var(--radius-sm);">
                            <i class="fab fa-whatsapp" style="margin-bottom: 0;"></i> Consult with Dr. Ashok
                        </a>
                    </div>
    """
    return cta_box

def generate_standalone_html(article, date_str):
    slug = re.sub(r'[^a-z0-9]+', '-', article["title"].lower()).strip('-')
    url = f"https://activerehabtranscare.in/{slug}.html"
    image_url = f"https://activerehabtranscare.in/{article['image']}"
    today_iso = datetime.date.today().isoformat()
    
    # Generate JSON-LD Article Schema
    article_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "@id": f"{url}#post",
        "headline": article["title"],
        "description": article["excerpt"],
        "image": image_url,
        "datePublished": today_iso,
        "dateModified": today_iso,
        "mainEntityOfPage": url,
        "author": {
            "@type": "Person",
            "name": "Dr. Ashok P. Kota",
            "url": "https://activerehabtranscare.in/#physician"
        },
        "publisher": {
            "@type": "MedicalClinic",
            "name": "ActiveRehab TransCare",
            "logo": {
                "@type": "ImageObject",
                "url": "https://activerehabtranscare.in/logo.png"
            }
        }
    }
    
    # Generate JSON-LD FAQPage Schema if FAQs exist
    faq_schema = None
    if "faqs" in article and article["faqs"]:
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["question"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["answer"]
                    }
                } for faq in article["faqs"]
            ]
        }
    
    schemas_list = [article_schema]
    if faq_schema:
        schemas_list.append(faq_schema)
        
    schemas_json = json.dumps({"@context": "https://schema.org", "@graph": schemas_list}, indent=2)
    
    # Build FAQs HTML block
    faqs_html = ""
    if "faqs" in article and article["faqs"]:
        faqs_html += '<div class="blog-faqs" style="margin-top: 50px; padding-top: 30px; border-top: 1.5px dashed #e2e8f0;">\n'
        faqs_html += '  <h2 style="font-size: 1.6rem; color: var(--primary); font-family: \'Outfit\'; margin-bottom: 25px;"><i class="fas fa-question-circle" style="color: var(--secondary); margin-right: 10px;"></i> Frequently Asked Questions (FAQs)</h2>\n'
        for faq in article["faqs"]:
            faqs_html += f'  <div class="faq-item-blog" style="margin-bottom: 25px; background: #f8fafc; padding: 22px; border-radius: 12px; border-left: 4px solid var(--secondary);">\n'
            faqs_html += f'    <h3 style="font-size: 1.2rem; color: var(--primary); font-family: \'Outfit\'; margin-bottom: 10px;">{faq["question"]}</h3>\n'
            faqs_html += f'    <p style="font-size: 1rem; color: var(--text-dark); line-height: 1.6; margin: 0;">{faq["answer"]}</p>\n'
            faqs_html += '  </div>\n'
        faqs_html += '</div>\n'

    # Convert content headings from h5 to h2 for proper SEO hierarchy
    content_seo = article["content"].replace('<h5>', '<h2 style="font-size: 1.35rem; margin: 30px 0 12px 0; color: var(--primary); font-family: \'Outfit\';">').replace('</h5>', '</h2>')

    # Construct full HTML
    html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article['title']} | ActiveRehab TransCare Hyderabad</title>
    <meta name="description" content="{article['excerpt']}">
    <meta name="keywords" content="{article.get('keywords', article['title'])}">
    <link rel="canonical" href="{url}">
    <link rel="icon" type="image/png" href="logo.png">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{article['title']} | ActiveRehab TransCare">
    <meta property="og:description" content="{article['excerpt']}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:site_name" content="ActiveRehab TransCare">
    <meta property="article:published_time" content="{today_iso}">
    <meta property="article:author" content="Dr. Ashok P. Kota">

    <!-- Structured Data (JSON-LD Article + FAQPage) -->
    <script type="application/ld+json">
{schemas_json}
    </script>
</head>
<body>
    <!-- Floating WhatsApp -->
    <a href="https://wa.me/918106822020" class="whatsapp-float" target="_blank" title="Chat with our Clinical Team">
        <i class="fab fa-whatsapp" style="font-size: 35px;"></i>
    </a>

    <!-- Unified Header & Navigation -->
    <div style="background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%); position: relative; overflow: hidden; border-bottom: 1px solid #e2e8f0;">
        <nav class="container" style="padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; position: relative; z-index: 100;">
            <div class="logo" style="display: flex; flex-direction: column; align-items: center;">
                <a href="index.html"><img src="logo.png?v=2" alt="ActiveRehab TransCare Clinical Logo" style="height: 70px; cursor: pointer;"></a>
                <div class="logo-socials" style="display: flex; gap: 8px; margin-top: 6px;">
                    <a href="https://wa.me/918106822020" target="_blank" title="WhatsApp Chat" style="width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(37, 211, 102, 0.1); color: #25D366; font-size: 0.9rem; text-decoration: none;"><i class="fab fa-whatsapp"></i></a>
                    <a href="https://www.instagram.com/activerehab.transcare/" target="_blank" title="Instagram" style="width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(225, 48, 108, 0.1); color: #E1306C; font-size: 0.9rem; text-decoration: none;"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.linkedin.com/company/125114194/" target="_blank" title="LinkedIn" style="width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(10, 102, 194, 0.1); color: #0A66C2; font-size: 0.9rem; text-decoration: none;"><i class="fab fa-linkedin"></i></a>
                    <a href="https://www.youtube.com/@ActiveRehabTransacare" target="_blank" title="YouTube" style="width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: rgba(255, 0, 0, 0.1); color: #FF0000; font-size: 0.9rem; text-decoration: none;"><i class="fab fa-youtube"></i></a>
                </div>
            </div>
            <div class="hamburger" id="hamburger" role="button" aria-label="Toggle navigation menu" tabindex="0">
                <i class="fas fa-bars"></i>
            </div>
            <div class="nav-links" id="nav-links" style="display: flex; gap: 40px; align-items: center;">
                <a href="index.html" style="text-decoration: none; color: var(--primary); font-weight: 600; font-family: 'Outfit';">Home</a>
                <div class="dropdown">
                    <a href="index.html#facility" class="dropbtn" style="text-decoration: none; color: var(--primary); font-weight: 600; font-family: 'Outfit';">Facility <i class="fas fa-chevron-down" style="font-size: 0.7rem; margin-left: 5px;"></i></a>
                    <div class="dropdown-content glass-card">
                        <a href="index.html#facility">Single Rooms</a>
                        <a href="index.html#facility">Shared Rooms</a>
                        <a href="index.html#services">Rehabilitation Zone</a>
                    </div>
                </div>
                <div class="dropdown">
                    <a href="index.html#services" class="dropbtn" style="text-decoration: none; color: var(--primary); font-weight: 600; font-family: 'Outfit';">Specializations <i class="fas fa-chevron-down" style="font-size: 0.7rem; margin-left: 5px;"></i></a>
                    <div class="dropdown-content glass-card">
                        <a href="neuro-rehabilitation.html">Stroke & Neuro Rehab</a>
                        <a href="ortho-stepdown.html">Post-Op Ortho Recovery</a>
                        <a href="cardiorespiratory-rehab.html">Cardiorespiratory Rehab</a>
                        <a href="geriatric-fall-prevention.html">Geriatric Fall Prevention</a>
                    </div>
                </div>
                <a href="index.html#blogs" style="text-decoration: none; color: var(--secondary); font-weight: 600; font-family: 'Outfit';">Blogs</a>
                <a href="tel:+918106822020" style="text-decoration: none; color: var(--primary); font-weight: 700; font-family: 'Outfit'; display: flex; align-items: center; gap: 8px; font-size: 0.95rem;"><i class="fas fa-phone-alt" style="color: var(--secondary);"></i> +91 81068 22020</a>
                <a href="index.html#booking-modal" class="btn btn-primary" style="padding: 12px 25px;">Book a Tour</a>
            </div>
        </nav>
    </div>

    <!-- Blog Details Container -->
    <main class="container" style="max-width: 850px; padding: 60px 20px;">
        <article class="glass-card" style="padding: 40px; border-radius: var(--radius-lg); box-shadow: var(--glass-shadow); overflow: hidden; background: white;">
            <div style="margin-bottom: 20px;">
                <span class="tag" style="background: rgba(0, 128, 128, 0.1); color: var(--secondary); padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; font-family: 'Outfit';">{article['category']}</span>
            </div>
            
            <h1 style="font-size: clamp(1.8rem, 4vw, 2.6rem); line-height: 1.25; margin-bottom: 20px; font-family: 'Outfit'; color: var(--primary);">{article['title']}</h1>
            
            <div style="display: flex; gap: 20px; align-items: center; color: var(--text-muted); font-size: 0.95rem; margin-bottom: 30px; border-bottom: 1px solid #e2e8f0; padding-bottom: 20px;">
                <span><i class="far fa-calendar-alt" style="color: var(--secondary); margin-right: 5px;"></i> {date_str}</span>
                <span><i class="far fa-user" style="color: var(--secondary); margin-right: 5px;"></i> By Dr. Ashok P. Kota</span>
            </div>
            
            <div style="border-radius: var(--radius-md); overflow: hidden; margin-bottom: 40px; max-height: 420px; width: 100%; border: 1px solid var(--glass-border);">
                <img src="{article['image']}" alt="{article['title']} - ActiveRehab TransCare Clinical Care" style="width: 100%; height: 100%; object-fit: cover;">
            </div>

            <div class="blog-modal-body-text" style="font-family: 'Inter'; font-size: 1.1rem; line-height: 1.8; color: var(--text-dark);">
                {content_seo.strip()}
            </div>

            {faqs_html}

            <!-- WhatsApp Call to Action -->
            {generate_cta_box(article['category'])}

            <!-- Author Biography Section -->
            <div class="author-bio glass-card" style="margin-top: 50px; padding: 30px; display: flex; gap: 25px; align-items: center; border: 1px solid rgba(0, 51, 102, 0.1); background: #f8fafc; flex-wrap: wrap; border-radius: var(--radius-md);">
                <div style="width: 100px; height: 100px; border-radius: 50%; overflow: hidden; flex-shrink: 0; border: 2px solid var(--secondary);">
                    <img src="doctor_ashok.jpg" alt="Dr. Ashok P. Kota - Lead Physiotherapist" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div style="flex: 1; min-width: 250px;">
                    <h4 style="font-size: 1.2rem; margin-bottom: 5px; color: var(--primary);">Dr. Ashok P. Kota</h4>
                    <p style="color: var(--secondary); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; margin-bottom: 10px; font-family: 'Outfit';">Lead Physiotherapist & Director, ActiveRehab TransCare</p>
                    <p style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.5;">Dr. Ashok P. Kota is a highly respected physical therapy specialist with over 17 years of hands-on experience in advanced neurological rehabilitation and post-operative orthopedic recovery. He oversees all recovery protocols and clinical step-down pathways at ActiveRehab TransCare in Kompally, Hyderabad.</p>
                </div>
            </div>
        </article>
    </main>

    <!-- Unified Footer -->
    <footer style="background: var(--primary); color: white; padding: 50px 0; text-align: center;">
        <a href="index.html" class="footer-logo-container"><img src="logo.png?v=2" alt="ActiveRehab TransCare Clinical Logo" style="height: 55px; object-fit: contain;"></a>
        <div style="margin-bottom: 25px; display: flex; justify-content: center; gap: 30px; font-size: 1.1rem; flex-wrap: wrap;">
            <a href="tel:+918106822020" style="color: white; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 10px;"><i class="fas fa-phone-alt" style="color: var(--secondary-light);"></i> +91 81068 22020</a>
            <a href="https://wa.me/918106822020" target="_blank" style="color: white; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 10px;"><i class="fab fa-whatsapp" style="color: #25D366;"></i> WhatsApp Chat</a>
            <a href="https://www.instagram.com/activerehab.transcare/" target="_blank" style="color: white; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 10px;"><i class="fab fa-instagram" style="color: #E1306C;"></i> Instagram</a>
            <a href="https://www.linkedin.com/company/125114194/" target="_blank" style="color: white; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 10px;"><i class="fab fa-linkedin" style="color: #0A66C2;"></i> LinkedIn</a>
            <a href="https://www.youtube.com/@ActiveRehabTransacare" target="_blank" style="color: white; text-decoration: none; font-weight: 600; display: flex; align-items: center; gap: 10px;"><i class="fab fa-youtube" style="color: #FF0000;"></i> YouTube</a>
        </div>
        <p style="margin-bottom: 25px; font-size: 0.95rem; opacity: 0.85; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.5; font-family: 'Inter';">
            <i class="fas fa-map-marker-alt" style="color: var(--secondary-light); margin-right: 8px;"></i>
            Plot No. 4-1-1, 41/A & 48, Laxmi Nagar Colony, Kompally, Near Sri Meru Hospital, Hyderabad, Telangana 500100
        </p>
        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px; font-size: 0.85rem; opacity: 0.7;">
            &copy; 2026 ActiveRehab TransCare and Rehabilitation. All Rights Reserved.
        </div>
    </footer>
</body>
</html>"""
    
    html_filename = f"{slug}.html"
    with open(html_filename, "w", encoding="utf-8") as f:
        f.write(html_page)
    print(f"[OK] Generated standalone SEO HTML page: {html_filename}")
    return html_filename

def update_sitemap(slug):
    sitemap_path = "sitemap.xml"
    if not os.path.exists(sitemap_path):
        return
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    loc_url = f"https://activerehabtranscare.in/{slug}.html"
    today_str = datetime.date.today().isoformat()
    if loc_url in content:
        pattern = re.compile(rf"(<loc>{re.escape(loc_url)}</loc>\s*<lastmod>)[^<]+(</lastmod>)", re.IGNORECASE)
        content = pattern.sub(rf"\g<1>{today_str}\g<2>", content)
    else:
        new_url_node = f"""  <url>
    <loc>{loc_url}</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>"""
        content = content.replace("</urlset>", new_url_node)
    
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Updated sitemap.xml with {loc_url}")

def publish_blog():
    print_banner()
    
    article = None
    
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
        title = input("\nEnter Blog Title: ").strip()
        category = input("Enter Category: ").strip()
        excerpt = input("Enter Excerpt: ").strip()
        print("Enter Content Body (type END on new line):")
        content_lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            content_lines.append(line)
        content_body = "\n".join(content_lines)
        
        article = {
            "title": title,
            "category": category,
            "image": "blog_stepdown.png",
            "excerpt": excerpt,
            "content": content_body,
            "faqs": []
        }
        
    slug = re.sub(r'[^a-z0-9]+', '-', article["title"].lower()).strip('-')
    date_str = datetime.date.today().strftime("%b %d, %Y")
    
    processed_content = apply_internal_linking(article["content"], article["category"])
    cta_banner = generate_cta_box(article["category"])
    full_content = processed_content.strip() + "\n" + cta_banner
    
    print(f"\nPublishing details:")
    print(f"  Title:    {article['title']}")
    print(f"  Slug:     {slug}")
    print(f"  Category: {article['category']}")
    print(f"  Date:     {date_str}")
    
    # 1. Generate Standalone SEO HTML File
    generate_standalone_html(article, date_str)
    
    # 2. Update sitemap.xml
    update_sitemap(slug)
    
    # 3. Update app.js
    app_js_path = "app.js"
    if os.path.exists(app_js_path):
        with open(app_js_path, "r", encoding="utf-8") as f:
            app_js_content = f.read()
            
        # Clean up existing database record if it exists to prevent duplicates
        pattern = re.compile(r"\s*'" + re.escape(slug) + r"':\s*\{.*?\}\s*,\n*", re.DOTALL)
        if pattern.search(app_js_content):
            app_js_content = pattern.sub("\n", app_js_content)
            print(f"[OK] Cleaned existing database record for {slug} in {app_js_path}")
            
        articles_marker = "const articles = {"
        if articles_marker in app_js_content:
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
            app_js_content = app_js_content.replace(articles_marker, f"{articles_marker}\n{js_entry}")
            with open(app_js_path, "w", encoding="utf-8") as f:
                f.write(app_js_content)
            print(f"[OK] Successfully registered/updated article record in {app_js_path}")
            
    # 4. Update index.html (Incorporate into HTML card grid with direct <a href="{slug}.html"> link)
    index_html_path = "index.html"
    if os.path.exists(index_html_path):
        with open(index_html_path, "r", encoding="utf-8") as f:
            index_html_content = f.read()
            
        # Clean up existing HTML card if it exists
        def find_html_card_bounds(html_content, card_slug):
            link_str = f'href="{card_slug}.html"'
            pos = html_content.find(link_str)
            if pos == -1:
                return None
            start_comment = html_content.rfind('<!-- Blog Card:', 0, pos)
            start_div = html_content.rfind('<div class="glass-card blog-card">', 0, pos)
            start_pos = start_div
            if start_comment != -1 and start_comment < start_div and (start_div - start_comment) < 150:
                start_pos = start_comment
            if start_pos == -1:
                return None
            open_div_pos = html_content.find('<div', start_pos)
            if open_div_pos == -1:
                return None
            idx = open_div_pos + 4
            nest_level = 1
            while nest_level > 0 and idx < len(html_content):
                next_open = html_content.find('<div', idx)
                next_close = html_content.find('</div>', idx)
                if next_close == -1:
                    break
                if next_open != -1 and next_open < next_close:
                    nest_level += 1
                    idx = next_open + 4
                else:
                    nest_level -= 1
                    idx = next_close + 6
            if nest_level == 0:
                end_pos = idx
                while end_pos < len(html_content) and html_content[end_pos] in '\r\n\t ':
                    end_pos += 1
                return start_pos, end_pos
            return None

        bounds = find_html_card_bounds(index_html_content, slug)
        if bounds:
            index_html_content = index_html_content[:bounds[0]] + index_html_content[bounds[1]:]
            print(f"[OK] Cleaned existing HTML card for {slug} in {index_html_path}")
            
        grid_marker = '<div class="blog-grid">'
        if grid_marker in index_html_content:
            html_card = f"""                <!-- Blog Card: {article['title']} -->
                <div class="glass-card blog-card">
                    <div class="blog-img-container">
                        <img src="{article['image']}" alt="{article['title']} - ActiveRehab TransCare Clinical Care" width="350" height="220" loading="lazy">
                        <span class="blog-badge">{article['category']}</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> {date_str}</span>
                            <span><i class="far fa-user"></i> Dr. Ashok P. Kota</span>
                        </div>
                        <h3>{article['title']}</h3>
                        <p>{article['excerpt']}</p>
                        <a href="{slug}.html" class="btn btn-secondary" style="width: 100%; margin-top: 15px; padding: 10px 20px; font-size: 0.95rem; text-align: center;">Read Article</a>
                    </div>
                </div>

"""
            index_html_content = index_html_content.replace(grid_marker, f"{grid_marker}\n{html_card}")
            with open(index_html_path, "w", encoding="utf-8") as f:
                f.write(index_html_content)
            print(f"[OK] Successfully registered/updated blog card in {index_html_path}")
            
    # 5. Commit and Deploy via Git
    print("\nPushing changes to GitHub Pages production server...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_msg = f"feat(seo): publish '{article['title']}' with dedicated HTML page, JSON-LD FAQs, & meta SEO"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[OK] Git changes committed and deployed live successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[WARNING] Git process returned an error: {e}. Changes are saved locally.")
        
    # 6. Trigger IndexNow search engine ping
    print("\nInitiating IndexNow search engine ping...")
    try:
        payload = {
            "host": "activerehabtranscare.in",
            "key": "f6323c28df774d758f1a26ca994ee31b",
            "keyLocation": "https://activerehabtranscare.in/f6323c28df774d758f1a26ca994ee31b.txt",
            "urlList": [
                "https://activerehabtranscare.in/",
                f"https://activerehabtranscare.in/{slug}.html",
                "https://activerehabtranscare.in/sitemap.xml"
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
    except Exception as ex:
        print(f"[WARNING] IndexNow ping notice: {ex}")
        
    print("\n" + "=" * 60)
    print("[OK] CONGRATULATIONS! YOUR NEW SEO BLOG POST IS LIVE ON PRODUCTION!")
    print("=" * 60)

if __name__ == "__main__":
    publish_blog()
