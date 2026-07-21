const puppeteer = require('puppeteer');
const path = require('path');

async function generateBrochurePdf() {
  try {
    console.log('Launching browser to generate brochure PDF...');
    const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();

    // Set viewport to exact A5 dimensions at 96 DPI (148mm x 210mm)
    // 148mm = 559px, 210mm = 794px at 96 DPI
    await page.setViewport({
      width: 559,
      height: 794,
      deviceScaleFactor: 2
    });
    
    // Load local brochure HTML
    const filePath = path.join(__dirname, 'index.html');
    console.log(`Loading index.html from path: ${filePath}`);
    await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });
    
    console.log('Generating A5 print PDF...');
    // Generate A5 portrait borderless PDF with backgrounds enabled
    await page.pdf({
      path: path.join(__dirname, 'brochure.pdf'),
      format: 'A5',
      landscape: false,
      printBackground: true,
      margin: {
        top: '0mm',
        right: '0mm',
        bottom: '0mm',
        left: '0mm'
      },
      preferCSSPageSize: true
    });

    await browser.close();
    console.log('Successfully generated brochure.pdf!');
  } catch (error) {
    console.error('Error generating brochure PDF:', error);
  }
}

generateBrochurePdf();
