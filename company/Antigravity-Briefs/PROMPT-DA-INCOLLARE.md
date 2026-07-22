---
Owner: Max · Controllore: Claude · Origine: FORGE · Governo: MANDATO Art.8 + ADR-008
Created: 2026-07-22 · Uso: copia-incolla diretto in Antigravity (Gemini)
---

# 📋 PROMPT DA INCOLLARE IN ANTIGRAVITY — istruzioni per Max

## Come funziona (leggi una volta, poi non serve più)

Gemini in Antigravity **vede tutto il monorepo**. Quindi **non devi incollare 200 righe di brief**.
Incolli un **prompt di lancio corto** che gli dice quale file leggere e cosa fare. Il brief completo
lo legge lui da solo dal disco.

**Percorso del repo** (serve nel prompt):
```
C:\Users\Utente\Desktop\qui tutto\Digital Empire
```

**Ordine di lancio:**
1. **GEM-04** ← parti da qui (anagrafe + link integrity). Non dipende da nulla che manchi.
2. **GEM-05** ← dopo GEM-04, oppure in parallelo se apri due sessioni Antigravity.

GEM-01/02/03/06 **non** vanno a Gemini: sono già assegnati (seed fatto da Claude, G-A/G-B/G-C a
Gael, M-A/M-B/M-C a Claude). Se Gemini prova a toccarli, fermalo.

---

## ▶️ PROMPT 1 — GEM-04 (parti da questo)

> Copia **tutto il blocco qui sotto**, dalla prima riga all'ultima, e incollalo in Antigravity.

