"""
Test del flusso automatico (2026-08-30).

Scritti contro la lezione 2 dell'archivio: *"un test che non guarda il prompt non testa la
scrittura"*. I test del vecchio tentativo usavano un invio finto che IGNORAVA il prompt, ed
e' per questo che nessuno si e' accorto per settimane che il capitolo 1 veniva istruito male.
Qui `ScrittoreFinto` conserva ogni prompt inviato e i test affermano su quelli.
"""
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine import auto, config  # noqa: E402
from engine.book_project import BookProject  # noqa: E402
from engine.scrittore import (Budget, BudgetSuperato, Esito,  # noqa: E402
                              ScrittoreClaudeCLI, ScrittoreFinto)

# Dimensioni REALI: il gate confronta con il minimo globale del libro
# (config.TARGET_WORD_COUNT_MIN, 36.800 parole), non con una soglia per capitolo. Un
# libro-giocattolo da 4 capitoli non puo' passare il gate per costruzione, quindi
# testarlo cosi' misurerebbe una cosa che nella vita vera non succede mai.
CAPITOLI = 24
PER_BLOCCO = 4
PAROLE = 1600
PAROLE_CORTE = 900          # sopra le 50 (soglia "capitolo esistente"), sotto il bersaglio


def _piano(capitoli=CAPITOLI):
    return {
        "titolo": "The Glass Orchard",
        "autore": "Nora Vale",
        "premessa": "Una donna torna al frutteto di famiglia.",
        "ambientazione": "Vermont, autunno.",
        "personaggi": [{"nome": "Iris", "ruolo": "protagonista",
                        "voluto": "vendere la casa", "segreto": "non vuole andarsene"}],
        "atti": ["a1", "a2", "a3"],
        "capitoli": [{"n": i, "titolo": "Cap %d" % i, "cosa_succede": "Iris fa qualcosa."}
                     for i in range(1, capitoli + 1)],
        "prompt_copertina": "An orchard at dusk",
    }


def _copy():
    return {"titolo": "The Glass Orchard", "sottotitolo": "A quiet reckoning",
            "descrizione": "d " * 200, "keyword": ["a", "b", "c", "d", "e", "f", "g"],
            "categorie": ["Fiction", "Literary"]}


_VOCAB = ("orchard lantern frost hollow ledger quiet ribbon amber thistle harbor "
          "gable cinder willow marrow tallow bracken cobalt vellum sorrel plinth "
          "kettle pewter almond furrow crescent bramble hinge lattice pollen shale").split()


def _prosa(n_parole: int, seme: int) -> str:
    """Testo finto ma che PASSA i validatori veri: parole varie (niente falso positivo di
    ripetizione), frasi chiuse col punto (niente falso troncamento), zero lineette lunghe."""
    import random
    r = random.Random(seme)
    parole, frasi = [], []
    while len(parole) < n_parole:
        lung = r.randint(8, 16)
        frase = [r.choice(_VOCAB) for _ in range(lung)]
        frase[0] = frase[0].capitalize()
        frasi.append(" ".join(frase) + ".")
        parole += frase
    return " ".join(frasi)


class ScrittoreCopione(ScrittoreFinto):
    """Finto ma coerente col protocollo: outline JSON, blocchi nel formato === CAP N ===."""

    def __init__(self, parole=PAROLE, **kw):
        super().__init__(parole_per_risposta=parole, **kw)
        self.parole = parole

    def genera(self, prompt, etichetta=""):
        self.prompt_ricevuti.append(prompt)
        if "prompt_copertina" in prompt:                       # outline
            return Esito(ok=True, testo=json.dumps(_piano()), prompt=prompt, parole=50)
        if "keyword" in prompt and "descrizione" in prompt:    # copy
            return Esito(ok=True, testo=json.dumps(_copy()), prompt=prompt, parole=50)
        nums = [int(n) for n in re.findall(r"cap (\d+) —", prompt)]
        pezzi = []
        for n in nums:
            pezzi.append("=== CAP %d ===\n# Cap %d\n%s"
                         % (n, n, _prosa(self.parole, seme=n)))
        pezzi.append("=== RIASSUNTI ===")
        pezzi += ["### cap %02d\nSuccede qualcosa." % n for n in nums]
        return Esito(ok=True, testo="\n\n".join(pezzi), prompt=prompt,
                     parole=self.parole * len(nums))


