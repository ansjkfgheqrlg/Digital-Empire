"""
empire.tests.test_dash — Test unitari per il modulo Dashboard e Metriche.

Owner: Max · Controllore: Claude · Origine: FORGE (GEM-05)
Governo: MANDATO Art.8 + ADR-008
"""
import unittest
import json
from pathlib import Path

from empire.paths import repo_root
from empire.dash.kpi import KPI
from empire.dash.collect import collect_all
from empire.dash.render_md import render_md
from empire.dash.render_html import render_html
from empire.dash.history import save_snapshot, get_history_trend


class TestDashboard(unittest.TestCase):
    def test_kpi_evaluation(self) -> None:
        """Verifica la corretta valutazione dello stato del KPI in base alle soglie."""
        # Un KPI con soglie
        kpi = KPI(
            id="test_kpi",
            label="Test KPI",
            source="manual",
            fmt="int",
            owner="TEST",
            good=">= 10",
            warn=">= 5",
            bad="< 5"
        )
        
        self.assertEqual(kpi.evaluate_status(12), "green")
        self.assertEqual(kpi.evaluate_status(7), "yellow")
        self.assertEqual(kpi.evaluate_status(3), "red")
        
        # Valori non disponibili
        self.assertEqual(kpi.evaluate_status(None), "gray")
        self.assertEqual(kpi.evaluate_status("n/d"), "gray")

    def test_collection_keys(self) -> None:
        """Verifica che il collettore raccolga tutti i KPI previsti dalla tassonomia."""
        data = collect_all()
        
        expected_keys = {
            "agenti_progettati",
            "agenti_cf_grade",
            "ecosistemi_completi",
            "artefatti_adr008",
            "link_rotti",
            "workflow_conformi",
            "spazio_sprecato",
            "runs_giornalieri",
            "scorecard_5d",
            "first_pass_rate",
            "ttd_medio",
            "tip_aperti",
            "traceability_rate",
            "anticipi_incassati",
            "decisioni_attive",
            "lead_concessionari",
            "gates_settimanali"
        }
        
        for key in expected_keys:
            self.assertIn(key, data)

    def test_renderers(self) -> None:
        """Verifica che i renderer MD e HTML scrivano correttamente i file su disco."""
        data = collect_all()
        
        # Test Markdown
        md_rel = render_md(data)
        md_path = repo_root() / md_rel
        self.assertTrue(md_path.exists())
        self.assertTrue(md_path.stat().st_size > 0)
        
        # Test HTML
        html_rel = render_html(data)
        html_path = repo_root() / html_rel
        self.assertTrue(html_path.exists())
        self.assertTrue(html_path.stat().st_size > 0)

    def test_history_snapshots(self) -> None:
        """Verifica il salvataggio degli snapshot storici e il caricamento del trend."""
        data = collect_all()
        
        # Salva snapshot
        snap_rel = save_snapshot(data)
        snap_path = repo_root() / snap_rel
        self.assertTrue(snap_path.exists())
        
        # Verifica contenuto snapshot
        with open(snap_path, "r", encoding="utf-8") as f:
            snap_data = json.load(f)
            
        self.assertIn("date", snap_data)
        self.assertIn("link_rotti", snap_data)
        
        # Verifica trend
        trend = get_history_trend(days=7)
        self.assertTrue(len(trend) >= 1)
        self.assertIn(snap_data["date"], trend)
