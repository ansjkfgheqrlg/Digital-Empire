# PLANNING-P4 — Ottimizzazione (ROI, batching, tagli 80/20)
> Livello 4 di 7 · migliora P3: massimizza €/ora, elimina lavoro che non produce revenue entro il 26/07.

## 1. Tabella ROI per task (€ attesi / ora umana)

| Task | Ore uomo | Revenue attesa (sett.) | €/h | Priorità |
|------|---------|------------------------|-----|----------|
| Contatti 7 concessionari (WA-first + call) | 3h | 1-3 setup + canoni (alto) | ★★★★★ | P0 |
| DEC-001/002/004 (veto 30 sec l'una) | 0.05h | sblocca 3 stream | ★★★★★ | P0 |
| Funnel S2 live (vendibile, non perfetto) | 4h | vendite Manuale da 23/07 | ★★★★ | P1 |
| Push S2 su canali caldi Max | 1h | vendite dirette | ★★★★ | P1 |
| Case study Novacar + promo-kit S6 | 4h | pipeline S6 (revenue sett. prox) | ★★★ | P2 |
| Batch caroselli S3 + bio→funnel | 3h | traffico→S2 (indiretta) | ★★ | P2 |
| Pipeline S4 100% auto | 6h | 0 diretta questa settimana (condizione Max) | ★★ | P3 |
| WF-YT test 1 video | 5h | 0 diretta (lead-gen inizia dopo) | ★ | P3 |

**Regola P4-1:** ogni ora contesa va alla riga con €/h più alto. In caso di conflitto con l'infra, vince S1/S2 (regola dossier n.1, confermata).

## 2. Acceleratore S1: chiusura asincrona (miglioramento operativo)
Il dossier prevede "call/whatsapp". Upgrade: **WhatsApp-first a 3 messaggi** (script in WF-S1):
1. Msg-1: riattivazione + prova (link/case Novacar).
2. Msg-2: offerta "Partenza Anticipata" con termini e scadenza 31/07.
3. Msg-3: domanda binaria ("parti ora o a settembre?") + call SOLO se richiesta.
Obiettivo: chiudere **senza** call dove possibile → riduce R-01 (tempo Max) e alza i contatti completati entro 22/07.

## 3. Batching (una sola accensione per tipo di lavoro)
- **Claude, batch copy unico 21/07 sera**: script S1 + landing S2 + 3 email + bio S3 + Oggetti follow-up. Un solo passaggio, un solo swarm (slot 2).
- **Gael, batch contenuti 23/07**: 7 caroselli S3 in un'unica run carousel-factory.
- **Max, batch contatti**: finestre fisse 21-23/07 h9:30 e h18:00 (mai a macchia di leopardo).
- **Checkpoint automatico EOD h19:00** ogni giorno (hook, vedi 06-NERVOUS-SYSTEM).

## 4. Definition of Done congelate (anti scope-creep — R-09)
| Deliverable | DoD (STOP qui) |
|-------------|----------------|
| Funnel S2 "vendibile" | 1 landing + 1 checkout funzionante (test €1) + 3 email caricate. Niente A/B, niente automazioni extra. |
| Promo-kit S6 | 1 landing Preventa + 1 demo video ≤2min + 1 case study PDF. |
| WF-YT v1 | 1 video renderizzato + pubblicato (anche non perfetto) + trace P12 + checkpoint. |

## 5. TAGLI 80/20 — cosa NON si fa questa settimana
- ❌ Scalare YouTube oltre 1 video (nicchia #2, più canali: settimana prox).
- ❌ Outreach S6 a freddo **prima** che case study + landing esistano (credibilità = conversione).
- ❌ Restyle brand S3/S4 oltre le config esistenti (ADR-003).
- ❌ A/B test, pixel, analytics avanzati sul funnel (si misura a mano: vendite e lead).
- ❌ Riattivare altre pagine oltre crea.illtuo_impero (+ mentalita.brutale SOLO se gate E2E ✅).
- ❌ Perfezionare P6/P7 oltre il necessario: il piano si migliora eseguendo (ReasoningBank in RETRO).

## 6. Miglioramento di metodo introdotto da P4
**"Vendibile > perfetto"** diventa vincolo di architettura (ADR-EST-005): ogni artefatto ha DoD congelata; superarla richiede una `decision` in memoria con razionale.

---
⛓️ Trace P12: `PLANNING-P4#estate-2026` · input: P3 · mitiga: R-01, R-07, R-09
