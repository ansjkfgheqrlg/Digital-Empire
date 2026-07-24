"""
EMPIRE — test delle 5 tracce (esecuzione del PIANO 2).

Owner: Claude · Origine: FORGE (CP-20260724)

I test scrivono in una cartella temporanea: eseguire la suite non deve mai inquinare le
tracce vere dell'azienda.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from empire import trace


class _Isolato(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._p = mock.patch.object(trace, "repo_root", lambda: self.root)
        self._p.start()

    def tearDown(self):
        self._p.stop()
        self._tmp.cleanup()


class TestRegoleNonNegoziabili(_Isolato):
    """Le due regole che rendono una traccia utile invece che decorativa."""

    def test_rifiuta_senza_autore(self):
        with self.assertRaises(ValueError) as e:
            trace.scrivi("decisione", "x", autore="  ", prova="p")
        self.assertIn("autore", str(e.exception))

    def test_rifiuta_senza_prova(self):
        # E' la regola gia' in vigore nei gate: senza evidenza e' solo una parola.
        with self.assertRaises(ValueError) as e:
            trace.scrivi("errore", "x", autore="Claude", prova="   ")
        self.assertIn("prova", str(e.exception))

    def test_rifiuta_tipo_sconosciuto(self):
        with self.assertRaises(ValueError):
            trace.scrivi("pippo", "x", autore="Claude", prova="p")


class TestScritturaELettura(_Isolato):
    def test_scrive_e_rilegge(self):
        trace.scrivi("decisione", "Prezzo del Manuale", autore="Max", prova="DEC-EST-001 attiva")
        letti = trace.leggi("decisione")
        self.assertEqual(len(letti), 1)
        self.assertEqual(letti[0].autore, "Max")
        self.assertEqual(letti[0].tipo, "decisione")

    def test_ogni_traccia_ha_data_e_id(self):
        trace.scrivi("lezione", "Una lezione", autore="Claude", prova="prova")
        t = trace.leggi("lezione")[0]
        self.assertTrue(t.quando)
        self.assertTrue(t.id.startswith("LEZ-"))

    def test_idempotente_nello_stesso_giorno(self):
        # Rilanciare un lavoro non deve moltiplicare le tracce.
        for _ in range(3):
            trace.scrivi("errore", "Stesso errore", autore="Claude", prova="p")
        self.assertEqual(len(trace.leggi("errore")), 1)

    def test_tipi_diversi_non_si_mescolano(self):
        trace.scrivi("decisione", "A", autore="Claude", prova="p")
        trace.scrivi("errore", "B", autore="Claude", prova="p")
        self.assertEqual(len(trace.leggi("decisione")), 1)
        self.assertEqual(len(trace.leggi("errore")), 1)

    def test_cartella_vuota_non_esplode(self):
        self.assertEqual(trace.leggi("sessione"), [])

    def test_file_corrotto_non_nasconde_gli_altri(self):
        trace.scrivi("decisione", "Buona", autore="Claude", prova="p")
        (trace.cartella_per("decisione") / "rotto.json").write_text("{non json", encoding="utf-8")
        self.assertEqual(len(trace.leggi("decisione")), 1)


class TestRicerca(_Isolato):
    """Una traccia che nessuno sa ritrovare e' peso morto (Piano 5)."""

    def setUp(self):
        super().setUp()
        trace.scrivi("decisione", "Prezzo Manuale a 67 euro", autore="Max",
                     prova="DEC-EST-001", tags=["prezzo"])
        trace.scrivi("errore", "Checkout con placeholder Stripe", autore="Claude",
                     prova="YOUR_STRIPE in manuale.html", tags=["cassa"])

    def test_trova_per_titolo(self):
        self.assertEqual(len(trace.cerca("67 euro")), 1)

    def test_cerca_anche_dentro_la_prova_non_solo_il_titolo(self):
        # "manuale" compare nel titolo della decisione E dentro la prova dell'errore
        # ("manuale.html"): trovarle entrambe e' corretto, non un falso positivo.
        # E' il comportamento che serve alla domanda "ho gia' sbagliato cosi'?".
        self.assertEqual(len(trace.cerca("manuale")), 2)

    def test_trova_per_prova(self):
        self.assertEqual(len(trace.cerca("YOUR_STRIPE")), 1)

    def test_trova_per_tag(self):
        self.assertEqual(len(trace.cerca("cassa")), 1)

    def test_filtra_per_tipo(self):
        self.assertEqual(len(trace.cerca("e", tipo="errore")), 1)

    def test_nessun_risultato_non_esplode(self):
        self.assertEqual(trace.cerca("parola-che-non-esiste"), [])


class TestConteggio(_Isolato):
    def test_conta_tutti_i_tipi(self):
        c = trace.conta()
        self.assertEqual(set(c), set(trace.TIPI))
        self.assertEqual(sum(c.values()), 0)

    def test_conta_dopo_scrittura(self):
        trace.scrivi("prestazione", "Fase chiusa", autore="Claude", prova="exit 0")
        self.assertEqual(trace.conta()["prestazione"], 1)

    def test_le_cinque_cartelle_sono_quelle_gia_esistenti(self):
        # Vincolo additivo: non si crea struttura nuova, si usano le cartelle vuote.
        attese = {"decisions", "errors", "performances", "reasoning-bank", "sessions"}
        self.assertEqual(set(trace.TIPI.values()), attese)


if __name__ == "__main__":
    unittest.main()
