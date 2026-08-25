const fs = require('fs');
let content = fs.readFileSync('porco-dio-empire.html', 'utf8');
const lines = content.split('\n');

let newLines = [];
let i = 0;
while (i < lines.length) {
    let line = lines[i];

    // Modify sticky CTA text
    if (line.includes('Scopri i Framework')) {
        line = line.replace('Scopri i Framework', 'Scegli un Percorso');
    }

    // Hide form section initially
    if (line.includes('id="form-section"') && line.includes('class="bg-ink-2')) {
        line = line.replace('class="bg-ink-2', 'class="bg-ink-2 hidden');
    }

    // Update openForm JS function
    if (line.includes("const target = document.getElementById('form-section');")) {
        newLines.push(line);
        newLines.push("      target.classList.remove('hidden');");
        i++;
        continue;
    }

    // Skip the sections we want to delete
    if (line.includes('<!-- ===================== STATS (bg-ink) ===================== -->')) {
        // Skip until we reach the form section
        while (i < lines.length && !lines[i].includes('<!-- ===================== CTA FINALE + FORM (bg-ink-2) ===================== -->')) {
            i++;
        }
        continue; 
    }

    newLines.push(line);
    i++;
}

fs.writeFileSync('porco-dio-empire.html', newLines.join('\n'), 'utf8');
console.log('Modified porco-dio-empire.html successfully');
