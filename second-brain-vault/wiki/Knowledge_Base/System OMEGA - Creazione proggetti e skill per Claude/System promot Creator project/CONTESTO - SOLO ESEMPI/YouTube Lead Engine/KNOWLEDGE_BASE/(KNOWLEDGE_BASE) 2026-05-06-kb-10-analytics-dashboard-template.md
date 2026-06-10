# KB_10_analytics-dashboard-template
            
> Path: [[Map - System_Omega_-_Creazione_Proggetti_E_Skill_Per_Claude|System OMEGA - Creazione proggetti e skill per Claude > System promot Creator project > CONTESTO - SOLO ESEMPI > YouTube Lead Engine > KNOWLEDGE_BASE]]

## Content

# KB_10 — ANALYTICS DASHBOARD TEMPLATE
# YouTube Lead Engine (P2) — Digital Empire
# Priorità: 🟢 Quando disponibile

---

## SCOPO

Questo file contiene il template completo del dashboard di analisi per il sistema YouTube Lead Engine. Include: metriche chiave per ogni step del funnel, soglie di performance (verde/giallo/rosso), frequenza di controllo, e le domande diagnostiche da porsi quando i numeri sono fuori target. Serve come riferimento settimanale per monitorare il sistema e decidere dove intervenire.

**Principio**: Non ottimizzare quello che non misuri. Il dashboard non è un report — è uno strumento decisionale. Ogni metrica deve rispondere alla domanda: "cosa faccio diversamente se questo numero è basso?"

---

## CONTENUTO PRINCIPALE

### SEZIONE 1 — STRUTTURA DEL DASHBOARD COMPLETO

```
╔══════════════════════════════════════════════════════════════╗
║            YOUTUBE LEAD ENGINE — DASHBOARD                   ║
╠══════════════════════════════════════════════════════════════╣
║  LIVELLO 1: VIDEO YOUTUBE           (settimanale)           ║
║  LIVELLO 2: BRIDGE PAGE / OPT-IN    (settimanale)           ║
║  LIVELLO 3: UPSELL €15              (settimanale)           ║
║  LIVELLO 4: SEQUENZA EMAIL 6 GIORNI (settimanale)           ║
║  LIVELLO 5: VSL EVENTO / WEBINAR    (per evento)            ║
║  LIVELLO 6: FOLLOW-UP POST-WEBINAR  (per evento)            ║
║  LIVELLO 7: NURTURE SETTIMANALE     (mensile)               ║
╚══════════════════════════════════════════════════════════════╝
```

---

### SEZIONE 2 — LIVELLO 1: METRICHE VIDEO YOUTUBE

**Frequenza controllo**: Ogni 7 giorni per i video dei primi 90 giorni. Ogni 30 giorni per video >90 giorni.

| Metrica | Formula | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|---------|---------|---------|---------|
| CTR (click-through rate) | Click / Impressioni | >5% | 3-5% | <3% |
| Watch time medio | Minuti guardati / Views | >50% durata video | 35-50% | <35% |
| Views 30 gg | Raw count | >1.000 | 300-1.000 | <300 |
| Click su link descrizione | Click / Views | >3% | 1-3% | <1% |
| Click su CTA pinned comment | Click / Views | >2% | 0.8-2% | <0.8% |

**Tabella per video tracking settimanale**:

```
VIDEO TRACKING — SETTIMANA [N]
Data: ____________

Titolo Video                     | Views | CTR | WT% | Link% | LM Opt-in
─────────────────────────────────|-------|-----|-----|-------|─────────
[Video 1]                        |       |     |     |       |
[Video 2]                        |       |     |     |       |
[Video 3]                        |       |     |     |       |
TOP PERFORMER SETTIMANA:         |
VIDEO DA OTTIMIZZARE:            |
AZIONE PRIORITARIA:              |
```

**Domande diagnostiche — quando CTR è 🔴**:
```
□ Il thumbnail mostra un volto o una promessa visiva chiara?
□ Il titolo include una parola ad alta intenzione di ricerca?
□ Il titolo supera i 50 caratteri? (troppo lungo = tagliato)
□ Il video è in un pillar a bassa competizione?
→ AZIONE: A/B test 2 nuovi thumbnail prima di creare nuovo video
```

**Domande diagnostiche — quando Watch Time è 🔴**:
```
□ I primi 30 secondi contengono il hook principale?
□ C'è un drop massiccio a un punto specifico?
   (controlla YouTube Analytics > Audience Retention)
□ La CTA soft è posizionata al 30% del video?
→ AZIONE: Rieditare intro o spostare hook principale
```

