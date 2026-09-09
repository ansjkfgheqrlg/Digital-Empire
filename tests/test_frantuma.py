# -*- coding: utf-8 -*-
"""Lo spaccatore di task grandi in micro-task (scripts/frantuma.py).

PERCHE' ESISTE. Max ha chiesto una funzione che spacchi una task grande in
micro-task ufficiali, ognuna con un CODICE -- la stessa cosa di un checkpoint
di ripresa (scripts/checkpoint.py): breve, sorteggiato, non progressivo, tale
che copiarlo in una chat nuova basta da solo per trovare ed eseguire proprio
quella micro-task. Prima versione usava numeri progressivi per-padre
(MT-01, MT-02): ambigui, perche' incollati senza dire anche il padre non
portano da nessuna parte. Corretta il 2026-09-09.
"""
import os
import re
import sys

import pytest

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RADICE, "scripts"))

import frantuma  # noqa: E402


@pytest.fixture
def base_finta(tmp_path, monkeypatch):
    monkeypatch.setattr(frantuma, "CARTELLA_BASE", str(tmp_path))
    monkeypatch.setattr(frantuma, "_codici_nella_storia", lambda: set())
    return tmp_path


def test_conia_produce_un_codice_nella_forma_mt_xxxx(base_finta):
    codice = frantuma.conia("TASK-A", "primo", "Primo pezzo")
    assert re.match(r"^MT-[A-Z0-9]{4}$", codice)


def test_il_codice_non_e_progressivo_ed_e_univoco_globalmente(base_finta):
    """Due task grandi diverse: i codici non si assomigliano ne' si ripetono
    -- non c'e' un contatore da azzerare per padre, e' un sorteggio globale."""
    a = frantuma.conia("TASK-A", "uno", "Uno")
    b = frantuma.conia("TASK-B", "uno", "Uno")
    assert a != b


def test_coniare_crea_il_file_con_quel_codice_nel_nome(base_finta):
    codice = frantuma.conia("TASK-LANCI-BUILD-W3", "s0-incasso", "Giorno zero")
    atteso = base_finta / "TASK-LANCI-BUILD-W3" / ("%s-s0-incasso.md" % codice)
    assert atteso.exists()


def test_un_codice_gia_occupato_non_viene_sovrascritto(base_finta, monkeypatch):
    """O_EXCL e' il punto di tutta la funzione: se il sorteggio ripete un
    codice gia' su disco, si risorteggia invece di scrivere sopra."""
    primo = frantuma.conia("TASK-A", "prima", "Prima")
    contenuto_primo = (base_finta / "TASK-A" / ("%s-prima.md" % primo)).read_text(
        encoding="utf-8")

    sequenza = iter([primo[3:], "9Q2K"])  # il primo sorteggio ripete un codice occupato
    monkeypatch.setattr(frantuma, "_sorteggia", lambda n=4: next(sequenza))
    secondo = frantuma.conia("TASK-A", "seconda", "Seconda")

    assert secondo != primo
    assert (base_finta / "TASK-A" / ("%s-prima.md" % primo)).read_text(
        encoding="utf-8") == contenuto_primo


def test_trova_cerca_in_tutte_le_task_padre(base_finta):
    """Il senso del codice: non serve sapere il padre per trovarla."""
    codice = frantuma.conia("TASK-LANCI-BUILD-W3", "chiave-brevo", "Sostituire la chiave")
    percorso = frantuma.trova_percorso(codice)
    assert percorso is not None
    assert "TASK-LANCI-BUILD-W3" in percorso


def test_trova_accetta_il_codice_senza_prefisso_mt(base_finta):
    codice = frantuma.conia("TASK-A", "uno", "Uno")
    assert frantuma.trova_percorso(codice[3:]) == frantuma.trova_percorso(codice)


def test_trova_un_codice_inesistente_da_none(base_finta):
    assert frantuma.trova_percorso("MT-ZZZZ") is None


def test_uno_slug_sporco_viene_rifiutato(base_finta):
    for cattivo in ("Slug Con Spazi", "slug_underscore", "../fuori", ""):
        with pytest.raises(SystemExit):
            frantuma.conia("TASK-A", cattivo, "Titolo")


def test_un_padre_sporco_viene_rifiutato(base_finta):
    with pytest.raises(SystemExit):
        frantuma.conia("../fuori", "slug", "Titolo")


def test_report_legge_i_titoli_veri_dai_file(base_finta):
    frantuma.conia("TASK-A", "uno", "Sostituire la chiave Brevo esposta")
    frantuma.conia("TASK-A", "due", "Catena dell'incasso")
    testo = frantuma.report("TASK-A")
    assert "Sostituire la chiave Brevo esposta" in testo
    assert "Catena dell'incasso" in testo


