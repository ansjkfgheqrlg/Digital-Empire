#!/usr/bin/env python3
"""
Script Generator — Digital Empire / Claude Code Mastery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Genera script video strutturati per TikTok/IG Reels/YouTube
basandosi sui pattern competitor analizzati e sulle regole
del sistema skill.md.

Funzionalità:
- Genera lo scheletro completo di uno script
- Seleziona automaticamente hook, meccanismo, e CTA
- Valida la struttura prima di output
- Produce output pronto da passare a Claude per la scrittura

Uso:
    python script_generator.py
    python script_generator.py --topic "CLAUDE.md" --formato 1 --hook A
    python script_generator.py --batch 5
"""

import argparse
import json
import random
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional


# ═══════════════════════════════════════════════════════════════
# ENUMERAZIONI
# ═══════════════════════════════════════════════════════════════

class Formato(Enum):
    TUTORIAL_PRATICO = 1
    DEMO_WOW = 2
    DISCOVERY_NEWS = 3
    LISTA_RISORSE = 4
    CONFRONTO_LIVELLI = 5


class HookType(Enum):
    AFFERMAZIONE_SHOCK = "A"
    DOMANDA_RETORICA = "B"
    TUTORIAL_DIRETTO = "C"


class Piattaforma(Enum):
    TIKTOK = "tiktok"
    INSTAGRAM = "ig_reel"
    ENTRAMBE = "entrambe"
    YOUTUBE = "youtube"


class LevEmotiva(Enum):
    FOMO = "fomo"
    SEMPLICITA = "semplicita"
    RISPARMIO = "risparmio"
    ESCLUSIVITA = "esclusivita"
    CURIOSITA = "curiosita"
    AUTORITA = "autorita"


class CTATipo(Enum):
    EBOOK = "ebook"
    KEYWORD = "keyword"
    SAVE = "save"
    CALL = "call"


class Durata(Enum):
    CORTO = "corto"      # 30-45 sec
    MEDIO = "medio"      # 45-70 sec
    LUNGO = "lungo"      # 70-90 sec


# ═══════════════════════════════════════════════════════════════
# DATABASE — HOOK TEMPLATES
# ═══════════════════════════════════════════════════════════════

HOOK_TEMPLATES = {

    HookType.AFFERMAZIONE_SHOCK: [
        "C'è una funzione di Claude che quasi nessuno usa bene.",
        "Qualcuno ha appena rilasciato qualcosa su Claude Code "
        "che non ti aspetti.",
        "Il 90% delle persone usa Claude nel modo sbagliato.",
        "C'è un file che Claude legge automaticamente. "
        "Quasi nessuno lo crea.",
        "Stai sprecando token ogni volta che apri Claude.",
    ],

    HookType.DOMANDA_RETORICA: [
        "Ma è possibile dare a Claude il contesto del tuo intero "
        "progetto senza riscriverlo ogni volta?",
        "Ma è possibile che Claude scriva email aggiornate "
        "senza che tu gli dica niente?",
        "Come fai a far sì che Claude ti risponda sempre "
        "nello stesso modo, ogni giorno?",
        "Perché i tuoi output con Claude sono inconsistenti "
        "e quelli di altri no?",
    ],

    HookType.TUTORIAL_DIRETTO: [
        "Ecco come creare il tuo primo CLAUDE.md in 4 minuti.",
        "Ecco come installare una skill su Claude Code in 60 secondi.",
        "Ecco come organizzare le cartelle perché Claude "
        "trovi tutto da solo.",
        "Ecco come usare i Progetti di Claude "
        "come se fossi un professionista.",
        "Ecco come creare una skill modulare da zero.",
    ],
}


# ═══════════════════════════════════════════════════════════════
# DATABASE — ARGOMENTI TECNICI
# ═══════════════════════════════════════════════════════════════

