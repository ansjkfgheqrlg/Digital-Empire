"""
Suite del Calc Layer APEX-7.

Come per l'orchestration layer, i test marcati REGRESSIONE riproducono un
errore reale dello zip `apex7_orchestrator` e pretendono che qui non si ripeta.

    python test_calc.py
"""
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from calc import catalogo, esegui, esegui_certificato, esegui_grafo


def v(risposta):
    """Valori di una risposta riuscita; fallisce con il motivo se non lo e'."""
    assert risposta["ok"], risposta["errore"]
    return risposta["valori"]


class TestContratto(unittest.TestCase):
    def test_catalogo_non_vuoto_e_serializzabile(self):
        import json
        c = catalogo()
        self.assertGreaterEqual(len(c), 16)
        json.dumps(c)   # il ponte trasporta solo JSON

    def test_modulo_sconosciuto_non_solleva(self):
        r = esegui({"modulo": "non_esiste"})
        self.assertFalse(r["ok"])
        self.assertIn("sconosciuto", r["errore"])

    def test_parametro_mancante_non_solleva(self):
        r = esegui({"modulo": "percentuale", "parte": 10})
        self.assertFalse(r["ok"])
        self.assertIn("totale", r["errore"])

    def test_parametro_non_numerico_rifiutato(self):
        r = esegui({"modulo": "percentuale", "parte": "dieci", "totale": 100})
        self.assertFalse(r["ok"])

    def test_le_assunzioni_sono_dichiarate(self):
        """Un numero uscito da un default non e' un numero misurato."""
        r = esegui({"modulo": "rendimento", "capitale": 1000, "anni": 5,
                    "rendimento_annuo": 0.07})
        nomi = [a["parametro"] for a in r["assunzioni"]]
        self.assertIn("inflazione_annua", nomi)
        self.assertIn("tassa", nomi)
        for a in r["assunzioni"]:
            self.assertTrue(a["fonte"], "assunzione senza fonte dichiarata")


class TestBase(unittest.TestCase):
    def test_percentuale(self):
        r = v(esegui({"modulo": "percentuale", "parte": 25, "totale": 200}))
        self.assertAlmostEqual(r["percentuale"], 12.5)
        self.assertAlmostEqual(r["percentuale_resto"], 87.5)

    def test_variazione_percentuale(self):
        r = v(esegui({"modulo": "variazione_percentuale", "da": 200, "a": 250}))
        self.assertAlmostEqual(r["variazione_pct"], 25.0)
        self.assertTrue(r["in_aumento"])

    def test_sconto(self):
        r = v(esegui({"modulo": "applica_percentuale", "valore": 100,
                      "percentuale": 30, "in_aumento": 0}))
        self.assertAlmostEqual(r["risultato"], 70.0)

    def test_crescita_composta_non_e_lineare(self):
        r = v(esegui({"modulo": "crescita_composta", "valore_iniziale": 1000,
                      "tasso_periodo": 0.10, "periodi": 3}))
        self.assertAlmostEqual(r["valore_finale"], 1331.0, places=2)


