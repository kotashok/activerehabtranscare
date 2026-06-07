const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateInstagramCarousel() {
  try {
    console.log("[System] Starting compilation for the 9-slide Instagram Carousel (1080x1350px)...");
    
    // Launch headless browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set viewport with scale factor 2 for crystal-clear text and rendering
    await page.setViewport({
      width: 1080,
      height: 1350,
      deviceScaleFactor: 2
    });

    const filePath = path.join(__dirname, 'instagram_carousel_blueprint.html');
    console.log(`[System] Loading blueprint from: file://${filePath}`);
    
    await page.goto(`file://${filePath}`, { 
      waitUntil: 'networkidle0',
      timeout: 120000 // 2 minutes timeout for rendering font assets
    });

    // Define target directories
    const artifactDir = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1";
    
    // Loop through each of the 9 slides and capture screenshots of individual slide containers
    for (let i = 1; i <= 9; i++) {
      const slideSelector = `#slide-${i}`;
      console.log(`[System] Capturing screenshot of ${slideSelector}...`);
      
      const slideElement = await page.$(slideSelector);
      if (!slideElement) {
        console.error(`[Error] Slide element ${slideSelector} not found!`);
        continue;
      }
      
      const localImgPath = path.join(__dirname, `instagram_carousel_slide_${i}.png`);
      const artifactImgPath = path.join(artifactDir, `instagram_carousel_slide_${i}.png`);
      
      const screenshotBuffer = await slideElement.screenshot({
        type: 'png'
      });

      // Save local copy in the website folder
      fs.writeFileSync(localImgPath, screenshotBuffer);
      console.log(`[OK] Saved local slide ${i} to: ${localImgPath}`);

      // Save copy in the brain artifacts folder
      fs.writeFileSync(artifactImgPath, screenshotBuffer);
      console.log(`[OK] Saved artifact slide ${i} to: ${artifactImgPath}`);
    }

    await browser.close();
    console.log("[OK] Instagram 9-slide Carousel successfully compiled!");
  } catch (error) {
    console.error("[Error] Generation failed:", error);
    process.exit(1);
  }
}

generateInstagramCarousel();
