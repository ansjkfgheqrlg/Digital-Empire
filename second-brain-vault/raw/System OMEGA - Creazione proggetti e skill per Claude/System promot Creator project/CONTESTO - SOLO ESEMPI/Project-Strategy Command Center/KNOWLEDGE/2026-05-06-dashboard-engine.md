# DASHBOARD_ENGINE

> Source: File system (`System OMEGA - Creazione proggetti e skill per Claude\System promot Creator project\CONTESTO - SOLO ESEMPI\Project-Strategy Command Center\KNOWLEDGE\DASHBOARD_ENGINE.md`)
> Collected: 2026-05-06
> Published: Unknown

# ═══════════════════════════════════════════════════════════════
# 📄 DASHBOARD_ENGINE.md
# ═══════════════════════════════════════════════════════════════
# Versione: 1.0
# Categoria: CORE_LOGIC
# Priorità: P0 — BLOCCANTE
# Dipendenze: GERARCHIA_PILLAR.md (per la sequenza di analisi)
# Referenziato da: Custom Instructions — Sezione 2.1 (Step 2), Sezione 2.2 (Dashboard), Sezione 4.4, Sezione 5.2, Sezione 8.1 (Step 3), Sezione 8.2 (Step 2), Sezione 8.3 (Step 1)
# ═══════════════════════════════════════════════════════════════

## 📋 SCOPO

Questo file contiene il template COMPLETO della Dashboard Empire — il pannello di controllo unificato che monitora tutti i pillar di Digital Empire in un'unica vista. È il documento più utilizzato del Command Center: ogni review (settimanale, mensile, trimestrale) parte da qui.

La dashboard trasforma dati grezzi in decisioni. Senza dashboard compilata, il Command Center è cieco.

Principio: "Se non lo misuri, non lo gestisci. Se non lo gestisci, non lo migliori."

---

## 📖 CONTENUTO PRINCIPALE

### 1. STRUTTURA DELLA DASHBOARD

La dashboard ha 7 sezioni, sempre nello stesso ordine:
ORDINE DI COMPILAZIONE E LETTURA
═════════════════════════════════

OVERVIEW EMPIRE → Vista d'insieme revenue totale
PILLAR 1: AGENZIA → Acquisizione + Delivery
PILLAR 2: INFO-BIZ → Lista + Prodotti + Funnel
PILLAR 3: YOUTUBE → Canale + Lead Gen
SATELLITE → KDP + AI Influencer
CROSS-POLLINATION → Azioni + Bridge Metrics
ALLARMI → Soglie superate
text


### 2. SISTEMA DI STATUS
SEMAFORO — Come assegnare 🟢🟡🔴
═════════════════════════════════

🟢 ON TRACK
Condizione: Il valore REALE è ≥ 80% del TARGET
Significato: Tutto procede. Nessuna azione correttiva necessaria.
Azione: Mantieni il ritmo.

🟡 A RISCHIO
Condizione: Il valore REALE è tra 50% e 79% del TARGET
Significato: C'è un gap significativo. Se non intervieni, diventerà 🔴.
Azione: Identifica la causa. Pianifica intervento entro 7 giorni.

🔴 OFF TRACK
Condizione: Il valore REALE è < 50% del TARGET oppure il valore è ZERO
Significato: Problema critico. Richiede azione immediata.
Azione: Intervento prioritario. Se è il pillar Agenzia → attiva
protocollo di riallocazione da GERARCHIA_PILLAR.md.

⚪ NON ATTIVO
Condizione: Il pillar o la metrica non è ancora stata avviata
Significato: Non c'è un target definito.
Azione: Nessuna — è parcheggiato. Non allocare tempo.

REGOLA DI ASSEGNAZIONE:

Calcola: (Valore Reale / Valore Target) × 100
SE ≥ 80% → 🟢
SE 50-79% → 🟡
SE < 50% o ZERO → 🔴
SE non avviato → ⚪
text


### 3. TEMPLATE DASHBOARD — SEZIONE 1: OVERVIEW EMPIRE
═══════════════════════════════════════════════════════════
DASHBOARD EMPIRE — [MESE] [ANNO]
Compilata il: [DATA]
═══════════════════════════════════════════════════════════

━━━ SEZIONE 1: OVERVIEW ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REVENUE TOTALE DIGITAL EMPIRE: €[___]