ARGOMENTI = {

    "base": [
        {
            "id": "claude_md_intro",
            "titolo": "Cos'è il CLAUDE.md e come crearlo",
            "concetto_chiave": "file di contesto permanente",
            "termine_tecnico": "CLAUDE.md",
            "spiegazione_termine": (
                "un file di testo nella cartella del progetto "
                "che Claude legge automaticamente ad ogni sessione"
            ),
            "esempio_specifico": (
                "crei un file chiamato CLAUDE.md, "
                "dentro scrivi chi sei, cosa stai costruendo, "
                "come vuoi che Claude risponda"
            ),
            "beneficio_concreto": (
                "non riscrivi il contesto ogni volta. "
                "Claude sa già tutto quando lo apri."
            ),
            "perche_funziona": (
                "il contesto fisso non deve stare nel prompt. "
                "Il prompt è per la richiesta nuova, non per chi sei."
            ),
            "formati_consigliati": [1, 5],
            "hook_consigliato": HookType.TUTORIAL_DIRETTO,
            "leva_emotiva": LevEmotiva.RISPARMIO,
        },
        {
            "id": "progetti_claude",
            "titolo": "Come usare i Progetti di Claude",
            "concetto_chiave": "spazio con contesto persistente",
            "termine_tecnico": "Progetti",
            "spiegazione_termine": (
                "uno spazio dentro Claude dove metti istruzioni fisse "
                "e file di contesto che restano attivi in ogni chat"
            ),
            "esempio_specifico": (
                "crei un Progetto per i tuoi contenuti, "
                "uno per lo studio, uno per il tuo side project. "
                "Ognuno con le sue istruzioni e i suoi file."
            ),
            "beneficio_concreto": (
                "ogni nuova chat dentro quel Progetto "
                "parte già con il contesto giusto"
            ),
            "perche_funziona": (
                "Claude non ricomincia da zero. "
                "Hai già il contesto caricato."
            ),
            "formati_consigliati": [1, 5],
            "hook_consigliato": HookType.AFFERMAZIONE_SHOCK,
            "leva_emotiva": LevEmotiva.RISPARMIO,
        },
        {
            "id": "tre_livelli_prompting",
            "titolo": "I 3 livelli del prompting",
            "concetto_chiave": "progressione da prompt base a knowledge",
            "termine_tecnico": "knowledge base",
            "spiegazione_termine": (
                "la serie di informazioni strutturate "
                "che dai all'AI perché sappia di più su di te "
                "e sul tuo lavoro"
            ),
            "esempio_specifico": (
                "livello 1: scrivi una richiesta semplice. "
                "Livello 2: aggiungi contesto nella chat. "
                "Livello 3: hai una cartella con documenti "
                "che Claude legge da solo."
            ),
            "beneficio_concreto": (
                "al livello 3 Claude conosce già il tuo progetto, "
                "il tuo tono, i tuoi obiettivi. "
                "Tu gli dai solo il task."
            ),
            "perche_funziona": (
                "più contesto strutturato hai fuori dal prompt, "
                "più il prompt può essere specifico e breve"
            ),
            "formati_consigliati": [4, 5],
            "hook_consigliato": HookType.CONFRONTO_LIVELLI
            if hasattr(HookType, 'CONFRONTO_LIVELLI')
            else HookType.DOMANDA_RETORICA,
            "leva_emotiva": LevEmotiva.CURIOSITA,
        },
    ],

    "intermedio": [
        {
            "id": "skill_modulare",
            "titolo": "Creare una skill modulare da zero",
            "concetto_chiave": "file di istruzioni separato dal contesto",
            "termine_tecnico": "skill",
            "spiegazione_termine": (
                "un file di testo con estensione .md "
                "che contiene istruzioni specifiche per un task. "
                "Claude le legge prima di rispondere."
            ),
            "esempio_specifico": (
                "crei un file chiamato email.md. "
                "Dentro scrivi le istruzioni per scrivere email. "
                "Poi crei sotto-file per ogni tipo: "
                "email-risposta.md, email-aggiornamento.md. "
                "Claude carica solo quello che serve."
            ),
            "beneficio_concreto": (
                "le istruzioni le scrivi una volta. "
                "Funzionano per sempre. "
                "Non ricominci da zero."
            ),
            "perche_funziona": (
                "un file unico con tutto dentro "
                "spreca contesto e produce output peggiori. "
                "La modularità carica solo quello che serve."
            ),
            "formati_consigliati": [1, 3],
            "hook_consigliato": HookType.AFFERMAZIONE_SHOCK,
            "leva_emotiva": LevEmotiva.RISPARMIO,
        },
        {
            "id": "yaml_front_matter",
            "titolo": "Struttura YAML front matter nelle skill",
            "concetto_chiave": "header strutturato per identificare la skill",
            "termine_tecnico": "YAML front matter",
            "spiegazione_termine": (
                "tre righe orizzontali, poi il nome della skill, "
                "poi la descrizione, poi altre tre righe. "
                "È l'intestazione che Claude usa per identificare "
                "quando attivare quella skill."
            ),
            "esempio_specifico": (
                "--- "
                "name: email-risposta "
                "description: risponde alle email in modo professionale "
                "--- "
                "poi sotto scrivi le istruzioni vere"
            ),
            "beneficio_concreto": (
                "Claude sa esattamente quando usare quella skill "
                "e quando no. Non devi dirglielo ogni volta."
            ),
            "perche_funziona": (
                "il front matter è come un'etichetta. "
                "Claude la legge e sa cosa contiene il file "
                "senza leggere tutto."
            ),
            "formati_consigliati": [1],
            "hook_consigliato": HookType.TUTORIAL_DIRETTO,
            "leva_emotiva": LevEmotiva.AUTORITA,
        },
        {
            "id": "knowledge_base_3livelli",
            "titolo": "Knowledge base a 3 livelli",
            "concetto_chiave": "struttura progressiva di contesto",
            "termine_tecnico": "knowledge base",
            "spiegazione_termine": (
                "la raccolta organizzata di documenti "
                "che Claude può leggere quando gli servono"
            ),
            "esempio_specifico": (
                "livello 1: un file markdown aggiornato ogni giorno. "
                "Livello 2: più file con un master che li coordina. "
                "Livello 3: cartella condivisa sul computer "
                "con sottocartelle per ogni area."
            ),
            "beneficio_concreto": (
                "al livello 3 Claude naviga da solo. "
                "Vai nella cartella giusto, "
                "trova il documento, risponde con contesto preciso."
            ),
            "perche_funziona": (
                "separare il contesto in livelli "
                "permette a Claude di caricare "
                "solo quello che serve in quel momento"
            ),
            "formati_consigliati": [4, 5],
            "hook_consigliato": HookType.TUTORIAL_DIRETTO,
            "leva_emotiva": LevEmotiva.CURIOSITA,
        },
    ],

    "avanzato": [
        {
            "id": "meta_prompting",
            "titolo": "Meta-prompting: usare l'AI per migliorare l'AI",
            "concetto_chiave": "loop di miglioramento con due chat",
            "termine_tecnico": "meta-prompting",
            "spiegazione_termine": (
                "usare una chat di Claude per migliorare "
                "le istruzioni che dai a un'altra chat di Claude"
            ),
            "esempio_specifico": (
                "Chat 1: scrivi il system prompt per le email. "
                "Chat 2: analizza quel system prompt, "
                "trovane i punti deboli, riscrivilo migliore. "
                "Ripeti il loop."
            ),
            "beneficio_concreto": (
                "ogni iterazione il system prompt diventa più preciso. "
                "Dopo 3-4 loop hai istruzioni che funzionano "
                "meglio di quelle scritte a mano."
            ),
            "perche_funziona": (
                "Claude conosce i pattern di istruzioni efficaci. "
                "Sa cosa manca. Sa cosa è ambiguo. "
                "Tu non devi saperlo. Gli chiedi tu."
            ),
            "formati_consigliati": [1, 3],
            "hook_consigliato": HookType.AFFERMAZIONE_SHOCK,
            "leva_emotiva": LevEmotiva.CURIOSITA,
        },
        {
            "id": "aggiornamenti_automatici",
            "titolo": "Claude con aggiornamenti automatici",
            "concetto_chiave": "contesto che si aggiorna da solo",
            "termine_tecnico": "cartella condivisa con automazioni",
            "spiegazione_termine": (
                "una cartella sul computer che riceve aggiornamenti "
                "automatici da tool o da te, "
                "e che Claude legge ogni volta che apri una sessione"
            ),
            "esempio_specifico": (
                "ogni volta che finisci una call, "
                "salvi 5 righe di appunti in quella cartella. "
                "La prossima volta che chiedi a Claude "
                "di scrivere un aggiornamento, "
                "lui sa già cosa è successo."
            ),
            "beneficio_concreto": (
                "non spieghi mai più cosa è successo di recente. "
                "Claude lo sa già. "
                "Lo ha letto dalla cartella."
            ),
            "perche_funziona": (
                "il contesto che cambia ogni giorno "
                "non può stare in un file statico. "
                "Deve aggiornarsi. "
                "La cartella condivisa è il meccanismo."
            ),
            "formati_consigliati": [1, 2],
            "hook_consigliato": HookType.DOMANDA_RETORICA,
            "leva_emotiva": LevEmotiva.FOMO,
        },
    ],

    "discovery": [
        {
            "id": "claude_flow",
            "titolo": "Agenti multipli in parallelo con Claude",
            "concetto_chiave": "orchestrazione di più istanze AI",
            "termine_tecnico": "agenti in parallelo",
            "spiegazione_termine": (
                "più istanze di Claude che lavorano "
                "contemporaneamente su parti diverse dello stesso task, "
                "coordinati da un agente principale"
            ),
            "esempio_specifico": (
                "un agente pianifica il task, "
                "un altro lo esegue, "
                "un altro lo controlla. "
                "Tutti in parallelo. "
                "Tutti condividono la stessa memoria."
            ),
            "beneficio_concreto": (
                "task complessi che richiedono ore "
                "vengono completati in minuti. "
                "Ogni agente è specializzato "
                "in una parte del processo."
            ),
            "perche_funziona": (
                "la specializzazione produce output migliori. "
                "Un agente che fa solo una cosa "
                "la fa meglio di uno che fa tutto."
            ),
            "formati_consigliati": [3, 2],
            "hook_consigliato": HookType.AFFERMAZIONE_SHOCK,
            "leva_emotiva": LevEmotiva.FOMO,
        },
    ],
}


