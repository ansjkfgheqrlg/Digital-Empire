# EMP-VPEE — Produzione 3 video Legamidiamore - script pronti, produzione da lanciare

- **Codice di ripresa:** `EMP-VPEE`
- **Aperto:** 2026-09-04 11:21
- **Stato:** APERTO
- **Chi riprende:** basta dire `EMP-VPEE` in una chat nuova dentro Digital Empire.

---

## 1. IL LAVORO IN UNA FRASE

ADR-021 pivot piano + produzione di giornata (ordine Max: 3 video oggi, uno alla volta, finiti bene). Max ha fermato qui per troppo contesto in chat — si riprende da zero contesto ma con questo file.

---

## 2. DOVE SIAMO — cosa e' FATTO davvero

- **ADR-021 scritto e attivo**: `company/Memory/decisions/ADR-021-pivot-piano-legamidiamore.md`. Decisione: le 3 strategie del piano 70 video non partono piu' in parallelo. Solo Strategia A attiva; B e C in pausa dichiarata (non cancellate) finche' A non tiene >=3 video/settimana per 3 settimane di fila. Verifica fissata al 2026-09-24. Causa vera del ritardo (89,5% sui primi 8 giorni): NON le strategie, ma `coda_produzione.json` che accetta solo script scritti a mano — dal lancio del piano (27/8) ne era stato scritto uno solo.
- **`memory/copy_intelligence_legamidiamore.json` creato** (non esisteva mai prima): 7 schemi favorevoli + 1 sfavorevole, dati reali gia' misurati altrove, mai formalizzati nel file che la pipeline legge davvero.
- **`memory/piano_editoriale_70.json`**: aggiunto blocco `_revisione_20260903` che documenta il pivot, le 70 righe originali intatte (niente cancellato).
- **`memory/coda_produzione.json`**: rifornita con 3 video pronti in ordine: `chVKOBlEpDI`, `qHB80wbamBI`, `XABjAjqfUxw` (tutti Strategia A, canale legamidiamore).
- **3 script adattati scritti da zero** in `05-TEMPLATES-E-KIT/script-adattati/`:
  - `chVKOBlEpDI.md` — **PRONTO, passa tutti e 3 i gate reali** (12,34 min, 0 sovrapposizioni con la fonte, 3 elementi di valore aggiunto).
  - `qHB80wbamBI.md` — **PRONTO, passa tutti e 3 i gate reali** (12,71 min, 0 sovrapposizioni, 3 elementi di valore aggiunto).
  - `XABjAjqfUxw.md` — **QUASI PRONTO, manca 1 gate**: 13,08 min OK, 0 sovrapposizioni OK, ma solo **2 elementi di valore aggiunto su 3 richiesti** (`MIN_ELEMENTI_NUOVI=3` in `regolatori.py`). Trovati finora: "effetto alone", "postura di confronto". Ne serve UNO in piu' con la stessa formula esatta.
- **video-05 sbloccato** (sessione precedente, CP-013/016): upload 100%, Privato per sicurezza, ancora da pubblicare — vedi debiti sotto.

## 3. COSA E' RIMASTO A META'

