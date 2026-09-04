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
    """Crediti per un corto da 1-3 minuti.

    IMPORTANTE — questi corti NON sono video generati. Max li ha descritti cosi':
    nessun avatar, nessun soggetto, eleganti, sottotitoli piccoli al centro, elementi
    che si spostano, grafica 3D. Cioe' sono progetti VIBE MOTION con qualche sfondo,
    non clip di modelli video. Nella revisione 3 li avevo costati come se fossero
    dodici clip generative a testa: sbagliato, e li' se ne andava meta' del conto.

    La voce di questi corti sta su ElevenLabs per volonta' di Max (voce profonda,
    qualita' massima), quindi NON consuma crediti Higgsfield.
    """
    return {
        # magro: solo Vibe Motion piu' immagini di sfondo
        "magro": CR_VIBE_MOTION + 20 * CR_SOUL2 * riprova,
        # medio: Vibe Motion piu' 4 clip di sfondo in movimento
        "medio": CR_VIBE_MOTION + 4 * CR_KLING_1080 * riprova + 20 * CR_SOUL2 * riprova,
        # ricco: Vibe Motion piu' 8 clip
        "ricco": CR_VIBE_MOTION + 8 * CR_KLING_1080 * riprova + 30 * CR_SOUL2 * riprova,
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
    ap.add_argument("--yt-mese", type=float, default=70,
                    help="video YouTube al mese (default: cadenza 3/2 alternata, 2 giorni di stop)")
    ap.add_argument("--corti-mese", type=float, default=102,
                    help="video corti al mese (default: 3 al giorno, 6 una volta a settimana)")
    ap.add_argument("--chiamate-giorno", type=float, default=100, help="chiamate dell'agente vocale")
    ap.add_argument("--minuti-chiamata", type=float, default=2.0, help="durata media chiamata")
    ap.add_argument("--riprova", type=float, default=2.0,
                    help="quante volte in media si rigenera una clip prima di tenerla")
    a = ap.parse_args()

    yt_mese = a.yt_mese
    corti_mese = a.corti_mese

    print("=" * 78)
    print("COSTO DI PRODUZIONE — volume Digital Empire dichiarato da Max il 2026-09-04")
    print("=" * 78)
    print(f"  Video YouTube : {yt_mese:,.0f} al mese  ({yt_mese * 10:,.0f} minuti finiti)"
          .replace(",", "."))
    print(f"                  cadenza 3-2-3-2 alternata, 2 giorni di stop al mese")
    print(f"  Video corti   : {corti_mese:,.0f} al mese  ({corti_mese * 2:,.0f} minuti finiti)"
          .replace(",", "."))
    print(f"                  3 al giorno, 6 una volta a settimana. Vibe Motion, voce ElevenLabs")
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
    print("-" * 78)
    print("  ELEVENLABS — conto separato")
    print("-" * 78)
    min_corti = corti_mese * 2
    cr_corti = min_corti * 1000
    min_chiamate = a.chiamate_giorno * 30 * a.minuti_chiamata
    print(f"    Voce dei corti : {min_corti:,.0f} minuti = {cr_corti/1000:,.0f}k crediti"
          .replace(",", "."))
    print(f"    Agente vocale  : {a.chiamate_giorno:g} chiamate/giorno x 30 x {a.minuti_chiamata:g} min"
          f" = {min_chiamate:,.0f} minuti".replace(",", "."))
    print()
    # I piani ElevenAgents costano esattamente $0,08 al minuto anche in eccedenza:
    # il livello non cambia il totale, cambia solo quanti crediti TTS e quanta concorrenza.
    for nome, prezzo, crediti_k, min_incl, conc in [
        ("Creator", 22, 121, 275, 10), ("Pro", 99, 600, 1238, 20),
        ("Scale", 299, 1800, 3738, 30), ("Business", 990, 6000, 12375, 40)]:
        ecc = max(0.0, min_chiamate - min_incl) * 0.08
        ok_cr = "si'" if crediti_k * 1000 >= cr_corti else "NO"
        print(f"    {nome:<9} ${prezzo:>4} + ${ecc:>7,.0f} eccedenza = ${prezzo+ecc:>7,.0f}/mese"
              f"   crediti bastano: {ok_cr:<4} concorrenza {conc}".replace(",", "."))
    print()
    print(f"    I piani sono LINEARI a $0,08 al minuto: salire di livello non fa risparmiare")
    print(f"    sulle chiamate. Si sceglie il piu' basso che copra i crediti TTS.")
    print(f"    A parte: telefonia Italia ~$0,03/min = ~${min_chiamate*0.03:,.0f}, LLM ~${min_chiamate*0.0012:,.0f}."
          .replace(",", "."))
    print()
    print(f"  VOCE DEI VIDEO LUNGHI — {yt_mese*10:,.0f} minuti al mese.".replace(",", "."))
    print(f"    Se sta su Higgsfield (TTS con ElevenLabs v3 dentro) costa crediti,")
    print(f"    MA IL COSTO NON E' PUBBLICATO: va misurato in-app il giorno 1.")
    print(f"    Se invece va su ElevenLabs sono {yt_mese*10*1000/1_000_000:.1f}M crediti in piu' e serve Scale.")
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
