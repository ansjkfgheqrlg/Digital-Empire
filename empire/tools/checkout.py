"""
EMPIRE -- checkout.py (LOTTO 3 "CASSA" -- swarm completamento Workflow Estate)

Gestisce la ladder di pagamento della landing "Manuale Claude Code"
(Crea siti/Siti CCM/manuale.html + pagamento.html) a partire da un'unica
fonte di verita': checkout.config.json.

Nessun link di pagamento va mai scritto a mano nell'HTML: questo script
legge checkout.config.json e inietta i link corretti in manuale.html e
pagamento.html (--apply), oppure verifica lo stato attuale senza scrivere
nulla (--check).

Ladder:
    Tier 1 -- Stripe live: si attiva da solo appena rails.stripe_base.url
              e' valorizzato e attivo=true in checkout.config.json.
    Tier 2 -- fallback ordine: pagamento.html mostra un form d'ordine
              (nome, email, prodotto, bump si/no) che invia una mailto:
              precompilata verso rails.ordine_email. Funziona oggi, senza
              aprire un solo account.
    Non esiste un "tier 3": se nessun rail e' pronto, il tier resta 2
    (pagamento.html non e' mai un vicolo cieco).

Uso (dalla radice del monorepo):
    python empire/tools/checkout.py --check
    python empire/tools/checkout.py --apply

Nessuna dipendenza esterna oltre alla libreria standard. Nessun eval().
Windows-safe: nessuna emoji nei print, sempre encoding="utf-8".
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

try:
    from empire import paths as _paths
except ImportError:  # pragma: no cover - fallback se eseguito fuori dal package
    _paths = None


# ---------------------------------------------------------------------------
# Path resolution (riusa empire.paths se disponibile, altrimenti fallback)
# ---------------------------------------------------------------------------

def _repo_root() -> Path:
    if _paths is not None:
        try:
            return _paths.repo_root()
        except Exception:
            pass
    # empire/tools/checkout.py -> tools -> empire -> radice del monorepo
    return Path(__file__).resolve().parents[2]


def _safe_stdout() -> None:
    """Evita UnicodeEncodeError su Windows/cp1252. Va chiamata come prima istruzione."""
    if _paths is not None:
        try:
            _paths.safe_stdout()
            return
        except Exception:
            pass
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


SITE_DIRNAME = ("Crea siti", "Siti CCM")
CONFIG_FILENAME = "checkout.config.json"
MANUALE_FILENAME = "manuale.html"
PAGAMENTO_FILENAME = "pagamento.html"
STATO_FILENAME = "CHECKOUT-STATO.md"

# quando uno stripe rail non e' pronto, i bottoni puntano al gradino 2
FALLBACK_HREF = "pagamento.html"
FALLBACK_BUMP_HREF = "pagamento.html?bump=1"

PLACEHOLDER_RE = re.compile(r"YOUR_STRIPE_[A-Z_]+")


def site_dir(repo_root: Path | None = None) -> Path:
    root = repo_root if repo_root is not None else _repo_root()
    return root.joinpath(*SITE_DIRNAME)


def config_path(base_dir: Path | None = None) -> Path:
    return (base_dir if base_dir is not None else site_dir()) / CONFIG_FILENAME


class CheckoutConfigError(RuntimeError):
    """checkout.config.json mancante o non valido."""


def load_config(path: Path | None = None) -> dict[str, Any]:
    p = path if path is not None else config_path()
    if not p.exists():
        raise CheckoutConfigError(f"config mancante: {p}")
    with open(p, "r", encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError as e:
            raise CheckoutConfigError(f"config non valida ({p}): {e}") from e


def _rail(config: dict[str, Any], name: str) -> dict[str, Any]:
    return (config.get("rails") or {}).get(name) or {}


def stripe_base_ready(config: dict[str, Any]) -> bool:
    r = _rail(config, "stripe_base")
    return bool(r.get("attivo") and r.get("url"))


def stripe_bump_ready(config: dict[str, Any]) -> bool:
    r = _rail(config, "stripe_bump")
    return bool(r.get("attivo") and r.get("url"))


def compute_tier(config: dict[str, Any]) -> tuple[int, str]:
    """(tier, etichetta). Tier 1 = Stripe live. Tier 2 = fallback ordine (sempre disponibile)."""
    if stripe_base_ready(config):
        return 1, "stripe live (pagamento automatico con carta)"
    return 2, "fallback ordine attivo (mailto verso ordine_email)"


def base_link(config: dict[str, Any]) -> str:
    return _rail(config, "stripe_base")["url"] if stripe_base_ready(config) else FALLBACK_HREF


def bump_link(config: dict[str, Any]) -> str:
    return _rail(config, "stripe_bump")["url"] if stripe_bump_ready(config) else FALLBACK_BUMP_HREF


def active_rails(config: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    rails = config.get("rails") or {}
    return [(name, r) for name, r in rails.items() if r.get("attivo")]


def inactive_rails(config: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    rails = config.get("rails") or {}
    return [(name, r) for name, r in rails.items() if not r.get("attivo")]


def count_placeholders(base_dir: Path | None = None) -> dict[str, int]:
    """Conta i placeholder YOUR_STRIPE_* residui in ogni *.html della cartella (non ricorsivo)."""
    d = base_dir if base_dir is not None else site_dir()
    result: dict[str, int] = {}
    if not d.exists():
        return result
    for html_file in sorted(d.glob("*.html")):
        text = html_file.read_text(encoding="utf-8")
        matches = PLACEHOLDER_RE.findall(text)
        if matches:
            result[html_file.name] = len(matches)
    return result


# ---------------------------------------------------------------------------
# --apply: iniezione idempotente (regex ancorate al contesto, non al valore)
# ---------------------------------------------------------------------------

_HREF_CHECKOUT_BTN_RE = re.compile(r'(<a\s+href=")[^"]*("\s+id="checkout-btn")')
_BASE_LINK_JS_RE = re.compile(r'(const baseLink\s*=\s*")[^"]*(")')
_BUMP_LINK_JS_RE = re.compile(r'(const bumpLink\s*=\s*")[^"]*(")')


def render_manuale(html: str, config: dict[str, Any]) -> tuple[str, bool]:
    """Inietta base/bump link in manuale.html. Ritorna (nuovo_html, cambiato?)."""
    new_base = base_link(config)
    new_bump = bump_link(config)

    out = _HREF_CHECKOUT_BTN_RE.sub(lambda m: m.group(1) + new_base + m.group(2), html, count=1)
    out = _BASE_LINK_JS_RE.sub(lambda m: m.group(1) + new_base + m.group(2), out, count=1)
    out = _BUMP_LINK_JS_RE.sub(lambda m: m.group(1) + new_bump + m.group(2), out, count=1)
    return out, out != html


def apply_manuale(config: dict[str, Any], path: Path) -> bool:
    if not path.exists():
        return False
    original = path.read_text(encoding="utf-8")
    updated, changed = render_manuale(original, config)
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


_CONFIG_SCRIPT_RE = re.compile(
    r'(<script id="checkout-config" type="application/json">\n?)(.*?)(\n?\s*</script>)',
    re.DOTALL,
)


def render_pagamento(html: str, config: dict[str, Any]) -> tuple[str, bool]:
    """Sostituisce il blocco JSON incorporato in pagamento.html. Ritorna (nuovo_html, cambiato?)."""
    if not _CONFIG_SCRIPT_RE.search(html):
        return html, False
    payload = json.dumps(config, ensure_ascii=False, indent=2)
    out = _CONFIG_SCRIPT_RE.sub(lambda m: m.group(1) + payload + m.group(3), html, count=1)
    return out, out != html


def apply_pagamento(config: dict[str, Any], path: Path) -> bool:
    if not path.exists():
        return False
    original = path.read_text(encoding="utf-8")
    updated, changed = render_pagamento(original, config)
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


def render_stato(config: dict[str, Any], tier: int, label: str, today: date | None = None) -> str:
    d = today if today is not None else date.today()
    lines = [
        "# CHECKOUT -- STATO REALE (LOTTO 3 CASSA)",
        "",
        f"Ultimo aggiornamento: {d.isoformat()} (via `python empire/tools/checkout.py --apply`)",
        "",
        f"## Tier attivo: {tier} -- {label}",
        "",
    ]
    if tier == 1:
        lines.append(
            "Il pagamento automatico con carta (Stripe) e' collegato. I bottoni di manuale.html "
            "e pagamento.html puntano ai Payment Link configurati in checkout.config.json."
        )
    else:
        lines.append(
            "Il pagamento automatico (Stripe) NON e' ancora collegato. Il gradino attivo oggi e' il "
            "modulo d'ordine in pagamento.html: il cliente compila nome ed email, il client di posta "
            "si apre precompilato verso l'indirizzo configurato in rails.ordine_email, Max chiude "
            "l'ordine manualmente. Non esiste un tier 3: un funnel senza modo di pagare non e' un funnel."
        )

    lines += ["", "## Rail configurati", "", "| Rail | Attivo | Dettaglio |", "|---|---|---|"]
    rails = config.get("rails") or {}
    for name, r in rails.items():
        attivo = "SI" if r.get("attivo") else "NO"
        if r.get("attivo"):
            dettaglio = r.get("url") or r.get("iban") or r.get("email") or "-"
        else:
            dettaglio = r.get("richiede", "-")
        lines.append(f"| {name} | {attivo} | {dettaglio} |")

    lines += [
        "",
        "## Per raggiungere il Tier 1 (Stripe live)",
        "1. Max crea 2 Payment Link su Stripe (prodotto base e bump order) e incolla i 2 URL in "
        "`checkout.config.json` -> `rails.stripe_base.url` e `rails.stripe_bump.url`, con `attivo: true`.",
        "2. Rilancia `python empire/tools/checkout.py --apply`: i bottoni su manuale.html e "
        "pagamento.html passano automaticamente da tier 2 a tier 1.",
        "",
    ]
    return "\n".join(lines)


def apply_stato(config: dict[str, Any], tier: int, label: str, path: Path, today: date | None = None) -> bool:
    new_content = render_stato(config, tier, label, today)
    if path.exists() and path.read_text(encoding="utf-8") == new_content:
        return False
    path.write_text(new_content, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def run_check(base_dir: Path | None = None, cfg_path: Path | None = None) -> int:
    d = base_dir if base_dir is not None else site_dir()
    p_cfg = cfg_path if cfg_path is not None else (d / CONFIG_FILENAME)
    try:
        config = load_config(p_cfg)
    except CheckoutConfigError as e:
        print(f"ERRORE CONFIG: {e}")
        return 1

    placeholders = count_placeholders(d)
    total_placeholders = sum(placeholders.values())
    tier, label = compute_tier(config)

    print(f"=== CHECKOUT CHECK -- {config.get('prodotto', 'prodotto')} ===")
    print(f"Placeholder residui: {total_placeholders}")
    for name, n in placeholders.items():
        print(f"  - {name}: {n} placeholder non sostituiti")

    print("Rail attivi:")
    act = active_rails(config)
    if act:
        for name, r in act:
            dettaglio = r.get("url") or r.get("iban") or r.get("email") or "-"
            print(f"  - {name}: {dettaglio}")
    else:
        print("  (nessuno)")

    print("Rail non attivi (mancanti):")
    inact = inactive_rails(config)
    if inact:
        for name, r in inact:
            print(f"  - {name}: {r.get('richiede', '-')}")
    else:
        print("  (nessuno)")

    print(f"tier {tier} - {label}")
    if tier == 1:
        print("Pagamento automatico live: Stripe e' collegato.")
    else:
        print(
            "Per il tier 1: incolla stripe_base.url e stripe_bump.url in checkout.config.json "
            "(attivo: true) e rilancia --apply."
        )

    return 0 if total_placeholders == 0 else 1


def run_apply(base_dir: Path | None = None, cfg_path: Path | None = None) -> int:
    d = base_dir if base_dir is not None else site_dir()
    p_cfg = cfg_path if cfg_path is not None else (d / CONFIG_FILENAME)
    try:
        config = load_config(p_cfg)
    except CheckoutConfigError as e:
        print(f"ERRORE CONFIG: {e}")
        return 1

    tier, label = compute_tier(config)

    changed_manuale = apply_manuale(config, d / MANUALE_FILENAME)
    changed_pagamento = apply_pagamento(config, d / PAGAMENTO_FILENAME)
    changed_stato = apply_stato(config, tier, label, d / STATO_FILENAME)

    print(f"=== CHECKOUT APPLY -- {config.get('prodotto', 'prodotto')} ===")
    print(f"manuale.html: {'aggiornato' if changed_manuale else 'gia allineato'}")
    print(f"pagamento.html: {'aggiornato' if changed_pagamento else 'gia allineato'}")
    print(f"CHECKOUT-STATO.md: {'aggiornato' if changed_stato else 'gia allineato'}")
    print(f"tier {tier} - {label}")

    return 0


def main(argv: list[str] | None = None) -> int:
    _safe_stdout()
    parser = argparse.ArgumentParser(
        description=(
            "Gestisce la ladder di pagamento del Manuale Claude Code "
            "(checkout.config.json come fonte unica di verita')."
        )
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--check", action="store_true",
        help="Verifica placeholder residui, rail attivi e tier raggiunto (read-only, non scrive nulla).",
    )
    group.add_argument(
        "--apply", action="store_true",
        help="Inietta i link dal config in manuale.html/pagamento.html (idempotente).",
    )
    args = parser.parse_args(argv)

    if args.check:
        return run_check()
    return run_apply()


if __name__ == "__main__":
    raise SystemExit(main())
