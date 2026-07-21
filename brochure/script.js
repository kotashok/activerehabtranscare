/* ====================================================================
   ACTIVE REHAB TRANSCARE - OFFICIAL BROCHURE INTERACTIVE SCRIPT
   ==================================================================== */

document.addEventListener("DOMContentLoaded", () => {
    
    // Select Carousel Elements
    const slider = document.getElementById("brochure-slider");
    const btnPrev = document.getElementById("btn-prev");
    const btnNext = document.getElementById("btn-next");
    const dotsContainer = document.getElementById("page-dots");
    const dots = document.querySelectorAll(".dot");
    
    let currentPage = 0;
    const totalPages = 4;

    // Check if slider exists (only active on screen layout, disabled on print stack)
    if (slider) {
        
        // 1. Update Slider Viewport Offset
        function updateSlider() {
            // Apply horizontal transform offset percentage
            slider.style.transform = `translateX(-${currentPage * 25}%)`;
            
            // Toggle Action buttons availability states
            if (btnPrev && btnNext) {
                btnPrev.disabled = currentPage === 0;
                btnNext.disabled = currentPage === totalPages - 1;
            }
            
            // Sync active dot highlight
            dots.forEach((dot, idx) => {
                if (idx === currentPage) {
                    dot.classList.add("active");
                } else {
                    dot.classList.remove("active");
                }
            });
        }

        // 2. Navigation Click Handlers
        if (btnNext) {
            btnNext.addEventListener("click", () => {
                if (currentPage < totalPages - 1) {
                    currentPage++;
                    updateSlider();
                }
            });
        }

        if (btnPrev) {
            btnPrev.addEventListener("click", () => {
                if (currentPage > 0) {
                    currentPage--;
                    updateSlider();
                }
            });
        }

        // 3. Dot Indicator Click Handlers
        if (dotsContainer) {
            dotsContainer.addEventListener("click", (e) => {
                const targetDot = e.target.closest(".dot");
                if (targetDot) {
                    const targetPage = parseInt(targetDot.getAttribute("data-page"), 10);
                    if (!isNaN(targetPage) && targetPage >= 0 && targetPage < totalPages) {
                        currentPage = targetPage;
                        updateSlider();
                    }
                }
            });
        }

        // 4. Keyboard Shortcuts Navigation (Buttery smooth sliding)
        document.addEventListener("keydown", (e) => {
            // Only capture arrow keys if user is not typing in inputs
            if (document.activeElement.tagName === "INPUT" || document.activeElement.tagName === "TEXTAREA") {
                return;
            }
            
            if (e.key === "ArrowRight") {
                if (currentPage < totalPages - 1) {
                    currentPage++;
                    updateSlider();
                }
            } else if (e.key === "ArrowLeft") {
                if (currentPage > 0) {
                    currentPage--;
                    updateSlider();
                }
            }
        });

        // Initialize Slider
        updateSlider();

    }

    // 5. Automatic VCard sharing redirect tracking
    const btnVCard = document.querySelector(".btn-vcard");
    if (btnVCard) {
        btnVCard.addEventListener("click", () => {
            // Can push clean clinical tracking analytics events here
        });
    }

});
