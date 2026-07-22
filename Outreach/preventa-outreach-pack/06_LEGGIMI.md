# LEGGIMI - Come usare il pacchetto outreach Preventa
### Per Max - Workflow di allargamento S1 oltre i 7 lead caldi WF-S1

Questo pacchetto è autonomo e serve per i lead NUOVI scoperti via Google Maps scraping. WF-S1 rimane intatto per i 7 lead caldi già in lavorazione (01-AGENCY). Questo è il motore per S1-FREDDO.

---

### 1. COSA C'È DENTRO E QUANDO USARLO

| File | Cosa è | Quando lo usi | Output atteso |
|------|--------|---------------|---------------|
| **01_SCRIPT_CHIAMATA_FREDDA** | Script chiamata APSOC completo, con 10 obiezioni | Ogni chiamata a concessionario da Maps | Demo fissata 15 min |
| **02_SCRIPT_WHATSAPP_EMAIL_3MSG** | Sequenza 3 messaggi scritti <600 char | Dopo chiamata senza risposta, o se hai solo cellulare/email | Risposta + micro-impegno |
| **03_ARGOMENTARIO_OBIEZIONI** | Tabella obiezione -> cosa nasconde -> risposta -> prova | Durante call e per allenare agente AI | Obiezione superata senza perdere lead |
| **04_5_VARIANTI_GANCIO_AB** | 5 aperture diverse da testare | Prime 150 chiamate per trovare gancio vincente zona per zona | Trovare gancio con >15% conversione demo |
| **05_FOLLOW_UP_G2_G5** | Copioni giorno +2 e +5 (voce + testo) | Dopo primo contatto senza demo fissata | Recupero 20-30% lead persi senza essere insistente |

---

### 2. WORKFLOW OPERATIVO COMPLETO (per agente / umano)

#### STEP 0: SCRAPING GOOGLE MAPS (Input)
Input agente: "Concessionari auto [Provincia]" -> Estrai: Nome, indirizzo, telefono, sito, recensioni, marchi da foto/sito.
Arricchimento rapido: Vai su sito -> trova nome titolare (chi siamo) -> trova 1 modello in pronta consegna.

#### STEP 1: PRIMO TOCCO - CHIAMATA (01 + 04)
Usa 01_SCRIPT_CHIAMATA. Per apertura scegli 1 gancio da 04 in base a:
- Se non conosci nulla -> Gancio 1 (Tempo perso)
- Se titolare + concessionario grande -> Gancio 4 (Controllo prezzi)
- Se città satura -> Gancio 2 (Cliente perso WA)

**Se risponde e parla >20 sec:** Vai a qualifica + pitch APSOC -> Chiudi con appuntamento.

**Se non risponde / segreteria:** Passa subito a STEP 2.

#### STEP 2: SECONDO TOCCO - WHATSAPP MSG1 (02)
Entro 60 secondi dalla chiamata senza risposta, invia WA MSG1 (Gancio).
Esempio automazione agente: `send_whatsapp(to=numero_maps, template=MSG1, vars=[Nome, Concessionaria, Marchi, Provincia])`

#### STEP 3: GESTIONE RISPOSTE (03)
Se risponde con obiezione, agente classifica obiezione con tabella 03 e risponde con risposta parola-per-parola + asset.
Mai vendere in chat. Obiettivo sempre: portare a demo 15 min.

#### STEP 4: VALORE + CHIUSURA - MSG2 e MSG3 (02)
Se risponde positiva a MSG1 -> MSG2 (valore/prova) -> offri esempio PDF.
Se accetta esempio -> MSG3 con 2 orari per demo.
Se non risponde a MSG1 dopo 24h -> invia MSG2.

#### STEP 5: FOLLOW-UP AUTOMATICO (05)
Se dopo STEP 1-4 non hai fissato demo:
- G+2: Scenario B (se ha parlato) o Scenario C (se mai risposto)
- G+5: Ultimo tocco + chiusura elegante "Ti archivio?"
Dopo G+5 -> tagga come "Freddo - Ricontatto 45gg". Non spammare.