---

### SEZIONE 3 — LIVELLO 2: METRICHE BRIDGE PAGE

**Frequenza controllo**: Settimanale.

| Metrica | Formula | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|---------|---------|---------|---------|
| Opt-in rate | Opt-in / Visite uniche | >35% | 20-35% | <20% |
| Visite totali / mese | Assoluto | >500 | 100-500 | <100 |
| Lead generati / mese | Assoluto | >175 | 20-175 | <20 |
| Bounce rate | Uscite senza interazione | <50% | 50-70% | >70% |
| Tempo medio sulla pagina | Secondi | >45s | 20-45s | <20s |

**Tabella per bridge page tracking**:

```
BRIDGE PAGE TRACKING — MESE [N]
Data: ____________

URL Bridge Page                  | Visite | Opt-in | Rate% | Source
─────────────────────────────────|--------|--------|-------|──────
/yt/[slug-video-1]              |        |        |       | YT Organico
/yt/[slug-video-2]              |        |        |       | YT Organico
/yt/[slug-video-3]              |        |        |       | YT Organico
─────────────────────────────────|--------|--------|-------|──────
TOTALE                          |        |        |       |
```

**Domande diagnostiche — quando Opt-in rate è 🔴**:
```
□ La headline corrisponde al contenuto del video che ha generato il click?
□ Il nome del lead magnet segue la Naming Formula di KB_02?
□ I 4 bullet point seguono la struttura di KB_06 (specificità)?
□ Il form ha più di 2 campi? (Nome + Email è il massimo)
□ La pagina si carica in <2 secondi su mobile?
→ AZIONE: Test A/B su headline (mantieni tutto il resto)
```

---

### SEZIONE 4 — LIVELLO 3: METRICHE UPSELL €15

**Frequenza controllo**: Settimanale.

| Metrica | Formula | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|---------|---------|---------|---------|
| Conversion rate upsell | Acquisti / Visualizzazioni | >15% | 8-15% | <8% |
| Revenue upsell / mese | Acquisti × €15 | >€500 | €150-500 | <€150 |
| % che completa VSL | Chi guarda >80% / Visite | >40% | 20-40% | <20% |
| Refund rate | Rimborsi / Acquisti | <3% | 3-8% | >8% |

**Formula economics upsell**:

```
CALCOLO ROI UPSELL MENSILE:
─────────────────────────────────────────
Opt-in totali mese:          [A]
× Conversion rate upsell:    [B]%
= Acquisti upsell:           [A × B/100]
× Prezzo:                    €15
= Revenue upsell mensile:    €[X]

Revenue upsell / Opt-in totali = €[CPL netto]
(Target: ≥ €1.50/opt-in per finanziare il sistema)
```

**Domande diagnostiche — quando CR upsell è 🔴**:
```
□ Il nome del corso €15 è specifico al video/LM del lead?
□ Il VSL dura tra 3-5 minuti? (più lungo = drop del 60%)
□ Il bottone "Sì, lo voglio" è above fold su mobile?
□ Il link "No, solo il PDF" è visibile e cliccabile?
   (se troppo nascosto → paura del trucco → abbandono)
□ La pagina ha nessun link di uscita oltre ai 2 CTA?
→ AZIONE: Riscrivi [2:00-3:30] del VSL (sezione soluzione)
```

---

### SEZIONE 5 — LIVELLO 4: METRICHE SEQUENZA EMAIL 6 GIORNI

**Frequenza controllo**: Settimanale (per i nuovi lead entrati nella settimana).

| Metrica | Giorno | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|--------|---------|---------|---------|
| Open rate Email 0 | Giorno 0 | >60% | 40-60% | <40% |
| Open rate Email 1 | Giorno 1 | >45% | 30-45% | <30% |
| Open rate Email 2 | Giorno 2 | >40% | 25-40% | <25% |
| Open rate Email 3 | Giorno 3 | >35% | 20-35% | <20% |
| Open rate Email 4 | Giorno 4 | >35% | 20-35% | <20% |
| Open rate Email 5 | Giorno 5 | >35% | 20-35% | <20% |
| CTR medio sequenza | Media D0-D5 | >8% | 3-8% | <3% |
| Click su VSL/webinar link | D4+D5 | >12% degli aperti | 5-12% | <5% |