@pytest.fixture
def libri(tmp_path, monkeypatch):
    """Isola LIBRI/ in una cartella temporanea: i test non toccano i libri veri.

    Non basta rattoppare `config.LIBRI_DIR`: `book_project.PROGETTI_DIR` e' calcolato
    all'import e resta quello vecchio. Prima versione di questo fixture -> il primo test
    ha creato 'the-glass-orchard' DENTRO i libri veri (2026-08-30, rimosso a mano).
    Si rattoppa la costante di ogni modulo che se l'e' copiata.
    """
    from engine import book_project, metriche as _metriche

    d = tmp_path / "LIBRI"
    lavorazione = d / "in_lavorazione"
    lavorazione.mkdir(parents=True)
    (d / "libri_pronti").mkdir(parents=True)

    monkeypatch.setattr(config, "LIBRI_DIR", d, raising=False)
    monkeypatch.setattr(config, "LIBRI_PRONTI_DIR", d / "libri_pronti", raising=False)
    monkeypatch.setattr(book_project, "PROGETTI_DIR", lavorazione, raising=False)
    monkeypatch.setattr(_metriche, "_percorso",
                        lambda slug: lavorazione / slug / _metriche.NOME_FILE)
    return d


def test_il_fixture_isola_davvero(libri):
    """Se questo cade, ogni altro test qui sotto sta scrivendo nei libri VERI."""
    from engine import book_project
    assert str(libri) in str(book_project.PROGETTI_DIR)


# ------------------------------------------------------------------ il prompt
def test_il_primo_blocco_dice_che_e_l_inizio_non_il_segnaposto(libri):
    """Il bug del 2026-08-15: il capitolo 1 riceveva l'intestazione di riassunti.md come
    se fosse trama gia' avvenuta. Il prompt del primo blocco deve dire l'opposto."""
    s = ScrittoreCopione()
    auto.produci("un frutteto", nicchia="literary", capitoli=CAPITOLI,
                 parole_per_capitolo=PAROLE, per_blocco=PER_BLOCCO, scrittore=s)
    primo_blocco = next(p for p in s.prompt_ricevuti if "=== CAP 1 ===" in p)
    assert "QUESTO E' L'INIZIO DEL LIBRO" in primo_blocco
    assert "Riassunti progressivi" not in primo_blocco
    assert "<!--" not in primo_blocco


def test_il_secondo_blocco_riceve_quello_che_e_gia_successo(libri):
    s = ScrittoreCopione()
    auto.produci("un frutteto", nicchia="literary", capitoli=CAPITOLI,
                 parole_per_capitolo=PAROLE, per_blocco=PER_BLOCCO, scrittore=s)
    # Il prompt mostra il formato solo per {da} e {da+1}: con blocchi da 4, il secondo
    # blocco (5-8) si riconosce da "=== CAP 5 ===".
    secondo = next(p for p in s.prompt_ricevuti if "=== CAP %d ===" % (PER_BLOCCO + 1) in p)
    assert "QUELLO CHE E' GIA' SUCCESSO" in secondo
    assert "Succede qualcosa" in secondo, "il riassunto reale non e' arrivato nel prompt"


def test_il_prompt_vieta_le_lineette_e_chiede_la_lunghezza(libri):
    s = ScrittoreCopione()
    auto.produci("un frutteto", nicchia="literary", capitoli=CAPITOLI,
                 parole_per_capitolo=PAROLE, per_blocco=PER_BLOCCO, scrittore=s)
    blocco = next(p for p in s.prompt_ricevuti if "=== CAP 1 ===" in p)
    assert "lineette lunghe" in blocco
    assert "ALMENO %d parole" % PAROLE in blocco


# ------------------------------------------------------------------ il flusso
def test_produce_un_libro_completo(libri):
    s = ScrittoreCopione()
    e = auto.produci("un frutteto", nicchia="literary", capitoli=CAPITOLI,
                     parole_per_capitolo=PAROLE, per_blocco=PER_BLOCCO, scrittore=s)
    assert e.ok, "%s: %s" % (e.fase_fallita, e.errore)
    assert e.capitoli_scritti == CAPITOLI
    p = BookProject(e.slug)
    assert p.stato().completo
    assert p.copy_kdp() is not None, "il copy non e' stato salvato"
    assert not e.pubblicabile, "senza immagine di copertina non deve dirsi caricabile su KDP"
    assert Path(e.cartella).exists(), "la cartella del pacchetto non esiste"