┌──────────────────┬──────────┬──────────┬──────────────┐
│ Pillar │ Revenue │ % Totale │ % Target │
├──────────────────┼──────────┼──────────┼──────────────┤
│ Agenzia CRO │ €[] │ []% │ 50-60% │
│ Info-Business │ €[] │ []% │ 20-30% │
│ YouTube │ €[] │ []% │ 5-15% │
│ KDP │ €[] │ []% │ 2-5% │
│ AI Influencer │ €[] │ []% │ 2-5% │
│ Altro │ €[] │ []% │ — │
├──────────────────┼──────────┼──────────┼──────────────┤
│ TOTALE │ €[___] │ 100% │ │
└──────────────────┴──────────┴──────────┴──────────────┘

TREND VS MESE PRECEDENTE:
├── Revenue totale: [↑ / ↓ / →] ([+/-]%)
├── Pillar in crescita: [quale]
├── Pillar in calo: [quale]
└── Pillar stabile: [quale]

TARGET TRIMESTRALE: €[]
PROGRESSO: €[] ([]%)
PROIEZIONE FINE Q: €[] (basata sul trend attuale)

text


**Istruzioni di compilazione per la Sezione 1:**
- Il revenue per pillar include TUTTO: progetti, vendite, AdSense, royalties, sponsorizzazioni
- La % Target indica la distribuzione IDEALE da GERARCHIA_PILLAR.md
- Se la distribuzione reale si discosta di più del 15% dalla target → segnalare
- La proiezione fine Q si calcola: (Revenue mesi completati / N mesi completati) × 3

---

### 4. TEMPLATE DASHBOARD — SEZIONE 2: AGENZIA CRO
━━━ SEZIONE 2: PILLAR 1 — AGENZIA CRO ━━━━━━━━━━━━━━━━

METRICHE ACQUISIZIONE:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Lead qualificati / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Call strategiche / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Proposte inviate / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Clienti chiusi / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Close rate │ [N]% │ [N]% │ [🟢🟡🔴]│
│ Revenue agenzia / mese │ €[N] │ €[N] │ [🟢🟡🔴]│
│ Valore medio progetto │ €[N] │ €[N] │ [🟢🟡🔴]│
└─────────────────────────┴──────────┴──────────┴────────┘

FUNNEL ACQUISIZIONE (conversion tra step):
┌─────────────────────────────────────────────────────────┐
│ Lead → Call: [N]% │ Call → Proposta: [N]% │
│ Proposta → Chiusura: [N]% │ Lead → Chiusura: [N]% │
└─────────────────────────────────────────────────────────┘

METRICHE DELIVERY:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Progetti attivi │ [N] │ [N] │ │
│ Progetti completati │ [N] │ [N] │ │
│ questo mese │ │ │ │
│ NPS clienti (media) │ >8 │ [N] │ [🟢🟡🔴]│
│ Uplift medio CR │ [N]% │ [N]% │ │
│ ottenuto │ │ │ │
│ Referral ricevuti │ [N] │ [N] │ │
│ questo mese │ │ │ │
│ Success fee incassato │ €[N] │ €[N] │ │
│ Retention rate clienti │ >70% │ [N]% │ [🟢🟡🔴]│
└─────────────────────────┴──────────┴──────────┴────────┘

FONTE DEI LEAD (da dove arrivano):
┌─────────────────────┬──────────┬──────────┐
│ Fonte │ N. Lead │ % Totale │
├─────────────────────┼──────────┼──────────┤
│ Outreach diretto │ [N] │ [N]% │
│ YouTube organico │ [N] │ [N]% │
│ Info-Biz (bridge) │ [N] │ [N]% │
│ Referral clienti │ [N] │ [N]% │
│ KDP (link nei libri)│ [N] │ [N]% │
│ Altro │ [N] │ [N]% │
└─────────────────────┴──────────┴──────────┘

HEALTH CHECK AGENZIA:
□ Pipeline piena per i prossimi 30 giorni?
□ Capacità di delivery sufficiente per nuovi clienti?
□ Clienti esistenti soddisfatti (NPS > 8)?
□ Outreach attivo e costante (min 5 contatti/giorno)?
□ Follow-up sistematico su lead aperti?
□ Almeno 1 caso studio documentato questo mese?

