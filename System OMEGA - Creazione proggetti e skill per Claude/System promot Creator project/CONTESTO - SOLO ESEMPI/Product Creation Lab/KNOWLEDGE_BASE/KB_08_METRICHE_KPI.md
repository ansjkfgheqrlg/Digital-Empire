# ═══════════════════════════════════════════════════════════════
# 📊 KB_08 — METRICHE & KPI
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: MEASUREMENT
# Priorità: P2
# Dipendenze: Prodotto lanciato (usato post-lancio)
# Referenziato da: CUSTOM_INSTRUCTIONS — Sezione 4.4
# ═══════════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────
# 📋 COME UTILIZZARE QUESTO FILE
# ──────────────────────────────────────────────────────

Questo file contiene il sistema di misurazione della qualità e della produzione.

Usalo in due momenti principali:
1. **+30 giorni dal lancio**: review post-lancio
2. **Review mensile**: revisione della pipeline di produzione

**Obiettivo**: Non raccogliere metriche "per sapere" — raccoglierle per rispondere a:
"Cosa devo fare diversamente nel prossimo prodotto?"


# ──────────────────────────────────────────────────────
# 🎯 KPI DI QUALITÀ PRODOTTO
# ──────────────────────────────────────────────────────

Raccogli 30 giorni dopo il lancio.

## Tabella KPI

| Metrica | Come misurarla | Target | Soglia Critica | Azione |
|---|---|---|---|---|
| **NPS Studenti** | Survey post-completamento | >8/10 | <6/10 | Ferma vendite, analizza feedback, rivedi contenuto |
| **Refund Rate** | (N rimborsi / N acquisti) × 100 | <5% | >10% | Identifica moduli deboli — migliora o riscrivi |
| **Completion Rate** | (N studenti che completano / N totali) × 100 | >40% | <20% | Analizza dove abbandonano — lezioni troppo lunghe? |
| **Modulo Preferito** | Da survey studenti | Distribuzione bilanciata | 1 modulo con 0 preferenze | Quel modulo è debole — riprogetta |
| **Testimonial** | Conteggio entro 30gg | ≥3 | 0 dopo 30gg | Problema qualità o raccolta — analizza |
| **Tempo Completamento** | Giorni medi dalla piattaforma | Entro 2× la stima | >3× la stima | Contenuto troppo denso — semplifica |

---

## Survey Post-Completamento (invia 7gg dopo completamento)

```
OGGETTO: Hai finito [NOME CORSO] — 3 minuti di feedback?

[Nome], sei tra i pochi che ha completato [NOME CORSO]. Grazie.
3 domande rapide:

1. Da 0 a 10, quanto consiglieresti questo corso a un collega?  [link Typeform]
2. Il modulo che ti ha dato più valore concreto?  [lista moduli]
3. Una cosa che cambieresti?  [campo aperto]

I tuoi riscontri migliorano il corso per i prossimi studenti.
```

---

## Interpretazione Metriche

### NPS < 6

1. Leggi tutti i feedback survey
2. Identifica il problema più citato
3. Era un red flag del quality check che hai saltato?
4. Se lezione specifica → ri-registra. Se strutturale → riprogetta moduli. Se promessa vs realtà → rivedi copy sales page.
5. Sospendi vendite durante la revisione.

### Refund Rate > 10%

1. Analizza QUANDO avvengono i rimborsi: entro 24h → problema aspettative (copy fuorviante); dopo Modulo X → problema in quel modulo
2. Invia sondaggio ai rimborsati: "Cosa l'ha portata a richiedere il rimborso?" (risponde il 10-20%)

### Completion Rate < 20%

Analizza dalla dashboard piattaforma:

| Causa | Segnale | Soluzione |
|---|---|---|
| Lezioni troppo lunghe | Abbandono a metà di una lezione | Spezza in 2 parti |
| Percorso non chiaro | Abbandono al Modulo 1-2 | Migliora welcome video + roadmap |
| Esercizi difficili | Abbandono dopo un esercizio | Semplifica o aggiungi guida |
| Mancanza motivazione | Abbandono dopo 2-3 settimane | Aggiungi email re-engagement |

