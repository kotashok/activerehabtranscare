import os
import sys
import json
import random
import subprocess
from exif_injector import inject_metadata

# Path to state file tracking the posting progress
STATE_FILE = "gmb_posting_state.json"

# Pre-defined high-converting clinical GMB posts
GMB_CAMPAIGNS = {
    "Day 1: Orthopedic Step-Down": {
        "title": "Computerized Gait Corridor & Limp Reversal",
        "category": "Ortho Care",
        "image_prompt": "A premium high-resolution professional photo for a healthcare GMB post. Inside a modern, spacious clinical physiotherapy room, a South Asian Indian female patient is undergoing knee joint replacement gait rehabilitation. Guided by a South Asian Indian male professional physiotherapist in a plain solid dark blue polo shirt. The patient is confidently walking inside clean parallel support rails on a gait analysis track. Bright natural light fills the space through a large clinical window. On the main clinic wall in the background, a clean, modern 3D corporate wall sign of 'ActiveRehab TransCare' (navy and saffron/orange) is professionally mounted and illuminated by warm accent lighting, forming a natural part of the clinical environment.",
        "text": """🏥 Restoring Walking Symmetry After Joint Surgery | ActiveRehab TransCare

Undergoing a total knee or hip replacement is a massive milestone—but the true success of your surgery is decided during post-operative orthopedic recovery. 

A common issue post-surgery is the protective reflex where the brain restricts full weight-bearing on the new joint. This leads to an asymmetrical limp that, if left uncorrected, places heavy stress on your back, hips, and other knee.

At ActiveRehab TransCare in Kompally, our specialized step-down clinical protocols use guided gait corridors and computerized stance re-education to:
✅ Eliminate post-surgical limping
✅ Restore full joint range of motion safely
✅ Rebuild lower-limb strength and quadriceps muscle volume
✅ Walk out on your own two feet with 100% confidence

Secure your transition care suite directly from hospital discharge. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 2: Neuroplasticity Focus": {
        "title": "Neuroplasticity in Action: Stroke Rehabilitation",
        "category": "Neuro Rehab",
        "image_prompt": "A premium high-resolution professional photo for a healthcare GMB post. Inside a bright, clinical room, a South Asian Indian stroke survivor is successfully practicing task-specific fine motor training using colored pegs on an occupational therapy board. A South Asian Indian male professional therapist in clean medical scrubs is guiding them with deep care and focus. The space is filled with warm natural light, having high ceilings. On the clinic wall in the background, a modern wood-accented clinical plaque presenting the 'ActiveRehab TransCare' logo is elegantly mounted, blending naturally into the environment.",
        "text": """🧠 Neuroplasticity in Action: Reclaiming Autonomy After a Stroke | ActiveRehab TransCare

A stroke disrupts neural pathways, but the human brain possesses a remarkable capability called neuroplasticity—allowing healthy brain areas to learn and assume control of motor functions.

Passive movements alone are not enough for a true recovery. True recovery requires task-oriented repetitive training that challenges the brain to forge new neural pathways.

Our neurological step-down program at Kompally focuses on:
✅ Repetitive, goal-driven physical tasks (reaching, grasping, standing)
✅ Expert clinical spasticity and reflex management
✅ Intensive daily rehabilitation during the crucial 3-to-6-month subacute golden window
✅ 24/7 registered nursing to manage vitals and coordinate transition care

Give your loved ones the ultimate chance at true physical restoration. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 3: Elderly Fall Prevention": {
        "title": "Elderly Stance Correction & Gait Safety",
        "category": "Fall Prevention",
        "image_prompt": "A premium high-resolution professional photo for a healthcare GMB post. A happy South Asian Indian senior adult is practicing safe balance exercises under South Asian Indian male therapist supervision. They are standing stably on a high-density clinical foam balance pad, focusing on posture. The therapist is wearing a solid dark navy polo shirt. The bright rehabilitation room features clean modern therapy equipment, soft clinical lighting, and high ceilings. On the wall in the background, a clean, modern corporate sign of 'ActiveRehab TransCare' is professionally mounted, blending naturally into the environment.",
        "text": """👵 Preventing Falls & Restoring Balance for Seniors | ActiveRehab TransCare

For older adults, a single fall can instantly threaten independence, leading to a fear of walking, muscle wasting, and hospital readmissions. Yet, advanced fall prevention therapy can successfully eliminate these hazards.

Gait instability is often caused by sarcopenia (age-related muscle loss) and degraded proprioception (the nerves in the feet that sense the ground).

At our Kompally facility, Dr. Ashok P. Kota and the team deploy specialized stance correction:
✅ Reversing sarcopenia with safe, low-impact resistance training
✅ Retraining the feet using high-density foam balance pods to restore fast reflexes
✅ Vestibular gaze stabilization exercises to eliminate dizzy spells
✅ Guided gait retraining to restore absolute walking safety

Keep your parents safe and independent in their golden years. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 4: Premium Recovery Suites": {
        "title": "Elite Inpatient Transition Suites",
        "category": "Facility",
        "image_prompt": "A premium high-resolution professional photo for a healthcare Google My Business (GMB) post. A pristine, luxury single inpatient recovery suite at ActiveRehab TransCare in Kompally. The room features a clean adjustable clinical bed, large windows with natural sunlight, warm wood-accented walls, modern air conditioning, and a clean flat-screen TV. A professional nursing call system is visible by the bedside. On the main wood-accented wall, a clean 3D corporate sign of 'ActiveRehab TransCare' is elegantly integrated into the paneling as part of the room environment.",
        "text": """🏥 Premium Recovery Suites: Hospital Comfort Meets Clinical Safety | ActiveRehab TransCare

The transition between surgery or hospital discharge and returning home is a critical period. Standard home settings often lack the sterile environment, monitoring, and round-the-clock clinical care required.

ActiveRehab TransCare offers luxury Single and Double sharing inpatient recovery suites in Kompally, Hyderabad, providing:
✅ 24/7 registered nursing support and continuous vitals tracking
✅ Intensive daily physical therapy led by Dr. Ashok P. Kota (17+ years experience)
✅ Luxury amenities (individual AC, private bathrooms, high-speed Wi-Fi)
✅ Strict clinical hygiene, sterile dressing care, and nutritious, customized recovery meals

Focus strictly on healing in a beautiful, medically-monitored sanctuary. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 5: Cardiorespiratory Rehab": {
        "title": "Heart-Rate Monitored Pacing Post-Surgery",
        "category": "Cardio Rehab",
        "image_prompt": "A premium high-resolution professional photo for a healthcare GMB post. A South Asian Indian cardiac patient is safely walking on a treadmill in a rehabilitation center under the monitoring of a South Asian Indian male physiotherapist. The patient is wearing oxygen and heart rate telemetry sensors. The therapy room is bright and clean with premium clinical design and high ceilings. On the wall behind the treadmills, a clean corporate sign reading 'ActiveRehab TransCare' is professionally mounted, appearing as a natural part of the facility environment.",
        "text": """❤️ Safe Aerobic Pacing & Cardiorespiratory Rehab Post-Surgery | ActiveRehab TransCare

Reconditioning the heart and lungs after a bypass surgery (CABG) or valve replacement requires precise clinical calibration. Pushing too hard or too quickly can be highly dangerous.

At ActiveRehab TransCare, our cardiorespiratory step-down protocols are designed to rebuild your cardiorespiratory endurance with absolute safety:
✅ Continuous telemetry-monitored vital tracking (oxygen saturation and heart rate mapping)
✅ Safe sternal protection coaching to ensure breastbone healing (8 to 12 weeks)
✅ Breath re-education and lung recruitment using incentive spirometry to prevent pneumonia
✅ Calibrated physical therapy pacing strictly aligned with metabolic equivalent (MET) goals

Rebuild your cardiovascular stamina safely under expert guidance. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 6: Dr. Ashok P. Kota Spotlight": {
        "title": "Clinical Leadership by Dr. Ashok P. Kota",
        "category": "Leadership",
        "image_prompt": "A premium professional medical portrait for Google My Business. South Asian Indian doctor Dr. Ashok P. Kota, Lead Physiotherapist and Clinical Director of ActiveRehab TransCare, is smiling warmly in a modern clinical room. He has a stethoscope around his neck and is wearing a clean doctor lab coat. In the background, there is a clean therapy room where a modern wall plaque with the official 'ActiveRehab TransCare' logo is professionally mounted as a natural part of the environment.",
        "text": """👨‍⚕️ Meet Our Director of Clinical Rehabilitation: Dr. Ashok P. Kota | ActiveRehab TransCare

True clinical healing requires experienced, evidence-based leadership. 

Our inpatient facility in Kompally is led by Lead Physiotherapist and Director **Dr. Ashok P. Kota**, who brings **17+ years of international clinical experience**:
🎓 Bachelor of Physiotherapy (BPT)
🎓 Post Graduate Diploma in Osteopathy (Canada)
🎓 Post Graduate Diploma in Chiropractic (Sweden)

By combining advanced Canadian osteopathic structural alignment and Swedish chiropractic techniques with customized physical reconditioning, Dr. Ashok P. Kota designs transition recovery pathways that get patients back on their feet faster and safer than traditional recovery.

Consult with Dr. Ashok P. Kota directly for your surgical or stroke recovery plan. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 7: Hospital-to-Home Transition": {
        "title": "Safe Hospital-to-Home Clinical Transition",
        "category": "Admissions",
        "image_prompt": "A premium welcoming shot of the ActiveRehab TransCare facility entrance. Clean, modern architectural signage with the official 'ActiveRehab TransCare' logo is professionally mounted above the glass entrance doors. Lush landscaping and a bright, inviting clinical reception area with a South Asian Indian receptionist and patients are visible through large clean glass panels, with the sign appearing as a natural part of the building exterior.",
        "text": """🏡 Seamless Hospital-to-Home Transitional Care | ActiveRehab TransCare Hyderabad

Discharge from an acute hospital is a relief—but going home directly is often overwhelming. Families are left struggling to manage surgical dressings, specialized therapy, and 24/7 vitals monitoring.

ActiveRehab TransCare bridges the gap perfectly. We manage the hard clinical details so you can focus strictly on resting and getting stronger:
✅ Coordination of hospital transfer logs & transition reports
✅ Intensive daily rehabilitation to ensure walking safety at home
✅ Telemetry monitored vitals and professional medication management
✅ Complete parent/family coaching for home navigation

Ensure a smooth, safe transition from hospital bed to home living. Click the 'Book' button below to consult with our clinical team directly on WhatsApp!"""
    },
    "Day 8: OPD General Physiotherapy": {
        "title": "Advanced Outpatient Physiotherapy Clinic Services",
        "category": "OPD Care",
        "image_prompt": "A premium high-resolution professional photo for a healthcare GMB post. Inside the modern, brightly lit ActiveRehab TransCare outpatient department (OPD) clinic in Kompally, a South Asian Indian professional male physiotherapist in a solid dark blue polo shirt is performing specialized manual osteopathic adjustments on the shoulder joint of a South Asian Indian patient. The therapy room is clean, features modern exercise machines, soft warm lighting, and high ceilings. On the wall in the background, a clean 3D corporate sign of 'ActiveRehab TransCare' (navy and saffron/orange) is professionally mounted, appearing as a natural part of the facility.",
        "text": """🏥 Complete Outpatient (OPD) Physiotherapy Services | ActiveRehab TransCare Hyderabad

Are you struggling with chronic back pain, stiff joints, sports injuries, or recovery from an accident? You don't need to be hospitalized to receive world-class, evidence-based care.

At our advanced outpatient clinic in Kompally, Lead Physiotherapist Dr. Ashok P. Kota (17+ years experience) and our specialist team provide customized OPD treatments for all major physical conditions:
✅ Orthopedic & Joint Pain (Osteoarthritis, Frozen Shoulder, Sciatica, Chronic Back/Neck Pain)
✅ Neurological Rehabilitation (Stroke Recovery, Parkinson's Balance Correction, Bell's Palsy)
✅ Sports Injury Recovery (Ligament Tears, Sprains, Muscle Strains, Post-Arthroscopy rehabilitation)
✅ Cardiorespiratory Care (Post-infectious lung expansion, chronic asthma stamina building)
✅ Pediatric & Geriatric posture correction and balance training

We combine advanced Canadian osteopathic adjustments, Swedish chiropractic techniques, and state-of-the-art clinical modalities to eliminate pain and restore full function.

📍 Walk-in or book a dedicated OPD consultation today! Click the 'Call Now' button below to schedule your appointment immediately."""
    }
}

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"current_day": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def run_campaign():
    state = load_state()
    day = state["current_day"]
    
    # Calculate list of keys
    keys = list(GMB_CAMPAIGNS.keys())
    # Rotate 1 to 7
    campaign_key = keys[(day - 1) % len(keys)]
    campaign = GMB_CAMPAIGNS[campaign_key]
    
    print("=" * 60)
    print(f"      GMB DAILY CAMPAIGN STATE MACHINE - RUNNING DAY {day}")
    print("=" * 60)
    print(f"Selected Campaign: {campaign_key}")
    print(f"Post Title:        {campaign['title']}")
    print("-" * 60)
    print("Post Text preview:")
    # Remove high-unicode characters dynamically for console preview safety on Windows
    safe_preview = campaign["text"][:350].encode('ascii', errors='ignore').decode('ascii')
    print(safe_preview + "...")
    print("-" * 60)
    print(f"Required Image Prompt:\n{campaign['image_prompt']}")
    print("=" * 60)
    
    # Save the selected campaign's prompt & text to temporary files for the AI shell to pick up and process
    with open("current_gmb_prompt.txt", "w", encoding="utf-8") as f:
        f.write(campaign["image_prompt"])
        
    with open("current_gmb_text.txt", "w", encoding="utf-8") as f:
        f.write(campaign["text"])
        
    # Advance state to next day automatically
    state["current_day"] = (day % len(keys)) + 1
    save_state(state)
    print(f"[OK] State advanced to Day {state['current_day']} for tomorrow.")

if __name__ == "__main__":
    run_campaign()