def test_il_gate_bocciato_fa_riscrivere_il_blocco_non_proseguire(libri):
    """Capitoli troppo corti -> il gate boccia -> si riscrive QUEL blocco."""
    s = ScrittoreCopione(parole=PAROLE_CORTE)   # sotto il bersaglio: il gate deve bocciare
    e = auto.produci("un frutteto", nicchia="literary", capitoli=CAPITOLI,
                     parole_per_capitolo=PAROLE, per_blocco=PER_BLOCCO, scrittore=s)
    assert not e.ok, "un libro con capitoli da 20 parole non deve passare"
    assert e.fase_fallita.startswith("capitoli 1-")
    assert e.riscritture >= auto.TENTATIVI_PER_BLOCCO
    riscrittura = [p for p in s.prompt_ricevuti if "HA BOCCIATO LA VERSIONE PRECEDENTE" in p]
    assert riscrittura, "la riscrittura non dice al modello cosa correggere"
    assert "sotto il minimo" in riscrittura[0]


def test_una_risposta_a_meta_non_viene_salvata(libri):
    """Se mancano capitoli nel blocco, si richiede tutto: mai salvare mezzo blocco."""
    errore = auto._spezza_blocco("=== CAP 1 ===\ntesto", da=1, a=2)
    assert isinstance(errore, str)
    assert "mancano i capitoli [2]" in errore


def test_senza_marcatori_lo_dice(libri):
    errore = auto._spezza_blocco("qui c'e' solo prosa senza formato", da=1, a=2)
    assert isinstance(errore, str) and "=== CAP N ===" in errore


# ------------------------------------------------------------------ il budget
def test_il_budget_ferma_il_flusso_e_salva():
    b = Budget(limite_usd=1.0, speso_usd=1.0)
    with pytest.raises(BudgetSuperato):
        b.verifica()


def test_budget_zero_significa_nessun_tetto():
    Budget(limite_usd=0.0, speso_usd=999.0).verifica()      # non solleva


# ------------------------------------- il guasto del 13 agosto (modello sbagliato)
def test_rileva_il_modello_sbagliato():
    s = ScrittoreClaudeCLI(modello="claude-sonnet-5", budget=Budget(0))
    esito = s._verifica({"result": "parola " * 100, "total_cost_usd": 0.1,
                         "modelUsage": {"claude-sonnet-4-6": {}}}, "p")
    assert not esito.ok
    assert "13 agosto" in esito.errore


def test_il_modello_accessorio_non_fa_fallire():
    """Il CLI usa sempre un modello piccolo per lavoro suo: non e' un errore."""
    s = ScrittoreClaudeCLI(modello="claude-sonnet-5", budget=Budget(0))
    esito = s._verifica({"result": "parola " * 100, "total_cost_usd": 0.1,
                         "modelUsage": {"claude-haiku-4-5-20251001": {},
                                        "claude-sonnet-5": {}}}, "p")
    assert esito.ok


def test_risposta_troppo_corta_non_e_un_successo():
    """Lezione 1: un successo dichiarato non e' un successo."""
    s = ScrittoreClaudeCLI(modello="claude-sonnet-5", budget=Budget(0))
    esito = s._verifica({"result": "Non posso aiutarti.", "total_cost_usd": 0.01,
                         "modelUsage": {"claude-sonnet-5": {}}}, "p")
    assert not esito.ok and "troppo corta" in esito.errore


def test_is_error_non_passa():
    s = ScrittoreClaudeCLI(modello="claude-sonnet-5", budget=Budget(0))
    esito = s._verifica({"result": "x" * 500, "is_error": True,
                         "modelUsage": {"claude-sonnet-5": {}}}, "p")
    assert not esito.ok


def test_l_argomento_dal_magazzino_e_testo_non_un_repr(libri, monkeypatch):
    """Al primo run reale (2026-08-30) il magazzino passava al modello il repr della
    dataclass — "Argomento(nicchia='...', titolo_lavoro=...)" — invece del tema. Il libro
    sarebbe nato da una riga di Python."""
    from engine import magazzino

    arg = magazzino.Argomento(nicchia="cozy mystery", titolo_lavoro="A Death in the Drawer",
                              premessa="Una pasticcera trova un corpo.", dati_amazon={})
    monkeypatch.setattr(magazzino, "prendi", lambda: arg)
    monkeypatch.setattr(magazzino, "collega_libro", lambda *a, **k: None)

    s = ScrittoreCopione()
    auto.produci(None, capitoli=CAPITOLI, parole_per_capitolo=PAROLE,
                 per_blocco=PER_BLOCCO, scrittore=s)
    outline = s.prompt_ricevuti[0]
    assert "A Death in the Drawer" in outline
    assert "Una pasticcera trova un corpo" in outline
    assert "Argomento(" not in outline, "e' finito il repr della dataclass nel prompt"