STATUS COMPLESSIVO AGENZIA: [🟢🟡🔴]
MOTIVAZIONE: [Frase che spiega lo status]

text


**Istruzioni di compilazione per la Sezione 2:**
- Close rate = Clienti chiusi / Call strategiche × 100
- NPS: chiedi ai clienti "Da 1 a 10, quanto consiglieresti il nostro servizio?" dopo ogni progetto
- Uplift CR: (CR dopo - CR prima) / CR prima × 100
- Fonte dei lead: fondamentale per capire quali canali funzionano. Se un canale genera 0 lead per 2+ mesi → investigare
- Health check: se 3+ caselle sono vuote → il pillar è a rischio

---

### 5. TEMPLATE DASHBOARD — SEZIONE 3: INFO-BUSINESS
━━━ SEZIONE 3: PILLAR 2 — INFO-BUSINESS ━━━━━━━━━━━━━━━

METRICHE LISTA EMAIL:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Dimensione lista totale │ [N] │ [N] │ │
│ Nuovi lead / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Fonte lead: YouTube │ [N] │ [N] │ │
│ Fonte lead: KDP │ [N] │ [N] │ │
│ Fonte lead: Ads/Altro │ [N] │ [N] │ │
│ Open rate medio │ >25% │ [N]% │ [🟢🟡🔴]│
│ Click rate medio │ >3% │ [N]% │ [🟢🟡🔴]│
│ Unsubscribe rate │ <1% │ [N]% │ [🟢🟡🔴]│
│ Engagement score │ >50% │ [N]% │ [🟢🟡🔴]│
│ (% lista attiva) │ │ │ │
└─────────────────────────┴──────────┴──────────┴────────┘

METRICHE PRODOTTI:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Prodotti attivi catalogo│ [N] │ [N] │ │
│ Revenue info-biz / mese │ €[N] │ €[N] │ [🟢🟡🔴]│
│ Revenue per livello: │ │ │ │
│ Lead magnet (€0) │ N/A │ [N] dwl │ │
│ Mini-corsi (€7-47) │ €[N] │ €[N] │ │
│ Corsi (€97-297) │ €[N] │ €[N] │ │
│ Percorsi (€497-997) │ €[N] │ €[N] │ │
│ Vendite totali / mese │ [N] │ [N] │ │
│ Refund rate medio │ <10% │ [N]% │ [🟢🟡🔴]│
│ NPS studenti medio │ >7 │ [N] │ [🟢🟡🔴]│
│ Lifetime Value cliente │ €[N] │ €[N] │ │
│ info-biz │ │ │ │
└─────────────────────────┴──────────┴──────────┴────────┘

METRICHE FUNNEL:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Opt-in rate landing │ >30% │ [N]% │ [🟢🟡🔴]│
│ Upsell rate (post │ >5% │ [N]% │ [🟢🟡🔴]│
│ opt-in → mini-corso) │ │ │ │
│ Iscrizione webinar │ >15% │ [N]% │ [🟢🟡🔴]│
│ (da lista) │ │ │ │
│ Show rate webinar │ >30% │ [N]% │ [🟢🟡🔴]│
│ Conversion webinar │ >5% │ [N]% │ [🟢🟡🔴]│
│ (presenti → acquisto) │ │ │ │
│ Email sequence CR │ >2% │ [N]% │ [🟢🟡🔴]│
│ (nurture → vendita) │ │ │ │
└─────────────────────────┴──────────┴──────────┴────────┘

LANCIO ATTIVO (se presente):
┌─────────────────────────────────────────────────────────┐
│ Prodotto: [Nome] │
│ Tipo: [Mini-corso / Corso / Percorso] │
│ Prezzo: €[N] │
│ Fase attuale: [Pre-lancio / Lancio / Post-lancio] │
│ Revenue target lancio: €[N] │
│ Revenue attuale: €[N] ([N]%) │
│ Unità vendute: [N] │
│ Data fine lancio: [GG/MM] │
│ Prossimo lancio: [Prodotto] — Data: [GG/MM] │
└─────────────────────────────────────────────────────────┘
SE nessun lancio attivo: "Nessun lancio attivo. Prossimo
lancio pianificato: [Prodotto] — [Data] / Non pianificato"