# ═══════════════════════════════════════════════════════════════
# DATABASE — CTA TEMPLATES
# ═══════════════════════════════════════════════════════════════

CTA_TEMPLATES = {

    CTATipo.EBOOK: {
        "breve": (
            "Ho scritto 206 pagine su questa roba. "
            "Gratis. Link in bio."
        ),
        "media": (
            "Se vuoi capire bene tutto questo, "
            "ho scritto un ebook gratuito: Claude Code Mastery. "
            "206 pagine pratiche. Link in bio."
        ),
        "lunga": (
            "Ho messo tutto questo in un ebook gratuito. "
            "Si chiama Claude Code Mastery. "
            "206 pagine. Pratico. In italiano. "
            "Trovi il link in bio. "
            "Lo scarichi, ti arriva via email, "
            "e inizi a leggerlo in 2 minuti."
        ),
    },

    CTATipo.KEYWORD: {
        "breve": (
            "Commenta CLAUDE qui sotto "
            "e ti mando i file direttamente."
        ),
        "media": (
            "Se vuoi i file di cui ho parlato, "
            "commenta CLAUDE qui sotto "
            "e te li mando in privato."
        ),
        "lunga": (
            "Ho preparato i file completi per quello "
            "che ho mostrato in questo video. "
            "Se li vuoi, commenta CLAUDE qui sotto. "
            "Te li mando direttamente in privato."
        ),
    },

    CTATipo.SAVE: {
        "breve": "Salvalo. Ti servirà.",
        "media": (
            "Salvalo per quando ti serve davvero. "
            "È di quelli che riapri."
        ),
        "lunga": (
            "Salva questo video. "
            "La prossima volta che lavori su Claude Code "
            "e ti blocchi su questo punto, riapri e segui i passaggi."
        ),
    },

    CTATipo.CALL: {
        "breve": (
            "Faccio call gratuite su Claude Code. "
            "45 minuti. 1 a 1. Link in bio."
        ),
        "media": (
            "Se vuoi che ti mostri tutto questo "
            "sul tuo caso specifico, "
            "faccio call gratuite di 45 minuti. "
            "8 posti a settimana. Link in bio."
        ),
        "lunga": (
            "Faccio call gratuite di 45 minuti su Claude Code. "
            "1 a 1. Sul tuo caso specifico. "
            "Non un webinar. Una call vera. "
            "90% formazione, 10% pitch. Carte scoperte. "
            "8 posti a settimana. Quando finiscono, finiscono. "
            "Link in bio per scegliere il tuo slot."
        ),
    },
}


# ═══════════════════════════════════════════════════════════════
# DATABASE — MECCANISMI COMPETITOR
# ═══════════════════════════════════════════════════════════════

