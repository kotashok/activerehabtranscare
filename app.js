document.addEventListener('DOMContentLoaded', () => {

    // Smooth Scroll for Nav Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
            // Close mobile menu if open
            const navLinks = document.getElementById('nav-links');
            if (navLinks && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
            }
        });
    });

    // Hamburger Menu Logic
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('nav-links');
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                // Close other items
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                    }
                });
                // Toggle current item
                item.classList.toggle('active');
            });
        }
    });

    // Blog Article Database & Dialog Logic
    const articles = {
        'neuroplasticity-in-action-rebuilding-independence-after-a-stroke': {
            title: "Neuroplasticity in Action: Rebuilding Independence After a Stroke",
            category: "Neuro Rehab",
            date: "May 29, 2026",
            author: "Dr. Ashok P. Kota",
            image: "blog_neuroplasticity_stroke.png",
            content: `
                <p class="lead">A stroke represents a major disruption to neural pathways, but cerebral tissue possesses a remarkable power called neuroplasticity. This allows healthy regions of the brain to learn and take over functions previously handled by the damaged areas.</p>
            <h5>1. Task-Oriented Repetitive Training</h5>
            <p>Passive range of motion is insufficient. True recovery requires stroke rehabilitation focused on goal-oriented tasks, such as reaching for objects or guided standing, to force the brain to forge new motor connections.</p>
            <h5>2. Regulating Hypertonia & Spasticity</h5>
            <p>Hyperactive muscle reflexes can lead to painful muscle shortening and joint contractures. Specialized <a href="neuro-rehabilitation.html" style="color: var(--secondary); font-weight: 600; text-decoration: underline;">neurological step-down rehabilitation</a> incorporates neuro-cryotherapy and prolonged stretching to calm overactive nerve groups.</p>
            <h5>3. The Subacute Recovery Window</h5>
            <p>The first 3 to 6 months post-stroke represent the golden window for motor recovery. In a dedicated transition facility, patients receive the intensive, multi-hour daily therapy and round-the-clock nursing supervision needed to maximize their independent walking outcomes.</p>

                    <!-- WhatsApp Call to Action (Point 3) -->
                    <div class="blog-cta-box glass-card" style="margin-top: 40px; padding: 30px; text-align: center; background: rgba(0, 128, 128, 0.05); border: 1px solid rgba(0, 128, 128, 0.15); border-radius: var(--radius-md);">
                        <i class="fab fa-whatsapp" style="font-size: 40px; color: #25D366; margin-bottom: 15px; display: inline-block;"></i>
                        <h3 style="font-size: 1.3rem; margin-bottom: 10px; color: var(--primary);">Secure Your Stroke & Neuro Recovery Suite</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">Coordinate a seamless transition from hospital discharge. Dr. Ashok P. Kota will build a targeted task-oriented neuroplasticity program.</p>
                        <a href="https://wa.me/918106822020" target="_blank" class="btn btn-whatsapp" style="display: inline-flex; padding: 12px 25px; align-items: center; justify-content: center; text-decoration: none; gap: 8px; border-radius: var(--radius-sm);">
                            <i class="fab fa-whatsapp" style="margin-bottom: 0;"></i> Consult with Dr. Ashok
                        </a>
                    </div>
            `
        },

        'restoring-balance-advanced-stance-gait-correction-after-knee-replacement': {
            title: "Restoring Balance: Advanced Stance & Gait Correction After Knee Replacement",
            category: "Ortho Care",
            date: "May 25, 2026",
            author: "Dr. Ashok P. Kota",
            image: "blog_ortho.png",
            content: `
                <p class="lead">Undergoing a total knee replacement is the first step toward pain-free living, but the final outcome is determined by <a href="ortho-stepdown.html" style="color: var(--secondary); font-weight: 600; text-decoration: underline;">post-operative orthopedic care</a>. A common complication is the development of an asymmetrical limp, which, if uncorrected, puts stress on the other knee, hips, and lower back.</p>
            <h5>1. Overcoming the Fear of Weight-Bearing</h5>
            <p>Directly after surgery, the brain protective reflex restricts loading on the joint. Specialized step-down clinical care utilizes guided parallel rail corridors to systematically retrain the foot-strike pattern and center of gravity, returning immediate walking confidence.</p>
            <h5>2. Reversing Quadriceps Muscle Atrophy</h5>
            <p>Surgery causes temporary muscle shutdown. Targeted isometric quadriceps contractions and light progressive resistance band training are essential to stabilize the patella and ensure complete knee extension angles.</p>
            <h5>3. The Clinical Step-Down Advantage</h5>
            <p>Step-down transitional facilities bridge the gap between hospital discharge and going home, providing continuous swelling monitoring, sterile dressing oversight, and intensive daily therapy sessions.</p>

                    <!-- WhatsApp Call to Action (Point 3) -->
                    <div class="blog-cta-box glass-card" style="margin-top: 40px; padding: 30px; text-align: center; background: rgba(0, 128, 128, 0.05); border: 1px solid rgba(0, 128, 128, 0.15); border-radius: var(--radius-md);">
                        <i class="fab fa-whatsapp" style="font-size: 40px; color: #25D366; margin-bottom: 15px; display: inline-block;"></i>
                        <h3 style="font-size: 1.3rem; margin-bottom: 10px; color: var(--primary);">Secure Your Post-Op Recovery Suite</h3>
                        <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">Our clinical team under Dr. Ashok P. Kota will review your surgical details, coordinate hospital transfer logs, and prepare a custom step-down roadmap.</p>
                        <a href="https://wa.me/918106822020" target="_blank" class="btn btn-whatsapp" style="display: inline-flex; padding: 12px 25px; align-items: center; justify-content: center; text-decoration: none; gap: 8px; border-radius: var(--radius-sm);">
                            <i class="fab fa-whatsapp" style="margin-bottom: 0;"></i> Consult with Dr. Ashok
                        </a>
                    </div>
            `
        },

        'knee-surgery': {
            title: "5 Steps to a Safe and Speedy Recovery After Knee Surgery",
            category: "Ortho Care",
            date: "May 15, 2026",
            author: "Dr. Ashok P. Kota",
            image: "blog_knee_surgery.png",
            content: `
                <p class="lead">Undergoing Total Knee Replacement (TKR) or arthroscopic surgery is a monumental step toward pain-free mobility. However, the success of the surgery is heavily determined by what happens next—your rehabilitation phase.</p>
                <h5>1. Immediate and Gradual Mobilization</h5>
                <p>Resting too long after surgery increases the risk of joint stiffness and deep vein thrombosis (DVT). Under professional guidance, gentle knee flexion and ankle pumps should start within hours of waking up. Gradually transitioning to weight-bearing exercises ensures that the muscles surrounding the knee rebuild their strength.</p>
                <h5>2. Professional Pain Management</h5>
                <p>Adequate pain control is vital for successful rehabilitation. If you are in too much pain, you won't be able to participate effectively in physiotherapy. Our step-down clinical team monitors your medication schedules and utilizes advanced ice therapy and compression techniques to control localized inflammation.</p>
                <h5>3. Dedicated Physical Therapy</h5>
                <p>Focused exercise regimens targeting the quadriceps, hamstrings, and calves are non-negotiable. An expert physiotherapist ensures that you achieve optimal range of motion (ROM) milestones safely, avoiding compensatory gaits that can damage other joints.</p>
                <h5>4. Incision Care and Infection Prevention</h5>
                <p>Keeping the wound clean and dry is critical. In a dedicated step-down facility, trained nurses monitor the incision line 24/7 for any signs of warmth, redness, or discharge, ensuring perfect healing before staples or sutures are removed.</p>
                <h5>5. Home-Readiness and Transition Safety</h5>
                <p>Before returning home, you must learn how to navigate stairs, transfer safely from chairs to beds, and use assistive devices (walkers or canes). Step-down care acts as the perfect simulation environment, helping you build the confidence required for independent living.</p>
            `
        },
        'stroke-recovery': {
            title: "The Critical Role of Neuro Rehabilitation in Stroke Recovery",
            category: "Neuro Rehab",
            date: "May 10, 2026",
            author: "Dr. Ashok P. Kota",
            image: "blog_stroke_recovery.png",
            content: `
                <p class="lead">A stroke is a life-altering neurological event. Once a patient is medically stable and discharged from the acute care hospital, the real challenge begins: reclaiming lost functions and retraining the nervous system.</p>
                <h5>The Science of Neuroplasticity</h5>
                <p>The human brain is remarkably resilient. Through a phenomenon known as neuroplasticity, the brain can rewire itself, allowing healthy areas to take over functions previously managed by the damaged regions. However, this rewiring does not happen automatically—it requires intensive, structured, and repetitive stimulation.</p>
                <h5>Intensive Multi-Disciplinary Rehabilitation</h5>
                <p>Effective stroke recovery demands a coordinated effort:</p>
                <ul>
                    <li><strong>Physical Therapy:</strong> Focuses on gait training, balance, and strengthening weakened limbs.</li>
                    <li><strong>Occupational Therapy:</strong> Assists patients in relearning daily tasks such as eating, dressing, and bathing.</li>
                    <li><strong>Speech Therapy:</strong> Essential for overcoming aphasia (difficulty speaking) and dysphagia (difficulty swallowing).</li>
                </ul>
                <h5>The Danger of Premature Home Discharge</h5>
                <p>Returning home immediately after hospital discharge often leads to rapid stagnation. Home environments rarely afford the intensive 3-to-4 hours of daily physical therapy needed during the critical subacute recovery window. Furthermore, stroke survivors face a high risk of falls in unadapted home settings.</p>
                <h5>Elite Step-Down Rehabilitation</h5>
                <p>Our dedicated Neuro Rehabilitation suite provides stroke survivors with a safe, continuous loop of therapy, clinical monitoring, and specialized nutrition, ensuring that every patient maximizes their recovery potential in a supportive, medicalized environment.</p>
            `
        },
        'stepdown-care': {
            title: "Why Step-Down Care Bridges the Gap Between Hospital and Home",
            category: "Step-Down Care",
            date: "May 05, 2026",
            author: "Dr. Ashok P. Kota",
            image: "blog_stepdown_care.png",
            content: `
                <p class="lead">The day of hospital discharge is often met with mixed emotions. While patients and families are eager to leave the sterile environment of an acute care ward, they are frequently unprepared for the complex medical and physical care required at home.</p>
                <h5>The "Care Gap" Dilemma</h5>
                <p>Modern hospitals are designed for acute crisis management. Once a patient is medically stable, the hospital's primary goal is discharge. However, being "medically stable" does not mean a patient is "fully healed." The sudden drop in supervision—from 24/7 ICU/ward nursing to family care—can lead to severe anxiety, medication errors, and physical setbacks.</p>
                <h5>What is Step-Down Care?</h5>
                <p>Step-down or transition care facilities represent the intermediate safety net. They provide a clinical, warm environment where patients receive continuous nurse monitoring, expert physiotherapy, wound care, and medication management without the astronomical costs of a hospital room.</p>
                <h5>Benefits of Step-Down Rehabilitation:</h5>
                <ul>
                    <li><strong>Reduced Readmission Rates:</strong> Continuous medical supervision prevents minor post-op complications from escalating into emergency hospital readmissions.</li>
                    <li><strong>Accelerated Recovery:</strong> Daily, structured physiotherapy ensures patients regain strength and mobility much faster than they would resting at home.</li>
                    <li><strong>Family Peace of Mind:</strong> Families are spared the intense stress of acting as untrained medical orderlies, knowing their loved ones are in expert clinical hands.</li>
                </ul>
                <p>Transition care is the final, essential link in the modern healthcare chain, ensuring that patients don't just survive their surgeries, but thrive in their recoveries.</p>
            `
        },
        'fall-prevention': {
            title: "Preventing Silent Falls: Advanced Balance & Vestibular Therapy for Seniors",
            category: "Fall Prevention",
            date: "May 18, 2026",
            author: "Dr. Ashok P. Kota",
            image: "blog_fall_prevention.png",
            content: `
                <p class="lead">Falls among the elderly are often called the "silent epidemic." A single fall can instantly compromise an older adult's independence, leading to a fear of walking, muscle wasting, and prolonged hospitalization. However, clinical studies show that over 80% of falls are entirely preventable with targeted, advanced balance therapies.</p>
                <h5>The Triad of Senior Balance</h5>
                <p>Human balance relies on three primary systems working in harmony: the visual system (eyesight), the somatosensory system (proprioceptive feedback from ankles and feet), and the vestibular system (inner ear balance). As we age, these systems gradually degrade, leading to unstable gaits and sudden stumbles.</p>
                <h5>What is Elderly Fall Prevention Therapy (EFPT)?</h5>
                <p>ActiveRehab TransCare utilizes a specialized, multi-system clinical protocol known as EFPT. This goes far beyond standard strength exercises:</p>
                <ul>
                    <li><strong>Proprioceptive Training:</strong> Exercising on unstable surfaces (like air-filled balance domes) to retrain deep pressure receptors in the feet, helping the body detect floor changes instantly.</li>
                    <li><strong>Vestibular Rehabilitation:</strong> Dynamic head and eye movements to retrain the inner ear's fluid receptors, eliminating the common "dizzy spells" seniors experience when looking up or turning quickly.</li>
                    <li><strong>Rapid Recovery Stepping:</strong> Safe, simulated stumble drills in harness tracks that train the brain to take an immediate protective step to catch oneself rather than falling.</li>
                </ul>
                <h5>The Transitional Care Solution</h5>
                <p>When a senior is discharged from the hospital after an illness, surgery, or minor slip, their muscles are severely deconditioned, multiplying their fall risk by up to 5x. Returning directly home without specialized gait retraining is a critical hazard.</p>
                <p>Our dedicated Geriatric and Fall Prevention suite offers computerized balance mapping, daily stabilization drills, and detailed family education, providing a warm, medicalized safety net that returns your loved one home with total walking confidence.</p>
            `
        }
    };

    const modal = document.getElementById('blog-modal');
    const modalImg = document.getElementById('modal-img');
    const modalBadge = document.getElementById('modal-badge');
    const modalDate = document.getElementById('modal-date');
    const modalAuthor = document.getElementById('modal-author');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    const modalClose = document.querySelector('.blog-modal-close');
    const modalOverlay = document.querySelector('.blog-modal-overlay');

    if (modal) {
        document.querySelectorAll('.blog-read-btn').forEach(button => {
            button.addEventListener('click', () => {
                const articleId = button.getAttribute('data-article');
                const article = articles[articleId];
                if (article) {
                    modalImg.src = article.image;
                    modalImg.alt = article.title;
                    modalBadge.textContent = article.category;
                    modalDate.innerHTML = `<i class="far fa-calendar-alt"></i> ${article.date}`;
                    modalAuthor.innerHTML = `<i class="far fa-user"></i> ${article.author}`;
                    modalTitle.textContent = article.title;
                    modalBody.innerHTML = article.content;

                    modal.classList.add('active');
                    document.body.classList.add('modal-open');
                }
            });
        });

        const closeModal = () => {
            modal.classList.remove('active');
            document.body.classList.remove('modal-open');
        };

        if (modalClose) modalClose.addEventListener('click', closeModal);
        if (modalOverlay) modalOverlay.addEventListener('click', closeModal);
        
        // Escape key to close modal
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modal.classList.contains('active')) {
                closeModal();
            }
        });
    }

    // Specialization Pathway Database & Dialog Logic
    const pathways = {
        'ortho': {
            title: "Ortho Step-Down Care",
            icon: "fa-bone",
            subtitle: "Comprehensive post-operative rehabilitation protocols designed for joint replacement and spinal surgeries.",
            timeline: `
                <div class="timeline-item" style="margin-bottom: 20px; border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Days 1 - 3: Immediate Post-Op</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Focus on safe bed-to-chair transfers, localized swelling management via motorized compression/cryotherapy, and gentle passive range of motion.</p>
                </div>
                <div class="timeline-item" style="margin-bottom: 20px; border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Days 4 - 10: Early Weight-Bearing</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Guided ambulation with walkers, active-assisted range of motion target drills, and progressive quadriceps/hamstrings isometrics to combat postoperative atrophy.</p>
                </div>
                <div class="timeline-item" style="border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Weeks 2 - 4: Mobility Mastery</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Complete independence in functional transfers, light resistance band exercises, and navigating household stairs safely under expert supervision.</p>
                </div>
            `,
            protocols: `
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Continuous Passive Motion (CPM)</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Utilizing automated mechanical knee flexion devices to systematically restore flex angles without active muscular strain or risk of adhesion.</p>
                </div>
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Gait Retraining & Balance</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Proprietary weight-shifting techniques and stance corrections to quickly reverse postoperative limps and safeguard contralateral joints.</p>
                </div>
                <div>
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Incision Line Protection</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Sterile medical dressing protocols and 24/7 nursing oversight to monitor suture integrity, warmth, and eliminate infection risks completely.</p>
                </div>
            `,
            equipment: `
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Advanced Cryotherapy Systems</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Controlled cold compression machines that cycle iced water through custom joint sleeves, drastically reducing post-surgical swelling and pain.</p>
                </div>
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Parallel Rails & Stance Corridors</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Double-sided rehabilitation support structures dedicated to post-operative posture correction, guided steps, and slip-free balance training.</p>
                </div>
                <div>
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">High-Density Standing Pads</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Specialized foam balance pods that challenge deep stability muscles and ankle joints, speeding up proprioceptive recovery.</p>
                </div>
            `
        },
        'neuro': {
            title: "Neuro Rehabilitation",
            icon: "fa-brain",
            subtitle: "Intensive neuroplasticity and motor recovery protocols for Stroke, Parkinson’s, and spinal injuries.",
            timeline: `
                <div class="timeline-item" style="margin-bottom: 20px; border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Week 1: Neural Stimulation</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Passive range of motion to prevent contractures, sensory stimulation of affected limbs, and critical speech/swallowing clinical evaluations.</p>
                </div>
                <div class="timeline-item" style="margin-bottom: 20px; border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Weeks 2 - 4: Motor Re-patterning</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">High-repetition bilateral coordination exercises, task-oriented gait training utilizing harness supports, and fine motor occupational therapies.</p>
                </div>
                <div class="timeline-item" style="border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Month 2+: Advanced Functional Reintegration</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Comprehensive Activities of Daily Living (ADLs) retraining (cooking, transfers, bathing), gait endurance builds, and neurological cognitive coaching.</p>
                </div>
            `,
            protocols: `
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Constraint-Induced Movement Therapy (CIMT)</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Restricting the unaffected limb to actively stimulate and retrain paretic pathways, leveraging the brain's neuroplastic potential.</p>
                </div>
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Speech & Dysphagia Therapy</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Targeted exercises for facial muscles and throat coordination to address speech clarity, aphasia, and critical swallowing mechanics.</p>
                </div>
                <div>
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Neurological Spasticity Management</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Combining therapeutic thermotherapy, deep passive stretching, and strategic clinical splinting to reduce tone and alleviate painful contractures.</p>
                </div>
            `,
            equipment: `
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Body-Weight Supported Harnesses</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Suspended pneumatic gait training systems that carry up to 60% of body weight, allowing stroke survivors to walk safely without fear of falls.</p>
                </div>
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Functional Electrical Stimulation (FES)</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Precision electrodes that deliver synchronized micro-currents to stimulate foot-drop muscles or paretic fingers during active movements.</p>
                </div>
                <div>
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Therapeutic Neuro-Benches</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Extra-wide, padded clinical platforms designed for safe rolling, trunk stability training, and sitting balance exercises.</p>
                </div>
            `
        },
        'geriatric': {
            title: "Geriatric & Fall Prevention Care",
            icon: "fa-user-clock",
            subtitle: "Advanced elder-focused stabilization protocols, computerized balance retraining, and home-safety prep to completely eliminate fall risks.",
            timeline: `
                <div class="timeline-item" style="margin-bottom: 20px; border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Days 1 - 5: Clinical Gait & Balance Battery</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Comprehensive physical assessment using clinical standards (Berg Balance Scale, Timed Up and Go, Dynamic Gait Index) alongside a detailed medical screening for visual or proprioceptive impairment.</p>
                </div>
                <div class="timeline-item" style="margin-bottom: 20px; border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Days 6 - 14: Active Balance & Vestibular Therapy</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Initiating Elderly Fall Prevention Therapy (EFPT). Focuses on computerized proprioceptive reconditioning, active stance recovery drills, and targeted vestibular exercises to eliminate dizziness during head movements.</p>
                </div>
                <div class="timeline-item" style="border-left: 3px solid var(--secondary); padding-left: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Weeks 3 - 4: Real-World Hazard Simulation & Safety Mastery</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Simulated walking on uneven surfaces, navigating dark paths, and dynamic obstacle avoidance. Includes a full clinical checklist for home environmental safety and family transfer training.</p>
                </div>
            `,
            protocols: `
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Elderly Fall Prevention Therapy (EFPT)</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Our primary evidence-based stabilization framework focusing on ankle/hip strategies, protective stepping techniques, and rapid center-of-gravity weight transfers under load.</p>
                </div>
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Gaze & Vestibular Stabilization</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Scientific gaze-stabilization drills (VOR x1 and VOR x2 exercises) that recalibrate head-eye coordination, helping seniors maintain sharp balance while turning or scanning the environment.</p>
                </div>
                <div>
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Sarcopenia & Posture Reversal</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Low-impact, high-yield progressive resistance drills targeting the gluteus medius, core, and ankle dorsiflexors—the key muscles responsible for catching oneself during a stumble.</p>
                </div>
            `,
            equipment: `
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Computerized Balance Testing (Biodex)</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Cutting-edge sensory-motor evaluation systems that measure limits of stability and body sway, providing detailed visual feedback and objective progress charts.</p>
                </div>
                <div style="margin-bottom: 20px;">
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Double-Guided Fall-Safe Corridors</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">Ultra-secure walking channels equipped with padded safety handrails and support harnesses, allowing patients to confidently practice challenging walking drills without any risk of a fall.</p>
                </div>
                <div>
                    <h5 style="color: var(--primary); font-size: 1.1rem; margin-bottom: 5px; font-weight: 700; font-family: 'Outfit';">Simulated Environmental Obstacle Track</h5>
                    <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.5;">A specialized indoor track with modular sections recreating home thresholds, low-pile rugs, ramp transitions, and varying textures (tiles, grass, foam) to build real-world confidence.</p>
                </div>
            `
        }
    };

    const pModal = document.getElementById('pathway-modal');
    const pTitle = document.getElementById('pathway-title');
    const pSubtitle = document.getElementById('pathway-subtitle');
    const pIcon = document.getElementById('pathway-icon');
    const tabTimeline = document.getElementById('tab-timeline');
    const tabProtocols = document.getElementById('tab-protocols');
    const tabEquipment = document.getElementById('tab-equipment');
    
    if (pModal) {
        document.querySelectorAll('.pathway-card').forEach(card => {
            card.addEventListener('click', () => {
                const pathwayId = card.getAttribute('data-pathway');
                const pathway = pathways[pathwayId];
                if (pathway) {
                    // Populate Details
                    pTitle.textContent = pathway.title;
                    pSubtitle.textContent = pathway.subtitle;
                    pIcon.className = `fas ${pathway.icon}`;
                    
                    // Populate Tab Contents
                    tabTimeline.innerHTML = pathway.timeline;
                    tabProtocols.innerHTML = pathway.protocols;
                    tabEquipment.innerHTML = pathway.equipment;
                    
                    // Reset to first tab (Timeline)
                    switchPathwayTab('timeline');
                    
                    pModal.classList.add('active');
                    document.body.classList.add('modal-open');
                }
            });
        });

        const closePathwayModal = () => {
            pModal.classList.remove('active');
            document.body.classList.remove('modal-open');
        };

        const pClose = pModal.querySelector('.pathway-modal-close');
        const pOverlay = pModal.querySelector('.pathway-modal-overlay');

        if (pClose) pClose.addEventListener('click', closePathwayModal);
        if (pOverlay) pOverlay.addEventListener('click', closePathwayModal);

        // Escape key lock
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && pModal.classList.contains('active')) {
                closePathwayModal();
            }
        });

        // Tab Clicking
        const tabBtns = pModal.querySelectorAll('.pathway-tab-btn');
        tabBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation(); // Avoid event bubble conflicts
                const tabName = btn.getAttribute('data-tab');
                switchPathwayTab(tabName);
            });
        });

        function switchPathwayTab(tabName) {
            // Update Tab Button styles
            tabBtns.forEach(btn => {
                if (btn.getAttribute('data-tab') === tabName) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });

            // Update Tab Contents
            const contents = {
                'timeline': tabTimeline,
                'protocols': tabProtocols,
                'equipment': tabEquipment
            };

            Object.keys(contents).forEach(key => {
                if (key === tabName) {
                    contents[key].style.display = 'block';
                    contents[key].classList.add('active-content');
                } else {
                    contents[key].style.display = 'none';
                    contents[key].classList.remove('active-content');
                }
            });
        }
    }

    // Simple Scroll Animation Observer
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    document.querySelectorAll('.glass-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
        observer.observe(card);
    });

    // --- Patient Pre-Screening & Tour Booking Intake Modal Logic ---
    const bookingModal = document.getElementById('booking-modal');
    const bookingForm = document.getElementById('booking-form');
    const bookingSteps = document.querySelectorAll('.booking-step');
    const progressSteps = document.querySelectorAll('.progress-step');
    const progressLineActive = document.getElementById('booking-progress-line');
    
    // Form navigation buttons
    const bookingBackBtn = document.getElementById('booking-back-btn');
    const bookingNextBtn = document.getElementById('booking-next-btn');
    const bookingSubmitBtn = document.getElementById('booking-submit-btn');
    
    // Trigger buttons
    const navBookBtn = document.getElementById('nav-book-btn');
    const heroContactBtn = document.getElementById('hero-contact-btn');
    const bookingCloseBtn = bookingModal ? bookingModal.querySelector('.booking-modal-close') : null;
    const bookingOverlay = bookingModal ? bookingModal.querySelector('.booking-modal-overlay') : null;
    
    let currentStep = 1;
    
    if (bookingModal && bookingForm) {
        // Open Modal function
        const openBookingModal = (e) => {
            if (e) e.preventDefault();
            bookingModal.classList.add('active');
            document.body.classList.add('modal-open');
            currentStep = 1;
            showStep(currentStep);
            clearValidationErrors();
        };
        
        // Close Modal function
        const closeBookingModal = () => {
            bookingModal.classList.remove('active');
            document.body.classList.remove('modal-open');
            bookingForm.reset();
            // Reset option buttons to defaults
            resetOptionButtons();
        };
        
        // Wire triggers
        if (navBookBtn) navBookBtn.addEventListener('click', openBookingModal);
        if (heroContactBtn) heroContactBtn.addEventListener('click', openBookingModal);
        
        
        // Partner with Us button now links directly to referrals.html, no modal interception needed
        
        
        if (bookingCloseBtn) bookingCloseBtn.addEventListener('click', closeBookingModal);
        if (bookingOverlay) bookingOverlay.addEventListener('click', closeBookingModal);
        
        // Escape key to close
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && bookingModal.classList.contains('active')) {
                closeBookingModal();
            }
        });
        
        // Form Option Buttons interactive logic
        const optionButtons = bookingForm.querySelectorAll('.form-option-btn');
        optionButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const field = btn.getAttribute('data-field');
                const value = btn.getAttribute('data-value');
                
                // Unselect others under the same field
                bookingForm.querySelectorAll(`.form-option-btn[data-field="${field}"]`).forEach(sibling => {
                    sibling.classList.remove('active-option');
                });
                
                // Select clicked button
                btn.classList.add('active-option');
                
                // Sync with hidden input
                const hiddenInput = document.getElementById(`book-${field}`);
                if (hiddenInput) {
                    hiddenInput.value = value;
                }
            });
        });
        
        // Show specific step
        function showStep(step) {
            // Toggle step visibility
            bookingSteps.forEach((stepEl, idx) => {
                if (idx + 1 === step) {
                    stepEl.classList.add('active-step');
                } else {
                    stepEl.classList.remove('active-step');
                }
            });
            
            // Update progress bar step numbers and labels
            progressSteps.forEach((stepEl, idx) => {
                const stepNum = idx + 1;
                stepEl.classList.remove('active', 'completed');
                
                if (stepNum === step) {
                    stepEl.classList.add('active');
                } else if (stepNum < step) {
                    stepEl.classList.add('completed');
                }
            });
            
            // Update active progress line width
            if (progressLineActive) {
                const widthPercent = ((step - 1) / (progressSteps.length - 1)) * 100;
                progressLineActive.style.width = `${widthPercent}%`;
            }
            
            // Update navigation buttons
            if (step === 1) {
                if (bookingBackBtn) bookingBackBtn.style.display = 'none';
                if (bookingNextBtn) bookingNextBtn.style.display = 'block';
                if (bookingSubmitBtn) bookingSubmitBtn.style.display = 'none';
            } else if (step === 2) {
                if (bookingBackBtn) bookingBackBtn.style.display = 'block';
                if (bookingNextBtn) bookingNextBtn.style.display = 'block';
                if (bookingSubmitBtn) bookingSubmitBtn.style.display = 'none';
            } else if (step === 3) {
                if (bookingBackBtn) bookingBackBtn.style.display = 'block';
                if (bookingNextBtn) bookingNextBtn.style.display = 'none';
                if (bookingSubmitBtn) bookingSubmitBtn.style.display = 'flex';
            }
        }
        
        // Reset custom option buttons to HTML default selections
        function resetOptionButtons() {
            // Define active values for resetting
            const defaults = {
                relation: 'Self',
                diagnosis: 'Geriatric & Fall Prevention',
                mobility: 'Bedridden / Needs Max Assistance',
                room: 'Single Sharing Suite'
            };
            
            optionButtons.forEach(btn => {
                const field = btn.getAttribute('data-field');
                const value = btn.getAttribute('data-value');
                
                if (defaults[field] === value) {
                    btn.classList.add('active-option');
                } else {
                    btn.classList.remove('active-option');
                }
            });
            
            // Reset hidden inputs
            Object.keys(defaults).forEach(field => {
                const hiddenInput = document.getElementById(`book-${field}`);
                if (hiddenInput) hiddenInput.value = defaults[field];
            });
        }
        
        // Live validation helpers
        const nameInput = document.getElementById('book-name');
        const phoneInput = document.getElementById('book-phone');
        const dateInput = document.getElementById('book-date');
        
        [nameInput, phoneInput, dateInput].forEach(input => {
            if (input) {
                input.addEventListener('input', () => {
                    removeError(input);
                });
            }
        });
        
        function showError(input, message) {
            removeError(input);
            input.classList.add('input-error');
            
            const errorEl = document.createElement('span');
            errorEl.className = 'error-message';
            errorEl.textContent = message;
            input.parentNode.appendChild(errorEl);
        }
        
        function removeError(input) {
            input.classList.remove('input-error');
            const parent = input.parentNode;
            const errorEl = parent.querySelector('.error-message');
            if (errorEl) {
                parent.removeChild(errorEl);
            }
        }
        
        function clearValidationErrors() {
            [nameInput, phoneInput, dateInput].forEach(input => {
                if (input) removeError(input);
            });
        }
        
        // Validate current step before proceeding
        function validateStep(step) {
            let isValid = true;
            
            if (step === 1) {
                // Validate Name
                if (!nameInput.value.trim()) {
                    showError(nameInput, 'Full Name is required.');
                    isValid = false;
                } else if (nameInput.value.trim().length < 3) {
                    showError(nameInput, 'Please enter a name with at least 3 characters.');
                    isValid = false;
                } else {
                    removeError(nameInput);
                }
                
                // Validate Phone
                const phoneVal = phoneInput.value.trim();
                const phonePattern = /^\+?(91)?\s*?[6-9]\d{9}$/; // Validates Indian phone numbers with optional country code
                if (!phoneVal) {
                    showError(phoneInput, 'Phone Number is required.');
                    isValid = false;
                } else if (!phonePattern.test(phoneVal.replace(/[\s-]/g, ''))) {
                    showError(phoneInput, 'Please enter a valid 10-digit mobile number.');
                    isValid = false;
                } else {
                    removeError(phoneInput);
                }
            } else if (step === 3) {
                // Validate Date
                if (!dateInput.value) {
                    showError(dateInput, 'Transition Date is required.');
                    isValid = false;
                } else {
                    const selectedDate = new Date(dateInput.value);
                    const today = new Date();
                    today.setHours(0, 0, 0, 0); // ignore time portion
                    
                    if (selectedDate < today) {
                        showError(dateInput, 'Date cannot be in the past.');
                        isValid = false;
                    } else {
                        removeError(dateInput);
                    }
                }
            }
            
            return isValid;
        }
        
        // Wire back button
        if (bookingBackBtn) {
            bookingBackBtn.addEventListener('click', () => {
                if (currentStep > 1) {
                    currentStep--;
                    showStep(currentStep);
                }
            });
        }
        
        // Wire next button
        if (bookingNextBtn) {
            bookingNextBtn.addEventListener('click', () => {
                if (validateStep(currentStep)) {
                    if (currentStep < bookingSteps.length) {
                        currentStep++;
                        showStep(currentStep);
                    }
                }
            });
        }
        
        // Form Submit Handler
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Final validation of step 3
            if (!validateStep(3)) {
                return;
            }
            
            // Gather form details
            const name = nameInput.value.trim();
            const phone = phoneInput.value.trim();
            const relation = document.getElementById('book-relation').value;
            const diagnosis = document.getElementById('book-diagnosis').value;
            const mobility = document.getElementById('book-mobility').value;
            const room = document.getElementById('book-room').value;
            const date = dateInput.value;
            
            // Construct premium clinical WhatsApp payload
            const payload = 
`*TRANSCARE REHABILITATION - PRE-SCREENING INTAKE*
=========================================

*👤 PATIENT DETAILS*
• *Name:* ${name}
• *Phone:* ${phone}
• *Inquirer Relation:* ${relation}

*🏥 CLINICAL NEED*
• *Primary Rehab Need:* ${diagnosis}
• *Current Mobility Status:* ${mobility}

*🛌 STAY PREFERENCES*
• *Preferred Suite:* ${room}
• *Target Admission Date:* ${date}

=========================================
Thank you! Our clinical team under Dr. Ashok P. Kota will review this profile immediately.`;

            // URL Encode and Redirect
            const encodedText = encodeURIComponent(payload);
            const waUrl = `https://wa.me/918106822020?text=${encodedText}`;
            
            window.open(waUrl, '_blank');
            
            // Reset and close
            closeBookingModal();
        });
    }
});
