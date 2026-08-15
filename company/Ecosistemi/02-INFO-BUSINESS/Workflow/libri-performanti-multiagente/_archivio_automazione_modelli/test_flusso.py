"""
Test del FLUSSO contro la specifica dei 4 step di Gael (2026-08-14).

Due regole della specifica erano scritte nei commenti ma non nel codice:

  STEP 0 — "NON si sceglie ogni volta: si sceglie una volta e ci si costruisce un catalogo;
            si cambia solo se ne esiste una nettamente migliore"
  STEP 3/4 — "genera SUBITO la copertina" e "mette TUTTO in libri_pronti/<Titolo>/"

La prima era violata da `nicchia-scegli`, che sovrascriveva la nicchia attiva in silenzio.
La seconda dal fatto che una copertina fallita faceva uscire il flusso con errore senza mai
arrivare allo STEP 4, buttando 24 capitoli gia' scritti.

Nessun test qui chiama un modello o la rete.

    python -m pytest tests/test_flusso.py -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import nicchia_attiva, workflow  # noqa: E402


@pytest.fixture
def stato_isolato(tmp_path, monkeypatch):
    """Ogni test lavora su un suo nicchia_attiva.json, mai su quello vero del catalogo."""
    monkeypatch.setattr(nicchia_attiva, "STATO_PATH", tmp_path / "nicchia_attiva.json")
    return tmp_path


# --------------------------------------------------------------------------- #
# STEP 0 — la nicchia si sceglie UNA VOLTA
# --------------------------------------------------------------------------- #

def test_prima_scelta_permessa(stato_isolato):
    n = nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    assert n.keyword == "small town romance suspense"
    assert nicchia_attiva.carica().keyword == "small town romance suspense"


def test_seconda_scelta_rifiutata(stato_isolato):
    """Il bug: bastava rilanciare 'nicchia-scegli' per perdere il catalogo."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    nicchia_attiva.registra_libro("The Quiet Hours")

    with pytest.raises(nicchia_attiva.NicchiaGiaScelta, match="gia' una nicchia attiva"):
        nicchia_attiva.imposta("cozy mystery cats", 99.0, "molto meglio")

    # e soprattutto: NON ha toccato niente
    n = nicchia_attiva.carica()
    assert n.keyword == "small town romance suspense"
    assert n.libri_pubblicati == ["The Quiet Hours"]


def test_cambio_rifiutato_senza_margine(stato_isolato):
    """Un vantaggio di pochi punti non ripaga il costo di abbandonare il catalogo."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    soglia = 77.7 + nicchia_attiva.MARGINE_PER_CAMBIARE

    with pytest.raises(nicchia_attiva.NicchiaGiaScelta, match="sotto la soglia"):
        nicchia_attiva.cambia("cozy mystery cats", soglia - 0.1, "di poco meglio")

    assert nicchia_attiva.carica().keyword == "small town romance suspense"


def test_cambio_accettato_col_margine_e_storia_conservata(stato_isolato):
    """Si cambia solo se e' NETTAMENTE migliore — e la nicchia lasciata non sparisce."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")
    nicchia_attiva.registra_libro("The Quiet Hours")
    nicchia_attiva.registra_libro("The Ninth Winter")

    nuova = nicchia_attiva.cambia("cozy mystery cats",
                                   77.7 + nicchia_attiva.MARGINE_PER_CAMBIARE,
                                   "nettamente meglio")

    assert nuova.keyword == "cozy mystery cats"
    assert nuova.libri_pubblicati == [], "il catalogo nuovo parte vuoto"

    assert len(nuova.storico) == 1
    lasciata = nuova.storico[0]
    assert lasciata["keyword"] == "small town romance suspense"
    assert lasciata["libri_pubblicati"] == ["The Quiet Hours", "The Ninth Winter"], (
        "i libri costruiti sulla nicchia precedente devono restare tracciati, altrimenti "
        "un cambio cancella la ragione per cui quel catalogo esisteva"
    )
    # ricaricando da disco la storia sopravvive
    assert nicchia_attiva.carica().storico[0]["keyword"] == "small town romance suspense"


def test_cambia_senza_nicchia_equivale_a_scegliere(stato_isolato):
    n = nicchia_attiva.cambia("small town romance suspense", 70.0, "prima volta")
    assert n.keyword == "small town romance suspense"
    assert n.storico == []


def test_cli_nicchia_scegli_non_sovrascrive(stato_isolato, capsys, monkeypatch):
    """Il comando non deve nemmeno partire: niente ricerche, niente sovrascrittura."""
    nicchia_attiva.imposta("small town romance suspense", 77.7, "motivo")

    def esplodi(*a, **k):
        raise AssertionError("non deve nemmeno cercare nicchie: ce n'e' gia' una attiva")

    from engine import niche_finder
    monkeypatch.setattr(niche_finder, "trova_nicchie", esplodi)

    rc = workflow.main(["nicchia-scegli", "--keywords", "cozy mystery cats"])

    assert rc == workflow.CONFIG_ERRATA
    assert "gia' una nicchia attiva" in capsys.readouterr().out
    assert nicchia_attiva.carica().keyword == "small town romance suspense"


# --------------------------------------------------------------------------- #
# STEP 3/4 — un libro scritto non si butta
# --------------------------------------------------------------------------- #

def _progetto_finto(tmp_path, monkeypatch, capitoli=2, scritti=(1, 2)):
    from engine import book_project

    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)
    p = book_project.BookProject.crea("Silence In Cedar Hollow", "small town romance suspense",
                                      capitoli=capitoli, parole_per_capitolo=100)
    p.outline_path.write_text("TITLE: Silence In Cedar Hollow\nACT1: qualcosa", encoding="utf-8")
    for n in scritti:
        p.path_capitolo(n).write_text("# Capitolo\n\n" + "parola " * 900, encoding="utf-8")
    return p


