# Enrichment Report — yX0XZh2PSYo
## Stage D/E/F/G — Memory Empire

**Video:** Merge Tag nell'email marketing
**Data:** 2026-08-24 (ripresa dopo limite di spesa — batch 1, agente originale morto prima di questo stage)

---

## Stage D — Connessioni Knowledge Base

| Questo video | Concetto esistente | Connessione |
|-------------|-------------------|--------------|
| Merge tag = campo dinamico da dato iscrizione (KA-02) | `emails/references/copy-guidelines.md` → Merge Fields | Concetto base già presente ("First name (fallback to 'there' or 'friend')") — questo video conferma e generalizza il principio con esempio esplicito di sintassi. |
| Posizione `{{nome}}` nell'oggetto (video 12, `hb89lccIacY` KA-03) | Stesso dominio (merge field), problema diverso | Video 12 = dove mettere il campo nell'oggetto (lunghezza). Video 15 = cosa succede quando il dato manca ovunque nel corpo (robustezza). Non sovrapposti. |
| Fallback chain generalizzata a qualsiasi campo (KA-06) | `emails/references/copy-guidelines.md` → Merge Fields (un solo bullet, solo su first name) | **Gap reale trovato**: la doc esistente copre il fallback SOLO sul nome ("there"/"friend"), non generalizza il pattern a CTA/altri campi come fa questo video. |

---

## Stage D — Nuovi Concetti Identificati

**Nessuna nuova pagina Concept.** Il fallback chaining è un'estensione tecnica di un principio già
noto (personalizzazione con fallback), non un framework nuovo — non giustifica una pagina Concept
dedicata. Il valore è nell'applicazione pratica (Stage F), non nella catalogazione teorica.

---

## Stage D — Applicazioni DE (dove usare QUESTO contenuto)

| Concetto | Applicazione Digital Empire | Azione |
|----------|------------------------------|--------|
| Fallback chaining su qualsiasi merge field (KA-05, KA-06) | `emails/references/copy-guidelines.md`, sezione "Merge Fields" | **APPLICATO in questa sessione**: aggiunto bullet "Fallback chaining" che generalizza il fallback esistente (solo first-name) a qualsiasi campo dinamico, con nota di fonte. |
| Problema campo vuoto come anti-pattern (KA-04) | `cro-copy-architect/references/checklist-audit-copy.md` | Nessuna azione — il gate anti-clichè già arricchito (video 11) copre l'hook/oggetto, non la robustezza dei merge field nel corpo; fuori scope di quella checklist, non forzare un collegamento debole. |

---

## Stage E — Gate di Qualità

| Check | Status | Note |
|-------|--------|------|
| NO-FINTO | PASS | 46/46 frame descritti = 46/46 letti nativamente (coverage 100%, video breve) |
| P12 traceability | PASS | Ogni KA ha source video#timestamp + frame |
| Coverage sezioni | PASS | 7 sezioni (S1-S7), tutte rappresentate nei KA |
| Quote dirette VTT | PASS | Trascrizione integrale in contenuto-integrale.md |
| Pattern estratti | PASS | 3 pattern operativi in video-analysis.md |
| Connessioni KB | PASS | 3 connessioni documentate |
| Nuovi concetti | PASS (nessuno creato, motivato) | Estensione tecnica, non framework nuovo |
| Applicazioni DE | PASS | 1 proposta applicata, 1 scartata motivatamente |

**GATE: PASS**

---

## Stage F — Applicazione

**Fatto in questa sessione:** patch reale a `C:\Users\Utente\.claude\skills\emails\references\copy-guidelines.md`,
sezione "Merge Fields" — aggiunto bullet "Fallback chaining" che generalizza il fallback (già presente
solo per first-name) a qualsiasi campo dinamico del copy, annotato con fonte Empire Studio.

**Motivazione applicazione diretta (non solo proposta):** a differenza del video 14 (nessun gap tecnico
reale, solo tecnica di formato non ancora confermata su un secondo esempio), qui il gap è concreto e
verificabile — la doc esistente aveva letteralmente un solo bullet limitato al nome, e il video fornisce
sintassi e logica condizionale esplicite, direttamente applicabili senza bisogno di ulteriore conferma.

---

## Stage G — Audit

**Lacune / incertezze:**
- Nessuna. Video breve (91s), coverage frame 100%, VTT completo, nessuna zona "DA VERIFICARE".

**Cross-reference:**
- Video 12 (`hb89lccIacY`) = posizione merge field nell'oggetto (lunghezza).
- Video 15 (questo) = robustezza merge field nel corpo (fallback su dato mancante), generalizzato a
  qualsiasi campo, non solo nome.

**Nota di ripresa:** questo video era stato completato per Stage 1-5 + wiki (Source page già presente:
`Source_Andrei_Pascu_Merge_Tag_Email_Marketing.md`) e Memory Empire 3/4 file da un agente del batch 1
del 2026-08-23, morto per limite di spesa mensile prima di scrivere questo enrichment-report. Nessuno
stage precedente è stato rifatto — solo questo file mancante è stato completato ora.

---

## Prossimo Video

Video 16 (`L5_Z63nxXjI`) — Memory Empire da completare (video-analysis.md già scritto dal batch 1).