# --------------------------------------------------------------------------- #
# FIX-6 / KDP-SCOUT (2026-09-02): il magazzino si rifornisce da solo
# --------------------------------------------------------------------------- #
class TestScout:
    """Ordine di Gael: 'gli argomenti settimanali li devi trovare in autonomia ogni
    settimana'. Il punto delicato e' che i numeri devono essere MISURATI, mai inventati."""

    class _Valutazione:
        def __init__(self, keyword, punteggio):
            self.keyword, self.punteggio = keyword, punteggio
            self.recensioni_mediana, self.prezzo_medio = 60.0, 11.0
            self.concorrenti_deboli, self.n_risultati = 7, 16

    def _scrittore(self, keywords, idee):
        class S(ScrittoreFinto):
            def genera(s, prompt, etichetta=""):
                s.prompt_ricevuti.append(prompt)
                testo = json.dumps(keywords if "SOTTO-NICCHIA" in prompt or
                                   "keyword di SOTTO-NICCHIA" in prompt else idee)
                return Esito(ok=True, testo=testo, prompt=prompt, parole=50)
        return S()

    def test_scarta_le_keyword_sotto_il_punteggio_minimo(self, monkeypatch, tmp_path):
        from engine import magazzino, niche_finder, scout
        monkeypatch.setattr(magazzino, "MAGAZZINO_PATH", tmp_path / "m.json", raising=False)
        monkeypatch.setattr(niche_finder, "trova_nicchie", lambda *a, **k: [
            self._Valutazione("witch bookshop cozy", 82.0),
            self._Valutazione("nicchia morta", 10.0),
        ])
        s = self._scrittore(["witch bookshop cozy", "nicchia morta"], [])
        e = scout.rifornisci(quante=5, nicchia="witch bookshop cozy fantasy",
                             dry_run=True, scrittore=s)
        assert e.keyword_promosse == 1, "la nicchia a 10/100 non deve passare"
        assert any("sotto il minimo" in x for x in e.scartati)

    def test_i_dati_amazon_sono_quelli_MISURATI_e_portano_la_data(self, monkeypatch, tmp_path):
        from engine import magazzino, niche_finder, scout
        monkeypatch.setattr(magazzino, "MAGAZZINO_PATH", tmp_path / "m.json", raising=False)
        monkeypatch.setattr(niche_finder, "trova_nicchie", lambda *a, **k: [
            self._Valutazione("witch bookshop cozy", 82.0)])
        idee = [{"keyword": "witch bookshop cozy", "titolo_lavoro": "The Ledger",
                 "premessa": "Una witch eredita una bookshop e trova un mystery."}]
        s = self._scrittore(["witch bookshop cozy"], idee)
        e = scout.rifornisci(quante=5, dry_run=True, nicchia="witch bookshop cozy fantasy",
                             scrittore=s)
        assert e.inseriti, "nessun argomento prodotto"
        dati = e.inseriti[0].dati_amazon
        assert dati["punteggio"] == 82.0, "il punteggio non e' quello misurato"
        assert dati["misurato_il"], "manca la data: i numeri vecchi hanno gia' fatto danni"

    def test_senza_nicchia_attiva_lo_dice_invece_di_inventarla(self, monkeypatch, tmp_path):
        from engine import nicchia_attiva, scout
        monkeypatch.setattr(nicchia_attiva, "carica", lambda: None)
        e = scout.rifornisci(scrittore=ScrittoreFinto())
        assert not e.inseriti and "nessuna nicchia attiva" in e.errore


# --------------------------------------------------------------------------- #
# TASK-KDP-PIANO-W2 (2026-09-02): piano editoriale, KDP-GATE, libro del giorno
# --------------------------------------------------------------------------- #
def _riga(giorno=1, **over):
    r = {
        "giorno": giorno, "data_produzione": "2026-09-02",
        "nicchia": "witch bookshop cozy", "punteggio_nicchia": 82.0,
        "dati_amazon": {"punteggio": 82.0, "recensioni_mediana": 60,
                        "prezzo_medio": 11.0, "concorrenti_deboli": 7,
                        "concorrenti_analizzati": 16, "misurato_il": "2026-09-02"},
        "titolo_lavoro": "The Ledger %d" % giorno, "autore": "Maren Ashcroft",
        "premessa": " ".join(["parola"] * 40),
        "struttura_prevista": {"capitoli": 24, "parole_per_capitolo": 1600,
                               "parole_totali_bersaglio": 38400, "pagine_minime_reali": 115},
        "angolo_differenziante": "A differenza di X e Y, qui il coven nasce dalla diffidenza.",
        "comando_cli": 'python -m engine.kdp nuovo "The Ledger %d" --nicchia "x"' % giorno,
    }
    r.update(over)
    return r


