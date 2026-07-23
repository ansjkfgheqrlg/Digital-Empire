# 03 — SHOTLIST (cosa si vede a schermo, scena per scena)

Legenda stato asset: **REGISTRARE** = va girato/generato per questa run (non esiste su disco) ·
**GENERARE** = grafica/slide da produrre (non richiede stock footage esterno) · nessuna scena di
questo video richiede stock footage generico (Pexels): è un tutorial procedurale, il contenuto
visivo principale è una registrazione schermo reale del setup + slide di testo.

---

## Scena 1 — HOOK (0:00–0:35)
- **Inquadratura:** schermo intero, editor/terminale con un progetto di test che ha un bug reale
  e visibile (form di contatto che non invia).
- **Azione a schermo:** il cursore digita il comando che invoca Claude Code; si vede l'output che
  identifica e corregge il file in pochi secondi (accelerato leggermente in montaggio, max 2x, per
  restare onesti sulla velocità reale).
- **Overlay testo:** "0 COPY-PASTE" in basso a destra, font sans-serif bold (Onest/Inter), colore
  arancione Claude #fb4604 su sfondo scuro (pattern da `02_PATTERN_VINCENTI.md` §2).
- **Stato asset:** REGISTRARE (serve un progetto di test con un bug reale riproducibile).

## Scena 2 — CTA GRATUITA (0:35–1:10)
- **Inquadratura:** slide a schermo intero.
- **Elementi grafici:** copertina "Manuale Claude Code — Parte 1 (GRATIS)", freccia animata verso
  il basso che punta all'area descrizione, testo "link qui sotto ⬇" (nel video: emoji solo in
  overlay grafico, mai nell'audio/TTS).
- **Stato asset:** GENERARE (slide statica, nessuna dipendenza da stock footage).

## Scena 3 — PROBLEMA (1:10–2:45)
- **Inquadratura:** split screen — a sinistra browser con ChatGPT aperto e codice incollato a
  mano, a destra lo stesso codice dentro l'editor con evidenziato un errore di variabile.
- **Overlay testo:** 3 bullet che appaiono in sync col parlato ("Non vede il progetto" /
  "Lavora solo su copia-incolla" / "Passacarte browser-editor").
- **Stato asset:** REGISTRARE (screencast reale di un confronto ChatGPT-browser vs terminale).

## Scena 4 — REQUISITI DI SISTEMA (2:45–3:45)
- **Inquadratura:** slide con 3 icone (Node.js, account Anthropic, terminale) che appaiono una a
  una in sync col parlato ("Uno... Due... Tre...").
- **Stato asset:** GENERARE (slide, nessuna clip necessaria).

## Scena 5 — INSTALLAZIONE DEL PACCHETTO (3:45–5:00)
- **Inquadratura:** terminale a schermo intero, font monospace grande e leggibile (min 18pt per
  leggibilità mobile), digitazione reale (non simulata).
- **Azione a schermo:** `node -v` → output versione; poi `npm install -g @anthropic-ai/claude-code`
  → output di installazione fino al prompt libero.
- **Nota produzione:** verificare il comando di installazione esatto al momento della
  registrazione (i pacchetti CLI cambiano nome/versione nel tempo) — non fidarsi ciecamente dello
  script se il comando risultasse deprecato.
- **Stato asset:** REGISTRARE.

## Scena 6 — AUTENTICAZIONE (5:00–6:15)
- **Inquadratura:** terminale → transizione a finestra browser (pagina di autorizzazione
  Anthropic) → ritorno al terminale con conferma.
- **Stato asset:** REGISTRARE (richiede un vero flusso di login, non simulabile con grafica).

## Scena 7 — PRIMO TEST REALE (6:15–8:45)
- **Inquadratura:** terminale a schermo intero.
- **Azione a schermo:** prompt digitato dal vivo ("controlla perché il form di contatto non invia
  l'email"), output di Claude Code che legge i file, mostra il diff proposto, utente preme invio,
  file modificato — evidenziare con un riquadro/freccia il punto esatto del diff.
- **Stato asset:** REGISTRARE (stesso progetto di test della Scena 1, continuità narrativa).

## Scena 8 — ERRORI COMUNI (8:45–10:00)
- **Inquadratura:** slide con 3 punti numerati che appaiono in sync; per il punto 2 inserire uno
  screenshot reale di un errore di compatibilità Node (va catturato, non simulato con testo finto).
- **Stato asset:** REGISTRARE (screenshot errore reale) + GENERARE (slide contenitore).

## Scena 9 — OFFERTA & CTA FINALE (10:00–12:30)
- **Inquadratura:** slide copertina Manuale completo + elenco puntato animato dei 3 bonus
  (`.claudeignore`, cheatsheet 50+ comandi, guida MCP) + prezzo in sovrimpressione (67 euro).
- **Stato asset:** GENERARE.

## Scena 10 — CHIUSURA (12:30–13:00)
- **Inquadratura:** slide di chiusura con bottone "Iscriviti" animato + invito al commento.
- **Stato asset:** GENERARE.

---

## Nota onesta sulla dipendenza "stock footage" della ladder di render
La ladder generale dello stream S5 prevede, al gradino 2, "script + stock footage (Pexels) + TTS +
ffmpeg". Per **questo video specifico** la voce "stock footage" non è il collo di bottiglia
principale: è un tutorial procedurale che vive quasi interamente di screen recording reale (non di
b-roll generico acquistabile su Pexels). I veri asset mancanti per completare il render sono due:
1. una registrazione schermo reale delle Scene 1/3/5/6/7/8 (serve un ambiente con un progetto di
   test predisposto, da girare a mano — non producibile da questo tool senza un umano al terminale),
2. l'audio di narrazione sintetizzato da `02-TTS.txt` (nessun motore TTS disponibile nel perimetro
   di questo lotto, per policy "nessuna dipendenza nuova" — vedi `05-STATO.md`).
Le slide (Scene 2/4/9/10) sono generabili senza stock footage con qualunque tool di grafica/slide.
