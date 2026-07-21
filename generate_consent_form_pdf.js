const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const forms = [
  {
    html: 'consent_form_print.html',
    pdf: 'ActiveRehab_TransCare_Consent_Form.pdf',
    label: 'Specialized Tracheostomy & Ventilator Consent Form'
  },
  {
    html: 'general_consent_form_print.html',
    pdf: 'ActiveRehab_TransCare_General_Consent_Form.pdf',
    label: 'General Inpatient Admission & Rehab Consent Form'
  }
];

async function generateAllConsentFormsPdf() {
  try {
    console.log("Launching Puppeteer browser for consent forms compilation...");
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set viewport for high-fidelity rendering
    await page.setViewport({
      width: 1200,
      height: 1600,
      deviceScaleFactor: 2
    });

    for (const form of forms) {
      const htmlPath = path.join(__dirname, form.html);
      const localPdfPath = path.join(__dirname, form.pdf);
      const artifactPdfPath = path.join("C:\\Users\\conta\\.gemini\\antigravity\\brain\\f14f7863-a35b-43c6-9436-0db3f541b923", form.pdf);

      console.log(`\nProcessing: ${form.label} (${form.html}) ...`);
      console.log(`Loading blueprint from: file://${htmlPath}`);
      
      await page.goto(`file://${htmlPath}`, { 
        waitUntil: 'networkidle0',
        timeout: 60000
      });
      
      // Allow fonts and layouts to settle
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      console.log(`Rendering multi-page PDF in standard A4 format to: ${localPdfPath}`);
      const pdfBuffer = await page.pdf({
        format: 'A4',
        printBackground: true,
        margin: { top: '0in', right: '0in', bottom: '0in', left: '0in' }
      });

      // Save locally
      fs.writeFileSync(localPdfPath, pdfBuffer);
      console.log(`Successfully saved local PDF to: ${localPdfPath}`);

      // Save to brain artifacts directory
      const artifactDir = path.dirname(artifactPdfPath);
      if (!fs.existsSync(artifactDir)) {
        fs.mkdirSync(artifactDir, { recursive: true });
      }
      fs.writeFileSync(artifactPdfPath, pdfBuffer);
      console.log(`Successfully saved artifact PDF to: ${artifactPdfPath}`);
    }

    await browser.close();
    console.log("\nAll consent form PDFs generated and backed up successfully!");
  } catch (error) {
    console.error("Error generating consent form PDFs:", error);
    process.exit(1);
  }
}

generateAllConsentFormsPdf();
