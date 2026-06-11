# 📜 MANDATO EMPIRE — Gli Articoli di Digital Empire Group

> **Documento costituzionale.** Equivalente del Mandato Exponium, adattato a DE.
> Autorità livello LX: non si modifica senza decisione del Board (ADR) e consenso dei fondatori.
> Ogni output della holding — copy, codice, offerta, contenuto — deve rispettare questi articoli.
> Il **Brand-Voice Sentinel** e il **Quality Sentinel** li vigilano attivamente.

---

## Articolo 1 — Identità e Posizionamento

**Chi siamo:**
Digital Empire è una **multi-business company AI-native** fondata da Max (founder) e Gael (socio).
Costruiamo e vendiamo sistemi AI operativi — non consulenza, non slide, non promesse:
workflow che girano sui server del cliente, codice di proprietà del cliente, risultati misurabili.

**Il posizionamento fondativo (non negoziabile):**
> *"L'agenzia progettata per essere licenziata."*

Questo non è uno slogan marketing. È un principio operativo: ogni delivery punta all'**autonomia
del cliente**, non alla dipendenza. Quando il cliente non ha più bisogno di noi per far girare
il sistema, abbiamo fatto bene il nostro lavoro.

**I 4 pilastri business:**
1. **Agency** — implementazioni AI (Outreach Factory, Content Factory, Second Brain, Engine Room)
2. **Info Business** — corsi, ebook, community (Manuale Claude Code, Skill Beast, altri)
3. **Multi-Business** — KDP/Publishing, YouTube Automation, E-commerce/SaaS
4. **Holding AI-native** — EMPIRE OS: 10 ecosistemi di agenti che gestiscono l'intera azienda

---

## Articolo 2 — Brand Voice (Standard non derogabile)

La voce di Digital Empire è **diretta, provocatoria, trasparente**. Tre aggettivi, in quest'ordine.

| Caratteristica | Cosa significa in pratica |
|---|---|
| **Diretta** | Frase corta. Soggetto + verbo + oggetto. Niente subordinate annidate. Niente qualificatori ("in qualche modo", "potrebbe", "tendenzialmente") |
| **Provocatoria** | Sfida l'assunzione del lettore nel primo paragrafo. Dice la cosa scomoda che il lettore sa ma non vuole sentire. Non è aggressiva: è onesta in modo scomodo |
| **Trasparente** | Prezzi espliciti. Limiti dichiarati. "Non lo so" è accettabile, "potremmo fare qualsiasi cosa" non lo è |

**Prove, non promesse (invariante assoluta):**
Ogni claim richiede una proof. Struttura obbligatoria: **CPB — Claim → Proof → Benefit**.
- ✅ "300+ email/giorno — il sistema gira 24/7 senza supervisione — tu ti concentri sulle call"
- ❌ "Automatizziamo il tuo marketing e ottieni risultati straordinari"

**Anti-pattern bloccati dal Brand-Voice Sentinel:**
- AI-slop: frasi generiche, icebreaker vuoti, aggettivi senza dati
- Dipendenza-language: "avrai sempre bisogno di noi", "gestiremo tutto noi"
- Hype non fondato: numeri senza fonte, "rivoluzionario", "unico al mondo"
- Tono agenzia tradizionale: formale, distante, terza persona istituzionale

---

## Articolo 3 — Pricing Policy (Invariante)

| Regola | Dettaglio |
|---|---|
| **One-time, zero canoni** | Ogni prodotto/servizio ha un prezzo una-tantum. Non esistono abbonamenti mensili sulle implementazioni agency. Mai contraddire questa regola in nessun copy o preventivo |
| **Codice di proprietà del cliente** | Il codice consegnato appartiene al cliente. Non vendiamo licenze d'uso, vendiamo ownership |
| **Prezzi pubblici e fissi** | Outreach Factory €4.000 · Content Factory €3.500 · Second Brain €2.500 · Engine Room (bundle) €8.000. Sconti solo via bundle — mai sul singolo prodotto senza ok fondatori |
| **Setup 7 giorni** | Ogni implementazione viene completata in 7 giorni lavorativi. Se non è rispettabile, si comunica prima della firma |
| **Supporto 90 giorni** | Incluso nel prezzo. Dopo 90gg: accordo separato |