**Tabella tracking sequenza**:

```
EMAIL SEQUENCE TRACKING — [MESE/ANNO]
Coorte: Lead entrati settimana [N]
Dimensione coorte: [N] lead

EMAIL     | Inviati | Aperti | OR%  | Click | CTR%
──────────|---------|--------|------|-------|─────
Email 0   |         |        |      |       |
Email 1   |         |        |      |       |
Email 2   |         |        |      |       |
Email 3   |         |        |      |       |
Email 4   |         |        |      |       |
Email 5   |         |        |      |       |
──────────|---------|--------|------|-------|─────
TOTALE    |         |        |      |       |

TASSO ISCRIZIONE WEBINAR DA SEQUENZA: [%]
```

**Domande diagnostiche — quando Open Rate crolla da Email 2 in poi**:
```
□ L'oggetto dell'email che ha perso è generico
  o troppo "marketing"?
□ Stai inviando dall'indirizzo email corretto?
  (dominio verificato, non spam)
□ Il sendtime è diverso da Email 0-1?
→ AZIONE: Ottimizza oggetto email con drop. Test A/B.
```

**Domande diagnostiche — quando CTR su VSL/webinar è 🔴**:
```
□ Il CTA nell'email è abbastanza diretto?
  (verbo + beneficio specifico, non "clicca qui")
□ La CTA è posizionata sia nel corpo che nel P.S.?
□ Il caso studio dell'Email 4 è sufficientemente specifico?
  (settore, numero, timeframe — vedi KB_09)
→ AZIONE: Riscrivi Email 4 con un caso studio più rilevante
  per il segmento che non clicca
```

---

### SEZIONE 6 — LIVELLO 5: METRICHE WEBINAR/VSL EVENTO

**Frequenza controllo**: Dopo ogni evento live. Per replay: settimanale.

| Metrica | Formula | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|---------|---------|---------|---------|
| Iscritti al webinar | Assoluto (da sequenza email) | >20% dei lead settimana | 10-20% | <10% |
| Show rate live | Presenti live / Iscritti | >30% | 20-30% | <20% |
| Watch time replay | % che guarda >60% | >35% | 20-35% | <20% |
| Conversion rate | Acquisti / (Presenti + Replay) | >5% | 2-5% | <2% |
| Revenue per partecipante | Revenue / Presenti totali | >€[X × 0.05] | — | — |

**Tabella per evento webinar**:

```
WEBINAR TRACKING — [DATA EVENTO]
Nome webinar: _____________________

FASE PRE-WEBINAR
Iscritti totali:              [A]
Via sequenza email:           [B] ([B/A]%)
Via nurture:                  [C] ([C/A]%)

FASE LIVE
Presenti live:                [D] ([D/A]% show rate)
Peak concurrent:              [E]
Drop al minuto [N]:           [F]%  ← indica dove si perde attenzione

FASE REPLAY
Replay views totali:          [G]
Watch time >60%:              [H] ([H/G]%)

CONVERSIONI
Acquisti durante live:        [I]
Acquisti entro 24h:           [J]
Acquisti follow-up (5gg):     [K]
Totale acquisti:              [I+J+K]
Conversion rate:              [I+J+K / D+G]%
Revenue totale evento:        €[X]
```

**Domande diagnostiche — quando Show Rate è 🔴**:
```
□ L'email di reminder è stata inviata? (24h prima + 1h prima)
□ Il webinar è in un orario non ottimale?
  (target: martedì-giovedì, 19:30-20:00 per business Italia)
□ Il titolo del webinar è specifico e orientato al risultato?
□ L'iscrizione è avvenuta >7 giorni prima?
  (più lungo il gap → più basso lo show rate)
→ AZIONE: Aggiungi SMS reminder se possibile
```

**Domande diagnostiche — quando CR webinar è 🔴**:
```
□ La presentazione segue la struttura APP-SOC (KB_07)?
□ Il P-Problem è stato abbastanza amplificato?
  (almeno 15-20 min del webinar dedicati al problema)
□ Il prezzo è stato rivelato prima dello stack del valore?
  (errore comune: il prezzo deve venire DOPO la value stack)
□ C'era una reason-now credibile (scarcità reale o deadline)?
→ AZIONE: Registra il webinar e analizza il drop-off
  nel replay per identificare il punto di perdita
```

---

### SEZIONE 7 — LIVELLO 6: FOLLOW-UP POST-WEBINAR (5 giorni)

