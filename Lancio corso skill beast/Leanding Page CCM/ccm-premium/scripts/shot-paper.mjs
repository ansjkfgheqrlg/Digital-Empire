import { chromium } from "@playwright/test";
const b = await chromium.launch();
const c = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1.5 });
const p = await c.newPage();
await p.goto("http://localhost:3000", { waitUntil: "networkidle", timeout: 60000 });
await p.waitForTimeout(1200);
// scroll to white section
await p.evaluate(() => window.scrollTo(0, 2400));
await p.waitForTimeout(800);
await p.screenshot({ path: "reference/ccm-paper.png" });
await p.evaluate(() => window.scrollTo(0, 5200));
await p.waitForTimeout(800);
await p.screenshot({ path: "reference/ccm-mid.png" });
console.log("shot ok");
await b.close();
