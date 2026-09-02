# MASTER RUN TRACKER — andrei-pascu-cs2online-001
## Corso a pagamento: "Claude Speedrun 2" (Andrei Pascu, andrei-copy.com)
**Run creato:** 2026-08-27 | **Pipeline:** Empire Studio Suite v2.0 (adattata a corso membership, non YouTube)

---

## SCOPE CONFERMATO (Max, 2026-08-27)

URL corso: `https://www.andrei-copy.com/cs2online` — piattaforma membership (Podia/simile), login richiesto.
**Credenziali fornite da Max**: email `max.infoproducer@gmail.com` — password NON salvata in chiaro in nessun file di questo repo (usata solo a runtime via variabile d'ambiente in sessione). Sessione autenticata salvabile in `storage_state.json` (NON committare — va in `.gitignore`, contiene cookie di sessione validi).

**Attenzione**: questo NON è un corso di copywriting puro — è un corso sull'uso di Claude/AI per business (freelance, copywriting, coding, video editing). Esiste un secondo prodotto membership ("Copywriting Mentorship") nello stesso account, NON ancora iniziato — resta in attesa, scope separato.

**Totale lezioni: 40** (24 lezioni core + 6 Bonus + 10 sezione "CS2"). Struttura reale confermata via enumerazione DOM autenticata (non contata a mano).

---

## REGOLA NUOVA (Max, 2026-08-27): TEORIA vs PRATICA

- **Lezione teorica** (spiega concetti, no dimostrazione live) → NO frame-by-frame screenshot. Si archivia: descrizione/panoramica ufficiale, "Cosa hai imparato" (bullet ufficiali della piattaforma), trascrizione (se scaricabile in .md, altrimenti trascritta da VTT/audio), risorse allegate (PDF, immagini, link).
- **Lezione pratica** (dimostrazione live, "come si fa X passo-passo") → SI frame-by-frame (stesso invariante Empire Studio: screenshot ogni ~2s + visione nativa Claude su ogni frame), perché il valore è nei passaggi UI/schermo mostrati.
- Classificazione fatta leggendo titolo + descrizione ufficiale sotto il video (non solo il titolo). Da confermare/correggere lezione per lezione quando aperta.

---

## STRUTTURA TECNICA CONFERMATA (ricognizione lezione 1, pilota)

- Piattaforma: form di login in iframe (`#login-email`, `#login-password` dentro `account/frame/login`), sessione salvabile.
- Video: embed Vimeo privato (`player.vimeo.com/video/<id>`) — accessibile solo da sessione autenticata.
- Ogni lezione ha (variabile, non tutte hanno tutto):
  - Panoramica (descrizione ufficiale)
  - "Cosa hai imparato" (bullet list ufficiale — sostituisce parte del lavoro di sintesi)
  - Schemi/immagini scaricabili (Google Drive link pubblico → `drive.google.com/uc?export=download&id=<ID>`)
  - PDF contenuti extra
  - Quiz esterno (link a `artificiale.art` per lezione 1)
  - **Trascrizione .md scaricabile — SOLO SU ALCUNE LEZIONI** (confermato: lezione 1 sì, "corretta e sanificata con AI, non verificata da umano" — dichiarazione esplicita della fonte, da trattare come atom con nota di cautela). Quando assente, trascrivere da audio/VTT del video Vimeo.
  - Link utili (URL esterni citati)

---

## STATO GLOBALE

| Sezione | Lezioni | Fatte | Pending |
|---|---|---|---|
| AI – Le basi | 9 (L1-L9) | 9 | 0 |
| AI – per produttività e freelance | 3 (L10-L12) | 2 | 1 |
| AI – per copywriting | 4 (L13-L16) | 2 | 2 |
| AI – per coding e simili | 7 (L17-L23) | 1 | 6 |
| AI – altri utilizzi | 1 (L24) | 0 | 1 |
| Lezioni BONUS | 6 | 6 | 0 |
| CS2 | 10 | 0 | 10 |
| **TOTALE** | **40** | **20** | **20** |

**⏭️ SALTO ORDINATO (Max, 2026-08-29):** lezioni 7-12 saltate (rimangono `pending`, non `skipped` — riprendibili in futuro se richiesto). Priorità spostata su **AI – per copywriting (13-16)**.

**⏭️ SALTO ORDINATO #2 (Max, 2026-08-29):** lezioni 14-15 saltate (pending, riprendibili). Ordine richiesto: Lezione 16 → Bonus 1-6, poi stop.

**✅ ORDINE MAX COMPLETATO 2026-08-29** (Lezione 16 → Bonus 1-6). Poi proseguito in autonomia su "continua": Lezioni 7, 8, 9 completate — **sezione "AI – Le basi" ORA COMPLETA (9/9)**.

**RIPRESA DA:** Lezione 12 — "Come fare preventivi con Claude" (`lezione-12-come-fare-preventivi-con-claude-3ddaf`), unica pending in sezione "produttivita'/freelance". Poi L14, L15 (pending/saltate), poi L18-L23 (coding), L24, C1-C10.

**✅ 2026-09-01 — Lezione 17 completata** (ripresa dopo crash sessione). Reclassificata da TEORIA a PRATICA. 78 frame su disco (estrazione parziale, copertura ~3 min video, resto del video intatto). Nessuna patch skill — contenuto entry-level. 18 KA estratti, 14 workflow documentati.

**⚠️ CONVERGENZA CROSS-RUN TROVATA (lezione 13, 2026-08-29)**: tecnica "ricerca voice-of-customer da recensioni YouTube" confermata 3 volte indipendenti (2 video YouTube gratuiti run `andrei-pascu-001` + questa lezione del corso a pagamento) — **PATCH REALE applicata** a `C:\Users\Utente\.claude\skills\copywriting\SKILL.md`, sezione "Customer Language Over Company Language".

**PRIMA LEZIONE PRATICA COMPLETATA (lezione 6)**: video scaricato, 43 frame visionati nativamente sui segmenti demo. Confermato che serve SEMPRE verificare con qualche frame campione prima di classificare teoria/pratica solo dal titolo — lezione 6 sembrava teorica dal nome ("Cucinando il tuo contesto") ma conteneva 5+ minuti di demo schermo reali.

**⚠️ ANOMALIA APERTA (lezione 2)**: skill `prompt-engegniring-skill` elencata tra le skill disponibili del sistema ma cartella non trovata in `C:\Users\Utente\.claude\skills\`. Segnalata a Max, non risolta.

**⚠️ ANOMALIA APERTA #2 (lezione 10, 2026-08-29)**: skill `client-handover` STESSO problema — elencata ma non su disco. 2 occorrenze ora, possibile problema sistemico di sincronizzazione skill. Da segnalare a Max con priorità.

---

## LISTA COMPLETA 40 LEZIONI (URL reali, verificati via DOM autenticato)

### AI – Le basi (9 lezioni)
| # | Titolo | Slug URL | Tipo (stimato da titolo) | Status |
|---|---|---|---|---|
| 1 | Introduzione all'intelligenza artificiale | `lezione-1-introduzione-allintelligenza-artificiale-2lsrz` | TEORIA | **DONE** (pilota) |
| 2 | Termini che devi sapere | `lezione-2-termini-che-devi-sapere-s527b` | TEORIA (confermato) | **DONE** |
| 3 | Livelli di utilizzo dell'intelligenza artificiale | `lezione-3-livelli-di-utilizzo-dellintelligenza-artificiale-srtyp` | TEORIA (confermato) | **DONE** |
| 4 | 3 tipi di lavoro | `lezione-4-3-tipi-di-lavoro-n4adw` | TEORIA (confermato) | **DONE** |
| 5 | Diversi tipi di task | `lezione-5-diversi-tipi-di-task-sekhw` | TEORIA (confermato) | **DONE** |
| 6 | Cucinando il tuo contesto | `lezione-6-cucinando-il-tuo-contesto-83c7l` | **PRATICA (confermato con video)** | **DONE** |
| 7 | Diversi tipi di contesto | `lezione-7-diversi-tipi-di-contesto-2xbzj` | **TEORIA (confermato)** | **DONE** |
| 8 | Context engineering | `lezione-8-context-engineering-y8leg` | **TEORIA (confermato)** | **DONE** |
| 9 | Come dare contesto alle AI | `lezione-9-come-dare-contesto-alle-ai-xmwmb` | **PRATICA (confermato)** | **DONE — SEZIONE COMPLETA 9/9** |

### AI – per produttività e freelance (3 lezioni)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 10 | Cliente manda audio Claude fa revisioni | `lezione-10-cliente-manda-audio-claude-fa-revisioni-zgc9x` | **PRATICA (confermato)** | **DONE** |
| 11 | Come organizzo la mia settimana con Claude | `lezione-11-come-organizzo-la-mia-settimana-con-claude-5982m` | **PRATICA (confermato)** | **DONE** |
| 12 | Come fare preventivi con Claude | `lezione-12-come-fare-preventivi-con-claude-3ddaf` | PRATICA — rilevante per tensione aperta `beast-preventivi` (vedi run YouTube) | pending |

### AI – per copywriting (4 lezioni)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 13 | Come faccio la ricerca di copywriting con l'AI | `lezione-13-come-faccio-in-ricerca-di-copywriting-con-lai-ryx39` | **PRATICA (confermato)** | **DONE** |
| 14 | Come usare la modalità co-work | `lezione-14-come-usare-la-modalita-cowork-4cccr` | PRATICA | pending |
| 15 | Questionario di ricerca di copywriting con l'AI | `lezione-15-questionario-di-ricerca-di-copywriting-con-lai-jk7pt` | MISTO (probabile template/documento + spiegazione) | pending |
| 16 | Copy per primary text (ads) con Claude | `lezione-16-copy-per-primary-text-ads-con-claude-wspxy` | **PRATICA (confermato)** | **DONE** |

### AI – per coding e simili (7 lezioni)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 17 | Introduzione al vibe coding | `lezione-17-introduzione-al-vibe-coding-3bgtt` | **PRATICA (confermato — 14 workflow demo)** | **DONE** |
| 18 | Diagrammi o flow chart | `lezione-18-come-scrivo-piccoli-codici-google-sites-h48d2` | PRATICA (nota: slug non combacia col titolo visualizzato — verificare al momento dell'apertura) | pending |
| 19 | Come fare caroselli con immagini hostate su imgur | `lezione-19-come-creare-codici-integrati-con-google-sheets-y4ljn` | PRATICA (stesso mismatch titolo/slug, verificare) | pending |
| 20 | Come scrivo piccoli codici Google Sites | `lezione-20-come-fare-caroselli-con-immagini-hostate-su-imgur-lfhtg` | PRATICA (stesso mismatch, verificare) | pending |
| 21 | Come creare codici integrati con Google Sheets | `lezione-21-come-creare-codici-integrati-con-google-sheets-dxhye` | PRATICA | pending |
| 22 | Codice per dashboard pubblica | `lezione-22-codice-per-dashboard-pubblica-7rsp9` | PRATICA | pending |
| 23 | Codici per pop-up semplici e complessi | `lezione-23-codici-per-popup-semplici-e-complessi-jjpxe` | PRATICA | pending |

**⚠️ NOTA APERTA**: i titoli visualizzati in UI per le lezioni 18-20 non corrispondono agli slug URL (es. titolo "Diagrammi o flow chart" ha lo slug di "google-sites"). Probabile rinominazione lato piattaforma dopo la creazione degli URL. Verificare il contenuto REALE aprendo la pagina, non fidarsi né del titolo né dello slug da soli.

### AI – altri utilizzi (1 lezione)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| 24 | Come facciamo brand guidelines con Claude | `lezione-24-come-facciamo-brand-guidelines-con-claude-tgcsa` | PRATICA | pending |

### Lezioni BONUS (6)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| B1 | Automatizzare processi | `bonus-1-automatizzare-processi-xcrw8` | **TEORIA (confermato)** | **DONE** |
| B2 | Come facciamo advertising report per tenere cliente in loop | `bonus-2-come-facciamo-advertising-report-per-tenere-cliente-in-loop-7j6dx` | **PRATICA (confermato)** | **DONE** |
| B3 | Come collegare Claude a qualsiasi cosa | `bonus-3--pjb6s` | **PRATICA (confermato)** | **DONE** |
| B4 | Claude Skills | `bonus-4--aeaj5` | **PRATICA (confermato)** | **DONE** |
| B5 | Projects dentro co-work | `bonus-5--m9dte` | **PRATICA (confermato)** | **DONE** |
| B6 | Automatizzare processi con skills | `bonus-6--346en` | **PRATICA (confermato)** | **DONE — ULTIMA LEZIONE ORDINE MAX** |

### CS2 (10 lezioni — sezione avanzata)
| # | Titolo | Slug URL | Tipo | Status |
|---|---|---|---|---|
| C1 | Terminal: perché? | `terminal-perch` | TEORIA | pending |
| C2 | Introduzione agli API & MCP | `lezione-2-introduzione-agli-api-mcp` | TEORIA | pending |
| C3 | Claude - Github - Lovable \| COME FARE | `claude-github-lovable-come-fare` | PRATICA | pending |
| C4 | Brain talk | `lezione-4-titolo` | TEORIA | pending |
| C5 | Come scrivo copy con l'AI [replicando il mio TOV] | `lezione-4-titolo-292y6` | PRATICA | pending |
| C6 | Le mie chiavi API preferite | `lezione-6-le-mie-chiavi-api-preferite` | TEORIA (lista/opinione) | pending |
| C7 | Come editare video con l'AI [pt. 1] | `lezione-7-come-editare-video-con-lai` | PRATICA | pending |
| C8 | Come editare video con l'AI [pt. 2] | `editare-video-pt-2` | PRATICA | pending |
| C9 | Come editare video con AI [pt. 3] | `lsxpy45na42telclrmnk2g2mr9ekt8` | PRATICA | pending |
| C10 | Come calcolare se guadagni dall'AI | `come-calcolare-se-guadagni-dallai` | TEORIA (calcolo/framework) | pending |

Tutti gli URL vanno prefissati con `https://www.andrei-copy.com/cs2online/`.

---

## OUTPUT PER LEZIONE (struttura confermata su lezione 1)

```
runs/andrei-pascu-cs2online-001/lessons/lezione-NN/
├── ingest.json              (metadata: slug, url, vimeo-id, tipo teoria/pratica, risorse)
├── lesson-analysis.md       (panoramica ufficiale + "cosa hai imparato" + knowledge atoms + [frame-by-frame SOLO se pratica])
├── resources/
│   ├── trascrizione.md      (se disponibile — scaricata da Google Drive, marcata "AI-corretta, non verificata da umano")
│   ├── *.pdf, *.png         (materiali scaricabili della lezione)
└── frames/                  (SOLO lezioni pratiche — screenshot ogni ~2s del video)

memory-empire/knowledge/cs2online-lezione-NN/   (stesso schema 4-file del run YouTube)
```

---

## SOP PER OGNI SESSIONE FUTURA

1. Leggi questo tracker, trova prossima lezione "pending".
2. Login (script Playwright, credenziali da env var runtime — MAI hardcoded in file salvati su disco).
3. Apri URL lezione → leggi panoramica + "Cosa hai imparato" + classifica teoria/pratica REALE (correggi tabella se lo stimato era sbagliato).
4. Scarica risorse (Drive links → `drive.google.com/uc?export=download&id=<ID>`).
5. Se PRATICA: scarica video Vimeo (yt-dlp con cookie di sessione se serve) + frame ogni 2s + visione Claude su ogni frame.
6. Se TEORIA: usa trascrizione .md se presente, altrimenti trascrivi da audio Vimeo.
7. Scrivi `lesson-analysis.md` con knowledge atoms (stesso standard P12 traceability del run YouTube).
8. Attiva Memory Empire: crea `memory-empire/knowledge/cs2online-lezione-NN/` (4 file), enrichment-report confronto con skill esistenti.
9. Aggiorna wiki (`second-brain-vault/wiki/sources/Source_CS2_Lezione_NN_*.md`).
10. Aggiorna questo tracker (status → DONE) + log ingestions.

---

## SICUREZZA CREDENZIALI

- Password fornita da Max in chat — NON scritta in nessun file salvato di questo repo.
- Sessione autenticata: `storage_state.json` di Playwright (contiene cookie validi) va tenuto SOLO in scratchpad locale/temp, MAI committato — se serve persistenza cross-sessione, salvarlo fuori dal repo git (es. `%LOCALAPPDATA%`) e aggiungere il path a `.gitignore` per sicurezza anche se fuori repo.
- Se serve rieseguire il login, richiedere di nuovo le credenziali a Max invece di cercarle salvate da qualche parte.
