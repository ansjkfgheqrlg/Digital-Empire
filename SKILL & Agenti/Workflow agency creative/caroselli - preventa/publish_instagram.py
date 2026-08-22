"""
Pubblica un carosello Preventa su Instagram (@digitalempireagency.e) RIUSANDO
il publisher gia' reale e funzionante in
"Workflow pubblicazione automatica/Instagram/instagram_publisher.py"
(stessa pagina, stesse credenziali che Max ha dato in chat - config.py di
quel folder le ha gia': IG_USERNAME=digitalempireagency.e).

Non duplica il motore (ADR-003): importa publish() da li', non lo riscrive.
Quel folder ha un proprio REGOLE.md di confinamento - non modificato, solo
importato, stesso pattern gia' usato per ArenaAI (caroselli - agency).

NON pubblica nulla in automatico se lanciato senza --live: di default fa
solo un dry-run (stampa cosa farebbe, non apre il browser reale su IG).
Serve conferma esplicita prima del primo post vero (stesso principio gia'
seguito oggi per WhatsApp e Arena).
"""
import argparse
import glob
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKFLOW_DIR = os.path.dirname(PROJECT_DIR)  # "Workflow agency creative/"
PUBLISHER_DIR = os.path.join(os.path.dirname(WORKFLOW_DIR), "Workflow pubblicazione automatica")
sys.path.insert(0, PUBLISHER_DIR)

ARSENALE = os.path.join(WORKFLOW_DIR, "Arsenale Caroselli")


def trova_slide(prodotto: str, nome_carosello: str) -> list[str]:
    cartella = os.path.join(ARSENALE, prodotto, nome_carosello)
    slide = sorted(glob.glob(os.path.join(cartella, "slide_*.png")))
    if not slide:
        raise FileNotFoundError(f"Nessuna slide trovata in {cartella}")
    return slide


def main():
    ap = argparse.ArgumentParser(description="Pubblica un carosello Preventa su Instagram")
    ap.add_argument("prodotto", help="Es. Preventa")
    ap.add_argument("nome_carosello", help="Es. 2026-08-06_tempo-perso-import")
    ap.add_argument("--caption", required=True, help="Caption gia' scritta (APSOC)")
    ap.add_argument("--live", action="store_true", help="Pubblica DAVVERO. Senza questo flag: solo dry-run.")
    args = ap.parse_args()

    slide = trova_slide(args.prodotto, args.nome_carosello)
    print(f"[PUBLISH] Trovate {len(slide)} slide:")
    for s in slide:
        print(f"  {s}")
    print(f"\n[PUBLISH] Caption ({len(args.caption)} caratteri):\n{args.caption}\n")

    if not args.live:
        print("[PUBLISH] DRY-RUN (default) — nessun post reale. Rilancia con --live per pubblicare davvero su @digitalempireagency.e.")
        return

    from Instagram.instagram_publisher import publish  # noqa: E402
    print("[PUBLISH] --live attivo: pubblicazione REALE in corso su @digitalempireagency.e...")
    publish(slide, args.caption, headless=False)


if __name__ == "__main__":
    main()
