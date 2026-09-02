"""
Suite di test del workflow KDP (RNF-07 del piano del 2026-08-10).

Girano senza dipendenze opzionali (niente Word, Tesseract, pdfplumber) e senza rete: sono
pensati per essere lanciati sempre, non solo quando l'ambiente e' completo.

I casi non sono inventati: quasi tutti riproducono un falso positivo o un bug REALE trovato
sul primo libro, cosi' se qualcuno "semplifica" un validatore il test lo riprende.

    python -m pytest tests/ -v
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine import config, report_validazione, validators  # noqa: E402
from engine.book_project import slugify  # noqa: E402


# --------------------------------------------------------------------------- #
# Trattini
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("testo", [
    "She was twenty-nine years old.",       # numero composto inglese: obbligatorio
    "Item forty-one on the list.",
    "A check-up at the dentist.",           # phrasal noun
    "The second-cheapest bottle.",
    "A self-made man.",
    "An accidental break-in.",
    "- primo punto di un elenco",
    "# Titolo markdown",
    "---",
    "Data 2024-01-01 e 12-03-2024.",
    "Link https://esempio.com/a-b-c ok.",
    "Frase del tutto normale.",
])
def test_trattini_leciti_non_segnalati(testo):
    """Questi trattini sono corretti: segnalarli farebbe riscrivere testo giusto.
    Caso reale: la prima versione bloccava 'twenty-nine' e 'M-A-R-S-H'."""
    assert validators.valida_trattini(testo) == []


# CONTRATTO CAMBIATO IL 2026-08-30 (FIX-4). Prima si segnalava ogni `parola-parola` sulla
# stessa riga: misurato sui 4 libri veri faceva 66 avvisi, 66 falsi positivi (100%), perche'
# in inglese il composto col trattino e' produttivo e nessuna lista di eccezioni lo copre.
# Ora si segnala solo la forma REALE del difetto: parola tagliata a fine riga
# dall'impaginazione, o trattino lasciato staccato dentro la parola.
@pytest.mark.parametrize("testo,attesi", [
    ("La parola impagina-\nzione spezzata.", 1),          # tagliata a fine riga
    ("qui c'e' impagina - zione dentro il testo", 1),     # trattino staccato
    ("primo impagina - zione e poi qualcosa - strano", 2),
])
def test_trattini_sospetti_segnalati(testo, attesi):
    assert len(validators.valida_trattini(testo)) == attesi


def test_trattini_riporta_riga_e_contesto():
    errori = validators.valida_trattini("prima riga\nqui c'e' aaa - bbb dentro")
    assert errori and "riga 2" in errori[0] and "aaa - bbb" in errori[0]


def test_composto_inglese_sulla_stessa_riga_non_e_piu_un_avviso():
    """La forma che generava i 66 falsi positivi. Vedi TestTrattiniFix4 in fondo al file."""
    assert validators.valida_trattini("prima riga\nqui c'e' spiral-bound dentro") == []


# --------------------------------------------------------------------------- #
# Report di validazione
# --------------------------------------------------------------------------- #

def test_report_nuovo_e_pubblicabile():
    assert report_validazione.ReportValidazione().pubblicabile is True


def test_solo_i_bloccanti_impediscono_la_pubblicazione():
    r = report_validazione.ReportValidazione()
    r.avvisa("un trattino da guardare")
    r.errore("un difetto minore")
    assert r.pubblicabile is True, "avvisi ed errori non devono bloccare la pubblicazione"
    r.blocca("copertina senza titolo")
    assert r.pubblicabile is False


def test_aggiungi_prefissa_l_etichetta():
    r = report_validazione.ReportValidazione()
    r.aggiungi("Trattini", ["riga 3: aaa-bbb"], gravita="avviso")
    assert r.avvisi == ["[Trattini] riga 3: aaa-bbb"]


def test_riepilogo_dice_lo_stato():
    r = report_validazione.ReportValidazione()
    assert "PUBBLICABILE" in r.riepilogo()
    r.blocca("pagine sotto il minimo")
    testo = r.riepilogo()
    assert "NON PUBBLICABILE" in testo and "pagine sotto il minimo" in testo


def test_salvataggio_su_file(tmp_path):
    r = report_validazione.ReportValidazione()
    r.blocca("problema")
    destinazione = r.salva(tmp_path / "sotto" / "validazione.json")
    assert destinazione.exists()
    assert '"pubblicabile": false' in destinazione.read_text(encoding="utf-8")


# --------------------------------------------------------------------------- #
# Validatori senza dipendenze installate
# --------------------------------------------------------------------------- #

def test_file_mancante_non_solleva_ma_segnala(tmp_path):
    """Un validatore non deve mai far crollare il workflow per un file assente:
    deve dirlo e lasciare decidere a chi chiama."""
    inesistente = tmp_path / "non_esiste.pdf"
    assert validators.valida_numerazione_pagine(inesistente)
    assert validators.valida_copertina_testo(tmp_path / "no.png")


# --------------------------------------------------------------------------- #
# Slug dei progetti
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("titolo,atteso", [
    ("The Quiet Hours", "the-quiet-hours"),
    ("Titolo: con  punteggiatura!", "titolo-con-punteggiatura"),
    ("", "libro"),
])
def test_slugify(titolo, atteso):
    assert slugify(titolo) == atteso


def test_slug_non_supera_i_60_caratteri():
    assert len(slugify("parola " * 40)) <= 60


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def test_cli_senza_keyword_esce_con_parametri_errati():
    from engine import kdp
    assert kdp.main(["nicchie"]) == kdp.CONFIG_ERRATA


def test_cli_stato_di_uno_slug_inesistente():
    from engine import kdp
    assert kdp.main(["stato", "slug-che-non-esiste-12345"]) == kdp.CONFIG_ERRATA


def test_cli_consegna_con_copertina_mancante():
    from engine import kdp
    assert kdp.main(["consegna", "qualsiasi", "--cover", "/percorso/inesistente.png"]) \
        == kdp.CONFIG_ERRATA


def test_i_quattro_exit_code_sono_distinti():
    from engine import kdp
    codici = {kdp.OK, kdp.VALIDAZIONE_FALLITA, kdp.CONFIG_ERRATA, kdp.ERRORE_SISTEMA}
    assert codici == {0, 1, 2, 3}


# --------------------------------------------------------------------------- #
# FIX-4 (2026-08-30): i 66 falsi positivi sui trattini
# --------------------------------------------------------------------------- #
class TestTrattiniFix4:
    """Misurato sui 4 libri consegnati: 66 avvisi trattino, 66 falsi positivi (100%).
    Erano parole composte inglesi corrette e un cognome doppio ripetuto 8 volte."""

    @pytest.mark.parametrize("parola", [
        "spiral-bound", "chain-link", "hand-painted", "night-time", "straight-backed",
        "pay-as-you-go", "red-rimmed", "soft-featured", "fingerprint-powder",
        "pie-eating", "Ashworth-Kane",
    ])
    def test_le_parole_composte_inglesi_non_sono_avvisi(self, parola):
        """Erano tutte segnalate prima del fix. Sono ortografia, non difetti."""
        assert validators.valida_trattini(f"She saw the {parola} thing on the table.") == []

    def test_la_parola_spezzata_dall_impaginazione_e_ancora_un_avviso(self):
        """Il difetto VERO che questa funzione deve trovare."""
        avvisi = validators.valida_trattini("the light was pouring in through the impagina-\nzione of the window")
        assert avvisi and "spezzata" in avvisi[0]

    def test_il_trattino_staccato_dentro_la_parola_e_ancora_un_avviso(self):
        avvisi = validators.valida_trattini("she walked through the impagina - zione slowly")
        assert avvisi and "staccato" in avvisi[0]

    def test_le_lineette_lunghe_restano_vietate(self):
        """FIX-4 non deve aver allentato il controllo che conta."""
        assert validators.valida_lineette("She turned to look — and saw nothing at all.")
        assert validators.valida_lineette("He waited – then left the room quietly.")

    def test_una_frase_pulita_non_genera_niente(self):
        testo = "The spiral-bound ledger sat on the counter. She had twenty-nine of them."
        assert validators.valida_trattini(testo) == []
        assert validators.valida_lineette(testo) == []


# --------------------------------------------------------------------------- #
# FIX-5 (2026-08-30): la stima pagine tarata sui libri veri
# --------------------------------------------------------------------------- #
class TestStimaPagineFix5:
    """Il divisore fisso parole/320 sbagliava fino a 8 pagine, e in modo NON monotono
    (il libro con piu' parole risultava averne meno). Il modello ora conta lo spazio
    occupato: caratteri + la coda di riga che ogni fine paragrafo spreca."""

    # (nome, caratteri, paragrafi, pagine REALI contate sul PDF)
    LIBRI_VERI = [
        ("Proof_of_Murder",           211931,  831, 111),
        ("The_Ninth_Winter",          194097, 1690, 119),
        ("The_Quiet_Hours",           195146, 1741, 118),
        ("The_Second-Hand_Spellbook", 199819, 1518, 118),
        ("The_Winter_Term",           205570, 1364, 116),
    ]

    @pytest.mark.parametrize("nome,caratteri,paragrafi,reale", LIBRI_VERI)
    def test_entro_tre_pagine_dal_reale(self, nome, caratteri, paragrafi, reale):
        stima = config.stima_pagine(caratteri, paragrafi)
        assert abs(stima - reale) <= 3, (
            "%s: stima %.1f contro %d reali (errore %.1f)" % (nome, stima, reale,
                                                              stima - reale))

    def test_piu_paragrafi_a_parita_di_caratteri_significa_piu_pagine(self):
        """Il fatto che il vecchio modello non poteva vedere: il dialogo occupa piu'
        pagine a parita' di testo, perche' ogni paragrafo spreca la coda di una riga."""
        prosa = config.stima_pagine(200000, 800)
        dialogo = config.stima_pagine(200000, 1800)
        assert dialogo > prosa

    def test_il_vecchio_divisore_fisso_sbagliava_davvero(self):
        """Prova del perche' e' stato cambiato: su The_Winter_Term sbagliava di 8 pagine."""
        vecchio = 39668 / config.WORDS_PER_PAGE_ESTIMATE
        assert abs(vecchio - 116) > 7

    def test_testo_vuoto_non_esplode(self):
        assert config.stima_pagine(0, 0) == 0.0
        assert config.stima_pagine_da_testo("") == 0.0


# --------------------------------------------------------------------------- #
# FIX-2 (2026-08-30): il margine protegge un investimento, non il nulla
# --------------------------------------------------------------------------- #
class TestCambioNicchiaFix2:
    """Il 2026-08-30 la nicchia attiva era la PEGGIORE fra quelle misurate (recensioni
    mediana 355,5 contro 33) e aveva 0 libri, ma la soglia fissa a 12 punti rendeva
    impossibile uscirne: il guardrail difendeva il nulla al prezzo del catalogo."""

    @staticmethod
    def _nicchia(monkeypatch, tmp_path, keyword, punteggio, libri):
        """La costante si chiama STATO_PATH. La prima versione di questo helper rattoppava
        un nome inesistente (`PERCORSO`) con raising=False: i test hanno scritto sul file
        di produzione e hanno sostituito la nicchia vera con 'nicchia molto migliore'
        (2026-08-30, ripristinato da git). Ora si verifica che il rattoppo abbia agganciato
        davvero, invece di fallire in silenzio."""
        from engine import nicchia_attiva
        falso = tmp_path / "nicchia_attiva.json"
        monkeypatch.setattr(nicchia_attiva, "STATO_PATH", falso)
        assert nicchia_attiva.STATO_PATH == falso, "isolamento non agganciato"
        n = nicchia_attiva.Nicchia(keyword=keyword, punteggio_iniziale=punteggio,
                                   scelta_il="2026-08-13T00:00:00", motivazione="test")
        n.libri_pubblicati = list(libri)
        nicchia_attiva.salva(n)
        assert falso.exists(), "il test sta scrivendo altrove: fermarsi"
        return nicchia_attiva

    def test_con_zero_libri_basta_essere_migliore(self, tmp_path, monkeypatch):
        na = self._nicchia(monkeypatch, tmp_path, "small town romance suspense", 77.4, [])
        nuova = na.cambia("cozy fantasy bookshop", 83.1, "punteggio piu' alto")
        assert nuova.keyword == "cozy fantasy bookshop"

    def test_con_zero_libri_una_nicchia_PEGGIORE_viene_comunque_rifiutata(self, tmp_path, monkeypatch):
        na = self._nicchia(monkeypatch, tmp_path, "small town romance suspense", 77.4, [])
        with pytest.raises(na.NicchiaGiaScelta):
            na.cambia("cozy mystery bakery", 70.0, "peggiore")

    def test_con_libri_pubblicati_il_margine_resta_pieno(self, tmp_path, monkeypatch):
        """Li' il costo del cambio e' reale: 5,7 punti non bastano."""
        na = self._nicchia(monkeypatch, tmp_path, "small town romance suspense", 77.4,
                           ["Un Libro"])
        with pytest.raises(na.NicchiaGiaScelta):
            na.cambia("cozy fantasy bookshop", 83.1, "solo 5,7 punti")

    def test_con_libri_pubblicati_un_vantaggio_netto_passa(self, tmp_path, monkeypatch):
        na = self._nicchia(monkeypatch, tmp_path, "small town romance suspense", 77.4,
                           ["Un Libro"])
        nuova = na.cambia("nicchia molto migliore", 95.0, "oltre 12 punti")
        assert nuova.keyword == "nicchia molto migliore"
        assert nuova.storico and nuova.storico[0]["keyword"] == "small town romance suspense"