```text
Sei l'esecutore del pacchetto di lavoro GEM-04 di Digital Empire.

REPO: C:\Users\Utente\Desktop\qui tutto\Digital Empire
Hai accesso completo in lettura e scrittura al monorepo.

PRIMA DI SCRIVERE UNA SOLA RIGA DI CODICE, leggi questi file interi, in quest'ordine:
1. company/Antigravity-Briefs/GEM-00-INDEX-E-PROTOCOLLO.md
   (regole non negoziabili, protocollo di verifica skill, formato di consegna, perimetro)
2. company/Antigravity-Briefs/GEM-04-ANAGRAFE-LINK-INTEGRITY.md
   (il tuo brief completo: architettura, sequenza task, 12 DoD, anti-pattern)
3. company/Mandato/MANDATO-EMPIRE.md  — in particolare l'Articolo 8
4. company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md
5. company/Memory/decisions/ADR-008-catena-intestazione-controllo.md
6. company/REGISTRO-IMPRESA.md e company/skills-map.yaml
7. empire/README.md  — il core runtime esiste già ed è testato: ci costruisci sopra

CONTESTO IN 5 RIGHE:
Digital Empire è un'azienda con 1.267 file .md e, fino a oggi, 0 file .py: un organigramma
completo che non gira. Claude ha costruito il seed `empire/` (paths, config, schema, conform,
cli — 23 test verdi). Tu costruisci `empire/registry/`: il censimento automatico di tutto ciò
che l'azienda possiede, il rilevamento degli artefatti orfani, dei link rotti e dei duplicati,
e il gate che impedisce a un artefatto senza intestazione ADR-008 di nascere.

VINCOLI CHE NON PUOI VIOLARE:
- ADR-003: si avvolge, non si riscrive. Nessun sistema attivo viene rifatto da zero.
- ADR-008: ogni file nuovo ha in testa Owner, Controllore, Origine, Governo.
- Windows-first: `from empire.paths import safe_stdout; safe_stdout()` come PRIMA istruzione di
  ogni entry-point; `encoding="utf-8"` in ogni open(). Uno script che crasha su Windows non è
  consegnato.
- Zero path assoluti: usa `empire.paths`. Il repo si sincronizza su due macchine.
- I path contengono spazi ("qui tutto", "Digital Empire"): pathlib.Path e liste di argomenti nei
  subprocess, mai interpolazione in stringa di shell.
- Standard library soltanto, salvo motivazione scritta.
- NON cancellare nulla. I duplicati si SEGNALANO, li decide Max con un ADR.
- NON installare hook git senza approvazione: li documenti soltanto.
- NON aggiungere sottocomandi modificando empire/cli.py: c'è il loop di plugin, crea
  `empire/registry/cli.py` con una funzione `register(sub)`.

PERIMETRO — cosa NON tocchi:
empire/loader*.py, empire/index*.py, empire/flow/**   (sono di Gael)
empire/memory/**, empire/inspect/**                    (sono di Claude)
company/Memory/**, company/Ispettorato/**              (sono di Claude)
company/Ecosistemi/**                                  (specifica approvata: si legge, non si riscrive)
EmpireDesk/platform/, Clienti/, .env, second-brain-vault/wiki/   (fuori perimetro)
TUO IN ESCLUSIVA: empire/registry/**, WORKFLOW-ESTATE/05-TEMPLATES-E-KIT/,
WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/

PRIMO PASSO OBBLIGATORIO — verifica delle skill.
Il brief cita delle skill. Non dare per scontato che esistano. Esegui:
  ls "C:/Users/Utente/.claude/skills/"
  ls ".claude/skills/"
  ls "DIGITAL-EMPIRE/05-SKILLS/"
  cat "company/skills-map.yaml"
e produci la tabella di verifica descritta in GEM-00 §2 (skill citata | path atteso | presente
SI/NO | azione se assente). Se una skill non c'è: NON inventarla, usa il fallback dichiarato nel
brief e segnalalo.

SECONDO PASSO — verifica che il seed funzioni:
  python -m empire status
  python -m empire conform WORKFLOW-ESTATE
  python -m unittest discover -s empire/tests -p "test_*.py"
Attesi: status con "alias rotti 0", conform con 6 block / 7 riparabili, 23 test OK.
Se non è così, FERMATI e segnalalo: qualcosa è cambiato sotto di te.

POI esegui i TASK 1..8 del brief GEM-04 nell'ordine scritto, superando ogni Gate prima di
passare al successivo.

REGOLA DI ONESTÀ — la più importante:
Un task è chiuso solo se hai INCOLLATO il comando eseguito e il suo output REALE.
"Dovrebbe funzionare" non è una prova. Se non hai potuto testare qualcosa, scrivilo nella
sezione F della consegna ("Cosa NON ho fatto e perché"). Dichiarare fatto ciò che non è
verificato è l'unico errore che non viene perdonato in questa azienda.

CONSEGNA FINALE:
Scrivi un solo file: company/Antigravity-Briefs/consegne/GEM-04-CONSEGNA.md
con esattamente le sezioni A..H descritte in GEM-00 §4.

Comincia dalla verifica delle skill. Riporta la tabella prima di procedere.
```

---

## ▶️ PROMPT 2 — GEM-05 (dopo GEM-04, o in parallelo in un'altra sessione)

