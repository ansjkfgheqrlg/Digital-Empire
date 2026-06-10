"""
Utility di logging centralizzata per l'agente outreach.

Input: nome workflow, path log directory
Output: oggetto logger configurato con handler su file e console
"""

import logging
import os
from datetime import datetime
from pathlib import Path


def get_logger(workflow_id: str, suffix: str = "", log_dir: str = "logs") -> logging.Logger:
    """
    Crea e configura un logger per un workflow specifico.

    Args:
        workflow_id: ID del workflow (es. "WF-A", "WF-B", "WF-D")
        suffix: Suffisso descrittivo per il nome del file (es. "milano_ristorante")
        log_dir: Directory dove salvare i log (default: "logs/")

    Returns:
        Logger configurato con handler su file e console
    """
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    data_oggi = datetime.now().strftime("%Y-%m-%d")
    suffix_clean = suffix.replace(" ", "_").lower() if suffix else ""
    nome_file = f"{data_oggi}_{workflow_id}"
    if suffix_clean:
        nome_file += f"_{suffix_clean}"
    nome_file += ".log"

    log_path = os.path.join(log_dir, nome_file)

    logger_name = f"{workflow_id}_{suffix_clean}" if suffix_clean else workflow_id
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # Evita handler duplicati se il logger esiste già
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Handler su file
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler su console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def log_errore_fatale(workflow_id: str, messaggio: str, log_dir: str = "logs") -> None:
    """
    Logga un errore fatale nel file errors.log centralizzato.

    Args:
        workflow_id: ID del workflow che ha generato l'errore
        messaggio: Messaggio di errore dettagliato
        log_dir: Directory dei log
    """
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    errors_path = os.path.join(log_dir, "errors.log")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(errors_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ERRORE FATALE [{workflow_id}]: {messaggio}\n")
