#!/usr/bin/env python3
"""
Calcolatore del costo di produzione video su Higgsfield, al volume vero di Digital Empire.

Nasce da un errore mio: nel dossier 28 revisione 2 avevo calcolato il costo di UN video
(€2,78) e mi ero fermato li'. Max ha chiesto il conto sul volume reale — 5 video YouTube
al giorno piu' 10 corti al giorno — e a quel volume la conclusione si ribalta: nessun piano
self-serve regge, e il discorso diventa Enterprise piu' architettura.

Questo file esiste perche' quei numeri vanno RIFATTI ogni volta che cambia un'ipotesi
(volume, mix di modelli, tasso di riprova), non ricordati a memoria.

Uso:
    python costo_produzione_higgsfield.py
    python costo_produzione_higgsfield.py --yt-giorno 3 --corti-giorno 5

Fonte dei prezzi: higgsfield.ai/pricing letto dal DOM il 2026-09-04. Tutti i prezzi in EUR,
IVA esclusa, tariffe annuali. Il costo in crediti del Text-to-Speech NON e' pubblicato:
dove serve, e' marcato come ignoto e non stimato.
"""
from __future__ import annotations

import argparse
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# --- Listino: crediti mensili -> costo mensile in EUR (tariffa annuale) -----------------
# Team e Scale sono PER POSTO: il prezzo qui e' gia' moltiplicato per i 5 posti minimi.
PIANI = [
    ("Plus",            1_200,   47.0),
    ("Ultra 3.000",     3_000,   99.0),
    ("Ultra 6.000",     6_000,  194.0),
    ("Ultra 9.000",     9_000,  270.0),
    ("Team (5 posti)",  5_000,  325.0),
    ("Scale (5 posti)", 12_500, 750.0),
]

# Pacchetti extra: ~20 crediti per dollaro. Cambio prudenziale 1 USD = 0,925 EUR.
EUR_PER_CREDITO_TOPUP = 0.05 * 0.925

# --- Costi per generazione (crediti), dal comparatore del sito --------------------------
CR_KLING_1080 = 8.0      # per clip da 5s
CR_SEEDANCE_1080 = 45.0  # per clip da 5s
CR_SOUL2 = 0.12          # per immagine
CR_SUPERCOMPUTER = 200.0 # produzione completa end-to-end, da guida ufficiale
CR_VIBE_MOTION = 40.0    # stima: ~150 crediti = 3-10 progetti (fonte terza). IPOTESI.


def scenari_youtube(riprova: float) -> dict[str, float]:
    """Crediti per un video YouTube da 10 minuti, faceless, modello misto."""
    return {
        # magro: poche clip, molte immagini mosse in montaggio da noi
        "magro": 8 * CR_KLING_1080 * riprova + 200 * CR_SOUL2 * riprova,
        # medio: b-roll vero
        "medio": 20 * CR_KLING_1080 * riprova + 120 * CR_SOUL2 * riprova,
        # ricco: 4 inquadrature di apertura su Seedance 2.0
        "ricco": (4 * CR_SEEDANCE_1080 * riprova + 16 * CR_KLING_1080 * riprova
                  + 120 * CR_SOUL2 * riprova),
    }


def scenari_corto(riprova: float) -> dict[str, float]:
    """Crediti per un corto da ~2 minuti: editing avanzato, grafica in movimento, voce."""
    return {
        # magro: Higgsfield fa solo gli asset, la grafica la montiamo noi (After Effects)
        "magro": 6 * CR_KLING_1080 * riprova + 20 * CR_SOUL2 * riprova,
        # medio: clip piu' un progetto Vibe Motion per la grafica
        "medio": (12 * CR_KLING_1080 * riprova + 30 * CR_SOUL2 * riprova
                  + CR_VIBE_MOTION),
        # ricco: Supercomputer end-to-end
        "ricco": (12 * CR_KLING_1080 * riprova + 30 * CR_SOUL2 * riprova
                  + CR_SUPERCOMPUTER),
    }


