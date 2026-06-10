"""
Test per implementation/utils/website_checker.py

Copre:
- Happy path: sito attivo e raggiungibile
- Input invalido: URL malformato, sito vuoto
- Servizio down: timeout, errore connessione, HTTP 500
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

# Verifica dipendenze necessarie prima di importare
try:
    import requests  # noqa: F401
    import bs4  # noqa: F401
    DIPENDENZE_OK = True
except ImportError:
    DIPENDENZE_OK = False

SKIP_MSG = "Dipendenze non installate. Esegui: pip install -r requirements.txt"

if DIPENDENZE_OK:
    from implementation.utils.website_checker import (
        verifica_sito_attivo,
        analizza_html_funnel,
        calcola_funnel_score
    )

# SheetsClient è importabile senza dipendenze opzionali (solo google-api-python-client)
try:
    from implementation.utils.sheets_client import SheetsClient
    SHEETS_OK = True
except Exception:
    SHEETS_OK = False


@unittest.skipUnless(DIPENDENZE_OK, SKIP_MSG)
class TestVerificaSitoAttivo(unittest.TestCase):

    def _mock_response(self, status_code=200, text="<html><body>Contenuto normale del sito web con molte informazioni utili per i clienti che cercano il nostro servizio.</body></html>", url="https://esempio.it"):
        mock_resp = MagicMock()
        mock_resp.status_code = status_code
        mock_resp.text = text
        mock_resp.url = url
        return mock_resp

    # --- TEST 1: Happy Path ---
    @patch("implementation.utils.website_checker.requests.get")
    def test_sito_attivo_restituisce_attivo_true(self, mock_get):
        """Sito con HTTP 200 e contenuto normale → attivo=True"""
        mock_get.return_value = self._mock_response(200, "A" * 600)
        risultato = verifica_sito_attivo("https://esempio.it")
        self.assertTrue(risultato["attivo"])
        self.assertEqual(risultato["status_code"], 200)
        self.assertIsNone(risultato["errore"])

    # --- TEST 2: Input Invalido ---
    @patch("implementation.utils.website_checker.requests.get")
    def test_sito_vuoto_restituisce_non_attivo(self, mock_get):
        """Sito con HTTP 200 ma contenuto < 500 caratteri → attivo=False"""
        mock_get.return_value = self._mock_response(200, "<html>ok</html>")
        risultato = verifica_sito_attivo("https://esempio.it")
        self.assertFalse(risultato["attivo"])
        self.assertIn("vuota", risultato["errore"])

    @patch("implementation.utils.website_checker.requests.get")
    def test_sito_in_costruzione_restituisce_non_attivo(self, mock_get):
        """Sito con testo 'coming soon' → attivo=False"""
        mock_get.return_value = self._mock_response(200, "A" * 600 + "coming soon")
        risultato = verifica_sito_attivo("https://esempio.it")
        self.assertFalse(risultato["attivo"])

    @patch("implementation.utils.website_checker.requests.get")
    def test_url_senza_schema_aggiunge_https(self, mock_get):
        """URL senza https:// → viene aggiunto automaticamente"""
        mock_get.return_value = self._mock_response(200, "A" * 600)
        verifica_sito_attivo("esempio.it")
        chiamata_url = mock_get.call_args[0][0]
        self.assertTrue(chiamata_url.startswith("https://"))

    # --- TEST 3: Servizio Esterno Down ---
    @patch("implementation.utils.website_checker.requests.get")
    def test_timeout_restituisce_errore(self, mock_get):
        """Timeout della connessione → attivo=False, errore='Timeout'"""
        import requests as req
        mock_get.side_effect = req.exceptions.Timeout()
        risultato = verifica_sito_attivo("https://esempio.it")
        self.assertFalse(risultato["attivo"])
        self.assertEqual(risultato["errore"], "Timeout")

    @patch("implementation.utils.website_checker.requests.get")
    def test_connessione_rifiutata_restituisce_errore(self, mock_get):
        """Connessione rifiutata → attivo=False, errore='Connessione rifiutata'"""
        import requests as req
        mock_get.side_effect = req.exceptions.ConnectionError()
        risultato = verifica_sito_attivo("https://esempio.it")
        self.assertFalse(risultato["attivo"])
        self.assertEqual(risultato["errore"], "Connessione rifiutata")

    @patch("implementation.utils.website_checker.requests.get")
    def test_http_404_restituisce_non_attivo(self, mock_get):
        """HTTP 404 → attivo=False"""
        mock_get.return_value = self._mock_response(404)
        risultato = verifica_sito_attivo("https://esempio.it")
        self.assertFalse(risultato["attivo"])