FUNNEL EVERGREEN (se attivo):
┌─────────────────────────────────────────────────────────┐
│ Prodotto evergreen: [Nome] │
│ Revenue / mese da evergreen: €[N] │
│ Vendite / mese: [N] │
│ Conversion rate funnel: [N]% │
│ Trend: [↑ / ↓ / →] │
└─────────────────────────────────────────────────────────┘

HEALTH CHECK INFO-BIZ:
□ Almeno 2 idee con score >60 nel backlog prodotti?
□ Funnel evergreen attivo e funzionante?
□ Nurture email settimanale inviato regolarmente?
□ Landing page opt-in testata e >30% CR?
□ Cross-pollination attiva con agenzia e YouTube?
□ Almeno 1 testimonial studente raccolta questo mese?

STATUS COMPLESSIVO INFO-BIZ: [🟢🟡🔴]
MOTIVAZIONE: [Frase che spiega lo status]

text


**Istruzioni di compilazione per la Sezione 3:**
- Engagement score = (lead che hanno aperto almeno 1 email negli ultimi 30gg / totale lista) × 100
- LTV cliente = Revenue totale info-biz / N clienti unici totali
- Il funnel evergreen è separato dal lancio attivo — monitora entrambi
- Se refund rate > 10% → problema di qualità prodotto o mismatch aspettative
- Se open rate < 20% → problema di deliverability o frequenza email troppo alta

---

### 6. TEMPLATE DASHBOARD — SEZIONE 4: YOUTUBE / CONTENT
━━━ SEZIONE 4: PILLAR 3 — YOUTUBE / CONTENT ━━━━━━━━━━━

METRICHE CANALE:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Iscritti totali │ [N] │ [N] │ │
│ Nuovi iscritti / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Views totali / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ Watch time medio │ [N] min │ [N] min │ [🟢🟡🔴]│
│ Video pubblicati / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ CTR medio thumbnail │ >5% │ [N]% │ [🟢🟡🔴]│
│ Retention rate medio │ >40% │ [N]% │ [🟢🟡🔴]│
│ (% video guardato) │ │ │ │
│ Revenue YT (AdSense + │ €[N] │ €[N] │ │
│ sponsorizzazioni) │ │ │ │
└─────────────────────────┴──────────┴──────────┴────────┘

METRICHE LEAD GENERATION:
┌─────────────────────────┬──────────┬──────────┬────────┐
│ Metrica │ Target │ Reale │ Status │
├─────────────────────────┼──────────┼──────────┼────────┤
│ Click su link in descr. │ [N] │ [N] │ │
│ Lead da YouTube / mese │ [N] │ [N] │ [🟢🟡🔴]│
│ (opt-in da link YT) │ │ │ │
│ Lead YT → call agenzia │ [N] │ [N] │ │
│ Lead YT → acquisto │ [N] │ [N] │ │
│ info-biz │ │ │ │
│ Conversion rate link │ >2% │ [N]% │ [🟢🟡🔴]│
│ (click → opt-in) │ │ │ │
└─────────────────────────┴──────────┴──────────┴────────┘

CONTENT MIX (dal YouTube Lead Engine P2):
┌──────────────┬──────────┬──────────┬──────────┬────────┐
│ Tipo │ Target % │ Target N │ Reale N │ Status │
├──────────────┼──────────┼──────────┼──────────┼────────┤
│ Anchor (70%) │ 70% │ [N] │ [N] │ [🟢🟡🔴]│
│ (educativi, │ │ │ │ │
│ valore) │ │ │ │ │
├──────────────┼──────────┼──────────┼──────────┼────────┤
│ Shift (20%) │ 20% │ [N] │ [N] │ [🟢🟡🔴]│
│ (opinioni, │ │ │ │ │
│ trend) │ │ │ │ │
├──────────────┼──────────┼──────────┼──────────┼────────┤
│ Conversion │ 10% │ [N] │ [N] │ [🟢🟡🔴]│
│ (10%) │ │ │ │ │
│ (CTA diretta │ │ │ │ │
│ agenzia/ │ │ │ │ │
│ info-biz) │ │ │ │ │
└──────────────┴──────────┴──────────┴──────────┴────────┘

TOP 3 VIDEO DEL MESE:
┌────┬────────────────────────┬────────┬──────────┬───────┐
│ # │ Titolo │ Views │ CTR │ Lead │
│ │ │ │ │generati│
├────┼────────────────────────┼────────┼──────────┼───────┤
│ 1 │ [Titolo] │ [N] │ [N]% │ [N] │
│ 2 │ [Titolo] │ [N] │ [N]% │ [N] │
│ 3 │ [Titolo] │ [N] │ [N]% │ [N] │
└────┴────────────────────────┴────────┴──────────┴───────┘

