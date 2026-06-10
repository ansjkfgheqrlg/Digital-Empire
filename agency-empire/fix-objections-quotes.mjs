import { readFileSync, writeFileSync } from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const filePath = path.join(__dirname, "src", "sections", "15-objections.tsx");

let src = readFileSync(filePath, "utf8");

// Replace curly left quote U+201C with “ escape
src = src.split("“").join("\\u201C");
// Replace curly right quote U+201D with ” escape
src = src.split("”").join("\\u201D");

writeFileSync(filePath, src, "utf8");
console.log("Done. Replaced curly quotes with Unicode escapes.");