class TestProbabilita(unittest.TestCase):
    def test_composta_and_or(self):
        r = v(esegui({"modulo": "probabilita_composta", "probabilita_pct": [50, 50]}))
        self.assertAlmostEqual(r["tutti_pct"], 25.0)
        self.assertAlmostEqual(r["almeno_uno_pct"], 75.0)

    def test_composta_rifiuta_fuori_intervallo(self):
        self.assertFalse(esegui({"modulo": "probabilita_composta",
                                 "probabilita_pct": [50, 150]})["ok"])

    def test_bayes_caso_classico(self):
        # prevalenza 1%, sensibilita' 99%, falsi positivi 5% -> ~16.7%
        r = v(esegui({"modulo": "bayes", "prior_pct": 1, "sensibilita_pct": 99,
                      "falsi_positivi_pct": 5}))
        self.assertAlmostEqual(r["posteriore_pct"], 16.6667, places=3)

    def test_soglia_senza_volatilita_e_deterministica(self):
        r = v(esegui({"modulo": "probabilita_soglia", "valore_iniziale": 100,
                      "soglia": 150, "tasso_atteso": 0.10, "volatilita": 0.0,
                      "periodi": 5}))
        self.assertTrue(r["deterministico"])
        self.assertAlmostEqual(r["probabilita_pct"], 100.0)

    def test_soglia_probabilita_in_intervallo(self):
        r = v(esegui({"modulo": "probabilita_soglia", "valore_iniziale": 1000,
                      "soglia": 5000, "tasso_atteso": 0.30, "volatilita": 0.5,
                      "periodi": 5}))
        self.assertTrue(0.0 <= r["probabilita_pct"] <= 100.0)
        self.assertLess(r["mediana"], r["valore_atteso"], "lognormale: mediana < media")

    def test_soglia_piu_alta_e_meno_probabile(self):
        base = dict(modulo="probabilita_soglia", valore_iniziale=1000,
                    tasso_atteso=0.15, volatilita=0.3, periodi=5)
        bassa = v(esegui({**base, "soglia": 1500}))["probabilita_pct"]
        alta = v(esegui({**base, "soglia": 9000}))["probabilita_pct"]
        self.assertGreater(bassa, alta)

    def test_monte_carlo_riproducibile(self):
        req = {"modulo": "monte_carlo", "valore_iniziale": 1000, "tasso_atteso": 0.08,
               "volatilita": 0.2, "periodi": 5, "simulazioni": 2000, "seme": 7}
        self.assertEqual(v(esegui(req)), v(esegui(req)), "stesso seme, risultato diverso")

    def test_monte_carlo_percentili_ordinati(self):
        r = v(esegui({"modulo": "monte_carlo", "valore_iniziale": 1000,
                      "tasso_atteso": 0.08, "volatilita": 0.25, "periodi": 10,
                      "simulazioni": 3000, "soglia": 2000}))
        self.assertLessEqual(r["p05"], r["p25"])
        self.assertLessEqual(r["p25"], r["mediana"])
        self.assertLessEqual(r["mediana"], r["p75"])
        self.assertLessEqual(r["p75"], r["p95"])
        self.assertIn("prob_sopra_soglia_pct", r)

    def test_scenari_valore_atteso(self):
        r = v(esegui({"modulo": "scenari_calibrati", "valore_migliore": 200,
                      "valore_base": 100, "valore_peggiore": 0}))
        self.assertAlmostEqual(r["valore_atteso"], 100.0)
        self.assertAlmostEqual(r["somma_probabilita_pct"], 100.0)

    def test_REGRESSIONE_scenari_rifiutano_probabilita_non_calibrate(self):
        r = esegui({"modulo": "scenari_calibrati", "valore_migliore": 200,
                    "valore_base": 100, "valore_peggiore": 0,
                    "prob_migliore_pct": 30, "prob_base_pct": 30, "prob_peggiore_pct": 30})
        self.assertFalse(r["ok"])
        self.assertIn("100%", r["errore"])

    def test_scenari_rifiutano_ordine_incoerente(self):
        r = esegui({"modulo": "scenari_calibrati", "valore_migliore": 10,
                    "valore_base": 100, "valore_peggiore": 50})
        self.assertFalse(r["ok"])


