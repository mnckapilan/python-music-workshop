// Screenshots specific slides at mid-step to verify pointer behaviour
const { chromium } = require('@playwright/test');
const path = require('path');

const BASE_URL = 'http://localhost:3030';
const OUT_DIR = path.join(__dirname, 'screenshots');

const targets = [
  { slide: 8,  clicks: 1, label: 'variables-code-step1'     },  // line 1 only
  { slide: 9,  clicks: 1, label: 'fstrings-step1'            },  // line 1 only
  { slide: 17, clicks: 1, label: 'loops-code-step1'          },  // line 1 only
  { slide: 22, clicks: 1, label: 'conditionals-code-step1'   },  // line 1 only
  { slide: 31, clicks: 1, label: 'why-functions-step1'       },  // first block step
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 720 });

  for (const { slide, clicks, label } of targets) {
    await page.goto(`${BASE_URL}/${slide}`, { waitUntil: 'networkidle', timeout: 10000 });
    await page.waitForTimeout(600);

    // Click to advance to the desired step
    for (let i = 0; i < clicks; i++) {
      await page.keyboard.press('ArrowRight');
      await page.waitForTimeout(300);
    }

    const file = path.join(OUT_DIR, `step-${label}.png`);
    await page.screenshot({ path: file });
    console.log(`Captured step: ${label}`);
  }

  await browser.close();
})();