HEALTH CHECK YOUTUBE:
□ Pubblicazione costante (min 1 video/settimana)?
□ CTA verso PDF/funnel info-biz in OGNI video?
□ Content mix rispetta le percentuali 70/20/10?
□ Video alimentano i topic dei prodotti info?
□ Link in descrizione funzionanti e tracciati (UTM)?
□ Thumbnail testate (CTR > 5%)?

STATUS COMPLESSIVO YOUTUBE: [🟢🟡🔴]
MOTIVAZIONE: [Frase che spiega lo status]

text


**Istruzioni di compilazione per la Sezione 4:**
- Lead da YouTube = chi clicca link in descrizione E completa l'opt-in nella landing page
- Usa UTM diversi per ogni video per tracciare quale video genera più lead
- Content mix: conta i video del mese e verifica la distribuzione %
- Se CTR < 3% → problema di thumbnail e titoli, non di contenuto
- Se watch time < 3 minuti → problema di hook e struttura video
- Se click su link ma 0 opt-in → problema di landing page, non di YouTube

---

### 7. TEMPLATE DASHBOARD — SEZIONE 5: SATELLITE
━━━ SEZIONE 5: SATELLITE — KDP + AI INFLUENCER ━━━━━━━━

KDP CONTENT FACTORY:
┌─────────────────────────┬──────────┬──────────┐
│ Metrica │ Target │ Reale │
├─────────────────────────┼──────────┼──────────┤
│ Libri pubblicati totali │ [N] │ [N] │
│ Nuovi libri questo mese │ [N] │ [N] │
│ Revenue KDP / mese │ €[N] │ €[N] │
│ Revenue per libro medio │ €[N] │ €[N] │
│ TikTok views totali │ [N] │ [N] │
│ (marketing libri) │ │ │
│ Lead da KDP → lista │ [N] │ [N] │
│ email info-biz │ │ │
│ Best performer │ — │ [Titolo] │
│ Best performer revenue │ — │ €[N]/mese│
└─────────────────────────┴──────────┴──────────┘

AI INFLUENCER LAB:
┌─────────────────────────┬──────────┬──────────┐
│ Metrica │ Target │ Reale │
├─────────────────────────┼──────────┼──────────┤
│ Personaggi attivi │ [N] │ [N] │
│ Follower totali │ [N] │ [N] │
│ Revenue / mese │ €[N] │ €[N] │
│ Revenue stream attivi │ [N] di 5 │ [N] di 5 │
│ Piattaforme attive │ [N] │ [N] │
│ Contenuti / mese │ [N] │ [N] │
└─────────────────────────┴──────────┴──────────┘

VERIFICA ALLOCAZIONE TEMPO SATELLITE:
Tempo dedicato ai satellite questo mese: [N] ore ([N]%)
Target: ≤ 10% del tempo totale
Status: [🟢 se ≤10% / 🔴 se >10%]
SE 🔴: "I satellite stanno rubando focus al core.
Riduci o delega."

STATUS COMPLESSIVO SATELLITE: [🟢🟡🔴⚪]

text


---

### 8. TEMPLATE DASHBOARD — SEZIONE 6: CROSS-POLLINATION
━━━ SEZIONE 6: CROSS-POLLINATION REPORT ━━━━━━━━━━━━━━━

AZIONI CROSS-PILLAR ESEGUITE QUESTO MESE:
┌────┬───────────────────────────┬────────────┬────────┬───────────────┐
│ # │ Azione │ Flusso │ Status │ Risultato │
│ │ │ (Da → A) │ │ │
├────┼───────────────────────────┼────────────┼────────┼───────────────┤
│ S1 │ [Azione settimana 1] │ [P→P] │ [✅❌] │ [Risultato] │
│ S2 │ [Azione settimana 2] │ [P→P] │ [✅❌] │ [Risultato] │
│ S3 │ [Azione settimana 3] │ [P→P] │ [✅❌] │ [Risultato] │
│ S4 │ [Azione settimana 4] │ [P→P] │ [✅❌] │ [Risultato] │
├────┼───────────────────────────┼────────────┼────────┼───────────────┤
│ │ TOTALE AZIONI ESEGUITE │ │ [N]/4 │ │
└────┴───────────────────────────┴────────────┴────────┴───────────────┘
Target: ≥ 4 azioni/mese (1/settimana)
Status: [🟢 se ≥4 / 🟡 se 2-3 / 🔴 se 0-1]

