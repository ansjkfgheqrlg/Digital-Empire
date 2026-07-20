# 🔍 COPY REVIEW APSOC — Sito "Agency page" (MIR-12, review ufficiale copy-workflow)

> **Intestazione ADR-008** — proprietario: 04-MARKETING / L2-1 Copywriting · controllore: copy-workflow
> (framework APSOC/CPB — il documento `CPB_Gestioneobiezioni.md` in questa cartella è la nostra stessa
> dottrina) + METHOD-GUARD per l'uso commerciale · origine: MIR-12 dossier 18 (2026-07-20, CP-20260720-012)
> — revisione condotta da sessione Claude su `Agency page - Copia/` (versione evoluta: blog + 5 CPB;
> `Agency page/` è la più vecchia, note delta in §7) · governo: ADR-002/003/008/009 · Art.2 (prove, non promesse).
>
> **Natura del documento:** REVIEW — nessun `.tsx` toccato (ADR-003: il sito è asset di Max).
> Patch proposte = da applicare in corsia grafica/deploy di Max dopo risposte ASK (§6).

## 0. Verdetto in una riga
Grafica e architettura persuasiva da livelli alti (struttura APSOC/CPB eseguita col nostro stesso metodo),
ma **sotto la soglia di pubblicazione: claim numerici senza prova (Art.2), tracciamento assente al 100%,
form che finge successo su errore, consenso privacy mancante, offerta gratuita non unificata** = lo stesso
sito viola 4 dei 21 punti della nostra checklist che vendiamo. Il cane deve mangiare il suo cibo.

## 1. Punteggi APSOC (gate minimo 85)

| Sezione | A | P | S | O | C | TOV/Verità | Parziale |
|---|---|---|---|---|---|---|---|
| Hero | 70 | 88 | 85 | 80 | 72 | 90 | 80 |
| AreaSelector (CRO/AI) | 85 | 88 | 90 | 75 | 80 | 85 | 84 |
| CroHeroBottom (4 Diagnosi) | 92 | 90 | 88 | 85 | 78 | 90 | 88 ✅ |
| FunnelComparison + CroFunnel (educational) | 88 | 90 | 92 | 80 | 75 | 95 | 87 ✅ |
| HowWeWork + Services (pilastri, esempio 1%→5%) | 85 | 90 | 92 | 80 | 78 | 92 | 87 ✅ |
| ScientificProofs | 82 | 85 | 80 | **55** | 70 | **40** | 62 ❌ |
| 5 CPB Obiezioni (CRO) | 88 | 82 | 85 | 78 | 80 | **35** | 72 ❌ |
| WhyUs | 90 | 88 | 88 | 80 | 78 | 85 | 86 ✅ |
| Trust / Offerta gratuita | 90 | 85 | 88 | 85 | 85 | **45** | 78 ❌ |
| Contact (form) | 80 | 82 | 85 | 70 | 75 | **30** | 68 ❌ |
| Newsletter | 70 | 72 | 65 | 60 | 68 | **40** | 63 ❌ |
| Footer | 78 | 80 | 80 | 75 | 75 | **50** | 73 ❌ |
| Percorso AI (6 sezioni) | 85 | 82 | 85 | 80 | 80 | **55** | 78 ❌ |
| **SITO (pesato)** | 83 | 84 | 85 | 76 | 76 | **58** | **78/100** ❌ (gate 85) |

Aderenza TOV DE (CARISMA-DIRETTO-SINCERO-SEMPLICE-FORMAZIONE): buona nel 70% del sito; i punti deboli
sono la verità dei numeri e lo stile paura/iperbole del percorso AI.

---

## 2. P0 — BLOCCANTI pre-pubblicazione (verità / legge / dati)

### P0-1 · Claim numerici senza fonte (violazione Art.2 — "prove, non promesse")
Il sito **predica giustamente** "usa dati e fonti" (il nostro manuale CPB, p.88: «Usa anche la fonte»),
ma poi non lo fa. Ogni numero o ha fonte reale o va riformulato:
| # | Dove | Claim | Problema |
|---|---|---|---|
| 1 | ObjectionCPB | "applicato in oltre **50 mercati** differenti" | mai successo (MKD brand-offer: nessuna prova del genere) |
| 2 | ObjectionCPB_Checkout | "**+600%** efficienza; converte dal **3% all'8%** vs 0.5%" | statistiche inventate, senza fonte |
| 3 | ObjectionCPB_Website | "incrementi misurabili fino al **+400%**" | idem |
| 4 | AiObjections | "recuperato entro **60 giorni netti**" | promessa temporale non misurata |
| 5 | AiObjections | "riduci il costo amministrativo del **70%**" | idem |
| 6 | AiEducation | "chi non integra l'AI è destinato a **scomparire nei prossimi 3 anni**" | profezia inventata |
| 7 | Footer | "**Milano & Dubai, UAE**" · tel "+39 02 369 369" · "Uptime 2024 99.98%" | sedi/numeri non verificabili; © 2025 stantio (siamo nel 2026) |
| 8 | ScientificProofs | "30% aperture / 50% clic" con `source: "#"` | fonte vuota = peggio di nessuna fonte |

