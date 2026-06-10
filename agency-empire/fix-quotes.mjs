import { readFileSync, writeFileSync } from 'fs';

const LEFT_CURLY = '“';   // "
const RIGHT_CURLY = '”';  // "

let content = readFileSync('src/sections/15-objections.tsx', 'utf8');

const before = [...content].filter(c => c === LEFT_CURLY || c === RIGHT_CURLY).length;

content = content.split(LEFT_CURLY).join('\\u201C');
content = content.split(RIGHT_CURLY).join('\\u201D');

const after = [...content].filter(c => c === LEFT_CURLY || c === RIGHT_CURLY).length;

writeFileSync('src/sections/15-objections.tsx', content, 'utf8');
console.log(`Replaced: ${before} curly quotes → ${after} remaining`);
