const fs = require('fs');
const path = require('path');

const files = [
  'service_card_neuro.html',
  'service_card_ortho.html',
  'service_card_cardio.html',
  'service_card_geriatric.html',
  'service_card_neuro_telugu.html',
  'service_card_ortho_telugu.html',
  'service_card_cardio_telugu.html',
  'service_card_geriatric_telugu.html'
];

files.forEach(filename => {
  const filePath = path.join(__dirname, filename);
  if (!fs.existsSync(filePath)) {
    console.log(`Skipping missing file: ${filename}`);
    return;
  }
  
  console.log(`\nUpdating card layouts and styling for: ${filename}`);
  let content = fs.readFileSync(filePath, 'utf8');
  
  // 1. Update CSS styles for .timeline-container
  const timelineContainerRegex = /\.timeline-container\s*\{[\s\S]*?\}/;
  const newTimelineContainerCSS = `.timeline-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
            height: 100%;
        }`;
  content = content.replace(timelineContainerRegex, newTimelineContainerCSS);
  
  // 2. Update CSS styles for .timeline-card to enable flex: 1 stretching
  const timelineCardRegex = /\.timeline-card\s*\{[\s\S]*?\}/;
  const isTelugu = filename.includes('telugu');
  const paddingVal = isTelugu ? '8px 12px' : '10px 14px';
  const newTimelineCardCSS = `.timeline-card {
            background-color: var(--bg-light);
            border-left: 3.5px solid var(--saffron);
            border-top: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
            border-radius: 0 10px 10px 0;
            padding: ${paddingVal};
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }`;
  content = content.replace(timelineCardRegex, newTimelineCardCSS);
  
  // 3. Update CSS styles for .modalities-container
  const modalitiesContainerRegex = /\.modalities-container\s*\{[\s\S]*?\}/;
  const newModalitiesContainerCSS = `.modalities-container {
            display: flex;
            flex-direction: column;
            height: 100%;
        }`;
  content = content.replace(modalitiesContainerRegex, newModalitiesContainerCSS);
  
  // 4. Inject .modalities-card-wrapper CSS definition if not present
  if (!content.includes('.modalities-card-wrapper')) {
    const modalitiesCardWrapperCSS = `
        .modalities-card-wrapper {
            background-color: var(--bg-light);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: ${isTelugu ? '10px 12px' : '12px 14px'};
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 8px;
        }`;
    // Insert after .modalities-container CSS block
    content = content.replace(newModalitiesContainerCSS, `${newModalitiesContainerCSS}\n\n        ${modalitiesCardWrapperCSS.trim()}`);
  }
  
  // 5. Update CSS styles for .action-block to increase padding and add margin-top
  const actionBlockRegex = /\.action-block\s*\{[\s\S]*?\}/;
  const newActionBlockCSS = `.action-block {
            background: linear-gradient(135deg, rgba(0, 51, 102, 0.03) 0%, rgba(230, 92, 0, 0.02) 100%);
            border: 1px solid rgba(0, 51, 102, 0.1);
            border-radius: 12px;
            padding: 12px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 10px;
            margin-bottom: 8px;
        }`;
  content = content.replace(actionBlockRegex, newActionBlockCSS);
  
  // 6. Wrap modality items inside modalities-card-wrapper HTML structure if not already wrapped
  if (!content.includes('class="modalities-card-wrapper"')) {
    // Locate the first modality-item inside modalities-container
    const searchStr = '<div class="modalities-container">';
    const spanStartIndex = content.indexOf(searchStr);
    if (spanStartIndex !== -1) {
      // Find the closing </span> of the column-title
      const titleSpanClose = '</span>';
      const titleCloseIndex = content.indexOf(titleSpanClose, spanStartIndex);
      if (titleCloseIndex !== -1) {
        const insertionPoint = titleCloseIndex + titleSpanClose.length;
        content = content.slice(0, insertionPoint) + '\n                <div class="modalities-card-wrapper">' + content.slice(insertionPoint);
      }
    }
    
    // Find the end of modalities-container to insert closing wrapper div
    // We target "</div>\s*</div>\s*</div>\s*<!-- Action Block -->" which is:
    // 1. Closes last modality-item
    // 2. Closes modalities-container
    // 3. Closes details-grid
    content = content.replace(/<\/div>\s*<\/div>\s*<\/div>\s*<!-- Action Block -->/, '</div>\n                </div> <!-- /modalities-card-wrapper -->\n            </div>\n\n        </div>\n\n        <!-- Action Block -->');
  }
  
  fs.writeFileSync(filePath, content, 'utf8');
  console.log(`Successfully updated ${filename}`);
});

console.log('\nAll card style and HTML wrapper modifications complete!');
