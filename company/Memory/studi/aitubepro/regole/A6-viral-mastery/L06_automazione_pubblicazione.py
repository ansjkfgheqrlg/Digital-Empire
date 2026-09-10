# -*- coding: utf-8 -*-
"""regole/A6-viral-mastery/L06_automazione_pubblicazione.py

Fonte: AI TUBE PRO / A6 Viral Mastery / L06 "Automazione della pubblicazione Video su YouTube"
(07:20, id a48bfb41-2b71-4be9-a9a4-4141c6ee0e23, docente Pietro Gangemi).

ATTENZIONE PRIMA DI APPLICARE: la fabbrica imposta SEMPRE "Privato" in
youtube_uploader_playwright.py NON per un difetto dimenticato ma per una policy dichiarata
altrove (YOUTUBE-AUTOMATION-FACTORY/.claude/commands/avvia-yt.md:82 - "Visibilita' sempre
Private, mai pubblico senza conferma esplicita di Max per quel video"). Verificato prima di
scrivere le regole sotto, per non proporre di rimuovere un gate di sicurezza voluto. Le regole
NON toccano quel gate: aggiungono lo scheduling data-driven come azione che avviene DOPO
l'approvazione di Max, non al posto di essa. Registrato l'arbitrato in CONFLITTI.md come C-008.
"""

FONTE = "AI TUBE PRO / A6 Viral Mastery / L06"
LEZIONE = "Automazione della pubblicazione Video su YouTube"

REGOLE = [
    {
        "id": "A6-L06-01",
        "tipo": "funzione",
        "regola": ("Quando Max approva un video per la pubblicazione, l'uploader dovrebbe poter "
                   "programmarlo (visibilita' 'Programmato', data/ora scelta) invece di lasciarlo "
                   "solo 'Privato' in attesa di un secondo intervento manuale per renderlo "
                   "pubblico. Oggi, anche dopo l'approvazione, non esiste un passo che porti un "
                   "video da privato a pubblico/programmato senza uscire dalla fabbrica e agire a "
                   "mano su YouTube Studio - il gap misurato da BASELINE.md ('solo 2 video su 8 "
                   "hanno una destinazione tracciata') e' anche qui."),
        "prova": ("parlato @ 03:44-04:26 (percorso Visibilita' -> Programmazione -> data/ora); "
                  "schermo frame-125.png @ 4:08 e frame-140.png @ 4:38 (elenco contenuti con "
                  "righe in stato 'Programmato'); codice: youtube_uploader_playwright.py:432-451 "
                  "imposta sempre Privato, .claude/commands/avvia-yt.md:82 conferma che e' "
                  "policy dichiarata, non svista"),
        "fonte": "entrambi",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "alto",
        "misura": ("esiste un percorso (funzione o comando) che, dato un video gia' approvato da "
                   "Max, lo programma su YouTube con data/ora invece di lasciarlo privato senza "
                   "seguito; il gate di conferma esplicita di Max resta INTATTO, cambia solo "
                   "cosa succede tecnicamente dopo il suo sì"),
    },
    {
        "id": "A6-L06-02",
        "tipo": "funzione",
        "regola": ("L'orario di pubblicazione, quando si programma, dovrebbe derivare dagli "
                   "analytics reali del canale (sezione Pubblico: quando e' online), non essere "
                   "fissato a caso o per convenzione. La fabbrica oggi non legge mai questo dato."),
        "prova": "parlato @ 02:15-03:19 (\"su YouTube Studio [...] Analytics nella sezione pubblico [...] a che ora e in quale giorno il nostro pubblico e' presente\")",
        "fonte": "parlato",
        "tocca": "02-AUTOMAZIONI-E-SCRIPTS/",
        "azione": "costruisci",
        "binario": "B",
        "rischio": "medio",
        "misura": ("nuova funzione orario_ottimale_da_analytics(canale) che restituisce almeno "
                   "una fascia oraria; finche' l'accesso via Playwright agli Analytics non e' "
                   "collaudato, la funzione puo' restituire un default dichiarato come tale, "
                   "mai un numero inventato spacciato per dato"),
    },
    {
        "id": "A6-L06-03",
        "tipo": "parametro",
        "regola": ("Il piano editoriale/coda di produzione dovrebbe distinguere contenuto "
                   "pianificabile (evergreen, va bene programmato in batch) da contenuto "
                   "trend/flash (va pubblicato subito, mai schedulato in anticipo) — oggi non "
                   "esiste nessun campo che rappresenti questa distinzione."),
        "prova": "parlato @ 06:14-06:57 (esempio: notizia improvvisa, \"non e' che lo posso programmare la settimana dopo\")",
        "fonte": "parlato",
        "tocca": "memory/coda_produzione.json",
        "azione": "costruisci",
        "binario": "A",
        "rischio": "basso",
        "misura": "il piano editoriale ha un campo tipo_pubblicazione (programmato | immediato) valorizzato per ogni riga",
    },
]
