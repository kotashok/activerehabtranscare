/* ====================================================================
   GOOGLE ANTIGRAVITY - e-CARD INTERACTIVE SCRIPT LOGIC
   ==================================================================== */

document.addEventListener("DOMContentLoaded", () => {
    
    // Elements Selection
    const card = document.getElementById("card");
    const btnSaveContact = document.getElementById("btn-save-contact");
    const btnShareCard = document.getElementById("btn-share-card");
    const qrCodeContainer = document.getElementById("qrcode");
    const toast = document.getElementById("toast");
    const toastMessage = document.getElementById("toast-message");

    // Dynamic e-Card Page URL (points to Kumar's live visiting card location)
    const cardUrl = "https://activerehabtranscare.in/visiting_card/";

    // 1. Render Themed QR Code (Centered on navy branding to match CSS)
    if (qrCodeContainer) {
        const qrColor = "003366"; // Clinical Trust Navy Hex
        const qrApiUrl = `https://api.qrserver.com/v1/create-qr-code/?size=120x120&color=${qrColor}&data=${encodeURIComponent(cardUrl)}`;
        
        qrCodeContainer.innerHTML = `<img src="${qrApiUrl}" alt="ActiveRehab QR" style="width: 100%; height: 100%; object-fit: contain;">`;
    }

    // 2. Buttery Smooth 3D Card Flip Handler
    if (card) {
        card.addEventListener("click", (e) => {
            // Prevent flipping if user clicks on actionable links (phone, email, etc.)
            if (e.target.closest("a") || e.target.closest("button")) {
                return;
            }
            card.classList.toggle("flipped");
        });
    }

    // 3. Dynamic vCard (.vcf) Compiler & Downloader
    if (btnSaveContact) {
        btnSaveContact.addEventListener("click", () => {
            // Assemble standard vCard 3.0 file format
            const vCardData = [
                "BEGIN:VCARD",
                "VERSION:3.0",
                "FN:Kumar Yeldi",
                "N:Yeldi;Kumar;;;",
                "ORG:ActiveRehab TransCare & Rehabilitation",
                "TITLE:Business Development Manager",
                "TEL;TYPE=CELL,VOICE;VALUE=uri:tel:+918106822020",
                "EMAIL;TYPE=PREF,INTERNET:activerehab.tc@gmail.com",
                "URL:https://activerehabtranscare.in",
                "ADR;TYPE=WORK,POSTAL,PARCEL:;;Plot No. 4-1-1\\, 41/A & 48\\, Laxmi Nagar Colony;Kompally\\, Hyderabad;Telangana;500100;IN",
                "REV:" + new Date().toISOString(),
                "END:VCARD"
            ].join("\n");

            // Convert to Blob text stream
            const blob = new Blob([vCardData], { type: "text/vcard;charset=utf-8;" });
            const fileName = "Kumar_Yeldi_ActiveRehab.vcf";

            // Trigger safe client-side browser download
            if (navigator.msSaveBlob) { 
                // IE 10+
                navigator.msSaveBlob(blob, fileName);
            } else {
                const link = document.createElement("a");
                if (link.download !== undefined) {
                    const url = URL.createObjectURL(blob);
                    link.setAttribute("href", url);
                    link.setAttribute("download", fileName);
                    link.style.visibility = "hidden";
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    
                    // Show helpful success toast
                    showToast("Contact added! Open file to save.");
                }
            }
        });
    }

    // 4. Share Sheet & Clipboard Sharing Integration
    if (btnShareCard) {
        btnShareCard.addEventListener("click", async () => {
            const shareData = {
                title: "Kumar Yeldi - ActiveRehab TransCare",
                text: "Business Development Manager, ActiveRehab TransCare & Rehabilitation. Save contact or connect directly:",
                url: cardUrl
            };

            // Check if Mobile Native Share sheet is supported
            if (navigator.share) {
                try {
                    await navigator.share(shareData);
                } catch (err) {
                    // Fail silently if user cancels the sheet
                }
            } else {
                // Fallback: Copy link to clipboard
                try {
                    await navigator.clipboard.writeText(cardUrl);
                    showToast("Visiting card link copied!");
                } catch (err) {
                    // Secondary Fallback: Select text and alert
                    showToast("Link: activerehabtranscare.in/visiting_card/");
                }
            }
        });
    }

    // 5. Toast Notification System
    function showToast(message) {
        if (!toast || !toastMessage) return;
        
        toastMessage.textContent = message;
        toast.classList.add("show");
        
        // Dynamic pop-down timeout
        setTimeout(() => {
            toast.classList.remove("show");
        }, 3000);
    }

});
