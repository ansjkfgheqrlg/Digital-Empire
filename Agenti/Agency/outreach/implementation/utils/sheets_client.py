"""
Client Google Sheets per lettura e scrittura dei lead e del tracker.

Input: credenziali service account, nome foglio
Output: wrapper con metodi per leggere/scrivere righe
"""

import os
import time
from typing import Optional
import logging

logger = logging.getLogger(__name__)

try:
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    SHEETS_DISPONIBILE = True
except ImportError:
    SHEETS_DISPONIBILE = False
    logger.warning("google-api-python-client non installato. Funzionalità Google Sheets disabilitate.")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Intestazioni attese nei fogli
INTESTAZIONI_NO_SITO = [
    "ID_LEAD", "DATA_TROVATO", "NOME_BUSINESS", "CATEGORIA", "INDIRIZZO",
    "CITTÀ", "TELEFONO", "EMAIL", "RATING_GOOGLE", "N_RECENSIONI",
    "PLACE_ID", "SCORE_PRIORITÀ", "FASCIA", "PRONTO_OUTREACH",
    "STATO_OUTREACH", "BOZZA_GENERATA", "DATA_BOZZA",
    "DATA_ULTIMO_CONTATTO", "DATA_RISPOSTA", "DATA_FOLLOWUP_SCHEDULATO",
    "STORICO_STATI", "NOTE", "MOTIVO_ESCLUSIONE"
]

INTESTAZIONI_FUNNEL_SCARSO = [
    "ID_LEAD", "DATA_TROVATO", "NOME_PAGINA", "SETTORE", "CITTÀ",
    "URL_PAGINA_FB", "URL_LANDING", "TELEFONO", "EMAIL",
    "SCORE_FUNNEL", "DETTAGLIO_SCORE", "N_ADS_ATTIVI",
    "SCORE_PRIORITÀ", "FASCIA", "PRONTO_OUTREACH",
    "STATO_OUTREACH", "BOZZA_GENERATA", "DATA_BOZZA",
    "DATA_ULTIMO_CONTATTO", "DATA_RISPOSTA", "DATA_FOLLOWUP_SCHEDULATO",
    "STORICO_STATI", "NOTE", "MOTIVO_ESCLUSIONE"
]

INTESTAZIONI_AI_PROSPECT = [
    "ID_LEAD", "DATA_TROVATO", "NOME_AZIENDA", "SETTORE", "CITTÀ",
    "SITO_WEB", "EMAIL", "TELEFONO", "REFERENTE",
    "N_DIPENDENTI_STIMATO", "SEGNALI_AUTOMAZIONE", "OFFERTE_LAVORO_TROVATE",
    "TOOL_USATI", "SCORE_AI_POTENZIALE", "PROCESSO_TARGET",
    "SCORE_PRIORITÀ", "FASCIA", "PRONTO_OUTREACH",
    "STATO_OUTREACH", "BOZZA_GENERATA", "DATA_BOZZA",
    "DATA_ULTIMO_CONTATTO", "DATA_RISPOSTA", "DATA_FOLLOWUP_SCHEDULATO",
    "STORICO_STATI", "NOTE", "MOTIVO_ESCLUSIONE"
]


