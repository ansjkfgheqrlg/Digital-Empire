"""
ONDATA 1 — Blocco 2: fonte dati Magic Eden.

Client per i 3 endpoint pubblici v2 di Magic Eden (nessuna API key), verificati
live in questa sessione (vedi STUDIO-NFT-FASE0.md §2, comandi + risposte reali):
  - GET /v2/collections/{symbol}/stats
  - GET /v2/collections/{symbol}/listings
  - GET /v2/collections/{symbol}/activities

Rate limit REALE misurato in questa sessione, non assunto dalla documentazione:
20 richieste concorrenti su /stats -> 0 x 429. Uso cumulato (~30 chiamate in
pochi minuti su endpoint diversi, incl. /v2/collections/{symbol} senza
suffisso) -> 429 reale: "You have exceeded the requests in 1 min limit!
Please try again soon." Molto piu' permissivo dell'RPC Solana pubblico
(429 dopo 2 chiamate, CP-20260728-006), ma non infinito.
"""
import json
import logging
import time
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

BASE_URL = "https://api-mainnet.magiceden.dev/v2"
LAMPORTS_PER_SOL = 1_000_000_000
DEFAULT_TIMEOUT_S = 10

# Pacing prudenziale sotto la soglia osservata (non un numero a caso: vedi
# docstring del modulo per la prova del 429 reale).
MIN_INTERVAL_S = 1.2
MAX_RETRIES_429 = 3


class MagicEdenRateLimited(Exception):
    """Sollevata quando il backoff sul 429 reale si esaurisce senza successo."""


class MagicEdenClient:
    """Unica porta verso i dati Magic Eden reali (Blocco 2)."""

    def __init__(self, base_url: str = BASE_URL, min_interval_s: float = MIN_INTERVAL_S):
        self.base_url = base_url
        self.min_interval_s = min_interval_s
        self._last_call_ts = 0.0
        self.calls_made = 0
        self.calls_429 = 0

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None):
        query = ""
        if params:
            query = "?" + "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{self.base_url}{path}{query}"

        wait = self.min_interval_s - (time.time() - self._last_call_ts)
        if wait > 0:
            time.sleep(wait)

        last_err = None
        for attempt in range(1, MAX_RETRIES_429 + 1):
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT_S) as resp:
                    self._last_call_ts = time.time()
                    self.calls_made += 1
                    return json.loads(resp.read())
            except urllib.error.HTTPError as e:
                self._last_call_ts = time.time()
                last_err = e
                if e.code == 429:
                    self.calls_429 += 1
                    backoff = 2 ** attempt
                    logger.warning(
                        f"[MagicEdenClient] 429 su {path} (tentativo {attempt}/{MAX_RETRIES_429}), "
                        f"attendo {backoff}s"
                    )
                    if attempt < MAX_RETRIES_429:
                        time.sleep(backoff)
                        continue
                    raise MagicEdenRateLimited(f"{path}: rate limit dopo {attempt} tentativi") from e
                raise
        raise MagicEdenRateLimited(str(last_err))

    def get_stats(self, symbol: str) -> Dict[str, Any]:
        return self._get(f"/collections/{symbol}/stats")

    def get_listings(self, symbol: str, offset: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        return self._get(f"/collections/{symbol}/listings", {"offset": offset, "limit": limit})

    def get_activities(self, symbol: str, offset: int = 0, limit: int = 20) -> List[Dict[str, Any]]:
        return self._get(f"/collections/{symbol}/activities", {"offset": offset, "limit": limit})


def best_rarity_rank(listing: Dict[str, Any]) -> Optional[float]:
    """
    Blocco 3 supporto: un listing reale porta fino a 3 fonti di rarity rank
    indipendenti (howrare/moonrank/meInstant) — verificato sui dati fetchati
    oggi. Usiamo la media di quelle disponibili invece di una sola fonte:
    piu' robusto a un provider che sballa su una singola collection.
    """
    rarity = listing.get("rarity") or {}
    ranks = []
    for provider in ("howrare", "moonrank", "meInstant"):
        r = (rarity.get(provider) or {}).get("rank")
        if isinstance(r, (int, float)):
            ranks.append(r)
    if not ranks:
        return None
    return sum(ranks) / len(ranks)