class TestKdpGate:
    """Chi scrive il piano non e' chi lo approva. Il gate fratello (`kdp blocco`) ha
    bocciato 2 volte su 7 su The Winter Term e aveva ragione entrambe."""

    def test_un_piano_completo_passa(self):
        from engine import piano
        assert piano.verifica([_riga(1), _riga(2)], giorni=2).ok

    def test_blocca_un_campo_mancante(self):
        from engine import piano
        v = piano.verifica([_riga(1, angolo_differenziante="")], giorni=1)
        assert not v.ok and any("angolo" in b for b in v.blocchi)

    def test_blocca_un_numero_senza_data_di_misura(self):
        """Il difetto del 2026-09-01: numeri di 19 giorni prima, nicchia da 83,1 a 72,9."""
        from engine import piano
        d = {"punteggio": 82.0}
        v = piano.verifica([_riga(1, dati_amazon=d)], giorni=1)
        assert not v.ok and any("data di misura" in b for b in v.blocchi)

    def test_blocca_punteggio_incoerente(self):
        from engine import piano
        v = piano.verifica([_riga(1, punteggio_nicchia=99.0)], giorni=1)
        assert not v.ok and any("non coincide" in b for b in v.blocchi)

    def test_blocca_comando_non_compilato(self):
        from engine import piano
        v = piano.verifica([_riga(1, comando_cli="python -m engine.kdp nuovo")], giorni=1)
        assert not v.ok and any("comando_cli" in b for b in v.blocchi)

    def test_blocca_titoli_duplicati(self):
        from engine import piano
        v = piano.verifica([_riga(1), _riga(2, titolo_lavoro="The Ledger 1")], giorni=2)
        assert not v.ok and any("duplicato" in b for b in v.blocchi)

    def test_meno_righe_e_un_avviso_non_un_blocco(self):
        """Meglio un piano da 4 righe vero che da 7 con tre inventate (Art.2)."""
        from engine import piano
        v = piano.verifica([_riga(1)], giorni=7)
        assert v.ok and any("meno righe" in a or "invece di" in a for a in v.avvisi)

    def test_raccoglie_TUTTI_i_problemi_non_solo_il_primo(self):
        from engine import piano
        v = piano.verifica([_riga(1, angolo_differenziante="", comando_cli="")], giorni=1)
        assert len(v.blocchi) >= 2, "un gate che si ferma al primo errore costa tre giri"


class TestLibroDelGiorno:
    def test_senza_piano_si_ferma_e_non_inventa(self, libri, monkeypatch):
        """B-018 e' nato cosi': un comando che improvvisa quando manca l'input."""
        from engine import libro_del_giorno, piano
        monkeypatch.setattr(piano, "carica_piano", lambda *a, **k: None)
        e = libro_del_giorno.apri()
        assert not e.ok and "piano" in e.errore.lower()

    def test_prende_la_riga_del_giorno_giusto(self, libri, monkeypatch):
        import datetime
        from engine import libro_del_giorno, piano
        monkeypatch.setattr(piano, "carica_piano",
                            lambda *a, **k: {"settimana_dal": "2026-08-31",
                                             "righe": [_riga(1), _riga(2), _riga(3)]})
        e = libro_del_giorno.apri(oggi=datetime.date(2026, 9, 2))   # mercoledi = giorno 3
        assert e.giorno == 3 and e.riga["titolo_lavoro"] == "The Ledger 3"

    def test_regola_6_riprende_il_libro_aperto(self, libri, monkeypatch):
        import datetime
        from engine import libro_del_giorno, piano
        from engine.book_project import BookProject
        BookProject.crea("Un Libro Aperto", "x", "Maren Ashcroft", 24, 1600)
        monkeypatch.setattr(piano, "carica_piano",
                            lambda *a, **k: {"settimana_dal": "2026-08-31",
                                             "righe": [_riga(1)]})
        e = libro_del_giorno.apri(oggi=datetime.date(2026, 8, 31))
        assert e.ripresa and e.slug == "un-libro-aperto"
        assert not e.ok, "non deve aprire un secondo libro sopra uno incompleto"