### Testimonial = 0 dopo 30gg

1. Hai chiesto i testimonial? → Manda la richiesta con template pre-compilato:
   "Puoi completare questa frase? '[PRIMA] stavo lottando con ___. [DOPO] il corso sono riuscito a ___. La cosa più preziosa è stata ___.' Bastano 2 righe."
2. Se NPS alto ma 0 testimonial → problema di raccolta, non di soddisfazione
3. Se NPS basso → problema di prodotto → vedi sopra


# ──────────────────────────────────────────────────────
# ⚙️ KPI DI PRODUZIONE
# ──────────────────────────────────────────────────────

Raccogli mensilmente.

| Metrica | Target | Cadenza |
|---|---|---|
| Prodotti in pipeline | ≥2 sempre | Mensile |
| Tempo da brief a delivery | PDF ≤1 sett; Mini ≤2 sett; Corso ≤5 sett | Per prodotto |
| Template creati per prodotto | Minimo per tipo (KB_07) | Per prodotto |
| Ricerca completata prima di iniziare | 100% dei prodotti | Per prodotto |
| Beta test per ≥€97 | 100% dei prodotti ≥€97 | Per prodotto |
| Red flag al quality check | 0 | Per prodotto |

---

## Cadenze di Review

### Fine Sessione di Produzione (ogni sessione)

```
□ La lezione/template ha un output pratico? SÌ / NO (se NO → fix ora)
□ Il template ha l'esempio compilato? SÌ / NO (se NO → compilalo ora)
```

### Fine Modulo

```
□ Tutte le lezioni hanno output pratico
□ Tutti i template hanno esempio compilato
□ L'esercizio ha output misurabile e criteri
□ PDF riassuntivo scritto
□ Checklist fine modulo pronta
□ Tutti i link funzionano
□ Ordine lezioni logico
```

### Fine Produzione (prima del quality check)

```
□ Tutti i moduli superano il checkpoint
□ Welcome video (2-3 min) registrato
□ Roadmap visuale pronta
□ Email onboarding scritta e testata
□ Tutti i file in cartella organizzata
□ Pagina accesso testata su mobile

Tempo totale produzione: ___ ore (target: ___ ore)
Template creati: ___ | Esercizi: ___ | Link testati: ___/___
```

### Review Post-Lancio (+30 giorni)

```
NPS medio: ___ | Refund: ___% | Completion: ___% | Testimonial: ___

Modulo più apprezzato: ___ | Meno apprezzato: ___
Principale feedback positivo: ___
Principale problema segnalato: ___

Decisione:
□ Nessuna azione — prodotto performante
□ Fix minore: [cosa — entro 30 giorni]
□ Fix maggiore: [cosa — stima tempi]
□ Sospendere vendite: [motivazione]

Learnings per il prossimo prodotto:
1. ___ | 2. ___ | 3. ___
```

### Review Mensile

```
Prodotti in pipeline: Architettura: ___ | Produzione: ___ | Qualità: ___ | Consegnati: ___

Tempo produzione:
- [nome prodotto]: ___ giorni (target: ___)

Qualità produzione:
- Red flag quality check: ___ | Red flag beta: ___
- Template con esempio compilato: ___% | Beta completati: ___%  | Ricerca completata: ___%

Colli di bottiglia: ___
Azioni mese successivo: 1. ___ | 2. ___ | 3. ___
```


# ──────────────────────────────────────────────────────
# 📈 BENCHMARK DI SISTEMA
# ──────────────────────────────────────────────────────

## Qualità

| Metrica Aggregata | Target | Azione se sotto |
|---|---|---|
| NPS medio tutti i prodotti | >8/10 | Revisione sistematica processo produzione |
| Refund rate medio | <5% | Analisi cross-prodotto: c'è un pattern comune? |
| Completion rate medio | >40% | Revisione struttura lezioni e percorso studente |
| % prodotti con ≥3 testimonial | >80% | Migliorare sistema raccolta testimonial |

