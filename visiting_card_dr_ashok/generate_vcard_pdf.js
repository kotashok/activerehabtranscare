const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateVCardPdf() {
  try {
    console.log('Launching browser to generate vCard PDF...');
    const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    // Standard business card: 3.5in x 2in
    // At 96 DPI: 336px x 192px
    await page.setViewport({
      width: 336,
      height: 192,
      deviceScaleFactor: 3   // High DPI for crisp print quality
    });

    // Load the print-specific HTML file with proper URL formatting
    const filePath = path.join(__dirname, 'physical_print.html');
    const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');
    console.log(`Loading: ${fileUrl}`);
    
    await page.goto(fileUrl, { 
      waitUntil: 'load', 
      timeout: 10000 
    }).catch(err => {
      console.log(`[System] Navigation log: ${err.message}. Proceeding to compile PDF...`);
    });

    console.log('Generating business card PDF (3.5in x 2in per page)...');
    const pdfPath = path.join(__dirname, 'vcard.pdf');
    const rootPdfPath = path.join(__dirname, '../Ashok_vCard.pdf');
    const artifactPdfPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1\\Ashok_vCard.pdf";

    const pdfBuffer = await page.pdf({
      width: '3.5in',
      height: '2in',
      printBackground: true,
      landscape: false,
      margin: {
        top: '0mm',
        right: '0mm',
        bottom: '0mm',
        left: '0mm'
      },
      preferCSSPageSize: false
    });

    // Save outputs
    fs.writeFileSync(pdfPath, pdfBuffer);
    fs.writeFileSync(rootPdfPath, pdfBuffer);
    
    const fsExtra = require('fs');
    const artifactDir = path.dirname(artifactPdfPath);
    if (!fsExtra.existsSync(artifactDir)) {
      fsExtra.mkdirSync(artifactDir, { recursive: true });
    }
    fsExtra.writeFileSync(artifactPdfPath, pdfBuffer);

    await browser.close();
    console.log('Successfully generated vcard.pdf!');
    console.log('Saved to:\n  - ' + pdfPath + '\n  - ' + rootPdfPath + '\n  - ' + artifactPdfPath);
  } catch (error) {
    console.error('Error generating vCard PDF:', error);
  }
}

generateVCardPdf();