**Frequenza controllo**: Giornaliera durante i 5 giorni di follow-up.

| Metrica | Email | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|-------|---------|---------|---------|
| OR email 1 (2h) | Riassunto | >55% | 35-55% | <35% |
| OR email 2 (24h) | Case study | >45% | 25-45% | <25% |
| OR email 3 (48h) | Obiezioni | >40% | 25-40% | <25% |
| OR email 4 (72h) | Urgenza | >45% | 25-45% | <25% |
| OR email 5 (finale) | Chiusura | >50% | 30-50% | <30% |
| Recupero totale | Acquisti follow-up / Iscritti non-acquirenti | >15% | 8-15% | <8% |

---

### SEZIONE 8 — LIVELLO 7: NURTURE SETTIMANALE

**Frequenza controllo**: Mensile (media delle ultime 4 settimane).

| Metrica | Formula | 🟢 Verde | 🟡 Giallo | 🔴 Rosso |
|---------|---------|---------|---------|---------|
| Open rate nurture | Media settimanale | >25% | 15-25% | <15% |
| CTR nurture | Media settimanale | >4% | 1.5-4% | <1.5% |
| Unsubscribe rate | Per email | <0.3% | 0.3-0.8% | >0.8% |
| Spam complaints | Per email | <0.05% | 0.05-0.1% | >0.1% |
| Riattivazione verso webinar | Da nurture / Mese | >3% dei lead in nurture | 1-3% | <1% |

---

### SEZIONE 9 — DASHBOARD SETTIMANALE MASTER (1 PAGINA)

Template da compilare ogni lunedì mattina in 15 minuti.

```
╔══════════════════════════════════════════════════════════════════╗
║         YOUTUBE LEAD ENGINE — WEEKLY REVIEW                      ║
║         Settimana: [N] | Data: ____________                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  📹 VIDEO                                                        ║
║  Top video settimana: _________________ | Views: _____ CTR: __% ║
║  Nuovi lead da YouTube: _____                                    ║
║                                                                  ║
║  📋 BRIDGE PAGE                                                  ║
║  Visite totali: _____ | Opt-in: _____ | Rate: ___%              ║
║  🔴 Pagina sotto target: _____________________                  ║
║                                                                  ║
║  💶 UPSELL €15                                                   ║
║  Acquisti: _____ | Revenue: €_____ | CR: ___%                   ║
║                                                                  ║
║  📧 SEQUENZA EMAIL                                               ║
║  OR medio: ___% | CTR medio: ___% | Click webinar: ___%         ║
║  Email con problema: _____________________                       ║
║                                                                  ║
║  🎯 WEBINAR (se attivo)                                          ║
║  Iscritti: _____ | Show rate: ___% | CR: ___% | Rev: €_____    ║
║                                                                  ║
║  📈 TOTALE SETTIMANA                                             ║
║  Lead totali: _____ | Revenue totale: €_____ | CAC netto: €___ ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║  🔧 AZIONE PRIORITARIA QUESTA SETTIMANA:                        ║
║                                                                  ║
║  [Scrivi 1 sola azione — il bottleneck principale]              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

### SEZIONE 10 — DIAGNOSI AUTOMATICA: DOVE SI PERDE IL FUNNEL

Usa questa tabella quando i lead entrano ma non avanzano.

```
SINTOMO                          CAUSA PROBABILE           KB DA CONSULTARE
──────────────────────────────────────────────────────────────────────────
Visite bridge page basse         CTR video basso           KB_03 (CTA video)
                                 Pinned comment assente    KB_03 (Pinned)

Opt-in rate <20%                 Mismatch video/LM         KB_01 (Deprivazione)
                                 Nome LM non specific.     KB_02 (Naming)
                                 Headline debole           KB_06 (Brand Voice)

CR upsell <8%                    VSL troppo generico       KB_04 (VSL upsell)
                                 Nome corso non specific.  KB_04 (Naming upsell)

OR email day 1-3 in calo        Oggetto non specifico     KB_08 (Email templates)
                                 Indottrinamento debole    KB_08 (Sezione 2)

Click su webinar <5%             Case study non rilevante  KB_09 (Storytelling)
(da email Day 4-5)               CTA troppo morbida        KB_06 + KB_03

Show rate webinar <20%           Reminder mancante         KB_04 (Sezione 5)
                                 Gap iscrizione troppo lng  Anticipo evento

