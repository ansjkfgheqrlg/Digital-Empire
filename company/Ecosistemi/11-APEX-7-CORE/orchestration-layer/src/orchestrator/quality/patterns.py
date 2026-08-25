"""NERVE-SAVE :: patterns.py
Source of truth per tutti i pattern regex del sistema di compressione ed economia token.
"""
from __future__ import annotations

import re

# ─────────────────────────────────────────────
# FILLER PATTERNS — P1 ELIMINATION ENGINE
# ─────────────────────────────────────────────
FILLER_PATTERNS: dict[str, list[str]] = {
    "introduttori_vuoti": [
        r"è importante sottolineare che\s*",
        r"è fondamentale notare che\s*",
        r"vale la pena menzionare che\s*",
        r"bisogna ricordare che\s*",
        r"occorre precisare che\s*",
        r"è necessario evidenziare che\s*",
        r"mi preme sottolineare che\s*",
        r"tengo a precisare che\s*",
        r"è doveroso specificare che\s*",
        r"è bene chiarire che\s*",
    ],
    "avverbi_decorativi": [
        r"\bfondamentalmente\b\s*,?\s*",
        r"\bsostanzialmente\b\s*,?\s*",
        r"\bessenzialmente\b\s*,?\s*",
        r"\bin pratica\b\s*,?\s*",
        r"\bin sostanza\b\s*,?\s*",
        r"\bdi fatto\b\s*,?\s*",
        r"\bchiaramente\b\s*,?\s*",
        r"\bovviamente\b\s*,?\s*",
        r"\bassolutamente\b\s*,?\s*",
        r"\bdecisamente\b\s*,?\s*",
        r"\bpraticamente\b\s*,?\s*",
        r"\bsicuramente\b\s*,?\s*",
        r"\beffettivamente\b\s*,?\s*",
        r"\bnaturalmente\b\s*,?\s*",
        r"\bsemplicemente\b\s*,?\s*",
    ],
    "riferimenti_interni": [
        r"come accennato (in precedenza|prima|sopra)\s*,?\s*",
        r"come (detto|menzionato|indicato) (sopra|prima|in precedenza)\s*,?\s*",
        r"come (abbiamo visto|abbiamo detto)\s*,?\s*",
        r"ricordiamo che\s*",
        r"come già (detto|indicato|spiegato)\s*,?\s*",
        r"come (anticipato|sottolineato) (in precedenza|prima)\s*,?\s*",
    ],
    "chiusure_sociali": [
        r"spero (che questo|di essere stato|che la risposta).{0,60}",
        r"fammi sapere se.{0,80}",
        r"non esitare a (chiedere|contattarmi).{0,60}",
        r"sono a (tua |vostra )?disposizione.{0,60}",
        r"se hai (altre )?domande.{0,60}",
        r"resto a disposizione.{0,60}",
        r"buon lavoro[.!]?\s*",
        r"in bocca al lupo[.!]?\s*",
    ],
    "metacommenti": [
        r"(risponderò|analizzerò|esaminerò) (a )?(questa )?(domanda|richiesta).{0,60}",
        r"analizziamo (insieme|questa).{0,60}",
        r"vediamo (insieme|come|cosa).{0,40}",
        r"procediamo (con|a|ad).{0,40}",
        r"iniziamo (con|da|col).{0,40}",
        r"partiamo (da|con|dal).{0,40}",
        r"di seguito (trovi|trovate|è presente).{0,40}",
    ],
    "conclusioni_ovvie": [
        r"in conclusione,?\s*(possiamo (dire|affermare) che)?\s*",
        r"per (concludere|riassumere|ricapitolare),?\s*",
        r"in sintesi,?\s*",
        r"riassumendo,?\s*",
        r"in breve,?\s*",
        r"quindi,? in definitiva,?\s*",
    ],
    "amplificatori_vuoti": [
        r"\bmolto importante\b",
        r"\bassolutamente fondamentale\b",
        r"\bdi cruciale importanza\b",
        r"\bdi primaria importanza\b",
        r"\bdi vitale importanza\b",
        r"\bstrateg(?:ico|icamente) rilevante\b",
    ],
    "conferme_ridondanti": [
        r"^(esatto|precisamente|certamente|assolutamente|certo)[,!.]?\s*",
        r"^(sì,?\s*)?(hai ragione|è corretto|è giusto)[,.]?\s*",
        r"^(perfetto|ottimo|benissimo)[,!.]?\s*",
        r"^(capisco|comprendo)[,.]?\s*",
    ],
    "riempitivi_generici": [
        r"\bcome (sappiamo|tutti sanno|è noto)\b\s*,?\s*",
        r"\bè risaputo che\s*",
        r"\bè noto che\s*",
        r"\bcome è ovvio\s*,?\s*",
        r"\bsenza (ombra di )?dubbio\b\s*,?\s*",
        r"\bè innegabile che\s*",
    ],
}

