# EMP-MCC4 — PIANO IMPERO VIVO (dal 18% vivo al 100%, tutto collegato)

- **Aperto:** 2026-09-05 · **Aggiornato:** 2026-09-06 · **Stato:** APERTO
- **Assetto:** GOD EMPEROR DOOM
- **Ultimo checkpoint:** [CP-20260906-J8EV](../checkpoints/CP-20260906-J8EV.md)

---

## 1. L'ORDINE DI MAX (non è cambiato)

**Portare Digital Empire dal 18% vivo al 100% vivo. Senza eliminare niente. Con tutto
collegato** — reparti, ecosistemi, flussi, comunicazioni interne, passaggio di informazioni.

**Metodo imposto, non negoziabile:** piano generale → critica indipendente → V2 → critica →
V3 → **V4 esecutivo**. Ogni versione è la critica della precedente. Obiettivo: **one shot**,
cioè che la costruzione riesca al primo colpo.

**Ordine permanente aggiunto il 2026-09-06:** *«non chiedermi più niente, per qualsiasi cosa
hai già un permesso, procedi senza fermarti»* → salvato in
`~/.claude/projects/.../memory/feedback_procedi_senza_chiedere.md`.

**⛔ DIVIETO IN VIGORE: nessuna modifica costruttiva al repository fino a V4.** Si legge, si
misura, si progetta. Non si tocca. Ordine esplicito di Max del 2026-09-06.

---

## 2. DOVE SI RIPRENDE — SUBITO

**Il prossimo lavoro è scrivere `V2-PIANO-AMPLIATO.md`.**

Leggi in quest'ordine:
1. `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/00-LEGGIMI.md` — le **sette leggi** e il metodo
2. `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/V1-PIANO-GENERALE.md` — il piano da superare
3. `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/_critica-v1/` — **41 rilievi, 10 fatali**: sono l'ordine del giorno di V2
4. `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/dati/` — **7.700 righe di censimento misurato**, la materia prima

**V2 non è un ritocco di V1: è un altro piano**, che parte dai dieci fatali.

---

## 3. LO STATO DEL LAVORO

| Tappa | Stato |
|---|---|
| Leggi e metodo fissati | ✅ |
| Otto censimenti | ✅ 7.700 righe |
| V1 — piano generale | ✅ scritta |
| **Critica 1** | ✅ **41 rilievi, 10 FATALI** |
| **V2 — piano ampliato** | ⬜ **← SI RIPRENDE DA QUI** |
| Critica 2 | ⬜ |
| V3 — piano assestato | ⬜ |
| V4 — esecutivo | ⬜ |
| Via alla costruzione | ⬜ solo dopo V4 |

**9.264 righe** prodotte in totale nella cartella del piano.

---

## 4. I DIECI RILIEVI FATALI — l'ordine del giorno di V2