def test_report_mostra_il_codice_non_il_percorso(base_finta):
    """Correzione di Max, 2026-09-09: un ID e' qualcosa che si copia e si
    incolla altrove, un percorso non lo e'."""
    frantuma.conia("TASK-A", "uno", "Prima")
    testo = frantuma.report("TASK-A")
    assert "company/Memory/tasks/micro" not in testo
    assert re.search(r"\*\*MT-[A-Z0-9]{4}\*\*", testo)


def test_report_ha_lo_schema_fisso_viola_con_frecce(base_finta):
    """La forma esatta approvata da Max: titolo, sottotitolo col conteggio,
    un ramo per micro-task (└── sull'ultima), tutte col marcatore 🟣."""
    frantuma.conia("TASK-A", "uno", "Prima")
    frantuma.conia("TASK-A", "due", "Seconda")
    righe = frantuma.report("TASK-A").split("\n")
    assert righe[0] == "🟣 **TASK-A**"
    assert righe[1] == "🟣 divisa in 2 micro-task ufficiali"
    assert righe[3].startswith("   ├──🟣→ **MT-")
    assert righe[4].startswith("   └──🟣→ **MT-")


def test_report_su_task_senza_micro_task_lo_dice_chiaro(base_finta):
    testo = frantuma.report("TASK-INESISTENTE")
    assert "Nessuna micro-task" in testo


# ---------------------------------------------------------------------------
# L'ORDINE (2026-09-09). Il codice e' sorteggiato: ordinare i file per nome
# significa ordinare a caso. Al primo uso reale su TASK-LANCI-BUILD-W3 il report
# ha messo S0.1 in cima e S0.0 in nona posizione, cioe' ha perso proprio cio' che
# ADR-025 chiama non negoziabile: il gesto zero viene prima di tutto.
# ---------------------------------------------------------------------------

def test_il_report_segue_l_ordine_di_conio_non_l_alfabeto(base_finta, monkeypatch):
    codici = iter(["ZZZZ", "AAAA", "MMMM"])
    monkeypatch.setattr(frantuma, "_sorteggia", lambda n=4: next(codici))
    frantuma.conia("PADRE", "primo", "il primo, coniato per primo")
    frantuma.conia("PADRE", "secondo", "il secondo")
    frantuma.conia("PADRE", "terzo", "il terzo")

    righe = [r for r in frantuma.report("PADRE").splitlines() if "MT-" in r]
    assert "MT-ZZZZ" in righe[0], "il primo coniato deve restare primo"
    assert "MT-AAAA" in righe[1]
    assert "MT-MMMM" in righe[2]


def test_conia_scrive_l_ordine_nel_file(base_finta):
    frantuma.conia("PADRE", "uno", "primo")
    codice = frantuma.conia("PADRE", "due", "secondo")
    testo = open(frantuma.trova_percorso(codice), encoding="utf-8").read()
    assert "- **Ordine:** 2" in testo


def test_una_micro_task_senza_ordine_finisce_in_fondo(base_finta, monkeypatch):
    """Le micro-task coniate prima di questo campo non devono far saltare il report."""
    monkeypatch.setattr(frantuma, "_sorteggia", lambda n=4: "OLDX")
    vecchia = frantuma.conia("PADRE", "vecchia", "coniata prima del campo Ordine")
    percorso = frantuma.trova_percorso(vecchia)
    testo = open(percorso, encoding="utf-8").read()
    righe = [r for r in testo.splitlines() if not r.startswith("- **Ordine:**")]
    open(percorso, "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(righe))

    monkeypatch.setattr(frantuma, "_sorteggia", lambda n=4: "NEWX")
    frantuma.conia("PADRE", "nuova", "coniata dopo")

    righe = [r for r in frantuma.report("PADRE").splitlines() if "MT-" in r]
    assert "MT-NEWX" in righe[0]
    assert "MT-OLDX" in righe[-1]


def test_il_report_si_stampa_anche_su_uno_stdout_che_non_regge_il_viola(base_finta, capsysbinary, monkeypatch):
    """Su Windows stdout e' cp1252 e il carattere viola lo faceva morire con
    UnicodeEncodeError prima di stampare una riga: il comando non funzionava
    sulla macchina su cui gira."""
    frantuma.conia("PADRE", "uno", "primo")
    monkeypatch.setattr(sys, "argv", ["frantuma.py", "report", "--padre", "PADRE"])
    assert frantuma.main() == 0
    assert b"MT-" in capsysbinary.readouterr().out
