const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function capture() {
  try {
    console.log("Launching Puppeteer to capture e-card screenshots...");
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Size matching standard mobile container viewport
    await page.setViewport({ width: 440, height: 600, deviceScaleFactor: 2 });
    
    // Intercept requests to abort external CDN calls so the local file loads instantly
    await page.setRequestInterception(true);
    page.on('request', (req) => {
      const url = req.url();
      if (url.startsWith('file://')) {
        req.continue();
      } else {
        req.abort();
      }
    });

    const filePath = path.join(__dirname, 'index.html');
    const fileUrl = 'file:///' + filePath.replace(/\\/g, '/');
    
    console.log("Loading page...");
    await page.goto(fileUrl, { waitUntil: 'load', timeout: 5000 }).catch(err => {
      console.log("Navigation timeout log:", err.message);
    });
    
    // Wait for animations to complete
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    const frontPath = path.join(__dirname, 'dr_ashok_vcard_front.png');
    const backPath = path.join(__dirname, 'dr_ashok_vcard_back.png');
    const artifactFrontPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1\\dr_ashok_vcard_front.png";
    const artifactBackPath = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1\\dr_ashok_vcard_back.png";
    
    console.log("Capturing front side...");
    const frontBuffer = await page.screenshot({ type: 'png' });
    fs.writeFileSync(frontPath, frontBuffer);
    fs.writeFileSync(artifactFrontPath, frontBuffer);
    
    console.log("Flipping card...");
    await page.evaluate(() => {
      const card = document.getElementById('card');
      if (card) card.classList.add('flipped');
    });
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    console.log("Capturing back side...");
    const backBuffer = await page.screenshot({ type: 'png' });
    fs.writeFileSync(backPath, backBuffer);
    fs.writeFileSync(artifactBackPath, backBuffer);
    
    await browser.close();
    console.log("Successfully captured front and back screenshots!");
  } catch (error) {
    console.error("Error during capture:", error);
  }
}

capture();