## Produzione

| Metrica Aggregata | Target | Azione se sotto |
|---|---|---|
| % prodotti con ricerca completata | 100% | Nessuna eccezione — processo rotto |
| % prodotti ≥€97 con beta test | 100% | Nessuna eccezione |
| Tempo produzione vs stima | Entro ±20% | Rivedere stime per tipo |
| % prodotti senza red flag al delivery | >90% | Rinforzare quality check |


# ──────────────────────────────────────────────────────
# 📋 DASHBOARD TRACKING
# ──────────────────────────────────────────────────────

```
PRODUCT CREATION LAB — DASHBOARD (Notion/Google Sheet)
────────────────────────────────────────────────────────
PRODOTTI IN PRODUZIONE:
Nome | Tipo | Prezzo | Fase | Data Avvio | Data Target | Status

PRODOTTI LANCIATI (ultimi 6 mesi):
Nome | Tipo | Prezzo | Data Lancio | NPS | Refund% | Completion% | Testimonial

METRICHE AGGREGATE:
NPS Medio: ___
Refund Rate Medio: ___
Completion Rate Medio: ___
Prodotti con ≥3 testimonial entro 30gg: ___%
% con ricerca completata: ___%
% ≥€97 con beta test: ___%
```


# ──────────────────────────────────────────────────────
# ⚠️ EDGE CASE E GESTIONE ERRORI
# ──────────────────────────────────────────────────────

## La piattaforma non fornisce dati di completion

**Soluzione**: Opzione A — survey manuale 21gg dopo acquisto. Opzione B — form Google nell'ultima lezione. Opzione C — cambia piattaforma (Kajabi, Teachable Pro, Podia hanno analytics integrate).

## NPS alto ma refund rate alto

**Situazione**: NPS 8.5, refund 12%.
**Soluzione**: Problema di TARGET, non di prodotto. Chi rimborsa non è il cliente ideale. Analisi: differenze tra chi rimborsa e chi dà NPS alto? Se sì → problema di targeting del marketing, non del prodotto. Porta a P4 Launch Command.

## Completion rate < 10% con NPS alto

**Situazione**: Chi finisce ama il corso (NPS 9) ma il 90% non lo finisce.
**Soluzione**: Problema di engagement, non di qualità. Soluzioni: sequenza email re-engagement, riduzione lunghezza lezioni, micro-wins ogni 2-3 lezioni, versione "Fast Track" del corso in 4 ore.

## Tempo produzione sempre 2× la stima

**Soluzione**: Analizza dove va il tempo extra (ricerca? scrittura? editing?). Aggiorna le stime in KB_01 con i tempi reali osservati su almeno 3 prodotti dello stesso tipo.

## 0 testimonial nonostante NPS >8

**Soluzione**: I testimonial non arrivano spontaneamente. Chiedi nel momento giusto (dopo completamento ultimo modulo) con template pre-compilato facile da completare. Offri accesso a risorsa bonus in cambio.


# ──────────────────────────────────────────────────────
# 🔗 DIPENDENZE E CROSS-REFERENCE
# ──────────────────────────────────────────────────────

| File | Relazione |
|---|---|
| `KB_05_QUALITY_SYSTEM.md` | Il quality check previene i problemi che le metriche misurano |
| `KB_06_PACKAGING_HANDOFF.md` | I testimonial e feedback vengono usati nel prossimo handoff |
| `KB_01_PRODUCT_PIPELINE.md` | Le metriche di produzione misurano l'efficienza della pipeline |
| `KB_07_STANDARD_PER_TIPO.md` | I target KPI variano per tipo di prodotto |
| P4 Launch Command | Riceve metriche per ottimizzare lanci futuri |
| P7 Info-Business HQ | Riceve learnings post-lancio per informare il backlog prodotti |
