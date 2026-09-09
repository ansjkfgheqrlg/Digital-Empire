# Lezione 13 — Quello che non misuri, non cresce: funnel troubleshooting

**Corso:** outFunnel (Armageddon Bundle) | **Sezione:** Sezione 3 - Strategie avanzate (2/5)
**URL:** https://www.andrei-copy.com/bjrkfv9/lezione-13-quello-che-non-misuri-non-cresce-funnel-troubleshooting-p4lg8
**Video:** Vimeo `1048162251` (privato, solo membri)
**Tipo:** TEORIA. **Fonte:** "Riassunto lezione" ufficiale, catturato integralmente.

---

## Panoramica ufficiale

Non basta creare un funnel e sperare che funzioni: bisogna misurare e ottimizzare ogni step.
Errore comune: concentrarsi solo sulla fase di acquisto, quando il problema può essere a monte.

---

## Knowledge Atoms

| ID | Atom | Fonte |
|---|---|---|
| KA-01 | Principio fondamentale: "ciò che non misuri non cresce" — vale per business, fitness, denaro e marketing; il dato principale da monitorare per un funnel è il CR (Conversion Rate) fra ogni coppia di step consecutivi. | "1. Il Principio Fondamentale" |
| KA-02 | Errore diagnostico comune, nominato esplicitamente: dare per scontato che il problema sia SEMPRE nell'ultimo step (la Sales Page) — in realtà spesso le persone si bloccano in uno step precedente, prima ancora di arrivare alla vendita. | "3. Errore Comune" |
| KA-03 | Metodo di ottimizzazione: identificare lo step con il CR più basso, poi testare varianti mirate (copy, immagini/design, riduzione campi nei form, targeting ads) — MA non testare troppe cose insieme, altrimenti diventa impossibile isolare cosa ha funzionato. | "4. Come Ottimizzare" |
| KA-04 | Strumento nominato esplicitamente: Milanote, per organizzare visivamente funnel e messaggi; più tabelle di percentuali di conversione per step, con tracciamento delle modifiche fatte. | "5. Strumenti" |
| KA-05 | Metodo riassunto in 3 verbi: analizza, testa, ottimizza — ciclo da ripetere finché il funnel non performa al massimo. | "Conclusione" |

## Pattern estratti

- **P1 — KA-02 è il gemello diagnostico esatto del difetto #1 in `ANATOMIA-DEI-LANCI.md`**: il
  concorrente stesso cade nell'errore che questa lezione avverte di evitare — la pagina di
  vendita di Armageddon funziona benissimo, ma la cassa vera è un 404 irraggiungibile: un CR
  dell'ultimo step pari a zero che nessuno guarderebbe se si fosse fermati a "la sales page
  converte bene". **Conferma diretta e citabile**: l'autore insegna esattamente il controllo che
  gli avrebbe evitato il suo stesso difetto più costoso.
- **P2 — KA-03 (un test alla volta) è metodologicamente identico al principio di controllo delle
  variabili di `ab-testing`**: nessun conflitto, rinforzo diretto dello standard già in uso.

## Connessione con Knowledge Base esistente

- **Match diretto e ad alta priorità con `ab-testing` e con il controllo 8 di ADR-024** ("Percorri
  la catena a macchina prima di aprire", `ANATOMIA-DEI-LANCI.md` Parte IX passo 12): questa
  lezione fornisce la giustificazione teorica del perché quel controllo è il primo gate
  obbligatorio di LANCI — un CR-per-step misurato end-to-end avrebbe reso impossibile non
  accorgersi del 404 sulla cassa. Nessuna modifica di skill richiesta: è una conferma che
  rafforza una decisione già presa (ADR-024), citabile come motivazione aggiuntiva.

## Gate di qualità

| Check | Status | Note |
|---|---|---|
| NO-FINTO | PASS | |
| NO-STUB | PASS | |
| P12 traceability | PASS | |

**Prossima lezione:** Lezione 14 — "KPIs"
