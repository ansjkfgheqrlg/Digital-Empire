"""
EMPIRE — test del misuratore di operativita' degli agenti (PEZZO 1, refinement APEX-7).

Owner: Claude · Origine: FORGE (CP-20260724)
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from empire import forge

DOCUMENTALE = "# Un agente\n\nFa delle cose utili per l'azienda.\n"

OPERATIVO = """---
Type: AGENT
---
# Agente Esempio
- **ID**: `test/esempio`

## Ruolo
Una sola responsabilita'.

## Input
| Fonte | Contenuto |
|---|---|
| lead.csv | i lead |

## Output
| Artefatto | Destinazione |
|---|---|
| esito | lead.csv |

## Criteri di successo
| G1 | soglia raggiunta |

## Procedura
1. **PRIMO** passo
2. **SECONDO** passo
"""


class _Tmp(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.root = Path(self._t.name)
        self._p = mock.patch.object(forge, "repo_root", lambda: self.root)
        self._p.start()

    def tearDown(self):
        self._p.stop()
        self._t.cleanup()

    def _scrivi(self, nome: str, testo: str) -> Path:
        p = self.root / nome
        p.write_text(testo, encoding="utf-8")
        return p


class TestMisura(_Tmp):
    def test_agente_documentale_prende_zero(self):
        s = forge.analizza(self._scrivi("vuoto.md", DOCUMENTALE))
        self.assertEqual(s.stato, "DOCUMENTALE")
        self.assertLess(s.punteggio, 6)

    def test_agente_completo_e_operativo(self):
        s = forge.analizza(self._scrivi("pieno.md", OPERATIVO))
        self.assertEqual(s.stato, "OPERATIVO")
        self.assertEqual(s.punteggio, 10.0)
        self.assertEqual(s.mancanti, [])

    def test_i_sei_criteri_sono_sempre_valutati(self):
        s = forge.analizza(self._scrivi("x.md", DOCUMENTALE))
        self.assertEqual(len(s.criteri), 6)
        self.assertEqual({c.nome for c in s.criteri}, set(forge.CRITERI))

    def test_ogni_criterio_passato_porta_una_prova(self):
        # Senza prova citata, un PASS e' un'opinione.
        s = forge.analizza(self._scrivi("pieno.md", OPERATIVO))
        for c in s.criteri:
            if c.passa:
                self.assertTrue(c.prova, f"{c.nome} passa ma non cita nulla")

    def test_file_illeggibile_non_esplode(self):
        s = forge.analizza(self.root / "non-esiste.md")
        self.assertEqual(s.punteggio, 0.0)

    def test_la_misura_non_modifica_il_file(self):
        p = self._scrivi("intatto.md", DOCUMENTALE)
        forge.analizza(p)
        self.assertEqual(p.read_text(encoding="utf-8"), DOCUMENTALE)


class TestGravita(_Tmp):
    """La gravita' ordina la checklist: mancare il comportamento pesa piu' dell'id."""

    def test_comportamento_pesa_piu_dell_identita(self):
        senza_c6 = OPERATIVO.replace("## Procedura", "## Note").replace(
            "1. **PRIMO** passo", "testo libero").replace("2. **SECONDO** passo", "altro testo")
        senza_c1 = OPERATIVO.replace("- **ID**: `test/esempio`", "nessun identificativo")
        g6 = forge.analizza(self._scrivi("a.md", senza_c6)).gravita
        g1 = forge.analizza(self._scrivi("b.md", senza_c1)).gravita
        self.assertGreater(g6, g1)

    def test_agente_perfetto_ha_gravita_zero(self):
        self.assertEqual(forge.analizza(self._scrivi("p.md", OPERATIVO)).gravita, 0)


class TestChecklist(_Tmp):
    def setUp(self):
        super().setUp()
        self._scrivi("rotto.md", DOCUMENTALE)
        self._scrivi("buono.md", OPERATIVO)
        self._files = mock.patch.object(
            forge, "_file_agenti",
            lambda: [self.root / "rotto.md", self.root / "buono.md"])
        self._files.start()

    def tearDown(self):
        self._files.stop()
        super().tearDown()

    def test_i_piu_gravi_stanno_in_cima(self):
        c = forge.checklist()
        self.assertEqual(c[0].id, "rotto")
        self.assertEqual(c[-1].id, "buono")

    def test_limite_rispettato(self):
        self.assertEqual(len(forge.checklist(limite=1)), 1)

    def test_salva_scrive_in_metrics(self):
        p = forge.salva_checklist(forge.checklist())
        self.assertTrue(p.exists())
        self.assertIn("metrics", str(p))


if __name__ == "__main__":
    unittest.main()
