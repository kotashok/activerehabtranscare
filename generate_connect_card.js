const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateConnectCard() {
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

    const htmlPath = path.join(__dirname, 'Connect Card', 'connect_card.html');
    console.log(`Opening HTML file: ${htmlPath}`);
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
    
    // Wait for the QR code images from the api to load completely
    console.log('Waiting for QR code images to load...');
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
    
    // Let's add a small delay to make sure rendering is 100% complete
    await new Promise(resolve => setTimeout(resolve, 2000));

    const outPathWebPng = path.join(__dirname, 'Connect Card', 'connect_card.png');
    const outPathWebPdf = path.join(__dirname, 'Connect Card', 'connect_card.pdf');
    const outPathBrainPng = 'C:\\Users\\conta\\.gemini\\antigravity\\brain\\8fd083a3-8729-4d82-a0c0-0ddb037a0b02\\connect_card.png';
    const outPathBrainPdf = 'C:\\Users\\conta\\.gemini\\antigravity\\brain\\8fd083a3-8729-4d82-a0c0-0ddb037a0b02\\connect_card.pdf';
    
    console.log(`Taking screenshot and saving PNG to: ${outPathWebPng}`);
    await page.screenshot({
      path: outPathWebPng,
      type: 'png',
      fullPage: true
    });

    console.log(`Generating print-ready PDF and saving to: ${outPathWebPdf}`);
    await page.pdf({
      path: outPathWebPdf,
      width: '148mm',
      height: '210mm',
      printBackground: true,
      margin: { top: '0in', right: '0in', bottom: '0in', left: '0in' }
    });
    
    console.log('Copying outputs to brain artifacts directory...');
    const brainDir = path.dirname(outPathBrainPng);
    if (!fs.existsSync(brainDir)) {
      fs.mkdirSync(brainDir, { recursive: true });
    }
    fs.copyFileSync(outPathWebPng, outPathBrainPng);
    fs.copyFileSync(outPathWebPdf, outPathBrainPdf);
    
    await browser.close();
    console.log('Successfully completed generating and backing up the connect card PNG and PDF!');
  } catch (error) {
    console.error('Error generating connect card:', error);
  }
}

generateConnectCard();
