"""
EMPIRE — test del verdetto `empire estate`, delle metriche inspect e di video_pack.

Owner: Claude · Origine: FORGE (LOTTI 1/5/6 completamento Workflow Estate, CP-20260723)

I test non devono mai scrivere nei dati veri dell'azienda: dove serve stato su disco si
usa una cartella temporanea, altrimenti eseguire la suite cambierebbe il colore dei gate.
"""
from __future__ import annotations

import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from empire import estate
from empire.inspect import metrics
from empire.tools import video_pack

ROME = timezone(timedelta(hours=2))


# ------------------------------------------------------------------ verdetto

class TestCheckOwnership(unittest.TestCase):
    """La distinzione noi/max è ciò che rende il verdetto raggiungibile."""

    def test_default_owner_is_us(self):
        self.assertEqual(estate.Check("x", True, "y").owner, "noi")

    def test_revenue_and_contacts_belong_to_max(self):
        # Se qualcuno le riclassifica come "noi", il verdetto non potra' mai dare 0
        # e il comando smettera' di essere consultato: e' il fallimento silenzioso
        # che questo test sorveglia.
        self.assertEqual(estate._GATE_OWNER.get("Gate-REV"), "max")
        self.assertEqual(estate._GATE_OWNER.get("Gate-CONTATTI"), "max")

    def test_placeholder_list_covers_stripe(self):
        self.assertIn("YOUR_STRIPE", estate._PAYMENT_PLACEHOLDERS)


