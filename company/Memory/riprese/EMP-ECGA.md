# EMP-ECGA — Ecosistema LANCI: piano consegnato, costruzione da avviare

- **Aperto:** 2026-09-05 · **Task:** TASK-LANCI-ECO-W2 · **Stato:** ✅ piano chiuso e salvato

---

## Il lavoro in una frase

Max ha fatto fare il piano architetturale completo dell'ecosistema dei lanci di Gael (L4-L5-L6
della sua task, e molto oltre). **Consegnato e committato: `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/`,
11 dossier, 3.718 righe.** Si comincia da `00-LEGGIMI-GAEL.md`.

## Cosa è FATTO — tutto verificato sul disco e in git

- [x] 11 dossier scritti e **committati** (`git ls-files` → 11)
- [x] Tre giri veri: V1 (3.761 righe) → critica di 3 revisori indipendenti (106 rilievi) → V3
- [x] Puntatori aggiornati **nello stesso turno**: `REGISTRO-NUMERI.md` (15 riservato, prossimo 16)
      · `TASK-GAEL-20260831-SETTIMANA-02.md` (nota d'apertura per Gael) · `26-ECOSISTEMA-LANCI.md`
      (marcato superato) · `STATO-EMPIRE.md` · `wiki/log.md`
- [x] Checkpoint `CP-20260905-015` scritto con `mem write` e poi compilato a mano nel contenuto
- [x] **Nessuna cartella `15-LANCI/` creata**, nessun agente, nessuna skill: era l'ordine di Max

## Cosa NON è a metà — non c'è cantiere aperto

Il piano è il deliverable e **è finito**. Non resta lavoro sospeso su questo fronte.

## Decisioni già prese (non rimetterle in discussione)

| # | Decisione |
|---|---|
| 1 | **Il numero è 15**, non 14 (il 14 è TESORERIA). Riservato, non libero |
| 2 | **12 reparti**, non gli 8 di L3: i quattro aggiunti (offerta, editoriale, tesoro, memoria) coprono cose senza proprietario |
| 3 | **I gate stanno dentro `lancio avanza`**, non in un reparto da chiamare |
| 4 | **La memoria è condizione di chiusura di fase** |
| 5 | **Si usa il campo `tools`** nel frontmatter: è l'unico vincolo meccanico |
| 6 | **Lo scaglione minimo è un vincolo tecnico** (11 agenti, 6 reparti), non un consiglio |
| 7 | **Il reparto Offerta istruisce la decisione**: "confermi 47?" invece di "che prezzo?" |
| 8 | Numerazione gate unica: **`GATE-<REPARTO>-<n>`** |

## Trappole — ogni riga qui vale un'ora risparmiata

1. **L'ADR-022 va registrato PRIMA di creare la cartella.** Lo impone ADR-009 e `empire/conform.py`
   lo verifica. È il passo zero, non l'ultimo. *(L'ultimo ADR esistente è il 021.)*
2. **`empire doctor` esce 1 oggi** per 2 bloccanti estranei ai lanci: la verifica finale è
   insoddisfacibile per ragioni non nostre. Non è colpa di chi costruisce.
3. **Nessun comando dell'Impero verifica se un agente è ufficiale.** Provato nel codice:
   `census.py:142` marca `.claude/` come vendored, `orphans.py:30` lo salta, `forge.py:157` guarda
   solo `company/`. → l'ecosistema si porta il proprio `registro.py`. **Difetto degli strumenti,
   da mettere in BACKLOG.**
4. **I componenti `ObjectionCPB_*` NON hanno props** e appartengono all'agency page CCM, non a un
   info-prodotto. Vanno parametrizzati (è una fase con le sue ore).
5. **Il servizio subagenti era instabile:** 9 teste perse su 15 per errori server e stalli.
   Antidoto adottato e funzionante: **far creare al subagente il file di uscita subito, con le
   sezioni vuote, e farlo risalvare a ogni sezione.** Chi muore lascia comunque il lavoro fatto.
6. **Il formato del battito è cambiato oggi** (CP-20260905-002, codice EMP-RCAP): titolo in
   grassetto, sei voci col pallino arancione. Va usato quello.

## Cosa aspetta MAX — e senza la prima il primo lancio non parte

| # | Decisione | Dove sono gli elementi per decidere |
|---|---|---|
| 1 | **Il Manuale Claude Code è a pagamento o è un regalo?** | dossier `04-WF-OFFERTA.md` §5 — le due strade con le conseguenze, e quale è reversibile |
| 2 | Approvare l'**ADR-022** | dossier `10-ADR-PROPOSTO-E-I-TRE-GIRI.md` |
| 3 | Lo standard dei testi (decide il CMO) | dossier `05-WF-COPY.md` |
| 4 | Il sistema visivo (decide la guild Design) | dossier `06-WF-FUNNEL-E-EDITORIALE.md` §A.11 |

## Il prossimo passo esatto

**Per Gael:**
```
PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI-GAEL.md   → §4 "il primo giorno"
```

**Per chi riprende questa chat:** il lavoro è chiuso. Se Max torna su questo fronte, le uniche
cose vive sono le quattro decisioni della tabella qui sopra.
