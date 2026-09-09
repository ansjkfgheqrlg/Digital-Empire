# CORSIA B — i riferimenti di scaffolding, arrivati da `empire-premium-style`

**Fusione eseguita il 2026-09-09**, come deciso nel dossier 33 §5 e in ADR-023.
Questi sei file **erano** l'ossatura della skill `empire-premium-style`. Ora vivono qui, dentro la
Fabbrica, perché la Fabbrica è l'unico posto da cui si costruisce un sito.

| File | Righe | Cosa serve |
|---|---|---|
| `reference-page-full.tsx` | 837 | **la libreria di sezioni già scritte** — 17 pattern in React, da cui la Corsia B copia struttura |
| `components.md` | 174 | i componenti e le loro classi |
| `build-playbook.md` | 66 | l'ordine dei passi di scaffolding Next.js |
| `layout-template.md` | 50 | il layout con smooth scroll e grana |
| `package.json.md` | 82 | le dipendenze, con le versioni |
| `reference-layout.tsx` | 37 | il layout minimo |

---

## Cosa è cambiato, e perché non è una copia

**Il canone non si è mosso di un valore.** Confrontati carattere per carattere i nove colori
condivisi fra `design-tokens.css` (empire-premium-style) e `canone/canone.css` (Fabbrica):

```
--orange #fb4604 · --orange-bright #ff6a2e · --orange-deep #c9370a
--silver #d9d4e1 · --silver-bright #ffffff · --silver-dim #8a8594
--ink #1c1c1c · --paper #fafafa · --grey #e8e8e6
```

**Identici, tutti e nove.** La fusione dei valori era già avvenuta con ADR-023: quello che restava
non era il colore, era **la struttura**. Ed è ciò che è arrivato qui.

**I 53 token `--color-*` di `design-tokens.css` NON entrano nel canone.** Sono il ponte verso
Tailwind v4 e shadcn (`--color-primary`, `--color-popover-foreground`, …): appartengono alla Corsia
B, non alla legge. Il canone resta vanilla-first come impone §5 — *dal vanilla al framework si sale,
dal framework al vanilla si riscrive*.

**`section-patterns.md` è morto.** Aveva 117 righe e **10 puntatori su 17 già stale** (righe di
`reference-page-full.tsx` che non corrispondevano più). Lo sostituisce la galleria generata:

```
python .claude/skills/fabbrica-siti/scripts/galleria.py
```

Una galleria che si rigenera dal disco non può diventare stale: è la stessa legge di
`stato_onde.py` nello studio — *ciò che dichiara "fatto" deve essere una macchina che guarda il
disco*.

---

## Come si usa questa cartella

1. Il cantiere sceglie la corsia con §5 della legge (≤3 pagine e nessuno stato → vanilla; il resto → Next.js 16).
2. Se è Corsia B, si parte da `build-playbook.md` e `package.json.md`.
3. Le sezioni si prendono da `reference-page-full.tsx`, **ma i valori vengono dal canone**, non dal
   file: se i due divergono, ha ragione il canone.
4. Il pattern nuovo si scrive **prima in vanilla** in `pattern/<nome>/`, poi la Corsia B lo avvolge
   (`pattern/CORSIA-B.md`).

---

## Connessioni
- `../CLAUDE-SITI.md` — la legge, §5 le due corsie
- `../pattern/CORSIA-B.md` — come si avvolge un pattern vanilla
- `../canone/canone.css` — i valori, l'unica fonte
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md` §5 — il perimetro della fusione
- `company/Memory/decisions/ADR-023-fabbrica-siti-due-corsie.md`
