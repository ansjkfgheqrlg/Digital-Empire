# ADR-013 — Blob pesanti fuori dalla storia git: .gitignore mirato + guard, NON Git LFS

- **Data:** 2026-08-27
- **Stato:** ATTIVO
- **Decisori:** sessione TASK-GITLFS-W1 (Claude), delega esplicita nella task
  ("una decisione presa e applicata, non solo scritta in backlog")
- **Chiude:** BACKLOG B-008 (aperto dal 2026-06, mai chiuso)

## Contesto — i numeri, non le impressioni

Misurato sulla storia reale del monorepo il 2026-08-27:

| | peso | file |
|---|---|---|
| `.png` | **2167,5 MB** | 10.679 |
| `.pdf` | 434,7 MB | 154 |
| `.pma` | 210,0 MB | 54 |
| `.md` | 182,8 MB | 10.015 |
| `.exe` | 110,8 MB | 3 |

`.git` pesa **3,1 GB**, working tree 5,0 GB. Le PNG da sole sono ~70% del repo.

**Il motore della crescita sono le copertine KDP**, non gli screenshot: 2,5-6,1 MB
l'una, e ogni libro ne tiene 3-4 copie (`copertina.png`, `copertina_kdp.png`,
`copertina_finale.png`, `Cover_<Titolo>.png`) = **~15 MB per libro**. Con l'obiettivo
dichiarato di **5-10 libri/settimana** fa **4-8 GB/anno di sole copertine**.

Secondo contributore, più piccolo ma gratuito da eliminare: gli intermedi di render
dei caroselli. Ogni `slide-NN.html` pesa ~628 KB perché **incorpora il font in
base64**, e ce n'è uno per slide: ~3,8 MB per carosello, di cui quasi tutto è lo
stesso font ripetuto 6 volte.

Rischio già materializzato una volta: un push da 899 MB morto per rete instabile.

## Decisione

**1. Git LFS: NON adottato.** Motivi, in ordine di peso:
   - La quota gratuita GitHub LFS è **1 GB**. Al ritmo misurato (4-8 GB/anno di sole
     copertine) si esaurisce in **settimane**, e oltre la quota il push *fallisce*.
     LFS non risolve il problema di volume: lo sposta in un secchio più piccolo.
   - Richiede `git lfs install` su **ogni** macchina. Se manca su una, quella macchina
     scarica **file-puntatore da 130 byte al posto delle immagini**, senza errore
     evidente. In un team di due persone che ha già perso ore su un merge, introdurre
     un modo nuovo e silenzioso di rompersi è il compromesso sbagliato.
   - Non risolve la duplicazione 3-4×: pagheremmo quota per la stessa copertina quattro volte.

**2. `.gitignore` mirato sugli artefatti di pubblicazione** (applicato):
   - `**/LIBRI/**/copertina*.png`, `**/LIBRI/**/Cover_*.png`
   - `**/libri_pronti/**/*.pdf`, `*.epub`, `*.docx`
   - `**/Arsenale Caroselli/**/slide-*.html`
   - `**/_diagnostica/`, `**/debug_screens*/`, `**/debug_*.png`, `**/*_diagnostic*.png`

   Il criterio non è "è pesante", è **"si rigenera e non viaggia fra Max e Gael"**.
   Una copertina va su KDP, non da Max a Gael: nel repo resta il `COPERTINA-PROMPT.md`
   che la rigenera, che è il sorgente vero. Stesso ragionamento per gli `slide-*.html`:
   il deliverable è il PNG.

**3. Un guard che lo fa rispettare da solo** — `.githooks/check_blob.py`, blocca in
   pre-commit qualsiasi file **> 5 MB** diretto alla storia normale. È il backstop per
   ciò che le regole non prevedono: le estensioni cambiano, il peso no. Soglia scelta
   sui dati: il deliverable legittimo più grosso (slide carosello 0,9 MB, PDF libro
   ~3 MB) sta sotto, quindi **il guard non spara sul lavoro normale** — e un guard che
   non dà falsi allarmi è un guard che nessuno disattiva.
   Deroghe motivate in una lista dentro il file, non con `--no-verify`.

## Cosa NON è stato fatto, di proposito

**Le copertine dei 4 libri già tracciati restano tracciate.** `git rm --cached` le
toglierebbe dal tracciamento, ma al primo `git pull` **sparirebbero dal disco di Max**:
se le ha solo lì, le perde. Non è una decisione che prendo per lui in una sessione dove
non c'è.

Comando pronto, da eseguire **con Max presente e dopo che ha una copia**:

```bash
git rm --cached -- "company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/LIBRI/**/copertina*.png"
```

La storia esistente non si riscrive (la task lo escludeva esplicitamente): l'obiettivo
era che **da ora in poi** il repo non ingrassi, e quello è ottenuto — i file nuovi
nascono già ignorati.

## Prova (gate)

Commit di prova su branch temporaneo, cartella con 3 file, `git add -A`:

```
$ git log --stat -1
 .githooks/check_blob.py                            | 122 +++++
 .githooks/check_memory.py                          | 230 +++++
 .githooks/pre-commit                               |  35 ++
 .gitignore                                         |  28 ++
 .../in_lavorazione/test-libro/COPERTINA-PROMPT.md  |   2 +
 5 files changed, 417 insertions(+)
```

`debug_prova.png` (0,17 MB) e `copertina_kdp.png` (5,26 MB) **non compaiono**: è entrato
solo il sorgente. Forzando la copertina con `git add -f`, il guard blocca:
`git commit exit = 1`.

## Alternative scartate

- **LFS per tutto il pesante** — vedi punto 1: quota, fallimento silenzioso, duplicazione.
- **Riscrivere la storia (`filter-repo`/BFG)** — recupererebbe i 3,1 GB già spesi, ma
  riscrive ogni SHA: rompe i clone esistenti e ogni riferimento a commit nei checkpoint
  della memoria. Costo alto, beneficio una tantum, e la task lo escludeva. Se un giorno
  servirà, va fatto in una sessione dedicata con entrambi i soci fermi.
- **Solo la regola scritta nel backlog** — già provata: B-008 è rimasto aperto da giugno
  ad agosto proprio così.

## Contradiction-check

Nessun conflitto con ADR-001/002/003. Coerente con ADR-005 (il backlog non blocca: qui
lo si chiude). Il `.gitattributes` esistente (`* -text`) **non** viene toccato.

## Connessioni

- Guard gemello sulla memoria: `.githooks/check_memory.py` (B-009 + B-028)
- Attivazione su una macchina: `python .githooks/installa.py`
