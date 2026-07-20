# PLAYBOOK — skill-cro-ricerca / Client Research Engine (4 scenari)

Tutti gli scenari si appoggiano al master `SKILL.md` (mappa in spec.md) e ai 7 knowledge. Regola di
navigazione: NON rileggere 1.625 righe a ogni uso — aprire il blocco giusto dalla mappa.

## S1 — Avvio ricerca nuovo cliente (happy path)
**Trigger:** "Dobbiamo partire col copy/strategia per il cliente X" · handler `inizia_ricerca_nuovo_cliente`.
1. STEP 0 (master r. 269-369): verifica gli 8 prerequisiti (briefing, settore, prodotto, target, traffico,
   piattaforme attive, competitor noti, mercato IT/EN). Se briefing assente → chiedi i dati minimi, warn
   esplicito, poi procedi commisurando.
2. STEP 1: selezione piattaforme — SEMPRE YouTube+Google (+Reddit se tech/internazionale); B2B → +LinkedIn/
   forum; B2C → +Amazon/FB Groups/Trustpilot; mercato IT → forum e gruppi italiani.
3. Genera le **query ESATTE personalizzate** per piattaforma (mai generiche) + cosa cercare (commenti, non
   solo contenuti) + quanto raccogliere + come documentare (copia-incolla + URL).
4. Presenta il piano completo con tempi per piattaforma (R1: 2-4h) e guida piattaforma per piattaforma.
5. Knowledge di supporto: YOUTUBE/REDDIT/X masterclass per cosa estrarre in ciascuna.

## S2 — L'utente porta dati grezzi (ciclo analisi)
**Trigger:** "Ecco i commenti/screenshot che ho trovato" · handler `analizza_dati_grezzi`.
1. Identifica la fase (R1? R2? quale piattaforma?).
2. Estrai frasi ESATTE (mai parafrasi), pattern, categorie (pain/obiezioni/linguaggio/insight).
3. Verifica completezza: <20 frasi esatte in R1 → **ricerca aggiuntiva con query specifiche, non inventare**.
4. R2 (r. 625-735): per ogni competitor compila la scheda completa (headline, struttura, social proof,
   obiezioni gestite/non gestite, CTA, pricing, ToV, forza/debolezza/gap) — 3 diretti + 2 indiretti.
5. R3/R4/R5 (r. 736-1120): TOV tabella USA/EVITA 10+ coppie · pain in 4 categorie scored I×F×A top 5-7 +
   leva emotiva ciascuno · obiezioni in 5 categorie scored F×I top 5-7 con posizionamento (copy vs FAQ).
6. CROSS-PLATFORM (knowledge 7): pattern ripetuto su 3 piattaforme = pattern di mercato → priorità #1.

## S3 — Compilazione e consegna del Report
**Trigger:** fasi R1-R5 complete · handler `compila_report_finale`.
1. Verifica output di tutte e 5 le fasi; se manca qualcosa → **segnalalo nel report** (regola 7), non
   riempire di supposizioni.
2. Compila le 10 sezioni (r. 1121-1275: logica sezioni in §OUTPUT, r. 82-86) usando solo dati con fonte.
3. Applica il gate qualità (tools.md §standard): 13 voci complete o 7 minimum dichiarate.
4. Stile: bullet/tabelle, virgolettati esatti, scoring numerico, raccomandazioni azionabili
   ("Usa questa frase nel copy" > "È interessante notare che...").
5. Consegna → CRO Copy Architect (a valle). Ricorda: questa skill NON scrive il copy.

## S4 — Richiesta fuori perimetro o ricerca parziale
- **Non-ricerca** (handler `non_ricerca`): copy → CRO Copy Architect · briefing → (skill a monte, vedi
  spec §debito 2) · strategia → Agency Operations. Dillo in una riga e rimanda, senza eseguire.
- **Ricerca parziale** (handler `ricerca_parziale`): se non c'è tempo per 5-10h → versione minima 2.5h
  (solo YouTube 5 video + Reddit 5 thread; 1 competitor; top 3 pain + top 3 obiezioni) con avvertenza
  esplicita nel report su cosa manca e impatto sulla qualità del copy.
- **Uso W7 YouTube (04-MARKETING):** quando la richiesta nasce dal canale (validazione argomenti, linguaggio
  del freelance target, obiezioni "agenzie costano troppo"), lo stesso metodo R1-R5 alimenta
  `youtube-script-factory`: frasi esatte → hook; obiezioni top → sezione obiezioni dello script;
  TOV USA/EVITA → VOCE del canale. Passa l'output allo script, non "adattarlo a sentimento".
