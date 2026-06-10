"""
Test per implementation/utils/contact_extractor.py

Copre:
- Happy path: email e telefono trovati
- Input invalido: URL invalido, pagina senza contatti
- Servizio esterno down: timeout, errori connessione
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

from implementation.utils.contact_extractor import (
    estrai_email_da_html,
    estrai_telefono_da_html,
    estrai_contatti_business
)


class TestEstraiEmailDaHtml(unittest.TestCase):

    def _mock_response(self, status_code=200, text=""):
        mock_resp = MagicMock()
        mock_resp.status_code = status_code
        mock_resp.text = text
        return mock_resp

    # --- TEST 1: Happy Path ---
    @patch("implementation.utils.contact_extractor.requests.get")
    def test_estrai_email_valida(self, mock_get):
        """Pagina con email valida → email estratta"""
        mock_get.return_value = self._mock_response(200, "Contattaci: mario.rossi@example.com")
        risultato = estrai_email_da_html("https://esempio.it")
        self.assertIn("mario.rossi@example.com", risultato)

    @patch("implementation.utils.contact_extractor.requests.get")
    def test_esclude_email_di_sistema(self, mock_get):
        """Email generiche come noreply@ → escluse"""
        mock_get.return_value = self._mock_response(200, "noreply@azienda.it e info@miosito.it")
        risultato = estrai_email_da_html("https://esempio.it")
        # noreply@ deve essere esclusa
        self.assertNotIn("noreply@azienda.it", risultato)

    # --- TEST 2: Input Invalido ---
    @patch("implementation.utils.contact_extractor.requests.get")
    def test_pagina_senza_email_restituisce_lista_vuota(self, mock_get):
        """Pagina senza email → lista vuota"""
        mock_get.return_value = self._mock_response(200, "<html><body>Nessun contatto</body></html>")
        risultato = estrai_email_da_html("https://esempio.it")
        self.assertEqual(risultato, [])

    @patch("implementation.utils.contact_extractor.requests.get")
    def test_http_404_restituisce_lista_vuota(self, mock_get):
        """HTTP 404 → lista vuota, nessun crash"""
        mock_get.return_value = self._mock_response(404)
        risultato = estrai_email_da_html("https://esempio.it/404")
        self.assertEqual(risultato, [])

    # --- TEST 3: Servizio Down ---
    @patch("implementation.utils.contact_extractor.requests.get")
    def test_timeout_restituisce_lista_vuota(self, mock_get):
        """Timeout → lista vuota, nessun crash"""
        import requests as req
        mock_get.side_effect = req.exceptions.Timeout()
        risultato = estrai_email_da_html("https://esempio.it")
        self.assertEqual(risultato, [])


class TestEstraiTelefonoDaHtml(unittest.TestCase):

    def _mock_response(self, text="", status_code=200):
        mock_resp = MagicMock()
        mock_resp.status_code = status_code
        mock_resp.text = text
        return mock_resp

    # --- TEST 1: Happy Path ---
    def test_regex_telefono_italiano_trovata(self):
        """Il pattern regex PATTERN_TEL_IT trova numeri italiani standard"""
        import re
        from implementation.utils.contact_extractor import PATTERN_TEL_IT

        numeri_validi = [
            "+39 02 12345678",
            "0212345678",
            "+390212345678",
            "02 1234567",
            "333 1234567"
        ]
        for numero in numeri_validi:
            trovati = re.findall(PATTERN_TEL_IT, numero)
            self.assertTrue(len(trovati) > 0, f"Regex non ha trovato: {numero}")

    # --- TEST 2: Input Invalido ---
    @patch("implementation.utils.contact_extractor.requests.get")
    def test_nessun_telefono_restituisce_none(self, mock_get):
        """Pagina senza telefono → None"""
        mock_get.return_value = self._mock_response("<html><body>Solo testo</body></html>")
        risultato = estrai_telefono_da_html("https://esempio.it")
        self.assertIsNone(risultato)

    # --- TEST 3: Servizio Down ---
    @patch("implementation.utils.contact_extractor.requests.get")
    def test_connessione_fallita_restituisce_none(self, mock_get):
        """Errore connessione → None, nessun crash"""
        import requests as req
        mock_get.side_effect = req.exceptions.ConnectionError()
        risultato = estrai_telefono_da_html("https://esempio.it")
        self.assertIsNone(risultato)


class TestEstraiContattiBusiness(unittest.TestCase):

    # --- TEST 1: Happy Path ---
    @patch("implementation.utils.contact_extractor._scarica_pagina")
    @patch("implementation.utils.contact_extractor.estrai_telefono_da_html")
    @patch("implementation.utils.contact_extractor.estrai_email_da_html")
    def test_contatti_trovati_da_sito(self, mock_email, mock_tel, mock_scarica):
        """Contatti trovati dal sito web → dizionario completo"""
        mock_scarica.return_value = "<html><body>contenuto pagina</body></html>"
        mock_email.return_value = ["contatto@business.it"]
        mock_tel.return_value = "+39 02 9876543"

        risultato = estrai_contatti_business(
            nome_business="Test Business",
            url_sito="https://testbusiness.it"
        )
        self.assertEqual(risultato["email"], "contatto@business.it")
        self.assertEqual(risultato["telefono"], "+39 02 9876543")
        self.assertEqual(risultato["fonte_email"], "sito_home")

    # --- TEST 2: Nessun contatto ---
    @patch("implementation.utils.contact_extractor._scarica_pagina")
    @patch("implementation.utils.contact_extractor.estrai_telefono_da_html")
    @patch("implementation.utils.contact_extractor.estrai_email_da_html")
    def test_nessun_contatto_restituisce_none(self, mock_email, mock_tel, mock_scarica):
        """Nessun contatto trovato → None per email e telefono"""
        mock_scarica.return_value = "<html><body>niente</body></html>"
        mock_email.return_value = []
        mock_tel.return_value = None

        risultato = estrai_contatti_business(
            nome_business="Business Invisibile",
            url_sito="https://niente.it"
        )
        self.assertIsNone(risultato["email"])
        self.assertIsNone(risultato["telefono"])

    # --- TEST 3: Sito non raggiungibile ---
    @patch("implementation.utils.contact_extractor.estrai_telefono_da_html")
    @patch("implementation.utils.contact_extractor.estrai_email_da_html")
    def test_senza_url_sito_restituisce_dizionario_vuoto(self, mock_email, mock_tel):
        """Nessun URL sito → non chiama le funzioni di estrazione da sito"""
        risultato = estrai_contatti_business(
            nome_business="Business Senza Sito"
        )
        mock_email.assert_not_called()
        mock_tel.assert_not_called()
        self.assertIsNone(risultato["email"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
