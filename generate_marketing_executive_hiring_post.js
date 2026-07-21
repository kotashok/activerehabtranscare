const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateHiringPoster() {
  try {
    console.log("[System] Starting compilation for the Marketing Executive hiring poster (1080x1080px)...");
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set 1080x1080 viewport with a scale factor of 2 for extremely crisp text and graphics
    await page.setViewport({
      width: 1080,
      height: 1080,
      deviceScaleFactor: 2
    });

    const filePath = path.join(__dirname, 'hiring_marketing_executive_blueprint.html');
    const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');
    console.log(`[System] Loading hiring poster blueprint from: ${fileUrl}`);
    
    await page.goto(fileUrl, { 
      waitUntil: 'load',
      timeout: 5000
    }).catch(err => {
      console.log(`[System] Navigation log: ${err.message}. Proceeding to render screenshot...`);
    });
    
    // Allow Google Fonts and FontAwesome resources 3 seconds to fully render
    await new Promise(resolve => setTimeout(resolve, 3000));
    
    const localImgPath = path.join(__dirname, 'hiring_marketing_executive_instagram.png');
    const localPdfPath = path.join(__dirname, 'hiring_marketing_executive_instagram.pdf');
    const artifactImgPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1\\hiring_marketing_executive_instagram.png";
    const artifactPdfPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1\\hiring_marketing_executive_instagram.pdf";
    
    console.log("[System] Capturing screenshot of the compiled HTML design...");
    const screenshotBuffer = await page.screenshot({
      type: 'png',
      fullPage: false
    });

    // Write PNG to the website project directory
    fs.writeFileSync(localImgPath, screenshotBuffer);
    console.log(`[System] Successfully saved local branded PNG to: ${localImgPath}`);

    console.log("[System] Compiling PDF with exact print dimensions: 1080px x 1080px...");
    const pdfBuffer = await page.pdf({
      width: '1080px',
      height: '1080px',
      printBackground: true,
      margin: { top: '0in', right: '0in', bottom: '0in', left: '0in' }
    });

    // Write PDF to the website project directory
    fs.writeFileSync(localPdfPath, pdfBuffer);
    console.log(`[System] Successfully saved local print-ready PDF to: ${localPdfPath}`);

    // Write to the brain artifacts directory
    const artifactDir = path.dirname(artifactImgPath);
    if (!fs.existsSync(artifactDir)) {
      fs.mkdirSync(artifactDir, { recursive: true });
    }
    fs.writeFileSync(artifactImgPath, screenshotBuffer);
    fs.writeFileSync(artifactPdfPath, pdfBuffer);
    console.log(`[System] Successfully saved artifact branded PNG and PDF to: ${artifactDir}`);

    await browser.close();
    console.log("[System] [OK] Instagram hiring poster successfully compiled!");
  } catch (error) {
    console.error("Error generating hiring poster:", error);
    process.exit(1);
  }
}

generateHiringPoster();