- **Nessun video prodotto per davvero oggi.** 3 tentativi di lancio di `produci_video_completo.py` su `chVKOBlEpDI`, tutti falliti in Fase 3 (script/orchestratore, PRIMA di spendere crediti Fliki/Arena — nessuna spesa reale avvenuta), per 3 gate diversi scoperti uno alla volta dal vivo:
  1. `apex7_orchestrator.py PAROLE_MINIME_SCRIPT=2220` (12 min a 185 parole/min) — non gli 8-10 min assunti da un vecchio gate diverso (`regolatori.py DURATA_MINIMA_S=480s`). Risolto: tutti e 3 gli script espansi.
  2. `regolatore-originalita` (n-grammi di 8+ parole identiche al transcript sorgente = BLOCCO). Risolto su `chVKOBlEpDI` e `qHB80wbamBI` con riscrittura mirata delle frasi troppo vicine alla fonte (verificato a 0 sovrapposizioni con lo script diretto `regolatori.verifica_originalita`).
  3. `MIN_ELEMENTI_NUOVI=3` (concetti nominati con formula esatta `lo chiamano|la chiamano|si chiama|viene chiamato|conosciuto come X` — ATTENZIONE: la frase deve stare su una riga sola, un "a capo" nel mezzo rompe il match perche' il regex usa uno spazio letterale, non `\s+`). Risolto su `chVKOBlEpDI` e `qHB80wbamBI`. **XABjAjqfUxw ancora a 2/3, non ancora ritentato.**
- **La produzione vera e propria (copertina Arena + video Fliki, che spende crediti reali) non e' MAI partita**: tutti i fallimenti sono avvenuti prima, nell'orchestratore. Nessun euro/credito speso finora su questi 3 video.

## 4. IL PROSSIMO PASSO ESATTO

1. Aggiungere UN quarto "concetto nominato" a `05-TEMPLATES-E-KIT/script-adattati/XABjAjqfUxw.md` (stessa formula: `lo chiamano X` / `la chiamano X` / `si chiama X`, tutto su una riga sola, X = 1-4 parole minuscole). Verificare con:
   ```
   cd "YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS"
   PYTHONIOENCODING=utf-8 python -c "import sys; sys.path.insert(0,'.'); from regolatori import _elementi_nuovi; print(_elementi_nuovi(open('../05-TEMPLATES-E-KIT/script-adattati/XABjAjqfUxw.md',encoding='utf-8').read()))"
   ```
   Deve stampare 3 elementi.
2. Lanciare la produzione reale del video 1 (`chVKOBlEpDI`, gia' pronto):
   ```
   cd "YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS"
   PYTHONIOENCODING=utf-8 python produci_video_completo.py
   ```
   Lanciarlo in background, aspettare la notifica, NON toccare/ricaricare nulla nel frattempo.
3. Se OK (mp4 + copertina generati): passare all'upload reale con `youtube_uploader_playwright.py` (SEMPRE aspettare fine reale, mai reload/nuova finestra sullo stesso profilo Chrome — vedi trappole sotto), poi ripetere per `qHB80wbamBI` e infine `XABjAjqfUxw`, UNO ALLA VOLTA come ordinato da Max — non parallelizzare.
4. Dopo i 3 video: checkpoint + aggiornare `memory/video_prodotti.json` (oggi ha ancora dati vecchi/sbagliati, vedi debito aperto in CP-016) + STATO-EMPIRE.

---

## 5. DECISIONI GIA' PRESE — non ridiscuterle

- **ADR-021**: solo Strategia A attiva, B e C in pausa fino a cadenza dimostrata (3 video/settimana x 3 settimane, verifica 24/9). Non riaprire la discussione su questo senza nuovi dati.
- **Target reale di durata per gli script Legamidiamore: 12-15 minuti (>=2220 parole a 185 parole/min)**, non 8-10 minuti. La nota "8-10 min" scritta in vecchi header di script (es. versione originale di `chVKOBlEpDI.md` del 23/8) e' SBAGLIATA/obsoleta — verificato dal vivo il 2026-09-04 col fallimento reale in Fase 3. Non fidarsi di quella nota se compare altrove nel repo.
- **I 2 video fermi in Privato** (`6hrhlS9jC4g`, `RIZuutLaEV0`) restano una decisione di Max, non presa in questa sessione — proporglieli, non pubblicarli di iniziativa.

## 6. TRAPPOLE — errori gia' fatti, non rifarli

- **MAI `page.reload()` o nuova navigazione su una pagina Playwright mentre un upload/produzione e' in corso** — l'ho scoperto a mie spese su video-05 (sessione precedente, CP-013): un reload "solo per controllare" abortisce l'upload in corso. Vale anche per eventuali controlli di stato: leggere un file di log e' sicuro, toccare il browser no.
- **Il regex di `_CONCETTO_NOMINATO` in `regolatori.py` usa uno spazio LETTERALE**, non `\s+`: se markdown va a capo nel mezzo di "lo chiamano X" (es. "lo\nchiamano"), il match fallisce silenziosamente. Sempre tenere la frase-trigger su una riga fisica sola.
- **Non fidarsi di UN SOLO gate verificato**: questo pomeriggio ne sono saltati fuori 3 diversi in sequenza (durata orchestratore, originalita' n-grammi, elementi di valore aggiunto), ognuno scoperto solo lanciando davvero l'orchestratore. Prima di dichiarare uno script "pronto", far girare tutti e 3 i controlli assieme (vedi comando sopra) invece di fermarsi al primo che passa.
- **`memory/video_prodotti.json` e `coda_produzione.json` non sono la stessa cosa**: il primo traccia cosa e' stato prodotto (e oggi ha 3 voci su 5 sbagliate, di un altro canale), il secondo cosa e' IN CODA da produrre. Non confonderli quando si aggiorna lo stato.

---

## 7. COMANDI PER RIPARTIRE

```bash
cd "YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS"
# 1. verifica/completa XABjAjqfUxw (vedi punto 4.1 sopra)
# 2. poi:
PYTHONIOENCODING=utf-8 python produci_video_completo.py --preflight
PYTHONIOENCODING=utf-8 python produci_video_completo.py
```

## 8. FILE TOCCATI

- `company/Memory/decisions/ADR-021-pivot-piano-legamidiamore.md` (nuovo)
- `company/Memory/checkpoints/CP-20260903-016.md`, `CP-20260903-018.md` (nuovi, sessione precedente)
- `company/Memory/STATO-EMPIRE.md` (aggiornato)
- `YOUTUBE-AUTOMATION-FACTORY/memory/coda_produzione.json` (rifornita)
- `YOUTUBE-AUTOMATION-FACTORY/memory/copy_intelligence_legamidiamore.json` (nuovo)
- `YOUTUBE-AUTOMATION-FACTORY/memory/piano_editoriale_70.json` (blocco `_revisione_20260903` aggiunto)
- `YOUTUBE-AUTOMATION-FACTORY/05-TEMPLATES-E-KIT/script-adattati/chVKOBlEpDI.md` (espanso e riscritto, PRONTO)
- `YOUTUBE-AUTOMATION-FACTORY/05-TEMPLATES-E-KIT/script-adattati/qHB80wbamBI.md` (scritto da zero, PRONTO)
- `YOUTUBE-AUTOMATION-FACTORY/05-TEMPLATES-E-KIT/script-adattati/XABjAjqfUxw.md` (scritto da zero, manca 1 gate)
- `YOUTUBE-AUTOMATION-FACTORY/memory/_transcript_pulito_*.txt` (3 transcript reali salvati, utili se serve riscrivere ancora)

---

*Chiudi con: `python scripts/checkpoint.py chiudi EMP-VPEE`*
