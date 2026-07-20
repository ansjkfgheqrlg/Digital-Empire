"""Instagram configuration for Mentalità Brutale.

Legacy browser publisher compatibility only. The API-first MB-OS runtime is the preferred path.
Credentials must come from environment variables; no password belongs in Git.
"""
import os

IG_USERNAME = os.environ.get("MENTALITA_IG_USERNAME", "mentalita.brutale")
IG_PASSWORD = os.environ.get("MENTALITA_IG_PASSWORD", "")

COPYWRITER_SYSTEM_PROMPT = """
Scrivi una caption potente, cruda e diretta per un Reel Instagram sulla crescita personale e il business.
Usa un tono assertivo, sfidante ma altamente ispirazionale ("Mentalità Brutale").
Niente filtri, vai dritto al punto. Formatta con frasi brevi.
Chiudi con una singola azione coerente con il contenuto.
"""

DEFAULT_HASHTAGS = "#mentalitavincente #disciplina #successo #businessitalia #crescitapersonale"
