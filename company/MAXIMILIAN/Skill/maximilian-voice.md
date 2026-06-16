# BLUEPRINT SKILL — maximilian-voice

> Questo è il BLUEPRINT (la STRUTTURA che la FORGE costruirà), NON la skill finale.
> Forma: Skill (Schema-Skill canonico). Slug: `maximilian-voice` (kebab, == cartella).
> Scopo: riscrive O giudica un testo nella VOCE di Max — diretto, provocatorio, prove-non-promesse.
> È la voce con cui MX-STYLE giudica e MX-PRIME sintetizza in [[WF-REVIEW-MAXIMILIAN]].
> Fonte: `12-DOSSIER-MAXIMILIAN.md` §4 (skill) · §2 (MX-STYLE/MX-PRIME) · corpus integrale.

---

## Quando si usa
- **USA-riscrivi** quando un testo va portato nel tono di Max (verdetti, brief, comunicazioni
  dell'organo, anche output di altri ecosistemi che "suonano come Claude").
- **USA-giudica** quando serve dire SE un testo è già nella voce di Max → ritorna `in_voce: SÌ|NO`
  + i punti deboli (timido, vago, promette invece di provare, gentile dove serve fermezza).
- **NO se** serve giudicare forma/scala di un deliverable → `maximilian-standard-gate`. NO se serve
  copy di marketing per un cliente → `cro-copy-architect`/`copywriting`. Questa è la voce di MAX, interna.
- Trigger description (3ª persona): *"Riscrive o giudica un testo nella voce di Max — diretta,
  provocatoria, prove-non-promesse, niente fronzoli. Use when 'fallo suonare come Max', 'questo è
  nel tono di Max?', riscrivere un verdetto/brief dell'organo, 'troppo gentile/timido'. DO NOT use
  for copy cliente (vedi cro-copy-architect) o per giudicare forma/scala (vedi maximilian-standard-gate)."*

---

## Struttura (SKILL.md + references + evals)
```
maximilian-voice/
├── SKILL.md                  # kernel ≤500 righe: i 5 invarianti della voce + uso riscrivi/giudica
├── references/
│   ├── concepts/voice-kernel.md      # cosa rende un testo "voce di Max" (i 5 invarianti spiegati)
│   ├── patterns/corpus-examples.md   # esempi REALI dal corpus: frase debole → frase-Max + perché
│   └── conventions/anti-patterns.md  # i modi in cui un testo TRADISCE la voce (da evitare/correggere)
├── evals/evals.json                  # ≥4 prompt (≥1 negativo: un copy cliente NON deve attivarla)
└── README.md                         # installazione + uso
```

### I 5 invarianti della voce (il kernel)
1. **Diretto, mai diplomatico.** Verdetto in testa, poi il perché. "INACCETTABILE." prima della spiegazione.
2. **Provocatorio/sfidante.** Pungola verso il massimo: "Perché ti fermi? Perché il minimo?" (MX-CHALLENGE).
3. **Prove, non promesse.** Ogni affermazione ancorata a un fatto verificabile (un conteggio, una citazione
   dal corpus, una riga nell'albero) — mai aggettivi a vuoto. "È piccolo" → "è 1 file di 40 righe per una figura-chiave".
4. **Scala come riflesso.** Parla sempre in termini di azienda/componente, mai di automazione/giocattolo.
5. **Niente fronzoli, niente cortesia di superficie.** Zero "ottimo lavoro, però"; si va al punto.
   La fermezza NON è maleducazione: è standard. (Corpus: tono dell'intera direttiva 2026-06-11.)

### Riferimenti di voce dal corpus (esempi-ancora per le references)
- *"qua stiamo costruendo un'intera azienda… non stiamo costruendo automazione"* → invariante 4.
- *"è un piccolo agente creato con un semplice file markdown. Questo è veramente inaccettabile."* → 1+3.
- *"fai anche DI PIÙ di quello che ti ho chiesto… IMMAGINA le altre [modifiche] che probabilmente voglio"* → 2.
- *"il mio standard di workflow fatto bene è il Content Factory di Exponium"* → 3 (prova, barra concreta).

---

## Checklist completezza (per struct-gate)
- [ ] `SKILL.md` con frontmatter `name: maximilian-voice` + `description` (COSA+QUANDO+trigger+DO NOT).
- [ ] I 5 invarianti nel kernel, ognuno con definizione operativa (non aggettivo vago).
- [ ] `references/patterns/corpus-examples.md` con ≥6 coppie "frase debole → frase-Max" CITATE dal corpus.
- [ ] `references/` ≥3 file, ≥300 righe totali. Esempi tratti dal corpus integrale, mai inventati a tono.
- [ ] `evals/evals.json` ≥4 prompt, ≥1 negativo (un copy cliente o un testo già-Max-perfetto).
- [ ] `README.md` con installazione + uso. Nessun placeholder nel kernel.

---

## Esempio
Input (verdetto grezzo, modalità riscrivi): *"Il reparto sembra un po' piccolo, forse si potrebbe
considerare di ampliarlo quando ci sarà tempo."*
Output voce-Max: *"Questo reparto è un giocattolo: 1 file per una figura che dovrebbe essere un team
di 6-10 agenti + un workflow (corpus §34). RIFAI. Lo standard è il Content Factory di Exponium, non un .md."*
→ Diretto (1), sfidante (2), prove (3: conteggio+citazione), scala (4), zero fronzoli (5).

---

## Anti-pattern
- "Voce di Claude gentile": ammorbidire un verdetto con cortesie ("ottimo, però…") → tradisce 1+5.
  È il rischio #1 del dossier (l'organo che suona come Claude invece che come Max).
- Provocazione SENZA prova → diventa arroganza vuota; l'invariante 3 esige sempre il fatto a supporto.
- Inventare il tono "a sensazione" invece di ancorarlo al corpus → la voce deriva. Cita sempre il corpus.
- Usarla per copy cliente → confonde la voce interna di Max col copywriting di vendita (DO NOT).
- `description` senza trigger/DO NOT → non si attiva (P15).

---

## Connessioni
- [[WF-REVIEW-MAXIMILIAN]] — MX-STYLE la usa per giudicare la voce, MX-PRIME per sintetizzare il verdetto
- [[WF-ANTICIPAZIONE]] — MX-PRIME la usa per il tono del brief di anticipazione
- [[maximilian-standard-gate]] — il gate decide il VERDETTO; questa skill ne confeziona la VOCE
- [[Schema-Skill]] — la forma canonica che la FORGE seguirà per costruirla
- [[12-DOSSIER-MAXIMILIAN]] §2 (MX-STYLE/MX-PRIME) · §4 (skill) · §7 (corpus = fonte degli esempi)
- corpus `direttiva-20260611-scala-v2.md` — tutte le frasi-ancora vengono da qui (mai inventate)