1. **I «2 vivi su 15» sono 0 su 15** per la legge L3 dello stesso piano. E uno dei due (`11-APEX-7`) è **progettato per non collegarsi**: unico schema dell'Impero **senza `from` e senza `to`**. In un piano sull'indirizzamento, avevo messo in vetrina l'anti-modello.
2. **Il ponte schede→esecutori tocca 439 file e ne scopre 162**, senza campi sorgente, senza nomi unici, senza guardia anti-divergenza: fabbricherebbe doppioni sopra i 36 esistenti.
3. **«Un proprietario» non basta**: l'Ispettorato ce l'ha — proprietario vero, comando reale, 30 test verdi — e ha **87 rapporti da un solo backfill, 44 giorni scoperti**. Serve un **consumatore quotidiano già esistente**. ⟵ **questa diventa la legge centrale di V2**
4. **Il ritorno più alto per il minor lavoro non è nel piano**: Ultimo Metro fermo per **una chiave mancante**, 25 pezzi in coda da 135 giorni.
5. **E0 ruota una chiave che tiene in piedi l'unico workflow vivo**, e il suo gate non se ne accorgerebbe.
6. **Il punto d'ingresso non va costruito: esiste già in doppia copia, vivo** (`empire/` a plugin + EmpireDesk a subprocess), **4 motori su 25 agganciati**.
7. **La fabbrica libri non è nel piano**: 9.737 righe, 6 libri (l'ultimo oggi), **orfana** — e i registri censiscono due gusci morti che le rubano il nome.
8. **Il magazzino pieno non esiste nel piano**: 25 pezzi finiti, **23 caricabili oggi**, nessuno scaglione li pubblica.
9. **Il ponte scarta senza dirlo** (viola L1): **162 esecutori su 164 non hanno una scheda** e la pipeline parte solo dalle schede.
10. **«L'ha fatto una volta, a vuoto» è falso**: **Preventa attraversa la catena da agosto con 22 contatti reali**, e V1 non la nomina.

---

## 5. IL VERDETTO SU NEXUS

**Come cinque funzioni regge. Come sedicesimo ecosistema no.** Quattro organi su cinque
esistono già in tutto o in parte: registro + INV-20 (tabella di instradamento in miniatura,
dentro i Lanci) · `company/Backbone/Bus/` · `empire/trace.py` (funziona, testato, rifiuta le
tracce senza prova — manca solo il punto di aggancio) · `scripts/tesoreria.py` (il ledger) ·
`gate_battito_hook.py` + registry gate (il guardiano).
**Il lavoro è aggancio e pompa, non fondazione.**

---

## 6. I NUMERI CHE COMANDANO IL PIANO (tutti misurati il 2026-09-06)

- **328 collegamenti progettati · 21 con contratto · 4 percorsi · ZERO fra ecosistemi** (82,6% dei 328 sono proprio INTER)
- **439 schede di agente · 164 esecutori · 2 nomi in comune**
- **314 agenti senza contratto d'uscita, ma 274 ce l'hanno già scritto** sotto il titolo sbagliato (`## Input / Output` invece di `## Output`) e **174 sono a un criterio dal pieno**: la prima ondata è una **rinomina**, e porta gli operativi dal 13,9% al **53,5%**
- **25 motori, ~135.000 righe di Python: 9 vivi, 3 rotti (stesso identico guasto), 8 orfani**
- **7 organi di governo che nessuno chiama · 0 sentinelle su 5 attive da sole · 4 conteggi di agenti che danno 4 numeri** (19/123/129/443)
- **33 cadute reali di agenti delegati → 29 regole, 12 da rendere meccaniche**
- `registry census` **è rotto**: bug di indentazione in `census.py`, artefatti = directory = 21.682

---

## 7. TRAPPOLE — non ricalpestarle

1. **Non scrivere il piano mentre gli agenti lavorano ancora.** L'ho fatto e ho dichiarato mancante un censimento già consegnato (1.064 righe). Stesso errore dell'audit di agosto.
2. **La regola anti-caduta va data alla granularità della SCHEDA, non della sezione.** Chi ha inteso «una sezione = tutto il censimento» è morto con tutto in mano (12 e 3 righe salvate); chi scriveva scheda per scheda ha salvato 384, 613, 1.096, 1.256, 1.426 righe.
3. **Fable stalla sui lavori lunghi** (watchdog a 600s). Perimetri corti, un rilievo per volta.
4. **Il limite di sessione dell'account esiste ed è reale.** Guardare l'orologio prima di dedurre: il 6 settembre ho fermato tutto credendolo attivo, quando si era azzerato sedici ore prima.
5. **Aprire sempre, non dedurre dai nomi.** La «cartella vuota» conteneva un bot con sei operazioni vere nel log.
6. **Altre sessioni lavorano sullo stesso repo**: un `SYNC-CONFLICT.txt` è comparso il 6 settembre. Verificare HEAD prima di committare; coniare i codici con `python scripts/checkpoint.py cp`, mai a mano.

---

## 8. RIFERIMENTI

- Piano: `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/`
- Misura di partenza: `PIANO-MAESTRO/30-PIANO-COMPLETAMENTO-IMPERO.md` (92% carta / 18% vivo)
- Task madre: `company/Memory/tasks/TASK-MAX-20260831-IMPERO-OPERATIVO.md` (B0..B8)
- Checkpoint: `CP-20260905-NUJJ` (la misura) · `CP-20260906-J8EV` (censimenti + V1 + critica 1)
