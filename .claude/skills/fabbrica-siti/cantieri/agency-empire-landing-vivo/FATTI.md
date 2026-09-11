# FATTI.md — ogni numero che il sito può dire, con la fonte (Dossier 37 v2, C2.4)

Regola: **un numero che non sta qui non entra in `COPY.md`** (`gate_fatti.py` lo boccia). Fonte = file:riga del sito vero
(`agency-empire-landing/src/…`, letto il 2026-09-12), oppure un checkpoint/skill del repo, oppure «Max, data ora».
Le righe «ARITMETICA» sono conti dichiarati su numeri di questa tabella, non misure.

| Fatto | Numero | Fonte |
|---|---|---|
| Setup dal contratto firmato al go-live | **7 giorni** lavorativi | `components/sections/faq.tsx:6` · `hero.tsx:57` |
| Messaggi al giorno dell'Outreach Factory (email + DM Instagram) | **300** al giorno («300+») | `hero.tsx:63` · `pillars.tsx:15` · `about-story.tsx:439` |
| Canone mensile | **0 €** — codice tuo, sui tuoi server | `hero.tsx` («€0 canoni mensili», «Codice tuo per sempre») |
| Costo del server (VPS del cliente: DigitalOcean, Hetzner, AWS) | **5-20 € al mese** | `faq.tsx:7` |
| Supporto tecnico dopo il go-live | **90 giorni** | `bonuses.tsx:39` · `clarity.tsx:39` · `faq.tsx:8` |
| Monitoraggio con dashboard e alert dopo il go-live | **30 giorni** | `flow-framework.tsx:24` |
| Garanzia: sistemiamo noi senza costi; se non risolvibile, rimborso integrale | **30 giorni** | `faq.tsx:10` · `my-promise.tsx:67-72` · `final-offer.tsx:12` |
| Outreach Factory — prezzo una tantum | **4.000 €** | `final-offer.tsx:203` · `pricing-roi.tsx` |
| Content Factory — prezzo una tantum | **3.500 €** | `final-offer.tsx:203` |
| Second Brain — prezzo una tantum | **2.500 €** | `final-offer.tsx:203` · `lib/constants.ts:2` |
| Engine Room (tutti e tre) — prezzo | **8.000 €** invece di **10.000 €** (risparmio **2.000 €**) | `final-offer.tsx:203` · `lib/constants.ts:3` · `pricing-roi.tsx` («Risparmio €2.000») |
| Pagamento | **50%** acconto, **50%** alla consegna; rateizzazione disponibile | `pricing-roi.tsx` («50% acconto, 50% consegna») · `final-offer.tsx:210` |
| SaaS di outreach a confronto (ricorrente) | **200 € al mese** = **2.400 € l'anno**; **20 mesi** per pareggiare i 4.000 | `pricing-roi.tsx` («€2.400/anno», «~20 mesi per pareggiare») |
| Sistemi che installiamo | **3** (Outreach Factory, Content Factory, Second Brain) | `scope-limits.tsx` («Facciamo tre cose»), `faq.tsx:9` |
| Team | **3** persone: Maximilian (Max), Gael, Leonardo | `about-story.tsx:316-355` |
| Agenzia nata | **gennaio 2026** | `about-story.tsx:43` · `about-story.tsx:187` |
| Storia di Max | «**sei** anni fa ero un ragazzo ossessionato da Internet»; **6** anni di marketing, **3** di AI a tempo pieno | `about-story.tsx:93` · `about-story.tsx:316` |
| Chiamata | **30 minuti**, gratuita, Calendly `max-infoproducer/30min` | `call-cta.tsx:12` · `agency-empire-vivo-wip:…/prenota/page.tsx:7` (200 il 2026-09-12) |
| Formazione del team del cliente | **1** sessione dal vivo sulla dashboard | `bonuses.tsx:47-48` |
| Componenti inclusi in ogni implementazione | **6** (codice, dashboard, proxy, copy engine APSOC, Slack/CRM, manuale + supporto) | `power-deck.tsx` («sei componenti distinti») |
| Novacar (PreventivoForge): preventivi generati su annunci veri, **collaudi nostri inclusi** | **65** preventivi · **11** marche · **~2 minuti** dal link al PDF · **6** controlli prima di ogni PDF · **3-13 luglio 2026** | `company/Memory/checkpoints/CP-20260723-003.md:22-26` (contati su disco) |
| Preventa (outreach WhatsApp ai concessionari) | fino a **50** messaggi al giorno, da un profilo vero | `.claude/skills/avvia-outreach-preventa/SKILL.md:18` |
| Piattaforme dell'outreach | **3**: email, DM Instagram, WhatsApp | `faq.tsx`, `SKILL.md` Preventa |
| ARITMETICA — 30 DM a mano | **30** DM × **5** minuti = **150** minuti = **2,5** ore | conto dichiarato in pagina (V9) |
| ARITMETICA — produttività | **30** / **2,5** = **12** l'ora · **300** / **0** ore tue | conto dichiarato in pagina (V9) |
| ARITMETICA — 300 contro 30 | **10×** | conto dichiarato in pagina |
| ARITMETICA — canone | **12** mesi × quello che paghi al tool | conto delegato al lettore (V4) |
| Ora del mattino usata come esempio («alle 7:40 ha già mandato 300 messaggi») | **7:40** | esempio dichiarato: 300 invii finiscono prima di colazione |
| Il controllo che è nato dal difetto Novacar (foto tagliate → foto intere) | controllo **n. 4** (gate IMG) | `company/Memory/checkpoints/CP-20260723-003.md:25` (gate A/B/C/D + IMG + R) |
| Quattro segnali, ne basta uno | **4** segnali, **1** basta | struttura di N2 (Dossier 37 v2) |
| Anno corrente | **2026** | data |
| Sezioni del sito nuovo | **20** + coda | Dossier 37 v2 Parte III |

## Numeri VIETATI (stavano sul sito vero o nella v1, senza prova)
«50+ sistemi» (`who-guides.tsx`) · «decine di implementazioni» (`my-promise.tsx:72`) · «Solo prime 3 implementazioni» (`bonuses.tsx`) ·
«312 · 24 · 1.4k» finti-live (`vsl.tsx`) · «99,7% / 100% / 99,8%» (`science-stats.tsx`) · «finestra aperta per altri 12 mesi» (`competitors.tsx`) ·
«3-7% di risposta», «60% delle risposte dal secondo messaggio» (wip, senza file dietro) · «Valore €500 / €300» dei bonus (`bonuses.tsx:42,49`) ·
«2.000 € Preventa» (nessuna fonte nel repo letta oggi).