BRIDGE METRICS:
┌───────────────────────────────┬──────────┬──────────┬───────┐
│ Flusso │ Mese │ Mese │ Trend │
│ │ Corrente │ Preced. │ │
├───────────────────────────────┼──────────┼──────────┼───────┤
│ Studenti info-biz → lead │ [N] │ [N] │ [↑↓→] │
│ agenzia │ │ │ │
│ Clienti agenzia → acquisto │ [N] │ [N] │ [↑↓→] │
│ corso info-biz │ │ │ │
│ Lead da YouTube → opt-in │ [N] │ [N] │ [↑↓→] │
│ lista info-biz │ │ │ │
│ Lettori KDP → opt-in lista │ [N] │ [N] │ [↑↓→] │
│ info-biz │ │ │ │
│ Lead YouTube → call agenzia │ [N] │ [N] │ [↑↓→] │
├───────────────────────────────┼──────────┼──────────┼───────┤
│ REVENUE da cross-pollination │ €[N] │ €[N] │ [↑↓→] │
└───────────────────────────────┴──────────┴──────────┴───────┘

FLUSSI PIÙ ATTIVI:

[Flusso con più attività/risultati]
[Secondo flusso]
FLUSSI DORMIENTI (0 attività per 30+ giorni):

[Flusso dormiente — azione suggerita]
[Flusso dormiente — azione suggerita]
text


---

### 9. TEMPLATE DASHBOARD — SEZIONE 7: ALLARMI
━━━ SEZIONE 7: ALLARMI ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────────────────────────┬────────┬───────────────┐
│ Allarme │ Stato │ Azione │
├────────────────────────────────┼────────┼───────────────┤
│ 🔴 Revenue agenzia ↓ per │ [OK/⚠️]│ [Se attivo: │
│ 2 mesi consecutivi │ │ STOP tutto, │
│ │ │ focus 100% │
│ │ │ pipeline] │
├────────────────────────────────┼────────┼───────────────┤
│ 🔴 Zero vendite info-biz │ [OK/⚠️]│ [Se attivo: │
│ per 30+ giorni │ │ diagnosi │
│ │ │ funnel] │
├────────────────────────────────┼────────┼───────────────┤
│ 🔴 Zero video YouTube │ [OK/⚠️]│ [Se attivo: │
│ per 3+ settimane │ │ ripristina │
│ │ │ produzione] │
├────────────────────────────────┼────────┼───────────────┤
│ 🔴 Zero azioni cross-pillar │ [OK/⚠️]│ [Se attivo: │
│ per 30+ giorni │ │ 1 azione │
│ │ │ obbligatoria │
│ │ │ lunedì] │
├────────────────────────────────┼────────┼───────────────┤
│ 🟡 OKR trimestrale < 30% │ [OK/⚠️]│ [Se attivo: │
│ a metà Q │ │ review OKR │
│ │ │ realismo] │
├────────────────────────────────┼────────┼───────────────┤
│ 🟡 Tempo satellite > 10% │ [OK/⚠️]│ [Se attivo: │
│ │ │ riduci o │
│ │ │ delega] │
└────────────────────────────────┴────────┴───────────────┘

ALLARMI ATTIVI QUESTO MESE: [N]
SE > 0: Elencare le azioni immediate in cima alla
prossima review settimanale.

text


---

### 10. VERSIONE RAPIDA — DASHBOARD SETTIMANALE

Per la review settimanale (15 minuti), usa questa versione ridotta:
━━━ DASHBOARD RAPIDA — SETTIMANA [N] — [DATE] ━━━━━━━━━