**Patch tipo:** o sostituire con dati nostri veri quando li avremo (caso Novacar, audit reali),
oppure riformulare senza numeri inventati: "lo stesso metodo si applica perché le leve decisionali
sono universali — e lo dimostriamo sul TUO caso nella sessione gratuita" (più forte, più onesto).

### P0-2 · Tracking assente al 100% (MIR-12 parte "eventi uniformi")
`grep` su tutto il progetto: **nessun gtag/dataLayer/Pixel/evento**. Il nostro blog insegna
«installa pixel di tracciamento su ogni pagina del tuo funnel» (data/blogPosts.tsx) e noi vendiamo
misurazione → **vera incoerenza dogfooding**. Schema minimo uniforme proposto (GA4 + Meta Pixel,
nome_evento snake_case + parametro `sezione`): `view_hero` · `select_area` (CRO/AI) ·
`click_cta` (sezione+label) · `submit_lead` · `lead_fail` (vedi P0-3) · `click_calendly`.

### P0-3 · Il form "mente" sull'errore (Contact.tsx)
Se `fetch(FORMSPREE_ENDPOINT)` fallisce, il catch esegue comunque `setIsSubmitted(true)` →
l'utente vede "richiesta inviata" ma **il lead è perso per sempre** (solo localStorage).
= vendiamo affidabilità e perdiamo lead in silenzio. Patch: stato errore onesto + retry +
mail di fallback + evento `lead_fail` tracciato.

### P0-4 · GDPR: consenso privacy assente
Contact e Newsletter raccolgono email **senza checkbox consenso né link all'informativa**
(obbligo UE). Il footer cita "Privacy Policy / Cookie Protocol" — le pagine vanno create/linkate.
Patch: checkbox obbligatorio con link informativa su entrambi i form prima dei bottoni.

### P0-5 · Offerta gratuita non unificata (3 nomi diversi!)
- **Trust:** "SESSIONE STRATEGICA GRATUITA — VALORE REALE: €500 · PER TE: €0 — **40 Minuti**" + scarcity "Solo 3 slot questa settimana" (testo statico = finta urgenza — viola il punto 6 della NOSTRA checklist 21 punti).
- **Contact:** bullet "Analisi Gratuita della tua presenza online" (durata non detta).
- **Kit canale YouTube (vita pubblica del brand):** "**Analisi Gratuita di 15 minuti**" + gate 3 domande.
UNA sola offerta, UN nome, UNA durata, ovunque → decisione in ASK §6 (Q1).

---

## 3. P1 — Copy/APSOC (impatto conversioni)

1. **Hero:** la H1 "ingegneria strategica per la tua scalata" è brand-poetica; l'Attenzione vera
   sta nel sub ("Misuriamo dove perdi clienti... conversione di ogni step"). ➕ Proposta v2 (stessa estetica,
   dolore prima): linea 1 rimane di brand; sub riscritto pain-first: *"Spendi in ads e il telefono non
   squilla? Misuriamo il punto esatto dove il tuo sito perde clienti — e lo sistemiamo. Prima misurato, poi migliorato."*
2. **Ripetizione verbatim**: la frase "Hai il tuo prodotto/servizio… non sta andando come speravi…
   il problema è il funnel" appare IDENTICA in AreaSelector e CroHeroBottom → tenere una volta sola.
3. **Jargon backstage in pubblico**: header "Protocollo CPB", "Security Protocol: High Scrutiny",
   "Protocollo Ponte" (mai definito) = etichette nostre interne che il visitatore non capisce.
   Il metodo si MOSTRA (come già fa CroHeroBottom), non si nomina. (Rispecchia la regola dei nostri video: niente dietro-le-quinte lessicali.)
4. **CTA**: 3+ frasi diverse ("esegui protocollo crescita" · "applica protocollo ora" · "BLOCCA IL TUO SLOT ORA") →
   unificare sul verbo dell'offerta scelta in Q1 (es. "Blocca la tua Analisi Gratuita"), varianti documentate nel kit.
5. **Tono paura/iperbole** nel percorso AI: "suicidio strategico", "adattarsi o estinguersi",
   "spietatamente superiore", "leve psicologiche infallibili che costringono ad agire" → frizione con
   SINCERO-FORMAZIONE e con la promessa "collaboriamo solo se possiamo aiutarti". Audacia sì, minaccia no.
   (E la stessa dottrina CPB del repo avverte: claim esagerati generano obiezioni nuove.)
