# WF-S1 — CONCESSIONARI: Partenza Anticipata Luglio 🥇
> Stream: S1 · Window: 21→26/07 · Owner: Max · DoD: **≥1 anticipo incassato**
> Trace: DEC-EST-003 · Gate: Gate-CONTATTI (23/07 h12), Gate-REV (26/07) · Config: workflows.yaml#WF-S1

## 1. Setup (21/07)
- **Max**: lista 7 lead → tabella `07-CONTROL/LISTA-7-LEAD.md`: nome · stato relazione · canale preferito · ultimo contatto · esito.
- **Claude**: questo script (già pronto sotto) + argomentario obiezioni.

## 2. Script WhatsApp in 3 messaggi (chiusura asincrona-first)

**MSG-1 — riattivazione + prova (h9:30)**
> Ciao [Nome]! Tutto bene? Ti scrivo perché il sistema preventivi che ti avevo mostrato è ufficialmente live — [NOVACAR] lo usa già ogni giorno: preventivo professionale con PDF brandizzato in 3 minuti, dati sempre aggiornati. Ti mando un esempio? *(allegare PDF/esempio reale Novacar)*

**MSG-2 — offerta a scadenza (dopo risposta, o h18:00)**
> Perfetto. Visto che eri tra i primi interessati ti riservo la **Partenza Anticipata di luglio**: setup scontato del 30% (oppure primo mese gratis) se attiviamo entro il 31/07, prezzo 2026 bloccato, e ti onboardiamo entro il 20 agosto. Motivo semplice: ad agosto si prepara il rientro — a settembre tu sei GIÀ operativo mentre gli altri stanno ancora installando.

**MSG-3 — domanda binaria (giorno dopo se c'è interesse)**
> Ti blocco una delle due attivazioni di luglio che ho ancora libere, o preferisci restare sul giro di settembre? (In entrambi i casi nessun problema — mi serve solo sapere come organizzarmi 🙂)

**Call SOLO se richiesta** (script call A8/WF-CLOSING-PREP esistente). Chiusura: mandare link pagamento setup (kit vendita in 07-CONTROL) + fattura. Gael clona l'app il giorno stesso (`/nuovo-concessionario`).

## 3. Argomentario obiezioni
| Obiezione | Risposta |
|---|---|
| "Ci sentiamo a settembre" | "Nessun problema. Il bonus luglio però scade il 31/07 — da settembre è listino pieno. Se attiviamo ora tu a settembre vendi, non installi." |
| "Ad agosto non c'è nessuno" | "Esatto: per questo è il momento migliore per settare tutto senza pressione. Al rientro sei il primo pronto." |
| "Quanto costa dopo?" | "Prezzo 2026 bloccato con l'attivazione anticipata — nessuna sorpresa." |
| "Devo pensarci" | "Certo. Ti tengo lo slot fino al [+3 giorni], poi lo libero per gli altri della lista. Preferisci setup −30% o primo mese gratis?" |

## 4. Cadence & tracking
- Finestre: **h9:30** e **h18:00** (21→23/07 copertura 7/7). Follow-up msg dopo 48h di silenzio (max 2, poi canale alternativo).
- EOD: `metric --name s1_lead_contattati --value <n>` · `s1_risposte` · su chiusura `s1_anticipi_chiusi` + `s1_incasso_eur` + `checkpoint --task WF-S1`.

## 5. Escalation
- 0 risposte sui primi 3 entro 22/07 h18:00 → checkpoint di allerta + revisione msg-1 (hook) con Claude.
- Veto extra-sconto → `decision --title "sconto eccezione lead X"` (mai sconti fuori termini non registrati).

---
⛓️ P12: `WF-S1#estate-2026` · owner esecuzione: Max (90'/g max) · supporto: claude, chief-forge