HEALTH CHECK VELOCE:
┌──────────────┬────────┬───────────────────────────────┐
│ Pillar │ Status │ 1 frase di contesto │
├──────────────┼────────┼───────────────────────────────┤
│ Agenzia CRO │ [🟢🟡🔴]│ [Es: "3 clienti attivi, │
│ │ │ 1 proposta in attesa"] │
├──────────────┼────────┼───────────────────────────────┤
│ Info-Business │ [🟢🟡🔴]│ [Es: "Funnel attivo, 12 │
│ │ │ vendite questa settimana"] │
├──────────────┼────────┼───────────────────────────────┤
│ YouTube │ [🟢🟡🔴]│ [Es: "2 video pubblicati, │
│ │ │ CTR 6.2%"] │
├──────────────┼────────┼───────────────────────────────┤
│ Satellite │ [🟢🟡🔴⚪]│ [Es: "KDP stabile, AI non │
│ │ │ ancora avviato"] │
└──────────────┴────────┴───────────────────────────────┘

NUMERI CHIAVE DELLA SETTIMANA:
├── Nuovi lead agenzia: [N]
├── Revenue incassato: €[N]
├── Vendite info-biz: [N] (€[N])
├── Video pubblicati: [N]
├── Lead da YouTube: [N]
└── Azione cross-pillar: [✅ Fatta / ❌ Non fatta]

ALLARMI: [Nessuno / Lista]
FOCUS PROSSIMA SETTIMANA: [1 frase]

text


---

### 11. ALBERO DIAGNOSTICO — QUANDO UN PILLAR È 🔴
DIAGNOSI PILLAR IN CRISI
═════════════════════════

AGENZIA CRO 🔴 — Perché?
├── Revenue in calo?
│ ├── Meno clienti chiusi → Problema ACQUISIZIONE
│ │ ├── Meno lead? → Aumenta outreach + attiva bridge info-biz
│ │ ├── Meno call? → Follow-up lead esistenti
│ │ ├── Close rate calato? → Rivedi script call (Sales Call Closer)
│ │ └── Valore progetto calato? → Rivedi pricing e positioning
│ └── Clienti persi? → Problema RETENTION
│ ├── NPS basso? → Migliora delivery
│ ├── Risultati scarsi? → Rivedi processo CRO
│ └── Competitor? → Differenzia offerta
└── Pipeline vuota per 30+ gg?
└── EMERGENZA → Protocollo riallocazione da GERARCHIA_PILLAR.md

INFO-BUSINESS 🔴 — Perché?
├── Zero vendite per 30+ gg?
│ ├── Traffico al funnel? → SE zero: problema TRAFFICO (YouTube, ads, lista)
│ │ └── Azione: aumenta CTA nei video, invia email alla lista, attiva ads test
│ ├── Traffico OK ma zero opt-in? → Problema LANDING PAGE
│ │ └── Azione: testa headline, CTA, offerta lead magnet
│ ├── Opt-in OK ma zero vendite? → Problema CONVERSIONE
│ │ └── Azione: rivedi email sequence, prezzo, sales page, offerta
│ └── Vendite ma tutti refund? → Problema PRODOTTO
│ └── Azione: raccogli feedback, migliora contenuto, aggiusta aspettative
└── Lista non cresce?
└── Azione: nuovi lead magnet, più CTA nei video, collaborazioni

YOUTUBE 🔴 — Perché?
├── Zero video pubblicati per 3+ settimane?
│ ├── Problema di TEMPO? → Verifica allocazione (deve essere 15-20%)
│ ├── Problema di IDEE? → Usa backlog contenuti + domande clienti
│ └── Problema di MOTIVAZIONE? → Semplifica formato (video più corti)
├── Video pubblicati ma zero views?
│ ├── CTR basso? → Problema THUMBNAIL + TITOLO
│ └── Views iniziali ma retention bassa? → Problema HOOK + STRUTTURA
└── Views OK ma zero lead?
├── CTA presente nei video? → SE NO: aggiungila
├── Link in descrizione funzionante? → Verifica
└── Landing page allineata al video? → Testa coerenza

text


---

## 🔧 COME UTILIZZARE QUESTO FILE

**Quando consultarlo:**
- Ogni volta che l'utente fornisce dati o chiede "come sta il business"
- Durante ogni review (settimanale: versione rapida, mensile: versione completa)
- Quando un pillar cambia status → usa l'albero diagnostico
- Quando l'utente chiede di compilare la dashboard → usa il template della sezione corrispondente

**Come integrare nella risposta:**
1. Usa il template come STRUTTURA — riempi con i dati dell'utente
2. Assegna SEMPRE il semaforo 🟢🟡🔴 usando le regole della Sezione 2
3. Se un allarme è attivo → segnalalo IN CIMA alla risposta, prima di qualsiasi altro contenuto
4. Se un pillar è 🔴 → usa l'albero diagnostico per identificare la causa e suggerire azioni
5. Se l'utente fornisce dati parziali → compila quello che puoi e chiedi specificamente i dati mancanti con "[DATO MANCANTE — fornisci: ___]"

**Regola di completamento:**
- Review SETTIMANALE → usa la Dashboard Rapida (Sezione 10)
- Review MENSILE → usa la Dashboard Completa (Sezioni 1-7 tutte)
- Review TRIMESTRALE → usa Dashboard Completa + confronto con i 2 mesi precedenti

---

## 🔗 COLLEGAMENTI

- **Dipende da**: `KB/GERARCHIA_PILLAR.md` (per la sequenza di analisi e le regole di priorità)
- **Alimenta**: `KB/OKR_SYSTEM.md` (i dati dashboard alimentano la review degli OKR), `KB/DECISION_FRAMEWORK.md` (lo stato dashboard è il punto di partenza per ogni decisione), `KB/SOGLIE_ALLARME.md` (la dashboard attiva gli allarmi)
- **Collegato a**: `KB/CROSS_POLLINATION_ENGINE.md` (Sezione 6 della dashboard), `KB/REVENUE_TRACKER.md` (dati storici per confronto)
- **Custom Instructions**: Sezione 2.2 (Dashboard), Sezione 4.4 (Esempio output), Sezione 5.2, Sezione 8.1-8.3

---

## 💡 ESEMPI PRATICI

### Esempio: Compilazione Overview con dati reali

**Dati ricevuti dall'utente:**
"Questo mese: agenzia €3.500, info-biz €450, YouTube €30 (AdSense), KDP €95, AI Influencer €0"

**Output generato:**
REVENUE TOTALE DIGITAL EMPIRE: €4.075

┌──────────────────┬──────────┬──────────┬──────────────┐
│ Pillar │ Revenue │ % Totale │ % Target │
├──────────────────┼──────────┼──────────┼──────────────┤
│ Agenzia CRO │ €3.500 │ 85.9% │ 50-60% ⚠️ │
│ Info-Business │ €450 │ 11.0% │ 20-30% ⚠️ │
│ YouTube │ €30 │ 0.7% │ 5-15% │
│ KDP │ €95 │ 2.3% │ 2-5% 🟢 │
│ AI Influencer │ €0 │ 0% │ 2-5% ⚪ │
├──────────────────┼──────────┼──────────┼──────────────┤
│ TOTALE │ €4.075 │ 100% │ │
└──────────────────┴──────────┴──────────┴──────────────┘

⚠️ NOTA: L'agenzia rappresenta l'85.9% del revenue —
ben sopra il target 50-60%. Questo NON è un problema
di per sé (l'agenzia è il core), ma indica che
l'Info-Business è sotto-performante rispetto al
potenziale. Azione: diagnosticare il funnel info-biz.

text


---

## ⚠️ NOTE E AVVERTENZE

1. **La dashboard NON è un documento statico.** Deve essere compilata con dati REALI ogni mese (versione completa) e ogni settimana (versione rapida). Una dashboard vuota è inutile.

2. **Non inventare MAI dati mancanti.** Se l'utente non fornisce un dato, segna "[DATO MANCANTE]" e chiedi. Una dashboard con dati inventati è peggio di nessuna dashboard.

3. **Il semaforo 🟢🟡🔴 è OGGETTIVO, non soggettivo.** Si basa sulla formula: Reale/Target × 100. Non assegnare 🟢 perché "sembra che vada bene" — calcola.

4. **L'ordine delle sezioni è fisso.** Sempre: Overview → Agenzia → Info-Biz → YouTube → Satellite → Cross-Poll → Allarmi. Questo ordine riflette la gerarchia dei pillar.

5. **L'albero diagnostico (Sezione 11) è lo strumento più potente** per quando un pillar è 🔴. Non limitarti a dire "è rosso" — usa l'albero per trovare la CAUSA e suggerire l'AZIONE specifica.

6. **I bridge metrics (Sezione 6) sono le metriche più sottovalutate.** Misurano se le sinergie tra pillar funzionano davvero. Se tutti i bridge sono a 0 → le sinergie sono un'idea, non una realtà.
