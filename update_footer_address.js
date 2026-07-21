const fs = require('fs');
const path = require('path');

const files = [
  path.join(__dirname, 'consent_form_print.html'),
  "C:/Users/conta/.gemini/antigravity/brain/f14f7863-a35b-43c6-9436-0db3f541b923/tracheostomy_ventilator_consent_form.md"
];

// Read HTML blueprint
const htmlPath = files[0];
let htmlContent = fs.readFileSync(htmlPath, 'utf8');

// Replace "Laxmi Nagar Colony, Kompally, Hyderabad" with "Kompally, Hyderabad"
htmlContent = htmlContent.replace(/Laxmi Nagar Colony,\s*Kompally/g, 'Kompally');
fs.writeFileSync(htmlPath, htmlContent, 'utf8');
console.log(`Successfully updated HTML blueprint: ${htmlPath}`);


// Read Markdown template
const mdPath = files[1];
if (fs.existsSync(mdPath)) {
  let mdContent = fs.readFileSync(mdPath, 'utf8');
  
  // Replace in markdown as well
  mdContent = mdContent.replace(/Laxmi Nagar Colony,\s*Kompally/g, 'Kompally');
  fs.writeFileSync(mdPath, mdContent, 'utf8');
  console.log(`Successfully updated Markdown template: ${mdPath}`);
} else {
  console.log(`Markdown file not found at: ${mdPath}`);
}
