import { chromium } from "@playwright/test";
import fs from "node:fs/promises";
import path from "node:path";

const OUT = path.resolve("reference");
await fs.mkdir(OUT, { recursive: true });

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();

await page.goto("https://claude-speedrun.com/", { waitUntil: "networkidle", timeout: 60000 });
await page.waitForTimeout(2500);

// Full page screenshot
await page.screenshot({ path: path.join(OUT, "fullpage.png"), fullPage: true });
// Hero screenshot
await page.screenshot({ path: path.join(OUT, "hero.png"), fullPage: false });

// HTML
const html = await page.content();
await fs.writeFile(path.join(OUT, "page.html"), html);

// Extract structured design info
const design = await page.evaluate(() => {
  const body = document.body;
  const cs = getComputedStyle(body);
  const pickFont = (el) => {
    const s = getComputedStyle(el);
    return { tag: el.tagName, text: (el.innerText||"").slice(0,80), font: s.fontFamily, size: s.fontSize, weight: s.fontWeight, style: s.fontStyle, color: s.color, lineHeight: s.lineHeight, letterSpacing: s.letterSpacing };
  };
  const headings = Array.from(document.querySelectorAll("h1,h2,h3")).slice(0,20).map(pickFont);
  const buttons = Array.from(document.querySelectorAll("a,button")).slice(0,20).map(el => {
    const s = getComputedStyle(el);
    return { tag: el.tagName, text: (el.innerText||"").slice(0,40), bg: s.backgroundColor, bgImage: s.backgroundImage, color: s.color, border: s.border, borderRadius: s.borderRadius, padding: s.padding, boxShadow: s.boxShadow };
  });
  const sections = Array.from(document.querySelectorAll("section, main > div, header, footer")).slice(0,30).map(el => ({
    tag: el.tagName,
    className: el.className?.toString().slice(0,100),
    text: (el.innerText||"").slice(0,200).replace(/\s+/g," ")
  }));
  return {
    bodyBg: cs.backgroundColor,
    bodyBgImage: cs.backgroundImage,
    bodyColor: cs.color,
    bodyFont: cs.fontFamily,
    title: document.title,
    headings,
    buttons,
    sections,
  };
});
await fs.writeFile(path.join(OUT, "design.json"), JSON.stringify(design, null, 2));

console.log("Done. Saved to", OUT);
await browser.close();