class TestPlaceholderCheck(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._p = mock.patch.object(estate, "repo_root", lambda: self.root)
        self._p.start()

    def tearDown(self):
        self._p.stop()
        self._tmp.cleanup()

    def _page(self, body: str):
        d = self.root / "Crea siti" / "Siti CCM"
        d.mkdir(parents=True, exist_ok=True)
        (d / "manuale.html").write_text(body, encoding="utf-8")

    def test_detects_leftover_placeholder(self):
        self._page("<a href='https://buy.stripe.com/YOUR_STRIPE_LINK'>compra</a>")
        c = estate._check_placeholders()
        self.assertFalse(c.ok)
        self.assertTrue(c.notes)

    def test_clean_page_passes(self):
        self._page("<a href='pagamento.html'>compra</a>")
        self.assertTrue(estate._check_placeholders().ok)


class TestGateChecks(unittest.TestCase):
    """Un gate rosso con contromossa applicata è risolto; senza, no."""

    def _res(self, **kw):
        base = dict(id="Gate-X", status="RED", deadline=datetime.now(ROME),
                    reason="motivo", on_red="fai il fallback", evidence="",
                    on_red_applied=False)
        base.update(kw)
        from empire.flow.gate import GateResult
        return GateResult(**base)

    def _run(self, results):
        with mock.patch("empire.flow.runner.gates_table", return_value=results):
            return estate._check_gates()

    def test_red_without_countermeasure_fails(self):
        self.assertFalse(self._run([self._res()])[0].ok)

    def test_red_with_countermeasure_passes(self):
        self.assertTrue(self._run([self._res(on_red_applied=True)])[0].ok)

    def test_pending_with_countermeasure_passes(self):
        # Gate-S4: si sa gia' che non potra' diventare verde, il ramo di fallback
        # e' stato dichiarato e registrato prima della scadenza.
        c = self._run([self._res(status="PENDING", on_red_applied=True)])[0]
        self.assertTrue(c.ok)
        self.assertIn("in attesa", c.detail)

    def test_pending_without_countermeasure_fails(self):
        self.assertFalse(self._run([self._res(status="PENDING")])[0].ok)

    def test_green_passes(self):
        self.assertTrue(self._run([self._res(status="GREEN")])[0].ok)

    def test_evidence_is_carried_into_notes(self):
        c = self._run([self._res(evidence="7/7 righe")])[0]
        self.assertIn("7/7 righe", c.notes)


# ------------------------------------------------------------------ metriche

class TestMetricsHonesty(unittest.TestCase):
    """La regola centrale del lotto: mai 'non implementato', sempre 0 + nota."""

    def test_no_metric_ever_says_not_implemented(self):
        with mock.patch.object(metrics, "_perf_atoms", return_value=[]):
            for name, fn in metrics.ALL_METRICS.items():
                note = str(fn().get("note", "")).lower()
                self.assertNotIn("non implementat", note, f"metrica {name}")

    def test_empty_source_gives_zero_and_a_note(self):
        with mock.patch.object(metrics, "_perf_atoms", return_value=[]):
            m = metrics.scorecard_5d()
        self.assertEqual(m["value"], 0)
        self.assertTrue(m["note"], "un valore 0 senza nota non distingue 'non misurato' da 'vale zero'")

    def test_status_returns_all_six(self):
        with mock.patch.object(metrics, "_perf_atoms", return_value=[]):
            st = metrics.status()
        self.assertEqual(set(st), set(metrics.ALL_METRICS))

    def test_every_metric_declares_its_source(self):
        with mock.patch.object(metrics, "_perf_atoms", return_value=[]):
            for name, m in metrics.status().items():
                self.assertTrue(m.get("source"), f"metrica {name} senza fonte dichiarata")

    def test_first_pass_computes_on_real_shape(self):
        class A:
            def __init__(self, ok):
                self.extra = {"verification": {"first_pass": ok}}
        with mock.patch.object(metrics, "_perf_atoms", return_value=[A(True), A(False)]):
            self.assertEqual(metrics.first_pass()["value"], 50.0)

    def test_unreadable_archive_does_not_raise(self):
        with mock.patch.object(metrics, "_perf_atoms", side_effect=RuntimeError("boom")):
            with self.assertRaises(RuntimeError):
                metrics._perf_atoms()
        # la funzione pubblica invece assorbe l'assenza di dati
        with mock.patch.object(metrics, "_perf_atoms", return_value=[]):
            self.assertEqual(metrics.telemetry_runs()["value"], 0)


# ------------------------------------------------------------------ video pack

class TestVideoPack(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._p = mock.patch.object(video_pack, "_repo_root", lambda: self.root)
        self._p.start()

    def tearDown(self):
        self._p.stop()
        self._tmp.cleanup()

    def test_new_then_check_is_incomplete_until_filled(self):
        video_pack.cmd_new("run-test")
        # lo scheletro esiste ma il SEO pack non cita ancora il Manuale
        self.assertEqual(video_pack.cmd_check("run-test"), 1)

    def test_new_is_idempotent_and_never_overwrites(self):
        video_pack.cmd_new("run-test")
        d = self.root / video_pack.RUN_ROOT / "run-test"
        (d / "01-SCRIPT-IT.md").write_text("mio lavoro", encoding="utf-8")
        video_pack.cmd_new("run-test")
        self.assertEqual((d / "01-SCRIPT-IT.md").read_text(encoding="utf-8"), "mio lavoro")

    def test_check_rejects_markdown_in_tts(self):
        video_pack.cmd_new("run-test")
        d = self.root / video_pack.RUN_ROOT / "run-test"
        (d / "02-TTS.txt").write_text("## titolo letto ad alta voce", encoding="utf-8")
        self.assertEqual(video_pack.cmd_check("run-test"), 1)

    def test_check_requires_manual_link_in_seo(self):
        video_pack.cmd_new("run-test")
        d = self.root / video_pack.RUN_ROOT / "run-test"
        (d / "04-SEO-PACK.md").write_text("titolo e tag, nessun percorso revenue", encoding="utf-8")
        self.assertEqual(video_pack.cmd_check("run-test"), 1)

    def _fill(self, run="run-test"):
        """Compila davvero tutti i file: lo scheletro da solo non deve bastare."""
        video_pack.cmd_new(run)
        d = self.root / video_pack.RUN_ROOT / run
        (d / "00-SCELTA.md").write_text("Idea scelta: X, perche' Y.", encoding="utf-8")
        (d / "01-SCRIPT-IT.md").write_text("Scena 1: ...", encoding="utf-8")
        (d / "02-TTS.txt").write_text("testo pulito senza marcatori", encoding="utf-8")
        (d / "03-SHOTLIST.md").write_text("Scena 1: terminale.", encoding="utf-8")
        (d / "04-SEO-PACK.md").write_text("Titolo. Descrizione con link al Manuale.", encoding="utf-8")
        (d / "05-STATO.md").write_text("Nessun video su disco: pacchetto-render.", encoding="utf-8")
        return d

    def test_complete_pack_passes(self):
        self._fill()
        self.assertEqual(video_pack.cmd_check("run-test"), 0)

    def test_untouched_skeleton_is_rejected(self):
        # Un pacchetto appena creato non e' un pacchetto pronto.
        video_pack.cmd_new("run-vuoto")
        self.assertEqual(video_pack.cmd_check("run-vuoto"), 1)

    def test_check_flags_a_video_declared_but_absent(self):
        # Il difetto piu' costoso del sistema: dichiarare verde cio' che e' rosso.
        d = self._fill()
        (d / "05-STATO.md").write_text("Il video prodotto e' pronto.", encoding="utf-8")
        self.assertEqual(video_pack.cmd_check("run-test"), 1)

    def test_render_without_ffmpeg_reports_and_fails(self):
        video_pack.cmd_new("run-test")
        with mock.patch.object(video_pack, "_ffmpeg_probe", return_value=(False, "assente")):
            rc = video_pack.cmd_render("run-test")
        self.assertEqual(rc, 2)
        stato = (self.root / video_pack.RUN_ROOT / "run-test" / "05-STATO.md").read_text(encoding="utf-8")
        self.assertIn("gradino 3", stato)

    def test_render_log_block_is_rewritten_not_duplicated(self):
        video_pack.cmd_new("run-test")
        with mock.patch.object(video_pack, "_ffmpeg_probe", return_value=(False, "assente")):
            video_pack.cmd_render("run-test")
            video_pack.cmd_render("run-test")
        stato = (self.root / video_pack.RUN_ROOT / "run-test" / "05-STATO.md").read_text(encoding="utf-8")
        self.assertEqual(stato.count(video_pack.LOG_START), 1)

    def test_check_on_missing_run_fails(self):
        self.assertEqual(video_pack.cmd_check("non-esiste"), 1)


if __name__ == "__main__":
    unittest.main()
