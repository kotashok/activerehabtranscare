const fs = require('fs');
const path = require('path');

const files = [
  path.join(__dirname, 'consent_form_print.html'),
  "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f14f7863-a35b-43c6-9436-0db3f541b923\\tracheostomy_ventilator_consent_form.md"
];

files.forEach(filePath => {
  if (!fs.existsSync(filePath)) {
    console.log(`File not found: ${filePath}`);
    return;
  }
  
  console.log(`Processing: ${filePath}`);
  let content = fs.readFileSync(filePath, 'utf8');
  
  // Replace SPONSOR, Sponsor, sponsor with GUARDIAN, Guardian, guardian respectively
  content = content.replace(/SPONSOR/g, 'GUARDIAN');
  content = content.replace(/Sponsor/g, 'Guardian');
  content = content.replace(/sponsor/g, 'guardian');
  
  // Also, replace the Telugu phonetic match if Sponsor was written in Telugu.
  // In our Telugu text: "నేను, ___________________ (స్పాన్సర్/రక్షకుడు)"
  // Let's replace "స్పాన్సర్/రక్షకుడు" or "స్పాన్సర్" with "సంరక్షకుడు" (Guardian in Telugu)
  content = content.replace(/స్పాన్సర్\/రక్షకుడు/g, 'సంరక్షకుడు');
  content = content.replace(/స్పాన్సర్/g, 'సంరక్షకుడు');
  
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Successfully updated: ${filePath}`);
});

console.log("Terminology replacement complete!");