class TestDenaro(unittest.TestCase):
    def test_REGRESSIONE_le_tasse_colpiscono_la_plusvalenza_nominale(self):
        """
        Lo zip tassava il rendimento REALE. In Italia non c'e' indicizzazione
        all'inflazione: si tassa il guadagno in euro correnti.
        """
        r = v(esegui({"modulo": "rendimento", "capitale": 100000, "anni": 10,
                      "rendimento_annuo": 0.075, "commissioni_annue": 0.0022,
                      "tassa": 0.26, "inflazione_annua": 0.025}))
        atteso_nominale = 100000 * (1.075 - 0.0022) ** 10
        self.assertAlmostEqual(r["nominale_lordo"], atteso_nominale, places=0)
        self.assertAlmostEqual(r["imposta"], (atteso_nominale - 100000) * 0.26, places=0)
        self.assertAlmostEqual(r["netto_reale"], 137040.68, places=0)

    def test_nessuna_imposta_senza_plusvalenza(self):
        r = v(esegui({"modulo": "rendimento", "capitale": 10000, "anni": 5,
                      "rendimento_annuo": -0.05, "tassa": 0.26}))
        self.assertEqual(r["imposta"], 0.0)
        self.assertEqual(r["plusvalenza_nominale"], 0.0)

    def test_REGRESSIONE_confronto_risk_free_omogeneo(self):
        """
        Lo zip confrontava un valore atteso NETTO con un BTP LORDO nominale, e
        concludeva che l'ETF perdeva di 10.812 EUR. A parita' di trattamento
        l'ETF vince: il segno della conclusione era sbagliato.
        """
        r = v(esegui({"modulo": "confronto_risk_free", "capitale": 100000, "anni": 10,
                      "rendimento_annuo": 0.075, "commissioni_annue": 0.0022}))
        self.assertTrue(r["conviene_rischiare"])
        self.assertGreater(r["premio_al_rischio"], 20000)
        # il risk-free e' netto anche lui, non il montante lordo 145.202
        self.assertLess(r["risk_free_netto_reale"], 115000)

    def test_confronto_risk_free_puo_dire_di_no(self):
        r = v(esegui({"modulo": "confronto_risk_free", "capitale": 100000, "anni": 10,
                      "rendimento_annuo": 0.02, "commissioni_annue": 0.01}))
        self.assertFalse(r["conviene_rischiare"])
        self.assertLess(r["premio_al_rischio"], 0)

    def test_costi_invisibili_sommano(self):
        r = v(esegui({"modulo": "costi_invisibili", "capitale": 100000, "anni": 10,
                      "rendimento_annuo": 0.075, "commissioni_annue": 0.0022}))
        somma = r["costo_commissioni"] + r["costo_tasse"] + r["costo_inflazione"]
        self.assertAlmostEqual(somma, r["costo_totale"], places=2)
        self.assertGreater(r["quota_erosa_pct"], 0)

    def test_REGRESSIONE_il_capitale_non_puo_diventare_negativo(self):
        """Lo zip certificava uno scenario con capitale finale -2,92 EUR."""
        respinto = esegui({"modulo": "rischio", "capitale": 100000, "anni": 5,
                           "rendimento_annuo": 0.08, "perdita_massima_pct": 1.5})
        self.assertFalse(respinto["ok"], "una perdita del 150% non e' stata rifiutata")

        r = v(esegui({"modulo": "rischio", "capitale": 100000, "anni": 5,
                      "rendimento_annuo": 0.08, "perdita_massima_pct": 1.0}))
        self.assertGreaterEqual(r["capitale_minimo_residuo"], 0.0)

    def test_rischio_segnala_asimmetria(self):
        r = v(esegui({"modulo": "rischio", "capitale": 10000, "anni": 1,
                      "rendimento_annuo": 0.05, "perdita_massima_pct": 0.50}))
        self.assertTrue(r["rischio_asimmetrico"])
        self.assertLessEqual(r["var_95"], 10000)


class TestGuadagni(unittest.TestCase):
    def test_kdp_fascia_70(self):
        r = v(esegui({"modulo": "royalty_kdp", "prezzo": 4.99, "peso_file_mb": 2,
                      "unita_vendute": 500, "costi_fissi": 300}))
        self.assertEqual(r["aliquota_applicata"], 0.70)
        self.assertTrue(r["in_fascia_70"])
        self.assertAlmostEqual(r["royalty_per_copia"], 4.99 * 0.70 - 0.30, places=3)
        self.assertTrue(r["in_utile"])

    def test_kdp_fuori_fascia_scende_al_35(self):
        r = v(esegui({"modulo": "royalty_kdp", "prezzo": 14.99, "unita_vendute": 100}))
        self.assertEqual(r["aliquota_applicata"], 0.35)
        self.assertEqual(r["costo_consegna"], 0.0)

    def test_kdp_cartaceo(self):
        r = v(esegui({"modulo": "royalty_kdp", "prezzo": 12.99, "formato": 0,
                      "costo_stampa": 4.50, "unita_vendute": 100}))
        self.assertEqual(r["aliquota_applicata"], 0.60)
        self.assertAlmostEqual(r["royalty_per_copia"], 12.99 * 0.60 - 4.50, places=3)

    def test_pareggio_e_perdita_per_copia(self):
        r = v(esegui({"modulo": "royalty", "prezzo": 10, "aliquota_royalty": 0.70,
                      "unita_vendute": 0, "costi_fissi": 350}))
        self.assertEqual(r["unita_per_pareggio"], 50)
        self.assertFalse(r["in_utile"])

        perdente = v(esegui({"modulo": "royalty", "prezzo": 2, "aliquota_royalty": 0.35,
                             "unita_vendute": 1000, "costo_per_unita": 1.0}))
        self.assertEqual(perdente["unita_per_pareggio"], -1.0)
        self.assertLess(perdente["royalty_per_unita"], 0)
        self.assertFalse(perdente["in_utile"])

    def test_prezzo_ottimale_rifiuta_elasticita_positiva(self):
        r = esegui({"modulo": "prezzo_ottimale", "prezzo_attuale": 5,
                    "unita_attuali": 100, "elasticita": 0.5})
        self.assertFalse(r["ok"])
        self.assertIn("negativo", r["errore"])

    def test_prezzo_ottimale_domanda_rigida_consiglia_di_alzare(self):
        r = v(esegui({"modulo": "prezzo_ottimale", "prezzo_attuale": 2.99,
                      "unita_attuali": 1000, "elasticita": -0.5, "prezzo_max": 9.99}))
        self.assertTrue(r["alzare_il_prezzo"])
        self.assertGreaterEqual(r["guadagno_aggiuntivo"], 0)


