# Struttura del documento finale — PIANO-IMPLEMENTAZIONE-ANDREI-PASCU

**Decisa da Emperator (P3), non dallo Scagnozzo.** Lo Scagnozzo dell'assemblaggio riempie questa
struttura in modo meccanico: nessuna decisione propria, nessuna azione aggiunta o tolta di sua
iniziativa. Se un contenuto non entra in nessuna sezione, lo mette in appendice e lo segnala.

**Missione del documento, in una riga:** trasformare lo studio Andrei Pascu in un piano eseguibile
che **fa incassare Digital Empire** — non in altra documentazione (ADR-016 / ULTIMO METRO).

---

## Sezioni obbligatorie, in quest'ordine

### 1. La pagina che conta (max 1 pagina)
Le **prime 5 azioni**, ordinate, con: cosa si fa, chi la fa, quanto costa in ore, **quale euro
sblocca**. Nient'altro. Chi legge solo questa pagina deve poter cominciare oggi.

### 2. Cosa cambia davvero in Digital Empire
La sintesi che nessuno aveva scritto: guardando TUTTO lo studio insieme (metodo + visivo + copy +
lanci), cosa fa l'Impero diversamente da ieri. Massimo 10 punti, ognuno con la lezione di origine.

### 3. Le azioni — tabella unica
Una riga per azione, dai due draft fusi e ripuliti dalle sovrapposizioni:
`ID | Azione | Corsia (C1/C2) | Classe (EURO DIRETTO / ABILITA UN EURO / INFRASTRUTTURA / DOCUMENTO)
| Effort | Blocca esattamente | Stato dopo P1/P2`
La colonna **"Blocca esattamente"** è obbligatoria per ADR-028: nessuna azione può restare con un
blocco implicito, e nessuna può essere precondizione di una micro-task di Gael.

### 4. Corsia C1 — libera, si esegue subito
Le azioni eseguibili da chiunque, zero collisione con `TASK-LANCI-BUILD-W3`. Ognuna con criterio di
"fatto" verificabile sul disco.

### 5. Corsia C2 — consegnata a Gael
Dichiarate, non eseguite da altre sessioni. Formato pronto da incollare nelle sue micro-task.

### 6. I NO-GO, con il motivo
Cosa NON si fa e perché (draft B: AP-006 automazione preventivi, AP-018, ecc.). Un no-go motivato
vale quanto un go: impedisce di riproporlo fra due mesi.

### 7. Il buco — la lezione non convertita
Quello che le Sentinelle hanno trovato mancante nei draft, e come si copre.

### 8. Cosa è già fatto (non rifare)
EMP-APDOC1 (4 documenti ufficiali) ed EMP-APIMPL1 (12 candidati su 13 SKILL.md). Lista esatta,
così nessuno ci ritorna sopra.

### 9. Numeri: quali sono misurati e quali sono stimati
Tabella secca. Ogni cifra del documento o ha una fonte, o è marchiata STIMA. Nessuna cifra nuda.

### 10. Registro delle critiche (P1 → P2 → P3)
Cosa ha colpito ogni giro, cosa è stato accolto, cosa è stato respinto e perché. È la prova che il
piano è stato criticato tre volte davvero, non a parole.

---

## Vincoli di forma
- Italiano, sempre. Frasi corte. Nessun claim senza prova.
- Ogni azione ha un ID stabile (AP-xxx) che non cambia mai più.
- Il documento finale va in `PIANO-IMPLEMENTAZIONE-ANDREI-PASCU.md` + PDF standard-oro
  (motore `PIANO-MAESTRO/scripts/pdf_engine_empire.py`, dossier 28) + doppione in
  `documentazione Empire/competitor/Andrei Pascu/`.
