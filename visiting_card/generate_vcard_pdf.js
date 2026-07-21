const puppeteer = require('puppeteer');
const path = require('path');

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

    // Load the print-specific HTML file
    const filePath = path.join(__dirname, 'physical_print.html');
    console.log(`Loading: ${filePath}`);
    await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });

    console.log('Generating business card PDF (3.5in x 2in per page)...');
    await page.pdf({
      path: path.join(__dirname, 'vcard.pdf'),
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
      preferCSSPageSize: false   // Use explicit width/height above
    });

    await browser.close();
    console.log('Successfully generated vcard.pdf!');
    console.log('Output: ' + path.join(__dirname, 'vcard.pdf'));
  } catch (error) {
    console.error('Error generating vCard PDF:', error);
  }
}

generateVCardPdf();
