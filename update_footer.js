const fs = require('fs');
const path = require('path');

const files = [
  path.join(__dirname, 'consent_form_print.html'),
  "C:/Users/conta/.gemini/antigravity/brain/f14f7863-a35b-43c6-9436-0db3f541b923/tracheostomy_ventilator_consent_form.md"
];

// Read HTML blueprint
const htmlPath = files[0];
let htmlContent = fs.readFileSync(htmlPath, 'utf8');

// Define new HTML footers for page 1 and page 2
const newFooterPage1 = `        <!-- Footer -->
        <div class="page-footer">
            <span class="address">
                <i class="fa-solid fa-location-dot"></i> Laxmi Nagar Colony, Kompally, Hyderabad | 
                <i class="fa-solid fa-phone" style="color: var(--saffron); margin-left: 5px; margin-right: 2px;"></i> +91 81068 22020 | 
                <i class="fa-solid fa-envelope" style="color: var(--saffron); margin-left: 5px; margin-right: 2px;"></i> activerehab.tc@gmail.com | 
                <i class="fa-solid fa-globe" style="color: var(--saffron); margin-left: 5px; margin-right: 2px;"></i> activerehabtranscare.in
            </span>
            <span>Page 1 of 2</span>
        </div>`;

const newFooterPage2 = `        <!-- Footer -->
        <div class="page-footer">
            <span class="address">
                <i class="fa-solid fa-location-dot"></i> Laxmi Nagar Colony, Kompally, Hyderabad | 
                <i class="fa-solid fa-phone" style="color: var(--saffron); margin-left: 5px; margin-right: 2px;"></i> +91 81068 22020 | 
                <i class="fa-solid fa-envelope" style="color: var(--saffron); margin-left: 5px; margin-right: 2px;"></i> activerehab.tc@gmail.com | 
                <i class="fa-solid fa-globe" style="color: var(--saffron); margin-left: 5px; margin-right: 2px;"></i> activerehabtranscare.in
            </span>
            <span>Page 2 of 2</span>
        </div>`;

// Replace Page 1 footer
htmlContent = htmlContent.replace(
  /<!-- Footer -->\s*<div class="page-footer">[\s\S]*?Page 1 of 2<\/span>\s*<\/div>/,
  newFooterPage1
);

// Replace Page 2 footer
htmlContent = htmlContent.replace(
  /<!-- Footer -->\s*<div class="page-footer">[\s\S]*?Page 2 of 2<\/span>\s*<\/div>/,
  newFooterPage2
);

fs.writeFileSync(htmlPath, htmlContent, 'utf8');
console.log(`Successfully updated HTML blueprint: ${htmlPath}`);


// Read Markdown template
const mdPath = files[1];
if (fs.existsSync(mdPath)) {
  let mdContent = fs.readFileSync(mdPath, 'utf8');
  
  if (!mdContent.includes('activerehab.tc@gmail.com')) {
    mdContent += `\n\n---\n**Contact & Center Details:**\n*   **Address:** Laxmi Nagar Colony, Kompally, Hyderabad\n*   **Mobile:** +91 81068 22020\n*   **Email:** activerehab.tc@gmail.com\n*   **Website:** activerehabtranscare.in\n`;
    fs.writeFileSync(mdPath, mdContent, 'utf8');
    console.log(`Successfully updated contact info in: ${mdPath}`);
  } else {
    console.log(`Contact info already present in: ${mdPath}`);
  }
} else {
  console.log(`Markdown file not found at: ${mdPath}`);
}