class SheetsClient:
    """
    Client per interagire con un Google Sheets specifico.

    Utilizza un service account per l'autenticazione.
    Tutte le operazioni hanno retry automatico in caso di rate limit.
    """

    def __init__(self, spreadsheet_id: str, credentials_path: str):
        """
        Inizializza il client Sheets.

        Args:
            spreadsheet_id: ID del Google Spreadsheet (dalla URL)
            credentials_path: Path al file JSON del service account
        """
        if not SHEETS_DISPONIBILE:
            raise ImportError("Installa google-api-python-client: pip install google-api-python-client google-auth")

        self.spreadsheet_id = spreadsheet_id
        self.service = None
        self._inizializza_servizio(credentials_path)

    def _inizializza_servizio(self, credentials_path: str) -> None:
        """Crea il servizio Google Sheets autenticato."""
        try:
            creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
            self.service = build("sheets", "v4", credentials=creds, cache_discovery=False)
            logger.debug("Google Sheets: autenticazione riuscita")
        except Exception as e:
            logger.error(f"Errore autenticazione Google Sheets: {e}")
            raise

    def _esegui_con_retry(self, operazione, max_tentativi: int = 3):
        """
        Esegue un'operazione API con retry automatico in caso di rate limit.

        Args:
            operazione: Callable da eseguire
            max_tentativi: Numero massimo di tentativi

        Returns:
            Risultato dell'operazione
        """
        for tentativo in range(max_tentativi):
            try:
                return operazione()
            except HttpError as e:
                if e.resp.status == 429:  # Rate limit
                    attesa = 2 ** tentativo * 2  # Backoff esponenziale: 2, 4, 8 secondi
                    logger.warning(f"Google Sheets rate limit. Attendo {attesa}s (tentativo {tentativo + 1}/{max_tentativi})")
                    time.sleep(attesa)
                    if tentativo == max_tentativi - 1:
                        raise
                else:
                    raise

    def leggi_tab(self, nome_tab: str) -> list:
        """
        Legge tutte le righe di un tab del foglio.

        Args:
            nome_tab: Nome del tab (es. "Lead_NoSito")

        Returns:
            Lista di dizionari (una per riga, con intestazioni come chiavi)
        """
        def operazione():
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=nome_tab
            ).execute()
            return result.get("values", [])

        righe = self._esegui_con_retry(operazione)

        if not righe:
            return []

        intestazioni = righe[0]
        dati = []
        for riga in righe[1:]:
            # Normalizza righe più corte delle intestazioni
            riga_padded = riga + [""] * (len(intestazioni) - len(riga))
            dati.append(dict(zip(intestazioni, riga_padded)))

        return dati

    def aggiungi_riga(self, nome_tab: str, riga: dict, intestazioni: list) -> bool:
        """
        Aggiunge una riga in fondo a un tab.

        Args:
            nome_tab: Nome del tab
            riga: Dizionario con i dati della riga
            intestazioni: Lista ordinata delle colonne

        Returns:
            True se successo, False altrimenti
        """
        valori = [str(riga.get(col, "") or "") for col in intestazioni]

        def operazione():
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f"{nome_tab}!A1",
                valueInputOption="USER_ENTERED",
                insertDataOption="INSERT_ROWS",
                body={"values": [valori]}
            ).execute()

        try:
            self._esegui_con_retry(operazione)
            logger.debug(f"Riga aggiunta in {nome_tab}: {riga.get('ID_LEAD', riga.get('NOME_BUSINESS', '?'))}")
            return True
        except Exception as e:
            logger.error(f"Errore aggiunta riga in {nome_tab}: {e}")
            return False

    def aggiorna_cella(self, nome_tab: str, numero_riga: int, colonna: str, valore: str, intestazioni: list) -> bool:
        """
        Aggiorna una cella specifica nel foglio.

        Args:
            nome_tab: Nome del tab
            numero_riga: Numero di riga (1-based, incluse intestazioni; riga dati 1 = riga foglio 2)
            colonna: Nome della colonna (come da intestazioni)
            valore: Nuovo valore
            intestazioni: Lista ordinata delle colonne

        Returns:
            True se successo
        """
        try:
            idx_colonna = intestazioni.index(colonna)
        except ValueError:
            logger.error(f"Colonna '{colonna}' non trovata nelle intestazioni")
            return False

        # Converti indice colonna in lettera (A, B, ... Z, AA, ...)
        lettera_col = self._indice_a_lettera(idx_colonna)
        cella = f"{nome_tab}!{lettera_col}{numero_riga + 1}"  # +1 perché riga 1 = intestazioni

        def operazione():
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=cella,
                valueInputOption="USER_ENTERED",
                body={"values": [[str(valore)]]}
            ).execute()

        try:
            self._esegui_con_retry(operazione)
            return True
        except Exception as e:
            logger.error(f"Errore aggiornamento cella {cella}: {e}")
            return False

    def trova_riga_per_id(self, nome_tab: str, id_lead: str) -> tuple:
        """
        Cerca una riga per ID_LEAD e restituisce (riga_dict, numero_riga).

        Args:
            nome_tab: Nome del tab
            id_lead: ID del lead da cercare

        Returns:
            Tupla (dict_riga, numero_riga) o (None, -1) se non trovato
        """
        righe = self.leggi_tab(nome_tab)
        for i, riga in enumerate(righe):
            if riga.get("ID_LEAD") == id_lead:
                return riga, i + 1  # +1 per compensare le intestazioni
        return None, -1

    def crea_intestazioni(self, nome_tab: str, intestazioni: list) -> bool:
        """
        Crea le intestazioni nel tab se non esistono già.

        Args:
            nome_tab: Nome del tab
            intestazioni: Lista delle colonne

        Returns:
            True se successo
        """
        def operazione():
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=f"{nome_tab}!A1",
                valueInputOption="RAW",
                body={"values": [intestazioni]}
            ).execute()

        try:
            self._esegui_con_retry(operazione)
            logger.info(f"Intestazioni create nel tab {nome_tab}")
            return True
        except Exception as e:
            logger.error(f"Errore creazione intestazioni: {e}")
            return False

    @staticmethod
    def _indice_a_lettera(indice: int) -> str:
        """Converte indice colonna (0-based) in lettera Excel (A, B, ..., Z, AA, ...)."""
        risultato = ""
        while True:
            risultato = chr(ord("A") + indice % 26) + risultato
            indice = indice // 26 - 1
            if indice < 0:
                break
        return risultato


def crea_client_da_env() -> Optional["SheetsClient"]:
    """
    Crea un SheetsClient usando le variabili d'ambiente.

    Returns:
        SheetsClient configurato o None in caso di errore
    """
    spreadsheet_id = os.getenv("GOOGLE_SPREADSHEET_ID")
    credentials_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_PATH", "credentials/service_account.json")

    if not spreadsheet_id:
        logger.error("GOOGLE_SPREADSHEET_ID non configurato nel .env")
        return None

    if not os.path.exists(credentials_path):
        logger.error(f"File credenziali non trovato: {credentials_path}")
        return None

    try:
        return SheetsClient(spreadsheet_id, credentials_path)
    except Exception as e:
        logger.error(f"Errore creazione SheetsClient: {e}")
        return None
