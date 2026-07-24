# P2 — Claim → Evidence → Example

> Per ogni affermazione (claim) del sorgente, identificare: **la tesi**, **il supporto** che la giustifica, **almeno un esempio concreto**. Se manca, generarne uno (etichettato `➕`).

## Cosa fa

Trasforma claims "nude" in claims "vestite": ogni asserzione è accompagnata dalla sua giustificazione e da un caso d'uso concreto. Combatte la tendenza degli LLM (e degli umani) a "sapere a parole" senza ancoraggio empirico.

## Chi lo applica

- **A2 `analyst-agent`** — annota `evidence` e `examples_from_source` per ogni atomo che è una claim.
- **Tutti i builder** — espandono ogni atomo claim in tripletta: definizione → evidenza → esempio. Se manca esempio o evidenza, generano (etichettando `➕`).

## Quando applicarlo

- Sempre per atomi `category: claim`.
- Spesso per `category: concept` (un concetto senza esempio è zoppo).
- Talvolta per `category: procedure` (la procedura è la "evidenza" del fatto che X funziona; serve esempio applicato).

## Quando NON applicarlo

- Per pure `category: definition` (la definizione è auto-supportante).
- Per `category: example` (è già un esempio — semmai applica P2 in reverse: a quale claim si appoggia?).

## Cuore del pattern

```python
# Triple struttura
claim_triple = {
    "claim": str,                    # la tesi
    "evidence": str | None,          # supporto: ragione, citazione, dato, ricerca
    "examples": [
        {"source": "from_source" | "generated", "text": str}
    ],
}
```

**Regola d'oro**: ogni claim non banale DEVE avere almeno un esempio. Se il sorgente non lo fornisce, il builder ne **genera uno** rilevante e lo marca con `➕`.

## Output canonico (esempio nel doc-builder)

```markdown
### 1.3 Few-shot prompting

**Claim** (definizione canonica): Mostrare 2-5 esempi al modello prima della richiesta migliora l'aderenza al pattern desiderato.

**Evidenza**: Il modello apprende il pattern dagli esempi e lo applica per coerenza statistica. (Brown et al., 2020 — GPT-3 paper; conferma empirica diffusa.)

**Esempio (sorgente)**: 3 traduzioni formali in input → traduzione formale in output.

**➕ Esempio aggiuntivo**: per generare commit message in formato Conventional Commits, mostrare 4 esempi di `<descrizione → feat(scope): message>`:
- "Added user login" → "feat(auth): implement user login flow"
- "Fixed off-by-one in pagination" → "fix(pagination): correct off-by-one in page calc"
- "Updated readme" → "docs: update README with install steps"
- "Removed old API" → "refactor(api): remove deprecated v1 endpoints"
Poi l'utente fornisce la propria descrizione e ottiene un commit message coerente con il formato.
```

## Come generare un buon esempio (quando il sorgente non ne ha)

```python
# Heuristica per generated_example
def generate_example(atom: dict, kg: dict) -> str:
    """Genera un esempio concreto, ancorato al dominio del sorgente, etichettato ➕."""
    # 1. Identifica il dominio del KG
    domain = kg["source_meta"].get("dominant_domain", "general")
    # 2. Mappa il claim a un caso d'uso realistico in quel dominio
    # 3. Scrivi un esempio CONCRETO con nomi, numeri, output atteso
    # 4. Prefisso con "➕" o introduzione esplicita "Esempio aggiuntivo generato da Forge:"
```

**Cosa rende un esempio "buono"**:
- Concreto (nomi specifici, numeri, output letterale)
- Auto-contenuto (si capisce senza altri esempi)
- Pertinente al dominio (non un esempio generico)
- Etichettato come generato (mai mascherato da "il sorgente dice")

## Anti-pattern

- **Claim nuda**: tesi senza alcun supporto → ricerca evidenza nel sorgente; se assente, genera (etichetta) o downgrada a `category: opinion`.
- **Esempio finto-citato**: spacciare un esempio generato per estratto dal sorgente → DA PROIBIRE; sempre etichettare `➕`.
- **Esempio generico** ("ad esempio una cosa qualsiasi"): inutile, non aggiunge concretezza → riscrivere o eliminare.
- **Evidenza circolare** (la claim si supporta da sola): cerca evidenza esterna o etichetta come `assumption`.

## Riferimenti

- Toulmin, S. — *The Uses of Argument* (modello claim/data/warrant)