# ─────────────────────────────────────────────
# INTENT PATTERNS — FASE 0 ENGINE
# ─────────────────────────────────────────────
INTENT_PATTERNS: dict[str, list[str]] = {
    "conferma": [
        r"\b(è corretto|va bene|funziona|giusto\?|è giusto)\b",
        r"\b(confermi|corretto\?|sì o no|devo o no)\b",
        r"\b(è vero che|è sbagliato)\b",
    ],
    "info_puntuale": [
        r"\bcos'è\b",
        r"\bche cos'è\b",
        r"\bcosa (significa|vuol dire|indica)\b",
        r"\bquant[io]\b",
        r"\bquando (è|avviene|succede)\b",
        r"\bdove (si trova|è|viene)\b",
    ],
    "how_to": [
        r"\bcome (si fa|faccio|posso|devo|funziona)\b",
        r"\bpassi per\b",
        r"\bprocedura per\b",
        r"\bcome (configurare|installare|impostare|avviare)\b",
        r"\bistruzioni per\b",
    ],
    "debug": [
        r"\b(errore|error|bug|eccezione|exception)\b",
        r"\bnon funziona\b",
        r"\b(fallisce|si blocca|crasha)\b",
        r"\bperché (non funziona|non parte|non risponde)\b",
        r"\bcome (risolvere|correggere|fixare)\b",
    ],
    "architettura": [
        r"\b(progetta|disegna|architetta|struttura)\b",
        r"\b(sistema|architettura|infrastruttura)\b",
        r"\b(piano|roadmap|schema|blueprint)\b",
        r"\bcome (organizzare|strutturare|progettare)\b",
    ],
    "codice": [
        r"\b(scrivi|implementa|crea|genera).{0,20}(codice|script|funzione|classe|modulo)\b",
        r"\bcodice per\b",
        r"\bin (python|javascript|typescript|sql|bash|java|go|rust)\b",
        r"\b(implementa|programma|sviluppa)\b",
    ],
    "comparazione": [
        r"\b(confronta|differenza tra|quale è meglio)\b",
        r"\bvs\.?\b",
        r"\bversus\b",
        r"\bpro e contro\b",
        r"\bvantaggi e svantaggi\b",
        r"\bmigliore tra\b",
    ],
    "spiegazione": [
        r"\b(spiegami|spiegare|non capisco)\b",
        r"\bcosa significa\b",
        r"\bcos'è\b",
        r"\bcome mai\b",
        r"\bperché\b",
        r"\bcome funziona\b",
    ],
    "documento": [
        r"\b(documento|documentazione|report|relazione)\b",
        r"\b(completo|dettagliato|approfondito|esaustivo)\b",
        r"\b(articolo|guida completa|manuale)\b",
        r"\bscrivimi (un|una|il|la)\b",
    ],
}

# ─────────────────────────────────────────────
# ESCALATION TRIGGERS — FASE 1
# ─────────────────────────────────────────────
ESCALATION_TRIGGERS: list[tuple[str, str]] = [
    (r"\b(completo|dettagliato|approfondito|esaustivo)\b", "Dettaglio esplicito richiesto dall'utente"),
    (r"\b(tutto|ogni|lista completa|elenco completo)\b", "Completezza esplicita richiesta"),
    (r"\b(documento|documentazione|report|guida)\b", "Formato documento richiesto"),
    (r"\b(step.by.step|passo.passo|nel dettaglio)\b", "Procedura dettagliata richiesta"),
    (r"\b(spiega tutto|dimmi tutto|voglio capire bene)\b", "Comprensione completa richiesta"),
]

# ─────────────────────────────────────────────
# FILLER WORDS — TES ENGINE
# ─────────────────────────────────────────────
FILLER_WORD_SET: frozenset[str] = frozenset({
    "fondamentalmente",
    "sostanzialmente",
    "essenzialmente",
    "praticamente",
    "assolutamente",
    "ovviamente",
    "chiaramente",
    "certamente",
    "decisamente",
    "semplicemente",
    "naturalmente",
    "sicuramente",
    "effettivamente",
    "innegabilmente",
    "indubbiamente",
    "necessariamente",
    "inevitabilmente",
    "comprensibilmente",
    "logicamente",
    "giustamente",
    "correttamente",
})

# ─────────────────────────────────────────────
# LEVEL BUDGETS — ECONOMY CLASSIFIER
# ─────────────────────────────────────────────
LEVEL_BUDGETS: dict[str, tuple[int, int]] = {
    "MICRO": (1, 50),
    "MEDIO": (50, 200),
    "ALTO": (200, 500),
    "MASSIMO": (500, 9999),
}

# ─────────────────────────────────────────────
# FORMAT HIERARCHY — P4 FORMAT INTELLIGENCE
# ─────────────────────────────────────────────
FORMAT_HIERARCHY: list[tuple[str, float]] = [
    ("tabella", 1.00),
    ("codice_commentato", 0.85),
    ("lista_ordinata", 0.70),
    ("lista_non_ord", 0.60),
    ("prosa_tecnica", 0.40),
    ("prosa_discorsiva", 0.20),
]
