const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateStoryQuizSequence() {
  try {
    console.log("[System] Starting compilation for the 4-frame Instagram Story Quiz Sequence (1080x1920px)...");
    
    // Launch headless browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    // Set viewport with scale factor 2 for crystal-clear story rendering (9:16 ratio)
    await page.setViewport({
      width: 1080,
      height: 1920,
      deviceScaleFactor: 2
    });

    const filePath = path.join(__dirname, 'instagram_story_quiz_blueprint.html');
    console.log(`[System] Loading blueprint from: file://${filePath}`);
    
    await page.goto(`file://${filePath}`, { 
      waitUntil: 'networkidle0',
      timeout: 120000 
    });

    // Define target directory for artifacts
    const artifactDir = "C:\\Users\\conta\\.gemini\\antigravity\\brain\\f96fbad7-b2f6-4d01-b97f-60ba183c82e1";
    
    // Ensure artifact directory exists
    if (!fs.existsSync(artifactDir)) {
      fs.mkdirSync(artifactDir, { recursive: true });
    }

    // Loop through each of the 4 frames and capture screenshots of individual frame containers
    for (let i = 1; i <= 4; i++) {
      const frameSelector = `#frame-${i}`;
      console.log(`[System] Capturing screenshot of ${frameSelector}...`);
      
      const frameElement = await page.$(frameSelector);
      if (!frameElement) {
        console.error(`[Error] Frame element ${frameSelector} not found!`);
        continue;
      }
      
      const localImgPath = path.join(__dirname, `instagram_story_slide_${i}.png`);
      const artifactImgPath = path.join(artifactDir, `instagram_story_slide_${i}.png`);
      
      const screenshotBuffer = await frameElement.screenshot({
        type: 'png'
      });

      // Save local copy in the website folder
      fs.writeFileSync(localImgPath, screenshotBuffer);
      console.log(`[OK] Saved local story frame ${i} to: ${localImgPath}`);

      // Save copy in the brain artifacts folder
      fs.writeFileSync(artifactImgPath, screenshotBuffer);
      console.log(`[OK] Saved artifact story frame ${i} to: ${artifactImgPath}`);
    }

    console.log("[System] Injecting print styles and compiling multi-page story PDF...");
    await page.addStyleTag({
      content: `
        @media print {
          body {
            background: white !important;
            padding: 0 !important;
            margin: 0 !important;
          }
          .frame {
            margin: 0 !important;
            box-shadow: none !important;
            page-break-after: always !important;
            break-after: page !important;
          }
        }
      `
    });

    const localPdfPath = path.join(__dirname, 'instagram_story_quiz.pdf');
    const artifactPdfPath = path.join(artifactDir, 'instagram_story_quiz.pdf');

    const pdfBuffer = await page.pdf({
      width: '1080px',
      height: '1920px',
      printBackground: true,
      margin: { top: '0in', right: '0in', bottom: '0in', left: '0in' }
    });

    fs.writeFileSync(localPdfPath, pdfBuffer);
    fs.writeFileSync(artifactPdfPath, pdfBuffer);
    console.log(`[OK] Saved local story PDF to: ${localPdfPath}`);
    console.log(`[OK] Saved artifact story PDF to: ${artifactPdfPath}`);

    await browser.close();
    console.log("[OK] Instagram 4-frame Story Quiz Sequence successfully compiled!");
  } catch (error) {
    console.error("[Error] Generation failed:", error);
    process.exit(1);
  }
}

generateStoryQuizSequence();
