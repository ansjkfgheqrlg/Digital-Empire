from __future__ import annotations

import unittest

from orchestrator.quality import (
    FILLER_PATTERNS,
    IntentType,
    TESGrade,
    TokenLevel,
    calculate_filler_density,
    calculate_tes,
    classify_query,
    compress_verified_output,
    count_semantic_repetitions,
    count_tokens,
    detect_format_efficiency,
)


class NerveSaveV2Tests(unittest.TestCase):
    def test_filler_categories_elimination(self):
        sample_with_fillers = (
            "È importante sottolineare che fondamentalmente il sistema funziona. "
            "Come accennato prima, di fatto non ci sono errori. "
            "Spero che questo ti sia stato utile! Fammi sapere se hai domande!"
        )
        res = compress_verified_output(sample_with_fillers)
        self.assertTrue(res.preservation_pass)
        self.assertNotIn("È importante sottolineare che", res.text)
        self.assertNotIn("fondamentalmente", res.text)
        self.assertNotIn("Come accennato prima", res.text)
        self.assertNotIn("Spero che questo ti sia stato utile", res.text)
        self.assertIn("il sistema funziona", res.text)
        self.assertIn("non ci sono errori", res.text)

    def test_protected_spans_preserved(self):
        text = "Il limite è 100% vietato con codice `rm -rf /` e warning critico."
        res = compress_verified_output(text)
        self.assertTrue(res.preservation_pass)
        self.assertIn("100%", res.text)
        self.assertIn("vietato", res.text)
        self.assertIn("`rm -rf /`", res.text)
        self.assertIn("warning critico", res.text)

    def test_intent_classification(self):
        # Micro: conferma
        c1 = classify_query("È corretto questo approccio?")
        self.assertEqual(c1.intent, IntentType.CONFERMA)
        self.assertEqual(c1.level, TokenLevel.MICRO)

        # Medio: how-to
        c2 = classify_query("Come faccio a configurare un circuit breaker?")
        self.assertEqual(c2.intent, IntentType.HOW_TO)
        self.assertEqual(c2.level, TokenLevel.MEDIO)

        # Alto: architettura
        c3 = classify_query("Progetta un'architettura distribuita per microservizi")
        self.assertEqual(c3.intent, IntentType.ARCHITETTURA)
        self.assertEqual(c3.level, TokenLevel.ALTO)

        # Escalation trigger: richiesta di dettaglio
        c4 = classify_query("Spiegami nel dettaglio tutto il flusso completo")
        self.assertTrue(c4.escalation.triggered)
        self.assertGreaterEqual(c4.level.value, TokenLevel.ALTO.value)

    def test_tes_calculation_and_audit(self):
        dense_text = """| Servizio | Stato | Latenza |
|---|---|---|
| auth | OK | 12ms |
| db | OK | 4ms |

1. Valida token
2. Esegui query
3. Ritorna risposta
"""
        report = calculate_tes(dense_text)
        self.assertGreaterEqual(report.tes_score, 0.60)
        self.assertIn(report.grade, (TESGrade.ECCELLENTE, TESGrade.ACCETTABILE))
        self.assertTrue(report.all_audits_passed)

    def test_filler_density_and_repetitions(self):
        diluted = "Fondamentalmente, sostanzialmente, essenzialmente, chiaramente è così."
        density = calculate_filler_density(diluted)
        self.assertGreater(density, 0.5)

        repetitive = "Il server principale è andato in timeout critico. Il server principale è andato in timeout critico."
        reps = count_semantic_repetitions(repetitive)
        self.assertEqual(reps, 1)

    def test_format_efficiency(self):
        table_text = "| A | B |\n|---|---|\n| 1 | 2 |"
        eff_table = detect_format_efficiency(table_text)
        self.assertGreaterEqual(eff_table, 0.70)


if __name__ == "__main__":
    unittest.main()
