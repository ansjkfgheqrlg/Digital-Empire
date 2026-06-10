#!/usr/bin/env python3
"""
Lancio Updater — Digital Empire / Claude Code Mastery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mantiene lancio.md sempre aggiornato con:
- Numeri dinamici (opt-in, call, follower)
- Fase del lancio attuale
- Posti call disponibili
- Argomenti pubblicati
- Report settimanali
- Storico completo del lancio

Uso:
    python lancio_updater.py                      # Menu interattivo
    python lancio_updater.py update               # Aggiornamento rapido numeri
    python lancio_updater.py fase 2               # Cambia fase
    python lancio_updater.py call --fatte 3        # Registra 3 call fatte oggi
    python lancio_updater.py pubblica "claude_md"  # Registra contenuto pubblicato
    python lancio_updater.py report                # Report settimanale
    python lancio_updater.py status                # Mostra stato attuale
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


# ═══════════════════════════════════════════════════════════════
# CONFIGURAZIONE
# ═══════════════════════════════════════════════════════════════

LANCIO_MD_PATH = Path("lancio.md")
DATA_PATH = Path("lancio_data.json")
STORICO_PATH = Path("lancio_storico.json")

FASI = {
    0: {
        "nome": "Pre-lancio",
        "descrizione": "Costruire audience e credibilità. Zero vendita.",
        "cta_primaria": "Follow + engagement",
        "cosa_non_fare": "Non menzionare nessun prodotto",
        "tono": "Educativo puro. Massimo valore.",
    },
    1: {
        "nome": "Warm-up",
        "descrizione": "Creare anticipazione senza rivelare il prodotto.",
        "cta_primaria": "Engagement — seguimi per non perdertelo",
        "cosa_non_fare": "Non rivelare nome prodotto. Non dare link.",
        "tono": "Misterioso ma credibile. Curioso ma specifico.",
    },
    2: {
        "nome": "Lead Capture",
        "descrizione": "Massimizzare opt-in per l'ebook gratuito.",
        "cta_primaria": "Ebook gratuito Claude Code Mastery → link in bio",
        "cosa_non_fare": "Non spingere corso, masterclass, o call negli script",
        "tono": "Educativo con CTA naturale verso ebook.",
    },
    3: {
        "nome": "Push Call",
        "descrizione": "Convertire lead caldi in prenotazioni call.",
        "cta_primaria": "Call gratuita 1:1 → link pagina call",
        "cosa_non_fare": "Non tornare a spingere ebook. Non spingere corso.",
        "tono": "Più personale. Più diretto. Trasparenza totale.",
    },
    4: {
        "nome": "Evergreen",
        "descrizione": "Funnel attivo in modo automatico.",
        "cta_primaria": "Alterna settimanalmente tra ebook e call",
        "cosa_non_fare": "Non forzare urgenza artificiale.",
        "tono": "Mix educativo con CTA naturali.",
    },
}

METRICHE_TEMPLATE = {
    "call_fatte_totale": 0,
    "call_fatte_settimana": 0,
    "call_convertite": 0,
    "posti_call_settimana": 8,
    "posti_call_disponibili": 8,
    "optin_totali": 0,
    "optin_settimana": 0,
    "masterclass_vendute": 0,
    "corso_venduti": 0,
    "follower_tiktok_ccm": 0,
    "follower_tiktok_impero": 0,
    "follower_tiktok_mentalita": 0,
    "follower_ig_ccm": 0,
    "follower_ig_impero": 0,
    "follower_ig_mentalita": 0,
    "iscritti_youtube": 0,
    "membri_telegram": 0,
    "revenue_masterclass": 0,
    "revenue_corso": 0,
}


# ═══════════════════════════════════════════════════════════════
# DATACLASS — STATO DEL LANCIO
# ═══════════════════════════════════════════════════════════════

@dataclass
class StatoLancio:
    """Stato completo del lancio."""
    fase: int = 0
    data_g0: str = ""
    data_ultimo_aggiornamento: str = ""
    metriche: dict = field(default_factory=lambda: METRICHE_TEMPLATE.copy())
    contenuti_pubblicati: list = field(default_factory=list)
    urgenze_attive: list = field(default_factory=list)
    note: str = ""
    settimana_corrente: int = 1
    piano_settimana: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> 'StatoLancio':
        stato = StatoLancio()
        for key, value in data.items():
            if hasattr(stato, key):
                setattr(stato, key, value)
        return stato


# ═══════════════════════════════════════════════════════════════
# STORAGE — GESTIONE DATI
# ═══════════════════════════════════════════════════════════════

class Storage:
    """Gestisce lettura e scrittura dei dati."""

    @staticmethod
    def carica_stato() -> StatoLancio:
        """Carica lo stato del lancio dal file JSON."""
        if DATA_PATH.exists():
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            return StatoLancio.from_dict(data)
        return StatoLancio(
            data_ultimo_aggiornamento=datetime.now().isoformat()
        )

    @staticmethod
    def salva_stato(stato: StatoLancio):
        """Salva lo stato del lancio nel file JSON."""
        stato.data_ultimo_aggiornamento = datetime.now().isoformat()
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(stato.to_dict(), f, ensure_ascii=False, indent=2)

    @staticmethod
    def aggiungi_storico(evento: dict):
        """Aggiunge un evento allo storico."""
        storico = []
        if STORICO_PATH.exists():
            with open(STORICO_PATH, "r", encoding="utf-8") as f:
                storico = json.load(f)

        evento["timestamp"] = datetime.now().isoformat()
        storico.append(evento)

        with open(STORICO_PATH, "w", encoding="utf-8") as f:
            json.dump(storico, f, ensure_ascii=False, indent=2)

    @staticmethod
    def carica_storico() -> list:
        """Carica lo storico completo."""
        if STORICO_PATH.exists():
            with open(STORICO_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        return []


# ═══════════════════════════════════════════════════════════════
# MARKDOWN UPDATER — AGGIORNA lancio.md
# ═══════════════════════════════════════════════════════════════

class MarkdownUpdater:
    """Aggiorna le sezioni dinamiche di lancio.md."""

    @staticmethod
    def genera_dashboard(stato: StatoLancio) -> str:
        """Genera la sezione dashboard rapida."""
        fase_info = FASI.get(stato.fase, FASI[0])

        giorni_da_g0 = ""
        if stato.data_g0:
            try:
                g0 = datetime.fromisoformat(stato.data_g0)
                diff = (datetime.now() - g0).days
                if diff < 0:
                    giorni_da_g0 = f"G{diff} (mancano {abs(diff)} giorni a G0)"
                elif diff == 0:
                    giorni_da_g0 = "G0 — OGGI È IL GIORNO"
                else:
                    giorni_da_g0 = f"G+{diff}"
            except ValueError:
                giorni_da_g0 = "Data G0 non valida"

        m = stato.metriche

        urgenze_str = ""
        if stato.urgenze_attive:
            urgenze_str = "\n".join(
                [f"→ {u}" for u in stato.urgenze_attive]
            )
        else:
            urgenze_str = "→ Nessuna urgenza attiva questa settimana"

        piano_str = ""
        if stato.piano_settimana:
            for giorno, info in stato.piano_settimana.items():
                piano_str += f"{giorno.upper()}: {info}\n"
        else:
            piano_str = "[Piano non ancora compilato per questa settimana]"

        dashboard = f"""
