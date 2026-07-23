"""Backend di generazione — seam pluggable per il "cervello" degli agenti.

- LocalMockBackend: offline, deterministico (default, nessuna dipendenza).
- LLMBackend: reale, basato su OpenAI-compatible Chat Completions.
  Install: pip install openai  (opzionale: non serve per il mock).
  Funziona anche con endpoint compatibili (Groq, Together, Ollama, Azure)
  passando base_url.
"""
from __future__ import annotations

import json
import re
from typing import Protocol, runtime_checkable

DIMENSIONS = ["completezza", "precisione", "creativita",
              "actionability", "coerenza"]


@runtime_checkable
class Backend(Protocol):
    def complete(self, system_prompt: str, user_prompt: str) -> str:
        ...


def _parse_scores(text: str) -> dict:
    """Estrae un dict con le 5 dimensioni (0-10) da un output LLM."""
    try:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        data = json.loads(m.group(0)) if m else {}
    except Exception:
        data = {}
    out = {}
    for d in DIMENSIONS:
        v = data.get(d)
        try:
            v = float(v)
        except (TypeError, ValueError):
            v = 5.0
        out[d] = max(0.0, min(10.0, v))
    return out


class LocalMockBackend:
    """Backend mock: testo deterministico dipendente da ruolo e iterazione."""

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        s = system_prompt.lower()
        if "writer" in s:
            return self._writer(user_prompt)
        if "analyst" in s:
            return self._analyst(user_prompt)
        if "refiner" in s:
            return self._refiner(user_prompt)
        if "meta" in s:
            return "Final quality gate passed."
        return f"[mock] {user_prompt[:60]}"

    @staticmethod
    def _writer(up: str) -> str:
        goal = up.split("GOAL:", 1)[1].split("|")[0].strip() if "GOAL:" in up else up
        it = up.split("ITER:", 1)[1].strip() if "ITER:" in up else "0"
        return (f"DRAFT v{it}: soluzione strutturata per '{goal}'. "
                f"Sezioni: obiettivo, passi operativi, criteri di verifica.")

    @staticmethod
    def _analyst(up: str) -> str:
        return ("ANALYSIS: contesto rilevante da memory; "
                "rischi: scope creep; opportunita: automazione ripetibile.")

    @staticmethod
    def _refiner(up: str) -> str:
        goal = up.split("GOAL:", 1)[1].split("|")[0].strip() if "GOAL:" in up else up
        return (f"REFINED DRAFT: prompt ottimizzato per '{goal}'. "
                f"Aggiunti: vincoli espliciti, passi numerati, "
                f"criteri di verifica misurabili.")


class LLMBackend:
    """Backend reale (OpenAI-compatible).

    Usa il metodo `score()` se presente: il Critic lo sfrutta per valutare
    il draft con il modello invece che con l'euristica mock.
    """

    def __init__(self, api_key: str | None = None, model: str = "gpt-4o-mini",
                 base_url: str | None = None, temperature: float = 0.7):
        try:
            from openai import OpenAI
        except ImportError as exc:  # pragma: no cover
            raise ImportError(
                "Per usare LLMBackend: pip install openai") from exc
        self.model = model
        self.temperature = temperature
        self._client = OpenAI(api_key=api_key, base_url=base_url)

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        resp = self._client.chat.completions.create(
            model=self.model,
            temperature=self.temperature,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return resp.choices[0].message.content or ""

    def score(self, system_prompt: str, user_prompt: str) -> dict:
        """Chiede al modello un JSON con le 5 dimensioni (0-10)."""
        instruction = (
            "Rispondi SOLO con un oggetto JSON, es. "
            '{"completezza":8,"precisione":8,"creativita":7,'
            '"actionability":8,"coerenza":9}. Nessun testo extra.'
        )
        try:
            resp = self._client.chat.completions.create(
                model=self.model,
                temperature=0.0,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{user_prompt}\n\n{instruction}"},
                ],
            )
            return _parse_scores(resp.choices[0].message.content or "{}")
        except Exception:
            # Fallback neutro: non blocca il loop di refine.
            return {d: 5.0 for d in DIMENSIONS}