MECCANISMI = {
    "specificita_tecnica": {
        "descrizione": "Specificità tecnica come prova di competenza",
        "impatto": 10,
        "istruzione": (
            "Usa nomi di file esatti (.md, .yaml), "
            "comandi precisi (cd, mkdir), "
            "estensioni specifiche. "
            "Non dire 'crea un file'. "
            "Dì 'crea un file chiamato skill.md'."
        ),
    },
    "perche_prima_del_come": {
        "descrizione": "Perché prima del come",
        "impatto": 9,
        "istruzione": (
            "Spiega sempre il motivo PRIMA della soluzione. "
            "Il perché crea comprensione. "
            "Il come senza perché viene dimenticato."
        ),
    },
    "esempio_specifico": {
        "descrizione": "Esempio sempre specifico",
        "impatto": 9,
        "istruzione": (
            "Non usare mai esempi generici. "
            "Usa sempre un caso concreto con nome, "
            "tipo di file, e azione precisa."
        ),
    },
    "termine_spiegato": {
        "descrizione": "Ogni termine tecnico spiegato in 1 frase",
        "impatto": 8,
        "istruzione": (
            "Ogni volta che introduci un termine tecnico, "
            "aggiungilo subito una spiegazione in 1 frase. "
            "Non assumere che il viewer sappia."
        ),
    },
    "numeri_esatti": {
        "descrizione": "Numeri esatti mai arrotondati",
        "impatto": 9,
        "istruzione": (
            "Usa sempre numeri precisi. "
            "'206 pagine' non 'tante pagine'. "
            "'4 minuti' non 'poco tempo'. "
            "'75%' non 'molto'."
        ),
    },
    "reveal_progressivo": {
        "descrizione": "Reveal progressivo che mantiene la curiosità",
        "impatto": 7,
        "istruzione": (
            "Ogni step risolve qualcosa "
            "ma apre una nuova domanda. "
            "Il viewer deve chiedersi "
            "cosa c'è nello step successivo."
        ),
    },
    "confronto_ab": {
        "descrizione": "Confronto A vs B per comprensione rapida",
        "impatto": 8,
        "istruzione": (
            "Mostra la differenza tra "
            "il modo sbagliato e quello giusto. "
            "Prima/dopo. Con contesto/senza. "
            "Il contrasto crea comprensione immediata."
        ),
    },
}


# ═══════════════════════════════════════════════════════════════
# DATACLASSES
# ═══════════════════════════════════════════════════════════════

@dataclass
class ScriptInput:
    """Input per la generazione dello script."""
    argomento_id: str
    formato: Formato
    hook_type: HookType
    piattaforma: Piattaforma
    durata: Durata
    cta_tipo: CTATipo
    leva_emotiva: Optional[LevEmotiva] = None
    meccanismi_aggiuntivi: list = field(default_factory=list)
    note_extra: str = ""


@dataclass
class ScriptOutput:
    """Output completo generato."""
    titolo: str
    argomento_tecnico: str
    angolo: str
    leva_emotiva: str
    formato: str
    piattaforma: str
    durata_stimata: str
    meccanismi_selezionati: list
    hook_principale: str
    hook_varianti: list
    struttura_corpo: list
    cta: str
    caption_tiktok: str
    caption_ig: str
    note_registrazione: list
    prompt_per_claude: str
    timestamp: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )
    validazione: dict = field(default_factory=dict)


# ═══════════════════════════════════════════════════════════════
# CORE GENERATOR
# ═══════════════════════════════════════════════════════════════