### STATO ATTUALE
FASE: Fase {stato.fase} — {fase_info['nome']}
DESCRIZIONE: {fase_info['descrizione']}
DATA OGGI: {datetime.now().strftime('%d/%m/%Y')}
GIORNO LANCIO: {giorni_da_g0}
SETTIMANA: {stato.settimana_corrente}

CTA PRIMARIA ATTIVA:
→ {fase_info['cta_primaria']}

COSA NON FARE:
→ {fase_info['cosa_non_fare']}

TONO:
→ {fase_info['tono']}

URGENZA REALE COMUNICABILE:
{urgenze_str}

NUMERI AGGIORNATI:
→ Call già fatte: {m['call_fatte_totale']}
→ Call questa settimana: {m['call_fatte_settimana']}/{m['posti_call_settimana']}
→ Posti call disponibili: {m['posti_call_disponibili']}
→ Opt-in totali: {m['optin_totali']}
→ Opt-in questa settimana: {m['optin_settimana']}
→ Masterclass vendute: {m['masterclass_vendute']}
→ Corso venduti: {m['corso_venduti']}
→ Revenue masterclass: €{m['revenue_masterclass']}
→ Revenue corso: €{m['revenue_corso']}
→ Revenue totale: €{m['revenue_masterclass'] + m['revenue_corso']}

text


### COSA SPINGERE QUESTA SETTIMANA
PRIORITÀ 1: {fase_info['cta_primaria']}
NON SPINGERE: {fase_info['cosa_non_fare']}

text


### FOLLOWER / AUDIENCE
TIKTOK:
→ @claudecodemastery: {m['follower_tiktok_ccm']}
→ @creailtuoimpero: {m['follower_tiktok_impero']}
→ @mentalitabusiness: {m['follower_tiktok_mentalita']}

INSTAGRAM:
→ @claudecodemastery: {m['follower_ig_ccm']}
→ @creailtuoimpero: {m['follower_ig_impero']}
→ @mentalitabusiness: {m['follower_ig_mentalita']}

YOUTUBE: {m['iscritti_youtube']}
TELEGRAM: {m['membri_telegram']}

text


### CONTENUTI DA PUBBLICARE QUESTA SETTIMANA
{piano_str}

text


Ultimo aggiornamento: {datetime.now().strftime('%d/%m/%Y ore %H:%M')}
"""
        return dashboard.strip()

    @staticmethod
    def genera_contenuti_pubblicati(stato: StatoLancio) -> str:
        """Genera la tabella dei contenuti pubblicati."""
        if not stato.contenuti_pubblicati:
            return """```
DATA | PAGINA | ARGOMENTO | FORMATO | PERFORMANCE
-----|--------|-----------|---------|------------
[Nessun contenuto pubblicato ancora]
```"""

        righe = ["```",
                 "DATA       | PAGINA | ARGOMENTO                    | PERFORMANCE"]
        righe.append("-" * 80)

        for c in stato.contenuti_pubblicati[-20:]:
            data = c.get("data", "?")
            pagina = c.get("pagina", "?")
            argomento = c.get("argomento", "?")[:30]
            views = c.get("views", "?")
            save = c.get("save", "?")
            commenti = c.get("commenti", "?")
            righe.append(
                f"{data:10} | {pagina:6} | {argomento:30} | "
                f"V:{views} S:{save} C:{commenti}"
            )

        righe.append("```")
        return "\n".join(righe)

    @staticmethod
    def genera_numeri_dinamici(stato: StatoLancio) -> str:
        """Genera la tabella numeri dinamici."""
        m = stato.metriche
        data = datetime.now().strftime('%d/%m/%Y')

        return f"""| DATO | VALORE ATTUALE | ULTIMO AGGIORNAMENTO |
