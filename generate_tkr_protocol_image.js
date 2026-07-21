const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function main() {
  try {
    console.log("Launching browser to render TKR Rehabilitation protocol...");
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Set viewport exactly to body size (Instagram portrait size 1080x1350)
    await page.setViewport({
      width: 1080,
      height: 1350,
      deviceScaleFactor: 2 // High DPI for crisp print quality
    });

    const filePath = path.join(__dirname, 'tkr_rehab_protocol_blueprint.html');
    const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');
    console.log(`Loading: ${fileUrl}`);

    await page.goto(fileUrl, { 
      waitUntil: 'load', 
      timeout: 10000 
    }).catch(err => {
      console.log(`[System] Navigation log: ${err.message}. Proceeding to render...`);
    });

    // Wait for fonts and layouts to settle
    await new Promise(resolve => setTimeout(resolve, 2000));

    console.log("Taking screenshot of TKR protocol infographic (1080x1350)...");
    const buffer = await page.screenshot({ type: 'png' });

    const localImgPath = path.join(__dirname, 'tkr_rehab_protocol.png');
    const artifactImgPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1\\tkr_rehab_protocol.png";

    fs.writeFileSync(localImgPath, buffer);
    fs.writeFileSync(artifactImgPath, buffer);

    await browser.close();
    console.log("Infographic rendered successfully!");
    console.log(`Saved locally:  ${localImgPath}`);
    console.log(`Saved artifact: ${artifactImgPath}`);

  } catch (error) {
    console.error("Error during compilation:", error);
  }
}

main();