def costo_mensile(crediti_servono: float) -> tuple[str, float, float]:
    """Piano piu' conveniente + eventuali pacchetti extra. -> (piano, incluso, extra)."""
    migliore = None
    for nome, inclusi, prezzo in PIANI:
        mancanti = max(0.0, crediti_servono - inclusi)
        totale = prezzo + mancanti * EUR_PER_CREDITO_TOPUP
        if migliore is None or totale < migliore[3]:
            migliore = (nome, prezzo, mancanti * EUR_PER_CREDITO_TOPUP, totale)
    return migliore[0], migliore[1], migliore[2]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--yt-giorno", type=float, default=5, help="video YouTube al giorno")
    ap.add_argument("--corti-giorno", type=float, default=10, help="video corti al giorno")
    ap.add_argument("--giorni", type=float, default=30, help="giorni di produzione al mese")
    ap.add_argument("--riprova", type=float, default=2.0,
                    help="quante volte in media si rigenera una clip prima di tenerla")
    a = ap.parse_args()

    yt_mese = a.yt_giorno * a.giorni
    corti_mese = a.corti_giorno * a.giorni

    print("=" * 78)
    print("COSTO DI PRODUZIONE HIGGSFIELD — volume Digital Empire")
    print("=" * 78)
    print(f"  Video YouTube : {a.yt_giorno:g}/giorno x {a.giorni:g} = {yt_mese:,.0f} al mese"
          f"  ({yt_mese * 10:,.0f} minuti finiti)".replace(",", "."))
    print(f"  Video corti   : {a.corti_giorno:g}/giorno x {a.giorni:g} = {corti_mese:,.0f} al mese"
          f"  ({corti_mese * 2:,.0f} minuti finiti)".replace(",", "."))
    print(f"  Tasso riprova : {a.riprova:g}x  (una clip su {a.riprova:g} si tiene)")
    print(f"  Tetto self-serve: 9.000 crediti al mese (Ultra 9.000, €270)")
    print()

    yt = scenari_youtube(a.riprova)
    co = scenari_corto(a.riprova)

    intest = f"  {'scenario':<9} {'cr/video YT':>12} {'cr/corto':>10} {'crediti/mese':>14} {'piano':>16} {'extra':>11} {'TOTALE/mese':>13}"
    print(intest)
    print("  " + "-" * (len(intest) - 2))

    for s in ("magro", "medio", "ricco"):
        tot_cr = yt[s] * yt_mese + co[s] * corti_mese
        piano, base, extra = costo_mensile(tot_cr)
        print(f"  {s:<9} {yt[s]:>12,.0f} {co[s]:>10,.0f} {tot_cr:>14,.0f}"
              f" {piano:>16} {'€' + format(extra, ',.0f'):>11}"
              f" {'€' + format(base + extra, ',.0f'):>13}".replace(",", "."))

    print()
    tot_medio = yt["medio"] * yt_mese + co["medio"] * corti_mese
    print(f"  Scarto dal tetto self-serve, scenario medio: {tot_medio / 9000:.0f}x")
    print()
    print("  VOCE — non e' inclusa qui.")
    minuti = yt_mese * 10 + corti_mese * 2
    caratteri = minuti * 1000
    print(f"    {minuti:,.0f} minuti al mese = ~{caratteri / 1_000_000:.1f}M caratteri"
          .replace(",", "."))
    print(f"    ElevenLabs Scale $299 copre 1,8M crediti; oltre si paga ~$0,17 al minuto.")
    print(f"    Higgsfield fa TTS con ElevenLabs v3 dentro i suoi crediti,")
    print(f"    ma IL COSTO IN CREDITI NON E' PUBBLICATO: va misurato in-app il giorno 1.")
    print(f"    A questo volume quell'incognita vale diverse centinaia di euro al mese.")
    print()
    print("  Le tre leve che spostano davvero il conto, in ordine di peso:")
    print("    1. Tasso di riprova. Provalo con --riprova 1.3: e' la meta' del costo.")
    print("    2. Immagini al posto delle clip. Soul 2.0 costa 0,12 crediti:")
    print("       un secondo di clip Kling costa ~66 volte un'immagine.")
    print("    3. Template. Canvas e Vibe Motion producono asset RIUSABILI:")
    print("       si costruisce lo stampo una volta e si rigenera solo il testo.")
    print()
    print("  Fonte prezzi: higgsfield.ai/pricing, DOM letto il 2026-09-04.")
    print("  Ipotesi mie, non dati ufficiali: composizione dei video, tasso di riprova,")
    print("  e il costo di un progetto Vibe Motion (CR_VIBE_MOTION).")


if __name__ == "__main__":
    main()