|------|---------------|---------------------|
| Call già fatte | {m['call_fatte_totale']} | {data} |
| Call fatte questa settimana | {m['call_fatte_settimana']} | {data} |
| Call convertite (totale) | {m['call_convertite']} | {data} |
| Posti call rimasti questa settimana | {m['posti_call_disponibili']} | {data} |
| Opt-in totali | {m['optin_totali']} | {data} |
| Opt-in questa settimana | {m['optin_settimana']} | {data} |
| Masterclass acquistate | {m['masterclass_vendute']} | {data} |
| Corso venduti | {m['corso_venduti']} | {data} |
| Follower @claudecodemastery TikTok | {m['follower_tiktok_ccm']} | {data} |
| Follower @creailtuoimpero TikTok | {m['follower_tiktok_impero']} | {data} |
| Follower @mentalitabusiness TikTok | {m['follower_tiktok_mentalita']} | {data} |
| Follower @claudecodemastery IG | {m['follower_ig_ccm']} | {data} |
| Follower @creailtuoimpero IG | {m['follower_ig_impero']} | {data} |
| Follower @mentalitabusiness IG | {m['follower_ig_mentalita']} | {data} |
| Iscritti YouTube | {m['iscritti_youtube']} | {data} |
| Membri community Telegram | {m['membri_telegram']} | {data} |"""

    @staticmethod
    def aggiorna_lancio_md(stato: StatoLancio):
        """Aggiorna lancio.md con i dati correnti."""
        if not LANCIO_MD_PATH.exists():
            print(f"⚠️  File {LANCIO_MD_PATH} non trovato.")
            print("Crealo prima con il template completo.")
            return False

        with open(LANCIO_MD_PATH, "r", encoding="utf-8") as f:
            contenuto = f.read()

        dashboard = MarkdownUpdater.genera_dashboard(stato)
        numeri = MarkdownUpdater.genera_numeri_dinamici(stato)
        pubblicati = MarkdownUpdater.genera_contenuti_pubblicati(stato)

        # Pattern per trovare e sostituire sezioni
        sostituzioni = [
            (
                r"### STATO ATTUALE.*?(?=\n═══|$)",
                f"### STATO ATTUALE\n\n{dashboard}",
            ),
        ]

        for pattern, sostituzione in sostituzioni:
            contenuto_nuovo = re.sub(
                pattern, sostituzione, contenuto, flags=re.DOTALL
            )
            if contenuto_nuovo != contenuto:
                contenuto = contenuto_nuovo

        with open(LANCIO_MD_PATH, "w", encoding="utf-8") as f:
            f.write(contenuto)

        print(f"✅ lancio.md aggiornato ({datetime.now().strftime('%H:%M')})")
        return True


# ═══════════════════════════════════════════════════════════════
# COMANDI OPERATIVI
# ═══════════════════════════════════════════════════════════════

class Comandi:
    """Tutti i comandi disponibili."""

    @staticmethod
    def status(stato: StatoLancio):
        """Mostra lo stato attuale del lancio."""
        fase_info = FASI.get(stato.fase, FASI[0])
        m = stato.metriche
        sep = "═" * 60
        lin = "─" * 60

        print(f"\n{sep}")
        print(f"  STATO LANCIO — CLAUDE CODE MASTERY")
        print(f"{sep}")
        print(f"\n  FASE:     {stato.fase} — {fase_info['nome']}")
        print(f"  CTA:      {fase_info['cta_primaria']}")
        print(f"  SETTIMANA: {stato.settimana_corrente}")

        if stato.data_g0:
            try:
                g0 = datetime.fromisoformat(stato.data_g0)
                diff = (datetime.now() - g0).days
                if diff < 0:
                    print(f"  G0:       Tra {abs(diff)} giorni")
                else:
                    print(f"  GIORNO:   G+{diff}")
            except ValueError:
                pass

        print(f"\n{lin}")
        print(f"  METRICHE")
        print(f"{lin}")
        print(f"  Call fatte:      {m['call_fatte_totale']} "
              f"(settimana: {m['call_fatte_settimana']}/"
              f"{m['posti_call_settimana']})")
        print(f"  Call convertite: {m['call_convertite']}")
        print(f"  Posti rimasti:   {m['posti_call_disponibili']}")
        print(f"  Opt-in totali:   {m['optin_totali']} "
              f"(settimana: {m['optin_settimana']})")
        print(f"  Masterclass:     {m['masterclass_vendute']} "
              f"(€{m['revenue_masterclass']})")
        print(f"  Corso:           {m['corso_venduti']} "
              f"(€{m['revenue_corso']})")
        print(f"  REVENUE TOTALE:  €{m['revenue_masterclass'] + m['revenue_corso']}")

        print(f"\n{lin}")
        print(f"  AUDIENCE")
        print(f"{lin}")
        print(f"  TikTok CCM:      {m['follower_tiktok_ccm']}")
        print(f"  TikTok Impero:   {m['follower_tiktok_impero']}")
        print(f"  TikTok Mentalità:{m['follower_tiktok_mentalita']}")
        print(f"  IG CCM:          {m['follower_ig_ccm']}")
        print(f"  IG Impero:       {m['follower_ig_impero']}")
        print(f"  IG Mentalità:    {m['follower_ig_mentalita']}")
        print(f"  YouTube:         {m['iscritti_youtube']}")
        print(f"  Telegram:        {m['membri_telegram']}")

        totale = (
            m['follower_tiktok_ccm'] + m['follower_tiktok_impero'] +
            m['follower_tiktok_mentalita'] + m['follower_ig_ccm'] +
            m['follower_ig_impero'] + m['follower_ig_mentalita'] +
            m['iscritti_youtube'] + m['membri_telegram']
        )
        print(f"  TOTALE:          {totale}")

        if stato.contenuti_pubblicati:
            print(f"\n{lin}")
            print(f"  ULTIMI 5 CONTENUTI")
            print(f"{lin}")
            for c in stato.contenuti_pubblicati[-5:]:
                print(f"  {c.get('data', '?')} | "
                      f"{c.get('pagina', '?')} | "
                      f"{c.get('argomento', '?')}")

        # Conversion rates
        if m['optin_totali'] > 0:
            print(f"\n{lin}")
            print(f"  CONVERSION RATES")
            print(f"{lin}")
            if m['masterclass_vendute'] > 0:
                cr_master = round(
                    m['masterclass_vendute'] / m['optin_totali'] * 100, 1
                )
                print(f"  Opt-in → Masterclass: {cr_master}%")
            if m['call_fatte_totale'] > 0:
                cr_call = round(
                    m['call_fatte_totale'] / m['optin_totali'] * 100, 1
                )
                print(f"  Opt-in → Call:        {cr_call}%")
            if m['call_convertite'] > 0 and m['call_fatte_totale'] > 0:
                cr_corso = round(
                    m['call_convertite'] / m['call_fatte_totale'] * 100, 1
                )
                print(f"  Call → Corso:         {cr_corso}%")

        print(f"\n{sep}\n")

    @staticmethod
    def aggiorna_numeri(stato: StatoLancio):
        """Aggiornamento interattivo dei numeri."""
        print("\n  AGGIORNAMENTO NUMERI")
        print("  " + "─" * 40)
        print("  Premi INVIO per mantenere il valore attuale.\n")

        m = stato.metriche
        campi = [
            ("optin_totali", "Opt-in totali"),
            ("optin_settimana", "Opt-in questa settimana"),
            ("masterclass_vendute", "Masterclass vendute"),
            ("corso_venduti", "Corso venduti"),
            ("call_fatte_totale", "Call fatte (totale)"),
            ("call_fatte_settimana", "Call fatte (settimana)"),
            ("call_convertite", "Call convertite (totale)"),
            ("posti_call_disponibili", "Posti call rimasti"),
            ("follower_tiktok_ccm", "Follower TT @claudecodemastery"),
            ("follower_tiktok_impero", "Follower TT @creailtuoimpero"),
            ("follower_tiktok_mentalita", "Follower TT @mentalitabusiness"),
            ("follower_ig_ccm", "Follower IG @claudecodemastery"),
            ("follower_ig_impero", "Follower IG @creailtuoimpero"),
            ("follower_ig_mentalita", "Follower IG @mentalitabusiness"),
            ("iscritti_youtube", "Iscritti YouTube"),
            ("membri_telegram", "Membri Telegram"),
        ]

        modificati = []
        for campo, label in campi:
            valore_attuale = m.get(campo, 0)
            nuovo = input(
                f"  {label} [{valore_attuale}]: "
            ).strip()
            if nuovo:
                try:
                    m[campo] = int(nuovo)
                    modificati.append(label)
                except ValueError:
                    print(f"    ⚠️ Valore non valido, mantengo {valore_attuale}")

        # Calcola revenue automaticamente
        m["revenue_masterclass"] = m["masterclass_vendute"] * 15
        m["revenue_corso"] = m["corso_venduti"] * 397

        if modificati:
            Storage.salva_stato(stato)
            Storage.aggiungi_storico({
                "tipo": "aggiornamento_numeri",
                "campi_modificati": modificati,
                "metriche": m.copy(),
            })
            print(f"\n  ✅ Aggiornati: {', '.join(modificati)}")
        else:
            print("\n  Nessuna modifica.")

    @staticmethod
    def cambia_fase(stato: StatoLancio, nuova_fase: int):
        """Cambia la fase del lancio."""
        if nuova_fase not in FASI:
            print(f"  ❌ Fase {nuova_fase} non esiste. Fasi disponibili: 0-4")
            return

        vecchia_fase = stato.fase
        fase_info = FASI[nuova_fase]

        print(f"\n  CAMBIO FASE")
        print(f"  " + "─" * 40)
        print(f"  Da: Fase {vecchia_fase} — {FASI[vecchia_fase]['nome']}")
        print(f"  A:  Fase {nuova_fase} — {fase_info['nome']}")
        print(f"\n  CTA attiva: {fase_info['cta_primaria']}")
        print(f"  Tono: {fase_info['tono']}")
        print(f"  Non fare: {fase_info['cosa_non_fare']}")

        conferma = input("\n  Confermi? (s/n): ").strip().lower()
        if conferma == "s":
            stato.fase = nuova_fase

            # Reset metriche settimanali
            stato.metriche["optin_settimana"] = 0
            stato.metriche["call_fatte_settimana"] = 0
            stato.metriche["posti_call_disponibili"] = (
                stato.metriche["posti_call_settimana"]
            )

            Storage.salva_stato(stato)
            Storage.aggiungi_storico({
                "tipo": "cambio_fase",
                "da": vecchia_fase,
                "a": nuova_fase,
                "nome_fase": fase_info["nome"],
            })
            print(f"\n  ✅ Fase cambiata a {nuova_fase} — {fase_info['nome']}")
        else:
            print("  Annullato.")

    @staticmethod
    def registra_call(stato: StatoLancio, fatte: int, convertite: int = 0):
        """Registra call effettuate."""
        m = stato.metriche
        m["call_fatte_totale"] += fatte
        m["call_fatte_settimana"] += fatte
        m["call_convertite"] += convertite
        m["posti_call_disponibili"] = max(
            0, m["posti_call_disponibili"] - fatte
        )

        if convertite > 0:
            m["corso_venduti"] += convertite
            m["revenue_corso"] = m["corso_venduti"] * 397

        Storage.salva_stato(stato)
        Storage.aggiungi_storico({
            "tipo": "call_registrate",
            "fatte": fatte,
            "convertite": convertite,
            "totale_call": m["call_fatte_totale"],
            "totale_convertite": m["call_convertite"],
        })

        print(f"\n  ✅ Registrate {fatte} call "
              f"({convertite} convertite)")
        print(f"  Call totali: {m['call_fatte_totale']}")
        print(f"  Posti rimasti questa settimana: "
              f"{m['posti_call_disponibili']}")

        if m["posti_call_disponibili"] == 0:
            print(f"\n  ⚠️  POSTI ESAURITI questa settimana!")

    @staticmethod
    def registra_optin(stato: StatoLancio, numero: int):
        """Registra nuovi opt-in."""
        m = stato.metriche
        m["optin_totali"] += numero
        m["optin_settimana"] += numero

        Storage.salva_stato(stato)
        Storage.aggiungi_storico({
            "tipo": "optin_registrati",
            "numero": numero,
            "totale": m["optin_totali"],
        })

        print(f"\n  ✅ Registrati {numero} opt-in")
        print(f"  Totale: {m['optin_totali']}")

    @staticmethod
    def registra_vendita(
        stato: StatoLancio,
        tipo: str,
        numero: int = 1
    ):
        """Registra vendite (masterclass o corso)."""
        m = stato.metriche

        if tipo == "masterclass":
            m["masterclass_vendute"] += numero
            m["revenue_masterclass"] = m["masterclass_vendute"] * 15
            print(f"\n  ✅ Registrate {numero} masterclass vendute")
            print(f"  Totale masterclass: {m['masterclass_vendute']} "
                  f"(€{m['revenue_masterclass']})")

        elif tipo == "corso":
            m["corso_venduti"] += numero
            m["revenue_corso"] = m["corso_venduti"] * 397
            print(f"\n  ✅ Registrati {numero} corsi venduti")
            print(f"  Totale corsi: {m['corso_venduti']} "
                  f"(€{m['revenue_corso']})")

        else:
            print(f"  ❌ Tipo '{tipo}' non valido. Usa 'masterclass' o 'corso'.")
            return

        Storage.salva_stato(stato)
        Storage.aggiungi_storico({
            "tipo": f"vendita_{tipo}",
            "numero": numero,
            "revenue_totale": m["revenue_masterclass"] + m["revenue_corso"],
        })

    @staticmethod
    def registra_contenuto(
        stato: StatoLancio,
        argomento: str,
        pagina: str = "tutte",
        formato: str = "tutorial",
    ):
        """Registra un contenuto pubblicato."""
        contenuto = {
            "data": datetime.now().strftime("%d/%m/%Y"),
            "pagina": pagina,
            "argomento": argomento,
            "formato": formato,
            "views": "?",
            "save": "?",
            "commenti": "?",
        }
        stato.contenuti_pubblicati.append(contenuto)

        Storage.salva_stato(stato)
        Storage.aggiungi_storico({
            "tipo": "contenuto_pubblicato",
            "contenuto": contenuto,
        })

        print(f"\n  ✅ Contenuto registrato:")
        print(f"  Argomento: {argomento}")
        print(f"  Pagina: {pagina}")
        print(f"  Formato: {formato}")

    @staticmethod
    def aggiorna_performance(
        stato: StatoLancio,
        indice: int = -1,
        views: int = 0,
        save: int = 0,
        commenti: int = 0,
    ):
        """Aggiorna la performance di un contenuto pubblicato."""
        if not stato.contenuti_pubblicati:
            print("  ❌ Nessun contenuto pubblicato da aggiornare.")
            return

        contenuto = stato.contenuti_pubblicati[indice]
        if views > 0:
            contenuto["views"] = views
        if save > 0:
            contenuto["save"] = save
        if commenti > 0:
            contenuto["commenti"] = commenti

        Storage.salva_stato(stato)
        print(f"\n  ✅ Performance aggiornata per: "
              f"{contenuto['argomento']}")
        print(f"  Views: {contenuto['views']} | "
              f"Save: {contenuto['save']} | "
              f"Commenti: {contenuto['commenti']}")

    @staticmethod
    def nuova_settimana(stato: StatoLancio):
        """Reset metriche settimanali e incremento settimana."""
        stato.settimana_corrente += 1
        stato.metriche["optin_settimana"] = 0
        stato.metriche["call_fatte_settimana"] = 0
        stato.metriche["posti_call_disponibili"] = (
            stato.metriche["posti_call_settimana"]
        )

        Storage.salva_stato(stato)
        Storage.aggiungi_storico({
            "tipo": "nuova_settimana",
            "settimana": stato.settimana_corrente,
        })

        print(f"\n  ✅ Nuova settimana: {stato.settimana_corrente}")
        print(f"  Opt-in settimana: reset a 0")
        print(f"  Call settimana: reset a 0")
        print(f"  Posti call: reset a {stato.metriche['posti_call_settimana']}")

    @staticmethod
    def report_settimanale(stato: StatoLancio):
        """Genera il report settimanale."""
        m = stato.metriche
        fase_info = FASI.get(stato.fase, FASI[0])
        sep = "═" * 60
        lin = "─" * 60

        revenue_totale = m["revenue_masterclass"] + m["revenue_corso"]

        # Calcola conversion rates
        cr_master = (
            round(m["masterclass_vendute"] / m["optin_totali"] * 100, 1)
            if m["optin_totali"] > 0 else 0
        )
        cr_call = (
            round(m["call_fatte_totale"] / m["optin_totali"] * 100, 1)
            if m["optin_totali"] > 0 else 0
        )
        cr_corso = (
            round(m["call_convertite"] / m["call_fatte_totale"] * 100, 1)
            if m["call_fatte_totale"] > 0 else 0
        )

        # Contenuti questa settimana
        oggi = datetime.now()
        contenuti_settimana = [
            c for c in stato.contenuti_pubblicati
            if c.get("data", "") >= (
                oggi - timedelta(days=7)
            ).strftime("%d/%m/%Y")
        ]

        # Totale follower
        totale_follower = (
            m["follower_tiktok_ccm"] + m["follower_tiktok_impero"] +
            m["follower_tiktok_mentalita"] + m["follower_ig_ccm"] +
            m["follower_ig_impero"] + m["follower_ig_mentalita"] +
            m["iscritti_youtube"] + m["membri_telegram"]
        )

        print(f"\n{sep}")
        print(f"  REPORT SETTIMANALE — Settimana {stato.settimana_corrente}")
        print(f"  Fase: {stato.fase} — {fase_info['nome']}")
        print(f"  Data: {oggi.strftime('%d/%m/%Y')}")
        print(f"{sep}")

        print(f"\n{lin}")
        print(f"  FUNNEL")
        print(f"{lin}")
        print(f"  Opt-in settimana:      {m['optin_settimana']}")
        print(f"  Opt-in totali:         {m['optin_totali']}")
        print(f"  Masterclass vendute:   {m['masterclass_vendute']} "
              f"(CR: {cr_master}%)")
        print(f"  Call fatte settimana:  {m['call_fatte_settimana']}")
        print(f"  Call fatte totale:     {m['call_fatte_totale']} "
              f"(CR: {cr_call}%)")
        print(f"  Call convertite:       {m['call_convertite']} "
              f"(CR: {cr_corso}%)")
        print(f"  Corso venduti:         {m['corso_venduti']}")

        print(f"\n{lin}")
        print(f"  REVENUE")
        print(f"{lin}")
        print(f"  Masterclass: €{m['revenue_masterclass']}")
        print(f"  Corso:       €{m['revenue_corso']}")
        print(f"  TOTALE:      €{revenue_totale}")

        print(f"\n{lin}")
        print(f"  AUDIENCE TOTALE: {totale_follower}")
        print(f"{lin}")

        print(f"\n{lin}")
        print(f"  CONTENUTI PUBBLICATI QUESTA SETTIMANA: "
              f"{len(contenuti_settimana)}")
        print(f"{lin}")
        for c in contenuti_settimana:
            perf = (
                f"V:{c.get('views', '?')} "
                f"S:{c.get('save', '?')} "
                f"C:{c.get('commenti', '?')}"
            )
            print(f"  {c.get('data', '?')} | {c.get('argomento', '?')} | {perf}")

        # Diagnosi e raccomandazioni
        print(f"\n{lin}")
        print(f"  DIAGNOSI")
        print(f"{lin}")

        if m["optin_settimana"] == 0 and stato.fase >= 2:
            print(f"  🔴 ZERO opt-in questa settimana → "
                  f"Verifica: landing page funziona? "
                  f"Link in bio corretto? Contenuti pubblicati?")

        if m["posti_call_disponibili"] == 0:
            print(f"  🟡 Posti call esauriti → "
                  f"Valuta se aumentare o mantenere scarsità")

        if (m["call_fatte_totale"] > 5 and
                m["call_convertite"] == 0):
            print(f"  🔴 {m['call_fatte_totale']} call, 0 conversioni → "
                  f"Rivedi lo script della call. "
                  f"Pitch troppo debole o target sbagliato.")

        if (m["call_fatte_totale"] > 0 and
                m["call_convertite"] / m["call_fatte_totale"] > 0.5):
            print(f"  🟢 CR call→corso sopra 50% → "
                  f"Ottimo! Valuta se scalare i posti.")

        if len(contenuti_settimana) < 5:
            print(f"  🟡 Solo {len(contenuti_settimana)} contenuti "
                  f"questa settimana → Target: 7/settimana")

        if revenue_totale > 0:
            print(f"  🟢 Revenue: €{revenue_totale} → "
                  f"Il funnel sta generando.")

        print(f"\n{sep}\n")

    @staticmethod
    def imposta_g0(stato: StatoLancio, data: str):
        """Imposta la data di G0."""
        try:
            datetime.fromisoformat(data)
            stato.data_g0 = data
            Storage.salva_stato(stato)
            Storage.aggiungi_storico({
                "tipo": "impostazione_g0",
                "data": data,
            })
            print(f"\n  ✅ G0 impostato: {data}")
        except ValueError:
            print(f"  ❌ Formato data non valido. "
                  f"Usa: YYYY-MM-DD (es: 2026-04-16)")

    @staticmethod
    def imposta_urgenza(stato: StatoLancio, urgenza: str, attiva: bool):
        """Aggiunge o rimuove un'urgenza."""
        if attiva:
            if urgenza not in stato.urgenze_attive:
                stato.urgenze_attive.append(urgenza)
                print(f"\n  ✅ Urgenza aggiunta: {urgenza}")
        else:
            if urgenza in stato.urgenze_attive:
                stato.urgenze_attive.remove(urgenza)
                print(f"\n  ✅ Urgenza rimossa: {urgenza}")
            else:
                print(f"  ⚠️ Urgenza non trovata.")
                return

        Storage.salva_stato(stato)

    @staticmethod
    def imposta_piano_settimana(stato: StatoLancio):
        """Imposta il piano contenuti della settimana."""
        print("\n  PIANO CONTENUTI SETTIMANA")
        print("  " + "─" * 40)
        print("  Per ogni giorno scrivi: argomento + formato + CTA")
        print("  Premi INVIO per lasciare vuoto.\n")

        giorni = [
            "lunedi", "martedi", "mercoledi",
            "giovedi", "venerdi", "sabato", "domenica"
        ]

        piano = {}
        for giorno in giorni:
            valore = input(f"  {giorno.capitalize()}: ").strip()
            if valore:
                piano[giorno] = valore

        stato.piano_settimana = piano
        Storage.salva_stato(stato)
        print(f"\n  ✅ Piano settimana {stato.settimana_corrente} salvato.")


