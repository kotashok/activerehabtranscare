const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const cards = [
  { html: 'service_card_neuro.html', png: 'service_card_neuro.png' },
  { html: 'service_card_ortho.html', png: 'service_card_ortho.png' },
  { html: 'service_card_cardio.html', png: 'service_card_cardio.png' },
  { html: 'service_card_geriatric.html', png: 'service_card_geriatric.png' },
  { html: 'service_card_neuro_telugu.html', png: 'service_card_neuro_telugu.png' },
  { html: 'service_card_ortho_telugu.html', png: 'service_card_ortho_telugu.png' },
  { html: 'service_card_cardio_telugu.html', png: 'service_card_cardio_telugu.png' },
  { html: 'service_card_geriatric_telugu.html', png: 'service_card_geriatric_telugu.png' }
];

async function generateServiceCards() {
  try {
    console.log('Launching Puppeteer browser...');
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set standard A5 size viewport with deviceScaleFactor: 3 for high resolution (1677x2382)
    await page.setViewport({
      width: 559,
      height: 794,
      deviceScaleFactor: 3
    });
    
    page.setDefaultNavigationTimeout(60000);

    for (const card of cards) {
      const htmlPath = path.join(__dirname, 'Services Cards', card.html);
      const outPathWebPng = path.join(__dirname, 'Services Cards', card.png);
      const outPathWebPdf = path.join(__dirname, 'Services Cards', card.png.replace('.png', '.pdf'));
      const outPathBrainPng = path.join('C:\\Users\\conta\\.gemini\\antigravity\\brain\\8fd083a3-8729-4d82-a0c0-0ddb037a0b02', card.png);
      const outPathBrainPdf = path.join('C:\\Users\\conta\\.gemini\\antigravity\\brain\\8fd083a3-8729-4d82-a0c0-0ddb037a0b02', card.png.replace('.png', '.pdf'));

      console.log(`\nProcessing: ${card.html} ...`);
      await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
      
      // Wait for all dynamic images (logo + dynamic QR code) to load
      await page.evaluate(async () => {
        const imgs = Array.from(document.querySelectorAll('img'));
        await Promise.all(imgs.map(img => {
          if (img.complete) return;
          return new Promise((resolve, reject) => {
            img.onload = resolve;
            img.onerror = reject;
          });
        }));
      });
      
      // Allow final font and CSS renderings to settle
      await new Promise(resolve => setTimeout(resolve, 2000));

      console.log(`Saving premium PNG screenshot to: ${outPathWebPng}`);
      await page.screenshot({
        path: outPathWebPng,
        type: 'png',
        fullPage: true
      });

      console.log(`Saving print-ready A5 PDF to: ${outPathWebPdf}`);
      await page.pdf({
        path: outPathWebPdf,
        width: '148mm',
        height: '210mm',
        printBackground: true,
        margin: { top: '0in', right: '0in', bottom: '0in', left: '0in' }
      });
      
      console.log(`Copying backups to brain artifacts folder...`);
      const brainDir = path.dirname(outPathBrainPng);
      if (!fs.existsSync(brainDir)) {
        fs.mkdirSync(brainDir, { recursive: true });
      }
      fs.copyFileSync(outPathWebPng, outPathBrainPng);
      fs.copyFileSync(outPathWebPdf, outPathBrainPdf);
    }
    
    await browser.close();
    console.log('\nSuccessfully generated and backed up all 4 individual service cards!');
  } catch (error) {
    console.error('Error generating service cards:', error);
  }
}

generateServiceCards();