CR webinar <2%                   Offerta non strutturata   KB_07 (APP-SOC O+C)
                                 Problem non amplificato   KB_07 (P-Problem)

Nurture OR <15%                  Email troppo promozionali KB_08 (Nurture)
                                 Frequenza troppo alta     KB_04 (Sezione 4)
```

---

### SEZIONE 11 — KPI MENSILI AGGREGATI

Da calcolare il primo lunedì di ogni mese per il mese precedente.

```
REPORT MENSILE — [MESE ANNO]

ACQUISIZIONE
─────────────────────────────────────────────────
Impressioni totali YouTube:          [A]
Views totali:                        [B]  (CTR: B/A%)
Click su link (descrizione+pinned):  [C]  ([C/B]% delle views)
Opt-in totali:                       [D]  ([D/C]% della bridge page)

MONETIZZAZIONE
─────────────────────────────────────────────────
Acquisti upsell €15:                 [E]  ([E/D]% degli opt-in)
Revenue upsell:                      €[E×15]
Iscritti webinar:                    [F]  ([F/D]% degli opt-in)
Presenti webinar:                    [G]  ([G/F]% show rate)
Acquisti premium:                    [H]  ([H/G]% CR webinar)
Revenue premium:                     €[H × prezzo premium]
Revenue totale mese:                 €[E×15 + H×prezzo]

ECONOMICS
─────────────────────────────────────────────────
Revenue per opt-in:                  €[Revenue totale / D]
CAC organico (tempo autore):         €[stima ore × valore orario / D]
LTV stimato:                         €[revenue media per cliente]
Payback period:                      [mesi]

BENCHMARK VS MESE PRECEDENTE
─────────────────────────────────────────────────
Opt-in: [D vs D-1] | Delta: [+/-]%
Revenue totale: [€X vs €X-1] | Delta: [+/-]%
CR webinar: [H/G% vs mese prec.] | Delta: [+/-pp]
```

---

## COME UTILIZZARE QUESTO FILE

1. **Setup iniziale**: Crea un foglio Google Sheets replicando le tabelle della Sezione 9 (Dashboard settimanale)
2. **Ogni lunedì mattina**: Compila la Dashboard Master (Sezione 9) — 15 minuti
3. **Quando un numero è 🔴**: Consulta la tabella diagnostica (Sezione 10) per identificare il KB da leggere
4. **Primo lunedì del mese**: Compila il Report Mensile (Sezione 11)
5. **Dopo ogni webinar**: Compila la tabella evento (Sezione 6) entro 24h

---

## COLLEGAMENTI

- **KB_01** — Test di Deprivazione: ottimizzare il LM quando il Opt-in Rate è 🔴
- **KB_02** — Naming Formulas: aggiornare il nome del LM se il CTR bridge page è basso
- **KB_03** — CTA Templates: ottimizzare i click da YouTube quando le visite bridge sono basse
- **KB_04** — Funnel Unico Perfetto: benchmark target di riferimento (tabella di KB_04)
- **KB_07** — APP-SOC: ottimizzare webinar quando il CR è sotto target
- **KB_08** — Email Sequence: ottimizzare open rate e CTR delle singole email
- **KB_09** — Storytelling Guide: migliorare il case study dell'Email 4 quando il click su webinar è basso

---

## NOTE E AVVERTENZE

- **Un bottleneck alla volta**: Non ottimizzare mai due step del funnel simultaneamente. Cambia una variabile, misura per 2 settimane, poi passa alla successiva.
- **Minimum viable data**: Non aspettare 1.000 opt-in per iniziare a ottimizzare. Con 50 opt-in puoi già identificare i problemi principali nella sequenza email.
- **Attribution window**: I lead da YouTube organico possono impiegare settimane per convertire. Il report mensile è più affidabile del settimanale per le decisioni strategiche.
- **Non confondere causa ed effetto**: Un basso CR webinar non significa che il webinar è scarso. Potrebbe significare che il traffico al webinar è di bassa qualità (leads non qualificati). Controlla sempre la qualità dell'input prima di ottimizzare l'output.

*KB_10 — Analytics Dashboard Template | YouTube Lead Engine (P2) | Digital Empire*

## Collegamenti Correlati
- [[Map - App|App Area]]
- [[Map - System_Omega_-_Creazione_Proggetti_E_Skill_Per_Claude|System Omega - Creazione Proggetti E Skill Per Claude Area]]