@unittest.skipUnless(DIPENDENZE_OK, SKIP_MSG)
class TestCalcolaFunnelScore(unittest.TestCase):

    HTML_FUNNEL_BUONO = """
    <html><body>
    <h1>Prenota una consulenza gratuita con il nostro team</h1>
    <form><input type="email" /><button>Contattaci ora</button></form>
    <p>⭐ Oltre 500 clienti soddisfatti — recensioni eccellenti</p>
    <p>Garanzia soddisfatti o rimborsati - Privacy Policy</p>
    <p>Chiamaci: 02 12345678</p>
    <script>fbq('init', '123');</script>
    <script>gtag('config', 'G-xxx');</script>
    </body></html>
    """ * 2  # Più caratteri per superare la soglia "vuoto"

    HTML_FUNNEL_SCARSO = "<html><body><p>Benvenuti.</p></body></html>" + "x" * 600

    # --- TEST 1: Happy Path ---
    @patch("implementation.utils.website_checker.requests.get")
    def test_funnel_buono_score_alto(self, mock_get):
        """Landing page con tutti gli elementi → score alto (>60)"""
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = self.HTML_FUNNEL_BUONO
        mock_resp.url = "https://esempio.it"
        mock_get.return_value = mock_resp

        risultato = calcola_funnel_score("https://esempio.it")
        self.assertGreater(risultato["score_finale"], 60)
        self.assertIsNone(risultato["errore"])

    # --- TEST 2: Funnel Scarso ---
    @patch("implementation.utils.website_checker.requests.get")
    def test_funnel_scarso_score_basso(self, mock_get):
        """Landing page senza elementi → score basso (<=60)"""
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = self.HTML_FUNNEL_SCARSO
        mock_resp.url = "https://esempio.it"
        mock_get.return_value = mock_resp

        risultato = calcola_funnel_score("https://esempio.it")
        self.assertLessEqual(risultato["score_finale"], 60)
        self.assertIn("breakdown_penalita", risultato)
        self.assertGreater(len(risultato["breakdown_penalita"]), 0)

    # --- TEST 3: Servizio Down ---
    @patch("implementation.utils.website_checker.requests.get")
    def test_pagina_irraggiungibile_score_zero(self, mock_get):
        """HTTP 500 → score=0, pagina marcata come irraggiungibile"""
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.text = ""
        mock_get.return_value = mock_resp

        risultato = calcola_funnel_score("https://esempio.it")
        self.assertEqual(risultato["score_finale"], 0)


@unittest.skipUnless(SHEETS_OK, "google-api-python-client non installato")
class TestIndiceALettera(unittest.TestCase):
    """Testa la conversione indice colonna → lettera Excel."""

    def test_converti_indici_corretti(self):
        from implementation.utils.sheets_client import SheetsClient
        # A=0, B=1, Z=25, AA=26
        self.assertEqual(SheetsClient._indice_a_lettera(0), "A")
        self.assertEqual(SheetsClient._indice_a_lettera(1), "B")
        self.assertEqual(SheetsClient._indice_a_lettera(25), "Z")
        self.assertEqual(SheetsClient._indice_a_lettera(26), "AA")
        self.assertEqual(SheetsClient._indice_a_lettera(27), "AB")
        self.assertEqual(SheetsClient._indice_a_lettera(51), "AZ")
        self.assertEqual(SheetsClient._indice_a_lettera(52), "BA")


if __name__ == "__main__":
    unittest.main(verbosity=2)