class ScriptGenerator:
    """
    Genera script strutturati per il lancio Claude Code Mastery.
    """

    def __init__(self):
        self.argomenti_usati = []
        self._carica_storico()

    def _carica_storico(self):
        """Carica lo storico degli argomenti già usati."""
        storico_path = Path("storico_script.json")
        if storico_path.exists():
            with open(storico_path, "r", encoding="utf-8") as f:
                self.argomenti_usati = json.load(f)
        else:
            self.argomenti_usati = []

    def _salva_storico(self, argomento_id: str):
        """Salva l'argomento nello storico."""
        self.argomenti_usati.append({
            "id": argomento_id,
            "data": datetime.now().isoformat()
        })
        with open("storico_script.json", "w", encoding="utf-8") as f:
            json.dump(self.argomenti_usati, f, ensure_ascii=False, indent=2)

    def _get_argomento(self, argomento_id: str) -> dict:
        """Trova l'argomento per ID in tutti i livelli."""
        for livello in ARGOMENTI.values():
            for arg in livello:
                if arg["id"] == argomento_id:
                    return arg
        raise ValueError(f"Argomento '{argomento_id}' non trovato.")

    def _get_hook(
        self,
        hook_type: HookType,
        argomento: dict
    ) -> str:
        """Seleziona il hook più adatto."""
        template_list = HOOK_TEMPLATES.get(hook_type, [])
        if template_list:
            return random.choice(template_list)
        return f"C'è qualcosa su {argomento['titolo']} che non sai."

    def _get_hook_varianti(
        self,
        hook_type: HookType,
        argomento: dict
    ) -> list:
        """Genera 3 varianti hook con tipologie diverse."""
        varianti = []
        tipi_usati = [hook_type]

        for tipo in HookType:
            if tipo not in tipi_usati and len(varianti) < 3:
                template_list = HOOK_TEMPLATES.get(tipo, [])
                if template_list:
                    varianti.append({
                        "tipo": tipo.value,
                        "testo": random.choice(template_list)
                    })
                    tipi_usati.append(tipo)

        while len(varianti) < 3:
            tipo = random.choice(list(HookType))
            template_list = HOOK_TEMPLATES.get(tipo, [])
            if template_list:
                varianti.append({
                    "tipo": tipo.value,
                    "testo": random.choice(template_list)
                })

        return varianti[:3]

    def _genera_struttura_corpo(
        self,
        formato: Formato,
        argomento: dict,
        durata: Durata
    ) -> list:
        """Genera la struttura step-by-step del corpo."""

        steps_base = []

        # Apertura con PERCHÉ
        steps_base.append({
            "step": "PERCHÉ",
            "descrizione": (
                f"Apri con il motivo. "
                f"Perché '{argomento['concetto_chiave']}' è importante. "
                f"Usa: '{argomento['perche_funziona']}'"
            ),
            "durata_sec": 8 if durata == Durata.CORTO else 12,
        })

        # Spiegazione termine tecnico
        steps_base.append({
            "step": "DEFINIZIONE",
            "descrizione": (
                f"Introduce il termine '{argomento['termine_tecnico']}' "
                f"e spiegalo subito in 1 frase: "
                f"'{argomento['spiegazione_termine']}'"
            ),
            "durata_sec": 8 if durata == Durata.CORTO else 10,
        })

        # Esempio specifico
        steps_base.append({
            "step": "ESEMPIO",
            "descrizione": (
                f"Dai l'esempio specifico: "
                f"'{argomento['esempio_specifico']}'. "
                f"Usa nomi di file esatti se disponibili."
            ),
            "durata_sec": 12 if durata == Durata.CORTO else 18,
        })

        # Beneficio concreto
        steps_base.append({
            "step": "BENEFICIO",
            "descrizione": (
                f"Chiudi il corpo con il beneficio concreto: "
                f"'{argomento['beneficio_concreto']}'. "
                f"Frase corta. Impatto diretto."
            ),
            "durata_sec": 5 if durata == Durata.CORTO else 8,
        })

        # Aggiusta per formato
        if formato == Formato.LISTA_RISORSE:
            steps_base.insert(2, {
                "step": "LISTA",
                "descrizione": (
                    "Inserisci lista di 5-7 elementi con nomi specifici. "
                    "Ogni elemento: nome + cosa fa in 3-4 parole."
                ),
                "durata_sec": 20 if durata != Durata.CORTO else 15,
            })

        if formato == Formato.CONFRONTO_LIVELLI:
            steps_base.insert(1, {
                "step": "LIVELLO BASE",
                "descrizione": (
                    "Descrivi il livello base (quello sbagliato o meno efficace). "
                    "Sii specifico. Il viewer si deve riconoscere."
                ),
                "durata_sec": 8,
            })
            steps_base.insert(2, {
                "step": "LIVELLO AVANZATO",
                "descrizione": (
                    "Descrivi il livello avanzato (quello giusto). "
                    "Contrasto netto col precedente."
                ),
                "durata_sec": 10,
            })

        if formato == Formato.DEMO_WOW:
            steps_base.insert(0, {
                "step": "WOW INIZIALE",
                "descrizione": (
                    "Prima il risultato wow. "
                    "Poi spieghi come. "
                    "Mostra/descrivi il risultato finale "
                    "nei primi 5 secondi dopo l'hook."
                ),
                "durata_sec": 5,
            })

        return steps_base

    def _seleziona_meccanismi(
        self,
        formato: Formato,
        argomento: dict
    ) -> list:
        """Seleziona i meccanismi più adatti."""
        meccanismi_selezionati = [
            "specificita_tecnica",
            "perche_prima_del_come",
            "esempio_specifico",
            "termine_spiegato",
        ]

        if formato in [Formato.CONFRONTO_LIVELLI, Formato.LISTA_RISORSE]:
            meccanismi_selezionati.append("confronto_ab")

        if formato == Formato.DEMO_WOW:
            meccanismi_selezionati.append("reveal_progressivo")

        return [
            {
                "id": m_id,
                "descrizione": MECCANISMI[m_id]["descrizione"],
                "istruzione": MECCANISMI[m_id]["istruzione"],
            }
            for m_id in meccanismi_selezionati
            if m_id in MECCANISMI
        ]

    def _genera_caption_tiktok(
        self,
        argomento: dict,
        hook: str,
        cta: str
    ) -> str:
        """Genera la caption per TikTok."""
        return (
            f"{hook}\n\n"
            f"{argomento['perche_funziona'].capitalize()}.\n\n"
            f"La soluzione: {argomento['concetto_chiave']}.\n"
            f"{argomento['beneficio_concreto']}\n\n"
            f"{cta}\n\n"
            f"#ClaudeCode #AIBuilder #Tutorial "
            f"#Automazione #DigitalEmpire"
        )

    def _genera_caption_ig(
        self,
        argomento: dict,
        hook: str,
        cta: str
    ) -> str:
        """Genera la caption per Instagram (prima riga ≤125 char)."""
        prima_riga = hook[:125] if len(hook) > 125 else hook
        return (
            f"{prima_riga}\n\n"
            f"{argomento['perche_funziona'].capitalize()}.\n\n"
            f"La soluzione concreta:\n"
            f"{argomento['esempio_specifico']}\n\n"
            f"Risultato: {argomento['beneficio_concreto']}\n\n"
            f"⬇️ {cta}\n\n"
            f"#ClaudeCode #AIBuilder #Tutorial "
            f"#ContextEngineering #DigitalEmpire"
        )

    def _genera_note_registrazione(
        self,
        formato: Formato,
        durata: Durata,
        hook_type: HookType
    ) -> list:
        """Genera note pratiche per la registrazione."""
        note = [
            "Face-to-camera. Nessun screen recording necessario.",
            "Prima frase: inizia a parlare immediatamente. "
            "Zero silenzio iniziale.",
        ]

        if hook_type == HookType.AFFERMAZIONE_SHOCK:
            note.append(
                "Tono nell'hook: serio, diretto. "
                "Nessun sorriso fino alla fine del hook."
            )
        elif hook_type == HookType.DOMANDA_RETORICA:
            note.append(
                "Tono nell'hook: leggermente interrogativo. "
                "Piccola pausa dopo la domanda (0.5 sec)."
            )
        elif hook_type == HookType.TUTORIAL_DIRETTO:
            note.append(
                "Tono nell'hook: energico e sicuro. "
                "Sai già dove stai andando."
            )

        if durata == Durata.CORTO:
            note.append(
                "Ritmo veloce. Ogni frase di fila. "
                "Pause solo sui punti chiave."
            )
        elif durata == Durata.LUNGO:
            note.append(
                "Ritmo variabile. "
                "Rallenta sui concetti tecnici. "
                "Accelera sulle transizioni."
            )

        note.append(
            "CTA finale: stessa energia del corpo. "
            "Non cambiare tono. Non sembrare un venditore."
        )

        return note

    def _genera_prompt_per_claude(
        self,
        argomento: dict,
        output: ScriptOutput
    ) -> str:
        """Genera il prompt pronto da dare a Claude per scrivere lo script."""
        meccanismi_str = "\n".join([
            f"- {m['descrizione']}: {m['istruzione']}"
            for m in output.meccanismi_selezionati
        ])

        struttura_str = "\n".join([
            f"{i+1}. [{s['step']} — {s['durata_sec']}s] "
            f"{s['descrizione']}"
            for i, s in enumerate(output.struttura_corpo)
        ])

        return f"""Scrivi uno script video per {output.piattaforma}.

ARGOMENTO: {output.argomento_tecnico}
ANGOLO: {output.angolo}
LEVA EMOTIVA: {output.leva_emotiva}
FORMATO: {output.formato}
DURATA TARGET: {output.durata_stimata}

HOOK PRINCIPALE DA USARE:
"{output.hook_principale}"

STRUTTURA DEL CORPO:
{struttura_str}

MECCANISMI DA APPLICARE:
{meccanismi_str}

TERMINE TECNICO DA SPIEGARE:
"{argomento['termine_tecnico']}" → "{argomento['spiegazione_termine']}"

ESEMPIO SPECIFICO DA USARE:
{argomento['esempio_specifico']}

BENEFICIO CONCRETO DA CHIUDERE:
{argomento['beneficio_concreto']}

CTA FINALE:
{output.cta}

REGOLE:
- Zero saluti all'inizio
- Frasi max 12 parole
- Un concetto principale
- Il perché prima del come
- Tono: amico tecnico, non professore
- La CTA deve avere lo stesso tono del corpo
- Output: solo lo script parola per parola, pronto da leggere

HOOK VARIANTI (per A/B test):
{chr(10).join([f"- [{v['tipo']}] {v['testo']}" for v in output.hook_varianti])}"""

    def _valida_output(self, output: ScriptOutput) -> dict:
        """Valida l'output prima di restituirlo."""
        errori = []
        warning = []

        if not output.hook_principale:
            errori.append("Hook mancante")

        if len(output.hook_principale) > 80:
            warning.append(
                f"Hook lungo ({len(output.hook_principale)} char). "
                f"Target: <80 char."
            )

        if not output.struttura_corpo:
            errori.append("Struttura corpo vuota")

        if len(output.struttura_corpo) > 6:
            warning.append(
                f"Troppi step nel corpo ({len(output.struttura_corpo)}). "
                f"Max consigliato: 5."
            )

        if not output.cta:
            errori.append("CTA mancante")

        if not output.meccanismi_selezionati:
            warning.append("Nessun meccanismo selezionato")

        return {
            "valido": len(errori) == 0,
            "errori": errori,
            "warning": warning,
            "score": max(0, 10 - len(errori) * 3 - len(warning)),
        }

    def genera(self, input_data: ScriptInput) -> ScriptOutput:
        """Genera lo script completo dall'input."""

        # Recupera argomento
        argomento = self._get_argomento(input_data.argomento_id)

        # Seleziona componenti
        hook = self._get_hook(input_data.hook_type, argomento)
        hook_varianti = self._get_hook_varianti(
            input_data.hook_type, argomento
        )
        struttura = self._genera_struttura_corpo(
            input_data.formato, argomento, input_data.durata
        )
        meccanismi = self._seleziona_meccanismi(
            input_data.formato, argomento
        )

        # Determina CTA
        cta_size = (
            "breve" if input_data.durata == Durata.CORTO
            else "media" if input_data.durata == Durata.MEDIO
            else "lunga"
        )
        cta = CTA_TEMPLATES[input_data.cta_tipo][cta_size]

        # Genera durata stimata
        durata_map = {
            Durata.CORTO: "30-45 secondi",
            Durata.MEDIO: "45-70 secondi",
            Durata.LUNGO: "70-90 secondi",
        }

        # Genera caption
        caption_tiktok = self._genera_caption_tiktok(
            argomento, hook, cta
        )
        caption_ig = self._genera_caption_ig(
            argomento, hook, cta
        )

        # Genera note
        note = self._genera_note_registrazione(
            input_data.formato,
            input_data.durata,
            input_data.hook_type
        )

        # Costruisce output
        output = ScriptOutput(
            titolo=argomento["titolo"],
            argomento_tecnico=argomento["concetto_chiave"],
            angolo=(
                f"Funzione poco usata — "
                f"'{argomento['concetto_chiave']}'"
            ),
            leva_emotiva=(
                input_data.leva_emotiva.value
                if input_data.leva_emotiva
                else argomento["leva_emotiva"].value
            ),
            formato=input_data.formato.name,
            piattaforma=input_data.piattaforma.value,
            durata_stimata=durata_map[input_data.durata],
            meccanismi_selezionati=meccanismi,
            hook_principale=hook,
            hook_varianti=hook_varianti,
            struttura_corpo=struttura,
            cta=cta,
            caption_tiktok=caption_tiktok,
            caption_ig=caption_ig,
            note_registrazione=note,
            prompt_per_claude="",
        )

        # Genera prompt per Claude
        output.prompt_per_claude = self._genera_prompt_per_claude(
            argomento, output
        )

        # Valida
        output.validazione = self._valida_output(output)

        # Salva storico
        self._salva_storico(input_data.argomento_id)

        return output