class TestGrafo(unittest.TestCase):
    def test_catena_di_calcoli(self):
        """Il guadagno da royalty diventa il capitale del calcolo successivo."""
        out = esegui_grafo([
            {"nome": "libro", "modulo": "royalty_kdp",
             "parametri": {"prezzo": 4.99, "unita_vendute": 2000, "costi_fissi": 500}},
            {"nome": "investi", "modulo": "rendimento", "dipende_da": ["libro"],
             "parametri": {"anni": 10, "rendimento_annuo": 0.07},
             "prendi": {"capitale": "libro.guadagno_netto"}},
        ])
        self.assertTrue(out["ok"], out["passi"])
        self.assertEqual(out["ordine"], ["libro", "investi"])
        guadagno = out["passi"]["libro"]["valori"]["guadagno_netto"]
        self.assertGreater(out["passi"]["investi"]["valori"]["netto_reale"], guadagno * 0.9)

    def test_riferimento_a_campo_inesistente_e_esplicito(self):
        out = esegui_grafo([
            {"nome": "a", "modulo": "percentuale", "parametri": {"parte": 1, "totale": 2}},
            {"nome": "b", "modulo": "rendimento", "dipende_da": ["a"],
             "parametri": {"anni": 1, "rendimento_annuo": 0.05},
             "prendi": {"capitale": "a.campo_che_non_esiste"}},
        ])
        self.assertFalse(out["ok"])
        self.assertEqual(out["stati"]["b"], "FAILED")

    def test_ciclo_bloccato_prima_di_eseguire(self):
        from orchestration import DAGCycleError
        with self.assertRaises(DAGCycleError):
            esegui_grafo([
                {"nome": "a", "modulo": "percentuale", "dipende_da": ["b"], "parametri": {}},
                {"nome": "b", "modulo": "percentuale", "dipende_da": ["a"], "parametri": {}},
            ])


class TestCertificazione(unittest.TestCase):
    def test_calcolo_valido_passa_i_gate(self):
        out = esegui_certificato({"modulo": "royalty_kdp", "prezzo": 4.99,
                                  "unita_vendute": 500, "costi_fissi": 300})
        self.assertTrue(out["certificato"], out["referto"])

    def test_calcolo_fallito_non_e_certificato(self):
        out = esegui_certificato({"modulo": "percentuale", "parte": 1, "totale": 0})
        self.assertFalse(out["certificato"])

    def test_scenari_diventano_la_distribuzione_verificata_da_L5(self):
        out = esegui_certificato({"modulo": "scenari_calibrati", "valore_migliore": 200,
                                  "valore_base": 100, "valore_peggiore": 0})
        self.assertTrue(out["certificato"], out["referto"])
        l5 = next(g for g in out["scorecard"] if g["level"] == 5)
        self.assertGreaterEqual(l5["checks_total"], 7, "L5 non ha verificato la calibrazione")


if __name__ == "__main__":
    unittest.main(verbosity=2)