```text
Sei l'esecutore del pacchetto di lavoro GEM-05 di Digital Empire.

REPO: C:\Users\Utente\Desktop\qui tutto\Digital Empire
Hai accesso completo in lettura e scrittura al monorepo.

PRIMA DI SCRIVERE CODICE leggi interi, in quest'ordine:
1. company/Antigravity-Briefs/GEM-00-INDEX-E-PROTOCOLLO.md
2. company/Antigravity-Briefs/GEM-05-DASHBOARD-E-METRICHE.md
3. la skill `dataviz` — LEGGILA PRIMA di scegliere un solo colore o un tipo di grafico
4. empire/README.md
5. WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/WF-MASTER.md  (la mappa dei 6 gate della settimana)
6. EmpireDesk/app.py e EmpireDesk/modules/metrics.py  (contratto esistente: lo leggi, non lo riscrivi)

COSA COSTRUISCI:
`empire/dash/` — il cruscotto dell'azienda: un HTML autocontenuto (zero richieste esterne,
apribile offline con doppio click, tema chiaro E scuro) più una versione Markdown in
WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/DASHBOARD.md che Max e Gael leggono da GitHub e dal
telefono. In cima: i 6 gate della settimana con deadline e stato.

REGOLA DURA SULLE METRICHE:
Una metrica che non ha una sorgente misurabile NON entra nella dashboard. Niente KPI
aspirazionali. Se il dato non c'è, la cella dice "n/d" con il motivo.
Devi distinguere visivamente tre stati: `misurato` (pieno), `inserito a mano` (bordo
tratteggiato), `n/d` (grigio). Confondere un dato reale con una stima è peggio che non avere
la dashboard.

VINCOLI CHE NON PUOI VIOLARE:
- Zero CDN, zero font remoti, zero librerie JS di charting. Grafici in SVG generato da Python.
- Windows-first: safe_stdout() come prima istruzione, encoding="utf-8" in ogni open().
- Zero path assoluti: usa empire.paths.
- NON toccare EmpireDesk/platform/ (è di Max) e NON riscrivere modules/metrics.py (ADR-003).
- Dopo l'integrazione, `python EmpireDesk/app.py --selftest` deve restare >= 16/16.
  Se scende, hai rotto qualcosa: torna indietro.
- Sottocomandi CLI via empire/dash/cli.py con register(sub), mai modificando empire/cli.py.
- NON schedulare task automatici senza approvazione di Max: li documenti soltanto.

PERIMETRO — TUO IN ESCLUSIVA: empire/dash/**, WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/
NON tocchi: empire/loader*|index*|flow (Gael), empire/memory|inspect (Claude),
company/Memory|Ispettorato (Claude), company/Ecosistemi (specifica approvata),
EmpireDesk/platform/, Clienti/, .env

PRIMO PASSO: verifica skill (GEM-00 §2) + verifica seed:
  python -m empire status ; python -m unittest discover -s empire/tests -p "test_*.py"

POI i TASK 1..8 del brief, un Gate alla volta.

REGOLA DI ONESTÀ: un task è chiuso solo con comando + output reale incollati.
Ciò che non hai testato va nella sezione F della consegna.

CONSEGNA: company/Antigravity-Briefs/consegne/GEM-05-CONSEGNA.md, sezioni A..H di GEM-00 §4.

Comincia dalla verifica delle skill.
```

---

## 🔁 PROMPT DI RIPRESA (se la sessione Gemini si interrompe a metà)

```text
Riprendi il pacchetto GEM-<NN> di Digital Empire.
REPO: C:\Users\Utente\Desktop\qui tutto\Digital Empire

Prima di riprendere:
1. leggi company/Antigravity-Briefs/GEM-00-INDEX-E-PROTOCOLLO.md
2. leggi company/Antigravity-Briefs/GEM-<NN>-*.md
3. leggi company/Antigravity-Briefs/consegne/GEM-<NN>-CONSEGNA.md se esiste già
4. esegui `git status` e `python -m empire status` per vedere lo stato reale sul disco
5. dimmi a che TASK del brief sei arrivato e quale Gate hai superato per ultimo,
   basandoti su ciò che TROVI SU DISCO, non su ciò che ricordi

Poi riparti dal primo TASK non completato. Non rifare quelli già chiusi e verificati.
```

---

## ✅ Quando Gemini ha finito — cosa controlli tu (Max)

Chiedi a Claude: **"fai il gate 5-bis su GEM-04"**. Claude verifica:

| Controllo | Come |
|---|---|
| I comandi dichiarati funzionano davvero | li riesegue e confronta l'output |
| Le DoD sono spuntate con prova, non a parola | legge la sezione C della consegna |
| Nulla fuori perimetro è stato toccato | `git diff --name-only` |
| Nessun file cancellato | `git status` |
| Le intestazioni ADR-008 ci sono | `python -m empire registry gate` |
| I test del seed sono ancora verdi | `python -m unittest discover -s empire/tests` |

Se un controllo fallisce, Claude te lo dice con path:riga e Gemini rifà quel task.
</content>