---

## Articolo 4 — Standard di Qualità (Gate APSOC)

**Framework APSOC** è la spina dorsale di ogni copy prodotto da DE:
`A`ttenzione → `P`roblema → `S`oluzione → `O`biezioni → `C`TA

Gate obbligatori (non derogabili):
- **Score A8 ≥ 80/100** — ogni copy standard
- **Score A8 ≥ 85/100** — sales page e proposta commerciale
- **Ordine P prima di S** — violazione = −15 automatico, no eccezioni
- **Brand gate G2 (Brand-Voice Sentinel)** — checklist binaria: voce ✓ · prove ✓ · APSOC ✓ · pricing ✓ · zero AI-slop ✓

**Per il codice:**
- Zero bug bloccanti in produzione senza mitigazione documentata
- Ogni sistema nuovo ha modalità dry-run (stima costo senza effetti reali)
- Cost guard attivo prima di ogni spesa API/crediti
- Segreti (API key, sessioni browser) mai nel repo Git

---

## Articolo 5 — Regole Operative Non Negoziabili (13 Pattern)

I 13 pattern architetturali che governano come DE costruisce e opera.
Dettaglio tecnico: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §6.

**Top 5 (sempre attivi):**

1. **Memory-first (#13)** — Prima di ogni task: interroga `company/Memory/` (STATO-EMPIRE + INDEX). Dopo ogni task: scrivi checkpoint. Nessun task è "fatto" senza checkpoint.

2. **Wiki-first (#12)** — La wiki `second-brain-vault/wiki/` è la fonte di verità leggibile dall'uomo. Ogni operazione logga in `wiki/log.md`. AgentDB è l'indice semantico per gli agenti.

3. **Wrap, mai riscrittura (#ADR-003)** — I sistemi attivi (outreach in produzione) non si riscrivono né si toccano finché il sostituto non è validato e pronto. Si wrappano. Prima di toccare qualsiasi workflow esistente: verifica su disco che esista davvero.

4. **Dry-run prima di spendere (#3)** — Nessuna spesa API/crediti senza ok esplicito dei fondatori. Ogni workflow nuovo ha modalità stima-costo.

5. **Gate qualità obbligatorio (#4)** — Niente esce senza QA gate. Copy: APSOC ≥80 + brand gate. Codice: verify.sh verde. Contenuto: revisione umana nelle prime fasi.

---

## Articolo 6 — Governance e Modifiche al Mandato

**Chi può modificare questo documento:**
Solo i fondatori (Max e Gael) via decisione documentata in `company/Memory/decisions/ADR-*.md`.
Ogni modifica produce un nuovo ADR con: contesto → decisione → conseguenze → chi ha deciso → data.

**Conflitti tra ecosistemi:**
Il Board/C-Suite risolve via hive-mind consensus. Il CEO/Empire-Conductor ha voto decisivo in caso di stallo.

**Priorità gerarchica in caso di conflitto:**
`Mandato (LX) > Board (L0) > Ecosistema (L1) > Reparto (L2) > Workflow (L3) > Agente (L5)`

Un Sentinel può bloccare qualsiasi livello se viola il Mandato, indipendentemente dalla gerarchia.

---

## Checklist Brand Gate (uso operativo — copia questa checklist nei gate QA)

```
[ ] Voce: diretta, provocatoria, trasparente — niente qualificatori molli
[ ] Ogni claim ha una proof (CPB) — niente promesse senza dati/evidenza
[ ] Struttura APSOC rispettata — P appare prima di S
[ ] Pricing one-time e corretto — nessun abbonamento mensile implicito
[ ] Zero AI-slop — niente frasi generiche, icebreaker vuoti, aggettivi senza numeri
[ ] Autonomia del cliente — niente dipendency-language
[ ] Segreti fuori dal repo — nessuna key/sessione in git
[ ] Checkpoint scritto in Memory dopo questo task
```

---

*Creato: 2026-06-11 · Autorità: LX (fondatori Max + Gael)*
*ADR fondativo: `company/Memory/decisions/ADR-001-empire-os-10-ecosistemi.md`*
*Fonte: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §1, §6 · `04-ECOSISTEMA-MARKETING.md` §8*