def test_copertina_fallita_non_perde_il_libro(tmp_path, monkeypatch, capsys):
    """Il difetto: STEP 3 rotto -> uscita con errore, STEP 4 mai raggiunto, capitoli buttati."""
    p = _progetto_finto(tmp_path, monkeypatch)

    monkeypatch.setattr(workflow, "step3_copertina",
                        lambda *a, **k: (_ for _ in ()).throw(RuntimeError("LM Arena giu'")))

    from datetime import datetime
    rc = workflow._step3_e_step4(p, "small town romance suspense", datetime.now())
    uscita = capsys.readouterr().out

    assert rc == workflow.ERRORE_SISTEMA
    # i capitoli devono essere ancora li'
    assert p.path_capitolo(1).exists() and p.path_capitolo(2).exists()
    # e il flusso deve dire come riprendere, non lasciare l'utente al buio
    assert "riprendi" in uscita and p.slug in uscita


class _SessioneFinta:
    """Sta in piedi al posto di una ArenaSession, senza aprire nessun browser."""

    def __init__(self):
        self.page = type("P", (), {"url": "https://arena.ai/c/finta",
                                    "goto": lambda self, *a, **k: None})()
        self.chiusa = False

    def close(self):
        self.chiusa = True


class _PlaywrightFinto:
    def start(self):
        return self

    def stop(self):
        pass


def _niente_browser(monkeypatch, tmp_path):
    """Sostituisce tutto cio' che aprirebbe un browser vero. Se un giorno `riprendi_libro`
    aggiunge un'altra chiamata di rete, questi test si piantano invece di passare in
    silenzio — e' voluto: un test che apre Chrome davvero non e' un test."""
    from engine import arena_book_writer, lmarena_client

    sessione = _SessioneFinta()
    monkeypatch.setattr("playwright.sync_api.sync_playwright", lambda: _PlaywrightFinto())
    monkeypatch.setattr(lmarena_client, "open_session", lambda *a, **k: sessione)
    monkeypatch.setattr(workflow, "_apri_staging_google_doc", lambda *a, **k: None)
    monkeypatch.setattr(workflow, "step2b_copy", lambda *a, **k: {})
    monkeypatch.setattr(workflow, "_step3_e_step4", lambda *a, **k: workflow.OK)

    chiamate = {}

    def finto_write_chapters(page, progetto, piano, **kw):
        chiamate.update(kw)

    monkeypatch.setattr(arena_book_writer, "write_chapters", finto_write_chapters)
    return sessione, chiamate


def test_riprendi_riparte_dal_capitolo_mancante(tmp_path, monkeypatch):
    """Riprendere deve costare solo il pezzo mancante: e' il senso della ripresa."""
    p = _progetto_finto(tmp_path, monkeypatch, capitoli=3, scritti=(1, 2))
    p.salva_piano({"title": "T", "characters": "C", "act1": "1", "act2": "2", "act3": "3",
                   "chapters": ["a", "b", "c"], "cover_prompt": "X"})
    contenuto_originale = p.path_capitolo(1).read_text(encoding="utf-8")

    sessione, chiamate = _niente_browser(monkeypatch, tmp_path)

    rc = workflow.riprendi_libro(p.slug)

    assert rc == workflow.OK
    assert chiamate.get("da_capitolo") == 3, (
        f"doveva ripartire dal capitolo 3, ha chiesto {chiamate.get('da_capitolo')}"
    )
    assert p.path_capitolo(1).read_text(encoding="utf-8") == contenuto_originale
    assert sessione.chiusa, "la sessione Arena va sempre chiusa, anche riprendendo"


def test_riprendi_senza_piano_non_apre_niente(tmp_path, monkeypatch, capsys):
    """Un libro iniziato con un flusso precedente non ha un piano: va detto, non tentato."""
    p = _progetto_finto(tmp_path, monkeypatch, capitoli=3, scritti=(1,))

    def esplodi(*a, **k):
        raise AssertionError("non deve aprire nessuna sessione senza un piano")

    from engine import lmarena_client
    monkeypatch.setattr(lmarena_client, "open_session", esplodi)

    rc = workflow.riprendi_libro(p.slug)

    assert rc == workflow.CONFIG_ERRATA
    assert "piano" in capsys.readouterr().out.lower()


def test_riprendi_libro_gia_completo_salta_la_scrittura(tmp_path, monkeypatch):
    """Se capitoli e copy ci sono gia', non si riapre Arena per niente: si va a copertina."""
    p = _progetto_finto(tmp_path, monkeypatch, capitoli=2, scritti=(1, 2))
    p.salva_piano({"title": "T", "characters": "C", "act1": "1", "act2": "2", "act3": "3",
                   "chapters": ["a", "b"], "cover_prompt": "X"})
    p.salva_copy({"titolo_finale": "T", "descrizione": "D", "keywords": ["k"]})

    from engine import lmarena_client

    def esplodi(*a, **k):
        raise AssertionError("non doveva aprire una sessione: non c'e' niente da scrivere")

    monkeypatch.setattr(lmarena_client, "open_session", esplodi)
    monkeypatch.setattr(workflow, "_step3_e_step4", lambda *a, **k: workflow.OK)

    assert workflow.riprendi_libro(p.slug) == workflow.OK


def test_riprendi_su_slug_inesistente_non_esplode(tmp_path, monkeypatch, capsys):
    from engine import book_project
    monkeypatch.setattr(book_project, "PROGETTI_DIR", tmp_path)

    rc = workflow.riprendi_libro("libro-che-non-esiste")

    assert rc == workflow.CONFIG_ERRATA
    assert "non trovato" in capsys.readouterr().out
