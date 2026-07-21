const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateHiringPoster() {
  try {
    printLog("Starting compilation for the Instagram hiring poster (1080x1080px)...");
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set 1080x1080 viewport with a scale factor of 2 for extremely crisp vector text and graphics
    await page.setViewport({
      width: 1080,
      height: 1080,
      deviceScaleFactor: 2
    });

    const filePath = path.join(__dirname, 'hiring_poster_blueprint.html');
    printLog(`Loading hiring poster blueprint from: file://${filePath}`);
    
    await page.goto(`file://${filePath}`, { 
      waitUntil: 'networkidle0',
      timeout: 60000
    });
    
    const localImgPath = path.join(__dirname, 'hiring_physiotherapist_instagram.png');
    const localPdfPath = path.join(__dirname, 'hiring_physiotherapist_instagram.pdf');
    const artifactImgPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\8fd083a3-8729-4d82-a0c0-0ddb037a0b02\\hiring_physiotherapist_instagram.png";
    const artifactPdfPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\8fd083a3-8729-4d82-a0c0-0ddb037a0b02\\hiring_physiotherapist_instagram.pdf";
    
    printLog("Capturing screenshot of the compiled HTML design...");
    const screenshotBuffer = await page.screenshot({
      type: 'png',
      fullPage: false
    });

    // Write PNG to the website project directory
    fs.writeFileSync(localImgPath, screenshotBuffer);
    printLog(`Successfully saved local branded PNG to: ${localImgPath}`);

    printLog("Compiling PDF with exact print dimensions: 1080px x 1080px...");
    const pdfBuffer = await page.pdf({
      width: '1080px',
      height: '1080px',
      printBackground: true,
      margin: { top: '0in', right: '0in', bottom: '0in', left: '0in' }
    });

    // Write PDF to the website project directory
    fs.writeFileSync(localPdfPath, pdfBuffer);
    printLog(`Successfully saved local print-ready PDF to: ${localPdfPath}`);

    // Write to the brain artifacts directory
    const artifactDir = path.dirname(artifactImgPath);
    if (!fs.existsSync(artifactDir)) {
      fs.mkdirSync(artifactDir, { recursive: true });
    }
    fs.writeFileSync(artifactImgPath, screenshotBuffer);
    fs.writeFileSync(artifactPdfPath, pdfBuffer);
    printLog(`Successfully saved artifact branded PNG and PDF to: ${artifactDir}`);

    await browser.close();
    printLog("[OK] Instagram hiring poster successfully compiled!");
  } catch (error) {
    console.error("Error generating hiring poster:", error);
    process.exit(1);
  }
}

function printLog(msg) {
  console.log(`[System] ${msg}`);
}

generateHiringPoster();