#### STEP 6: DEMO 15 MIN (Non in questo pacchetto, ma output)
Demo = mostra 1 preventivo fatto con loro auto reale. Non slide. Solo schermo Preventa -> PDF.
Chiusura demo: Micro-impegno prova con 2 venditori a canone [PREZZO]. Kill-switch come garanzia.

---

### 3. MAPPA CONSAPEVOLEZZA APSOC IN TUTTO IL FUNNEL

| Fase | Consapevolezza | Asset | Messaggio chiave |
|------|----------------|-------|------------------|
| Maps Scraping | Unaware | Gancio 1/2/3 | "C'è un problema che non stai misurando: perdi tempo e clienti" |
| Chiamata qualifica | Problem-Aware | 01 - domande qualifica | "Quanto tempo perdi? Succede anche a voi?" |
| Pitch + WA MSG2 | Solution-Aware | 01 Pitch + 02 MSG2 + esempio PDF | "Esiste modo per fare PDF in 2 min brandizzato, non su Excel" |
| Gestione obiezioni + MSG3 | Product-Aware | 03 Argomentario + 02 MSG3 | "Preventa lo fa così, a canone [PREZZO], con kill-switch, provato da X" |
| Demo | Most-Aware | Demo live | "Ecco il TUO preventivo, con i TUOI prezzi" |

Non saltare livelli. Se parti subito con "Ho un software" a uno unaware, ti chiude.

---

### 4. VARIABILI DA PERSONALIZZARE (Placeholder)

Prima di lanciare workflow, sostituisci nel tuo agente:

- `[Nome]` -> Nome titolare / responsabile (se non lo hai, usa "Buongiorno in [Nome Concessionaria]")
- `[Nome Concessionaria]` -> Da Maps
- `[Marchio1]/[Marchio2]` -> Da foto Maps / sito
- `[Provincia]` -> Provincia scraping
- `[Modello]` -> Modello in pronta consegna visto su sito loro (iper-personalizzazione)
- `[Tuo Nome]` -> Nome closer
- `[PREZZO]` -> Placeholder canone. NON inventare. Lascia [PREZZO] se non deciso da Max.
- `[Telefono]` -> Tuo recapito

**NON USARE:** promesse tipo "raddoppi vendite", "garanzia 10 clienti". Illegale e brucia trust.

---

### 5. COME ALLENARE AGENTE AI / CLOSER

1.  Fai leggere 01, 03, 04. Fallo provare su di te.
2.  Role-play: tu fai concessionario scettico, lui deve usare risposte parola-per-parola da 03.
3.  Registra 10 chiamate vere, trascrivi, correggi.
4.  Solo dopo dai accesso a 02 e 05 per follow-up testuale.

**KPI per validare pacchetto:**
- 20% delle chiamate diventa conversazione >30 sec
- 10-15% conversazioni fissa demo
- 40% WA MSG1 ottiene risposta (anche "no")
- Follow-up G+2 recupera 20% dei no iniziali

Se sotto, cambia gancio (file 04), non script.

---

### 6. COSA NON È QUESTO PACCHETTO (Importante)

- NON sostituisce WF-S1 (7 lead caldi). Quello è relazione calda A5/A8. Questo è S1-FREDDO puro.
- NON è un manuale di prodotto. Parla di problema e tempo, non di features.
- NON include PDF esempio (crealo tu con Preventa usando un'auto vera, oscura prezzi se serve).

---

### 7. ORDINE DI ESECUZIONE RAPIDO PER MAX

Se vuoi partire OGGI:

1.  Apri 04, scegli Gancio 1.
2.  Apri 01, stampa pagina apertura + qualifica.
3.  Chiama 10 concessionari da Maps.
4.  A chi non risponde, manda 02 - WA MSG1.
5.  Segna obiezioni su 03.
6.  Dopo 2 giorni, applica 05.

Tutto il resto è ottimizzazione.

Buon closing. Tono peer-to-peer, zero fame.

— Pacchetto Preventa S1-Freddo - Build per Max - 22/07/2026
