import { chromium } from "playwright-core";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const EXE = "C:\\Users\\Utente\\AppData\\Local\\ms-playwright\\chromium-1217\\chrome-win64\\chrome.exe";
const htmlUrl = pathToFileURL(path.join(__dirname, "slides.html")).href;

const browser = await chromium.launch({ executablePath: EXE, headless: true });
const page = await browser.newPage({
  viewport: { width: 1080, height: 1350 },
  deviceScaleFactor: 2,
});

await page.goto(htmlUrl, { waitUntil: "networkidle", timeout: 60000 });
// Ensure web fonts are loaded before snapping
await page.evaluate(async () => { await document.fonts.ready; });
await page.waitForTimeout(400);

const ids = ["s1", "s2", "s3", "s4", "s5"];
for (let i = 0; i < ids.length; i++) {
  const el = page.locator(`#${ids[i]}`);
  const out = path.join(__dirname, `slide-${i + 1}.png`);
  await el.screenshot({ path: out });
  console.log("saved", out);
}

await browser.close();
console.log("DONE");