# ═══════════════════════════════════════════════════════════════
# FORMATTER — OUTPUT LEGGIBILE
# ═══════════════════════════════════════════════════════════════

class OutputFormatter:
    """Formatta l'output in modo leggibile."""

    @staticmethod
    def formatta_console(output: ScriptOutput) -> str:
        """Formatta per output su console."""
        separatore = "═" * 60
        linea = "─" * 60

        righe = [
            f"\n{separatore}",
            f"  SCRIPT GENERATO — {output.titolo.upper()}",
            f"{separatore}",
            f"\n  ARGOMENTO:     {output.argomento_tecnico}",
            f"  ANGOLO:        {output.angolo}",
            f"  LEVA:          {output.leva_emotiva}",
            f"  FORMATO:       {output.formato}",
            f"  PIATTAFORMA:   {output.piattaforma}",
            f"  DURATA:        {output.durata_stimata}",
            f"\n{linea}",
            f"  HOOK PRINCIPALE",
            f"{linea}",
            f'  "{output.hook_principale}"',
            f"\n{linea}",
            f"  HOOK VARIANTI (A/B TEST)",
            f"{linea}",
        ]

        for i, v in enumerate(output.hook_varianti, 1):
            righe.append(f"  {i}. [{v['tipo']}] {v['testo']}")

        righe += [
            f"\n{linea}",
            f"  STRUTTURA CORPO",
            f"{linea}",
        ]

        for step in output.struttura_corpo:
            righe.append(
                f"  [{step['step']} — {step['durata_sec']}s]"
            )
            righe.append(f"  {step['descrizione']}")
            righe.append("")

        righe += [
            f"{linea}",
            f"  MECCANISMI DA APPLICARE",
            f"{linea}",
        ]
        for m in output.meccanismi_selezionati:
            righe.append(f"  ✓ {m['descrizione']}")

        righe += [
            f"\n{linea}",
            f"  CTA FINALE",
            f"{linea}",
            f"  {output.cta}",
            f"\n{linea}",
            f"  NOTE DI REGISTRAZIONE",
            f"{linea}",
        ]
        for nota in output.note_registrazione:
            righe.append(f"  • {nota}")

        righe += [
            f"\n{linea}",
            f"  CAPTION TIKTOK",
            f"{linea}",
            output.caption_tiktok,
            f"\n{linea}",
            f"  CAPTION INSTAGRAM",
            f"{linea}",
            output.caption_ig,
            f"\n{linea}",
            f"  PROMPT PER CLAUDE",
            f"{linea}",
            output.prompt_per_claude,
        ]

        # Validazione
        val = output.validazione
        stato = "✅ VALIDO" if val["valido"] else "❌ ERRORI PRESENTI"
        righe += [
            f"\n{linea}",
            f"  VALIDAZIONE — {stato} (Score: {val['score']}/10)",
            f"{linea}",
        ]
        if val["errori"]:
            for e in val["errori"]:
                righe.append(f"  🚫 ERRORE: {e}")
        if val["warning"]:
            for w in val["warning"]:
                righe.append(f"  ⚠️  WARNING: {w}")
        if not val["errori"] and not val["warning"]:
            righe.append("  Nessun problema rilevato.")

        righe.append(f"\n{separatore}\n")
        return "\n".join(righe)

    @staticmethod
    def salva_json(output: ScriptOutput, path: str):
        """Salva output in JSON."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(output), f, ensure_ascii=False, indent=2)
        print(f"✅ Salvato: {path}")


# ═══════════════════════════════════════════════════════════════
# INTERFACCIA INTERATTIVA
# ═══════════════════════════════════════════════════════════════

def interfaccia_interattiva() -> ScriptInput:
    """Guida l'utente nella creazione dell'input."""

    print("\n" + "═" * 60)
    print("  SCRIPT GENERATOR — Claude Code Mastery")
    print("═" * 60)

    # Lista argomenti disponibili
    print("\n  ARGOMENTI DISPONIBILI:")
    print("  " + "─" * 40)
    for livello, argomenti in ARGOMENTI.items():
        print(f"\n  [{livello.upper()}]")
        for arg in argomenti:
            print(f"  • {arg['id']}: {arg['titolo']}")

    argomento_id = input(
        "\n  Inserisci ID argomento (o INVIO per random): "
    ).strip()

    if not argomento_id:
        tutti = [
            arg for livello in ARGOMENTI.values()
            for arg in livello
        ]
        argomento_id = random.choice(tutti)["id"]
        print(f"  → Selezionato: {argomento_id}")

    # Formato
    print("\n  FORMATI:")
    for f in Formato:
        print(f"  {f.value}. {f.name}")
    formato_input = input("  Scegli formato (1-5, INVIO=1): ").strip()
    formato = Formato(int(formato_input)) if formato_input else Formato.TUTORIAL_PRATICO

    # Hook
    print("\n  HOOK TYPE:")
    print("  A. Affermazione shock")
    print("  B. Domanda retorica")
    print("  C. Tutorial diretto")
    hook_input = input("  Scegli hook (A/B/C, INVIO=C): ").strip().upper()
    hook_map = {"A": HookType.AFFERMAZIONE_SHOCK,
                "B": HookType.DOMANDA_RETORICA,
                "C": HookType.TUTORIAL_DIRETTO}
    hook_type = hook_map.get(hook_input, HookType.TUTORIAL_DIRETTO)

    # Durata
    print("\n  DURATA:")
    print("  1. Corto (30-45s)")
    print("  2. Medio (45-70s)")
    print("  3. Lungo (70-90s)")
    durata_input = input("  Scegli durata (1/2/3, INVIO=2): ").strip()
    durata_map = {"1": Durata.CORTO, "2": Durata.MEDIO, "3": Durata.LUNGO}
    durata = durata_map.get(durata_input, Durata.MEDIO)

    # CTA
    print("\n  CTA:")
    print("  1. Ebook gratuito")
    print("  2. Keyword comment")
    print("  3. Save")
    print("  4. Call gratuita")
    cta_input = input("  Scegli CTA (1/2/3/4, INVIO=1): ").strip()
    cta_map = {
        "1": CTATipo.EBOOK,
        "2": CTATipo.KEYWORD,
        "3": CTATipo.SAVE,
        "4": CTATipo.CALL,
    }
    cta_tipo = cta_map.get(cta_input, CTATipo.EBOOK)

    # Piattaforma
    print("\n  PIATTAFORMA:")
    print("  1. TikTok")
    print("  2. Instagram")
    print("  3. Entrambe")
    piatt_input = input("  Scegli piattaforma (1/2/3, INVIO=3): ").strip()
    piatt_map = {
        "1": Piattaforma.TIKTOK,
        "2": Piattaforma.INSTAGRAM,
        "3": Piattaforma.ENTRAMBE,
    }
    piattaforma = piatt_map.get(piatt_input, Piattaforma.ENTRAMBE)

    return ScriptInput(
        argomento_id=argomento_id,
        formato=formato,
        hook_type=hook_type,
        piattaforma=piattaforma,
        durata=durata,
        cta_tipo=cta_tipo,
    )


# ═══════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Script Generator — Claude Code Mastery"
    )
    parser.add_argument(
        "--topic",
        help="ID argomento (es: claude_md_intro)"
    )
    parser.add_argument(
        "--formato",
        type=int,
        choices=[1, 2, 3, 4, 5],
        default=1,
        help="Formato script (1-5)"
    )
    parser.add_argument(
        "--hook",
        choices=["A", "B", "C"],
        default="C",
        help="Tipo hook"
    )
    parser.add_argument(
        "--durata",
        choices=["corto", "medio", "lungo"],
        default="medio",
        help="Durata target"
    )
    parser.add_argument(
        "--cta",
        choices=["ebook", "keyword", "save", "call"],
        default="ebook",
        help="Tipo CTA"
    )
    parser.add_argument(
        "--piattaforma",
        choices=["tiktok", "ig_reel", "entrambe"],
        default="entrambe",
        help="Piattaforma target"
    )
    parser.add_argument(
        "--batch",
        type=int,
        help="Genera N script in batch (argomenti random)"
    )
    parser.add_argument(
        "--output",
        help="Salva output in JSON (path)"
    )
    parser.add_argument(
        "--interattivo",
        action="store_true",
        help="Modalità interattiva guidata"
    )

    args = parser.parse_args()
    generator = ScriptGenerator()
    formatter = OutputFormatter()

    # Modalità interattiva
    if args.interattivo or len(sys.argv) == 1:
        script_input = interfaccia_interattiva()
        output = generator.genera(script_input)
        print(formatter.formatta_console(output))
        if args.output:
            formatter.salva_json(
                output,
                args.output
            )
        return

    # Modalità batch
    if args.batch:
        tutti_argomenti = [
            arg for livello in ARGOMENTI.values()
            for arg in livello
        ]
        selezionati = random.sample(
            tutti_argomenti,
            min(args.batch, len(tutti_argomenti))
        )

        for i, arg in enumerate(selezionati, 1):
            print(f"\n[SCRIPT {i}/{args.batch}]")
            script_input = ScriptInput(
                argomento_id=arg["id"],
                formato=Formato(args.formato),
                hook_type={"A": HookType.AFFERMAZIONE_SHOCK,
                           "B": HookType.DOMANDA_RETORICA,
                           "C": HookType.TUTORIAL_DIRETTO}[args.hook],
                piattaforma=Piattaforma(args.piattaforma),
                durata=Durata(args.durata),
                cta_tipo=CTATipo(args.cta),
            )
            output = generator.genera(script_input)
            print(formatter.formatta_console(output))

            if args.output:
                path = f"{args.output.replace('.json', '')}_{i}.json"
                formatter.salva_json(output, path)
        return

    # Modalità singola
    if not args.topic:
        tutti = [
            arg for livello in ARGOMENTI.values()
            for arg in livello
        ]
        args.topic = random.choice(tutti)["id"]
        print(f"Argomento selezionato: {args.topic}")

    script_input = ScriptInput(
        argomento_id=args.topic,
        formato=Formato(args.formato),
        hook_type={"A": HookType.AFFERMAZIONE_SHOCK,
                   "B": HookType.DOMANDA_RETORICA,
                   "C": HookType.TUTORIAL_DIRETTO}[args.hook],
        piattaforma=Piattaforma(args.piattaforma),
        durata=Durata(args.durata),
        cta_tipo=CTATipo(args.cta),
    )

    output = generator.genera(script_input)
    print(formatter.formatta_console(output))

    if args.output:
        formatter.salva_json(output, args.output)


if __name__ == "__main__":
    main()