6. **Obiezioni mancanti (più forti per ICP)**: coperte 5 (specificità, checkout-diretto, sito esistente,
   passaparola, tempo) + 2 AI. Manca la N.1: **"le agenzie mi hanno già fregato"** → CPB #6 da aggiungere
   (risposta pronta dalla nostra descrizione canale: "lavoriamo a progetto, misuriamo prima/dopo, ti lasciamo il metodo").
   E **"quanto costa?"**: mai gestita (ticket €1.000-1.500 + variabile da MKD — almeno l'ancora "progetto, non abbonamento").
7. **ScientificProofs**: aneddoto in prima persona ("Sono recentemente stato pagato da…") su sito di brand
   senza firma = voce confusa → firmare (es. "Max, founder") o rimuovere.
8. **Dettagli**: "=" nel sub hero → freccia/due punti; "ai"/"Ai"/"AI" → normalizzare; placeholder
   "Enter your email" inglese su sito italiano; "Dubai" da verificare (v. P0-1 #7).

## 4. P2 — Tecnica/struttura
- **Dead code**: 7 componenti non renderizzati (`Philosophy`, `HopeSection`, `AutomationSection`,
  `SocialFunnelSection`, `ObjectionFlow`, `ScrollRevealText`, `WebDesignShowcase`) + `BlogParts`
  → cancellare o spostare in `_archive/` (regole repo: niente codice morto negli asset attivi).
- **SEO**: HashRouter → blog non indicizzabile per-post; su landing mono-pagina ok, ma se il blog
  conta per il funnel organico (e conterà: contenuti TOFU), serve router history/SSG.
- **Select Contact** include "Social Growth & Marketing" — ⚠️ contraddice MKD ("non facciamo
  contenuti sui social"): confermare con Max se il sito precede il posizionamento o se l'offerta è cambiata.

## 5. Cosa è da lodare (non replicare errori = anche studiare i successi)
✅ Struttura persuasiva di alto livello: diagnosi pain-first (4 Diagnosi = esattamente il nostro ICP),
educational vero (calcolatore 10.000 visite 0.8%→2.4% = 240 clienti), WhyUs differenziante
("Ingegneri non Artisti · Profitto non Like · Imperi non Siti"), meta-copy onesto
("più resti qui, più acquisisci formazione… nel peggiore dei casi ne uscirai con del valore in più")
= TOV FORMAZIONE perfetto, coerente col canale YouTube. La ossatura NON si tocca: si puliscono verità,
uniformità e tracking.

## 6. ASK (MIR-3 — ASK-PROTOCOL, prima applicazione reale)
| # | Domanda (1 decisione) | Opzioni | Raccomandazione | Default [ASSUNZIONE] | Trigger |
|---|---|---|---|---|---|
| Q1 | Offerta gratuita definitiva: nome+durata? | A) "Analisi Gratuita 15 min" (canale) · B) "Sessione Strategica 40 min (€500→0)" | **A** (coerenza totale canale↔sito; 15 min protegge il tempo, gate 3 domande già pronto; l'ancora €500 si può citare come "valore consulenza" senza inventare durate) | A | T1/T3 |
| Q2 | Sedi/telefono/metriche footer (Dubai, +39 02 369 369, uptime 99.98%) sono reali? | A) reali → le teniamo · B) estetiche → via/sostituire | **B sospetta** (Art.2: fino a prova, togliere o mettere solo Milano reale) | B | T2 |
| Q3 | "Social Growth & Marketing" nella select Contact: l'offerta include social? | A) sì, MKD superato · B) no → togliere dalla select | **B** (MKD dice "non facciamo contenuti sui social"; se cambia, va aggiornato il MKD per decreto, mai il sito a insaputa del canone) | B | T4 |

## 7. Delta `Agency page/` (versione vecchia)
Stessa hero e sezioni base ma SENZA: blog, 5 CPB, Trust/Sessione, percorso AI, calcolatore funnel.
La evoluta ("- Copia") è chiaramente il ramo vivo → **raccomandazione Max: deprecare/archiviare
`Agency page/` per evitare divergenze** (inventaria: 2 grafiche da tenere sincronizzate = anti-pattern).

---
**Esito review:** 78/100 → dopo patch P0 (verità, tracking, form onesto, GDPR, offerta unica)
stimato 90+ (gate A8 85 PASS). Applicazione patch = corsia Max (grafica/deploy). AL REVIEWER: A+ sulla struttura, C- sulla verifica dei numeri — e questa seconda si sistema in un pomeriggio.
