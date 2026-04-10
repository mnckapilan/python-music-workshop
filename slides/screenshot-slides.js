const { chromium } = require('@playwright/test');
const path = require('path');
const fs = require('fs');

const BASE_URL = 'http://localhost:3030';
const OUT_DIR = path.join(__dirname, 'screenshots');
const TOTAL_SLIDES = 30; // we'll stop when navigation fails

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Slidev uses 1280x720 by default
  await page.setViewportSize({ width: 1280, height: 720 });

  let slide = 1;
  while (slide <= 60) {
    await page.goto(`${BASE_URL}/${slide}`, { waitUntil: 'networkidle', timeout: 10000 }).catch(() => null);

    // Check if we've gone past the last slide (URL won't change or redirects to /1)
    const url = page.url();
    const currentSlide = parseInt(url.split('/').pop()) || 1;
    if (slide > 1 && currentSlide < slide) {
      console.log(`Reached end at slide ${slide - 1}`);
      break;
    }

    // Wait for fonts and shiki highlighting to render
    await page.waitForTimeout(800);

    const file = path.join(OUT_DIR, `slide-${String(slide).padStart(2, '0')}.png`);
    await page.screenshot({ path: file, fullPage: false });
    console.log(`Captured slide ${slide} → ${path.basename(file)}`);

    slide++;
  }

  await browser.close();
  console.log(`\nDone. Screenshots in: ${OUT_DIR}`);
})();