# ═══════════════════════════════════════════════════════════════
# MENU INTERATTIVO
# ═══════════════════════════════════════════════════════════════

def menu_interattivo():
    """Menu interattivo principale."""
    stato = Storage.carica_stato()

    while True:
        fase_info = FASI.get(stato.fase, FASI[0])

        print(f"\n{'═' * 60}")
        print(f"  LANCIO UPDATER — Fase {stato.fase}: {fase_info['nome']}")
        print(f"  Settimana {stato.settimana_corrente}")
        print(f"{'═' * 60}")
        print(f"""
  1. Status completo
  2. Aggiorna numeri
  3. Cambia fase
  4. Registra call (fatte + convertite)
  5. Registra opt-in
  6. Registra vendita (masterclass/corso)
  7. Registra contenuto pubblicato
  8. Aggiorna performance contenuto
  9. Report settimanale
  10. Nuova settimana (reset contatori)
  11. Imposta G0
  12. Gestisci urgenze
  13. Piano settimana
  14. Aggiorna lancio.md
  15. Storico eventi
  0. Esci
""")

        scelta = input("  Scegli: ").strip()

        if scelta == "0":
            print("\n  Ciao.\n")
            break
        elif scelta == "1":
            Comandi.status(stato)
        elif scelta == "2":
            Comandi.aggiorna_numeri(stato)
        elif scelta == "3":
            fase = input("  Nuova fase (0-4): ").strip()
            if fase.isdigit():
                Comandi.cambia_fase(stato, int(fase))
        elif scelta == "4":
            fatte = input("  Call fatte oggi: ").strip()
            conv = input("  Di cui convertite: ").strip()
            if fatte.isdigit():
                Comandi.registra_call(
                    stato,
                    int(fatte),
                    int(conv) if conv.isdigit() else 0
                )
        elif scelta == "5":
            num = input("  Nuovi opt-in: ").strip()
            if num.isdigit():
                Comandi.registra_optin(stato, int(num))
        elif scelta == "6":
            tipo = input("  Tipo (masterclass/corso): ").strip()
            num = input("  Quanti: ").strip()
            Comandi.registra_vendita(
                stato, tipo, int(num) if num.isdigit() else 1
            )
        elif scelta == "7":
            arg = input("  Argomento: ").strip()
            pag = input("  Pagina (tutte/p1/p2/p3): ").strip() or "tutte"
            fmt = input("  Formato (tutorial/lista/discovery/confronto): "
                       ).strip() or "tutorial"
            Comandi.registra_contenuto(stato, arg, pag, fmt)
        elif scelta == "8":
            indice = input(
                "  Indice contenuto (-1 per ultimo): "
            ).strip()
            v = input("  Views: ").strip()
            s = input("  Save: ").strip()
            c = input("  Commenti: ").strip()
            Comandi.aggiorna_performance(
                stato,
                int(indice) if indice else -1,
                int(v) if v.isdigit() else 0,
                int(s) if s.isdigit() else 0,
                int(c) if c.isdigit() else 0,
            )
        elif scelta == "9":
            Comandi.report_settimanale(stato)
        elif scelta == "10":
            conferma = input(
                "  Sei sicuro? Reset contatori settimanali (s/n): "
            ).strip()
            if conferma == "s":
                Comandi.nuova_settimana(stato)
        elif scelta == "11":
            data = input("  Data G0 (YYYY-MM-DD): ").strip()
            Comandi.imposta_g0(stato, data)
        elif scelta == "12":
            azione = input("  Aggiungi (a) o rimuovi (r)? ").strip()
            urgenza = input("  Testo urgenza: ").strip()
            if urgenza:
                Comandi.imposta_urgenza(
                    stato, urgenza, azione == "a"
                )
        elif scelta == "13":
            Comandi.imposta_piano_settimana(stato)
        elif scelta == "14":
            MarkdownUpdater.aggiorna_lancio_md(stato)
        elif scelta == "15":
            storico = Storage.carica_storico()
            print(f"\n  STORICO ({len(storico)} eventi)")
            print(f"  {'─' * 50}")
            for e in storico[-10:]:
                ts = e.get("timestamp", "?")[:16]
                tipo = e.get("tipo", "?")
                print(f"  {ts} | {tipo}")
        else:
            print("  ⚠️ Scelta non valida.")

        stato = Storage.carica_stato()


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Lancio Updater — Claude Code Mastery"
    )
    subparsers = parser.add_subparsers(dest="comando")

    # Status
    subparsers.add_parser("status", help="Mostra stato attuale")

    # Update
    subparsers.add_parser("update", help="Aggiorna numeri interattivo")

    # Fase
    fase_parser = subparsers.add_parser("fase", help="Cambia fase")
    fase_parser.add_argument("numero", type=int, choices=[0, 1, 2, 3, 4])

    # Call
    call_parser = subparsers.add_parser("call", help="Registra call")
    call_parser.add_argument("--fatte", type=int, required=True)
    call_parser.add_argument("--convertite", type=int, default=0)

    # Optin
    optin_parser = subparsers.add_parser("optin", help="Registra opt-in")
    optin_parser.add_argument("numero", type=int)

    # Vendita
    vendita_parser = subparsers.add_parser("vendita", help="Registra vendita")
    vendita_parser.add_argument("tipo", choices=["masterclass", "corso"])
    vendita_parser.add_argument("--numero", type=int, default=1)

    # Pubblica
    pubblica_parser = subparsers.add_parser(
        "pubblica", help="Registra contenuto"
    )
    pubblica_parser.add_argument("argomento")
    pubblica_parser.add_argument("--pagina", default="tutte")
    pubblica_parser.add_argument("--formato", default="tutorial")

    # Report
    subparsers.add_parser("report", help="Report settimanale")

    # Nuova settimana
    subparsers.add_parser("nuova-settimana", help="Reset contatori")

    # G0
    g0_parser = subparsers.add_parser("g0", help="Imposta data G0")
    g0_parser.add_argument("data", help="YYYY-MM-DD")

    # Sync lancio.md
    subparsers.add_parser("sync", help="Aggiorna lancio.md")

    args = parser.parse_args()
    stato = Storage.carica_stato()

    if args.comando is None:
        menu_interattivo()
    elif args.comando == "status":
        Comandi.status(stato)
    elif args.comando == "update":
        Comandi.aggiorna_numeri(stato)
    elif args.comando == "fase":
        Comandi.cambia_fase(stato, args.numero)
    elif args.comando == "call":
        Comandi.registra_call(stato, args.fatte, args.convertite)
    elif args.comando == "optin":
        Comandi.registra_optin(stato, args.numero)
    elif args.comando == "vendita":
        Comandi.registra_vendita(stato, args.tipo, args.numero)
    elif args.comando == "pubblica":
        Comandi.registra_contenuto(
            stato, args.argomento, args.pagina, args.formato
        )
    elif args.comando == "report":
        Comandi.report_settimanale(stato)
    elif args.comando == "nuova-settimana":
        Comandi.nuova_settimana(stato)
    elif args.comando == "g0":
        Comandi.imposta_g0(stato, args.data)
    elif args.comando == "sync":
        MarkdownUpdater.aggiorna_lancio_md(stato)


if __name__ == "__main__":
    main()