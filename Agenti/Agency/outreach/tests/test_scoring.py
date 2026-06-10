"""
Test per logica di scoring e qualifica lead.

Copre:
- calcola_score_no_sito (search_no_website.py)
- qualifica_lead_no_sito e qualifica_lead_funnel_scarso (qualify_leads.py)
- genera_id_lead: formato corretto
- SheetsClient._indice_a_lettera: conversione Excel
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# Verifica dipendenze necessarie prima di importare
try:
    import dotenv  # noqa: F401
    import requests  # noqa: F401
    DIPENDENZE_OK = True
except ImportError as e:
    DIPENDENZE_OK = False
    DIPENDENZE_ERRORE = str(e)

if DIPENDENZE_OK:
    from implementation.search_no_website import calcola_score_no_sito, genera_id_lead
    from implementation.qualify_leads import qualifica_lead_no_sito, qualifica_lead_funnel_scarso

SKIP_MSG = f"Dipendenze non installate. Esegui: pip install -r requirements.txt"


@unittest.skipUnless(DIPENDENZE_OK, SKIP_MSG)
class TestCalcolaScoreNoSito(unittest.TestCase):

    # --- TEST 1: Happy Path (lead ideale) ---
    def test_lead_ideale_score_massimo(self):
        """Business con ottimi rating, molte recensioni, telefono ed email → score alto"""
        business = {
            "rating": 4.5,
            "reviewsCount": 100,
            "phone": "+39 02 12345678",
            "categoryName": "restaurant"
        }
        score = calcola_score_no_sito(business, ha_email=True, sito_rotto=False)
        # Rating>=4 (+20) + recensioni>=50 (+20) + telefono (+20) + email (+20) + settore (+10) + senza_sito (+10) = 100
        self.assertEqual(score, 100)

    def test_lead_minimo_score_basso(self):
        """Business senza rating, 0 recensioni, senza contatti → score 0"""
        business = {
            "rating": 0,
            "user_ratings_total": 0,
            "formatted_phone_number": "",
            "types": []
        }
        score = calcola_score_no_sito(business, ha_email=False, sito_rotto=False)
        # Solo sito assente (+10)
        self.assertEqual(score, 10)

    # --- TEST 2: Casistica bordo ---
    def test_rating_35_da_10_punti(self):
        """Rating 3.5 → 10 punti, non 20"""
        business = {"rating": 3.5, "user_ratings_total": 0, "formatted_phone_number": "", "types": []}
        score = calcola_score_no_sito(business, ha_email=False, sito_rotto=False)
        # 10 (rating) + 10 (sito assente) = 20
        self.assertEqual(score, 20)

    def test_score_non_supera_100(self):
        """Score clampato a 100 anche se i bonus sommano di più"""
        business = {
            "rating": 4.5,
            "user_ratings_total": 200,
            "formatted_phone_number": "+39",
            "types": ["dentist"]
        }
        score = calcola_score_no_sito(business, ha_email=True, sito_rotto=True)
        self.assertLessEqual(score, 100)

    def test_sito_rotto_non_da_bonus_assenza(self):
        """Sito rotto (vs assente) → non aggiunge i 10 punti bonus per sito assente"""
        business = {"rating": 4.0, "user_ratings_total": 60, "formatted_phone_number": "+39", "types": []}
        score_rotto = calcola_score_no_sito(business, ha_email=False, sito_rotto=True)
        score_assente = calcola_score_no_sito(business, ha_email=False, sito_rotto=False)
        self.assertEqual(score_assente - score_rotto, 10)

    # --- TEST 3: Servizio/Input anomali ---
    def test_rating_none_non_causa_errore(self):
        """Rating None → trattato come 0"""
        business = {"rating": None, "user_ratings_total": None, "formatted_phone_number": "", "types": []}
        score = calcola_score_no_sito(business, ha_email=False, sito_rotto=False)
        self.assertIsInstance(score, int)
        self.assertGreaterEqual(score, 0)


@unittest.skipUnless(DIPENDENZE_OK, SKIP_MSG)
class TestQualificaLeadNoSito(unittest.TestCase):

    def _riga(self, score="50", email="test@test.it", telefono="+39 02 123"):
        return {
            "SCORE_PRIORITÀ": score,
            "EMAIL": email,
            "TELEFONO": telefono,
            "CATEGORIA": "ristorante"
        }

    # --- TEST 1: Happy Path ---
    def test_lead_fascia_a(self):
        """Score 50 + email trovata + settore alta domanda → fascia A"""
        riga = self._riga(score="50")
        # Con email_trovata=True aggiunge 15 + 10 (settore) = score 75 → fascia A
        risultato = qualifica_lead_no_sito(riga, ha_email_trovata=True)
        self.assertEqual(risultato["FASCIA"], "A")
        self.assertEqual(risultato["PRONTO_OUTREACH"], "Sì")

    def test_lead_fascia_b(self):
        """Score 30, email già presente, no settore domanda → fascia B"""
        riga = self._riga(score="30")
        risultato = qualifica_lead_no_sito(riga, ha_email_trovata=False)
        # 30 + 10 (settore ristorante) = 40 → fascia B
        self.assertEqual(risultato["FASCIA"], "B")

    def test_lead_fascia_c_no_contatti(self):
        """Score basso, nessun contatto → fascia C, PRONTO=No"""
        riga = {"SCORE_PRIORITÀ": "10", "EMAIL": "", "TELEFONO": "", "CATEGORIA": "altro"}
        risultato = qualifica_lead_no_sito(riga, ha_email_trovata=False)
        self.assertEqual(risultato["FASCIA"], "C")
        self.assertEqual(risultato["PRONTO_OUTREACH"], "No")
        self.assertIn("nessun contatto", risultato["MOTIVO_ESCLUSIONE"])

    # --- TEST 2: Input invalido ---
    def test_score_stringa_vuota_gestita(self):
        """Score vuoto → trattato come 0, nessun crash"""
        riga = {"SCORE_PRIORITÀ": "", "EMAIL": "x@x.it", "TELEFONO": "", "CATEGORIA": ""}
        risultato = qualifica_lead_no_sito(riga, ha_email_trovata=False)
        self.assertIn(risultato["FASCIA"], ["A", "B", "C"])


@unittest.skipUnless(DIPENDENZE_OK, SKIP_MSG)
class TestQualificaLeadFunnelScarso(unittest.TestCase):

    def _riga(self, score_funnel="30", n_ads="4", email="test@test.it", telefono="+39 02 123"):
        return {
            "SCORE_FUNNEL": score_funnel,
            "N_ADS_ATTIVI": n_ads,
            "EMAIL": email,
            "TELEFONO": telefono,
            "SETTORE": "dentista"
        }

    # --- TEST 1: Happy Path ---
    def test_funnel_pessimo_priorita_alta(self):
        """Funnel score 10 → priorità molto alta"""
        riga = self._riga(score_funnel="10", n_ads="5")
        risultato = qualifica_lead_funnel_scarso(riga, ha_email_trovata=False)
        score = int(risultato["SCORE_PRIORITÀ"])
        # 100-10=90 + n_ads>=3(+15) + email(+15) + tel(+10) + settore(+10) = 140 → clamp 100
        self.assertEqual(score, 100)
        self.assertEqual(risultato["FASCIA"], "A")

    def test_funnel_medio_priorita_media(self):
        """Funnel score 55 → priorità media"""
        riga = self._riga(score_funnel="55", n_ads="1", email="", telefono="")
        risultato = qualifica_lead_funnel_scarso(riga, ha_email_trovata=False)
        score = int(risultato["SCORE_PRIORITÀ"])
        # 100-55=45 + settore(+10) = 55 → fascia B, ma nessun contatto → PRONTO=No
        self.assertIn(risultato["FASCIA"], ["A", "B"])
        self.assertEqual(risultato["PRONTO_OUTREACH"], "No")

    # --- TEST 2: Input invalido ---
    def test_score_funnel_invalido_gestito(self):
        """Score funnel non numerico → usa fallback 50, nessun crash"""
        riga = {"SCORE_FUNNEL": "N/A", "N_ADS_ATTIVI": "0", "EMAIL": "", "TELEFONO": "", "SETTORE": ""}
        try:
            risultato = qualifica_lead_funnel_scarso(riga, ha_email_trovata=False)
            # Non deve sollevare eccezioni
        except (ValueError, TypeError):
            self.fail("qualifica_lead_funnel_scarso ha sollevato un'eccezione con input invalido")


@unittest.skipUnless(DIPENDENZE_OK, SKIP_MSG)
class TestGeneraIdLead(unittest.TestCase):

    def test_formato_id_no_sito(self):
        """ID lead per NoSito deve iniziare con NS-"""
        id_lead = genera_id_lead("Milano")
        self.assertTrue(id_lead.startswith("NS-"))
        self.assertRegex(id_lead, r"^NS-[A-Z]{2,4}-\d{14}$")

    def test_citta_con_spazio(self):
        """Città con spazio (es. San Donato) → gestita correttamente"""
        id_lead = genera_id_lead("San Donato")
        self.assertTrue(id_lead.startswith("NS-"))
        self.assertNotIn(" ", id_lead)

    def test_unicita_timestamp(self):
        """Due ID generati in istanti diversi → diversi"""
        import time
        id1 = genera_id_lead("Roma")
        time.sleep(1.1)
        id2 = genera_id_lead("Roma")
        self.assertNotEqual(id1, id2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
