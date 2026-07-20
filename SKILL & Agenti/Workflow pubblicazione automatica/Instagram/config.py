"""Instagram configuration for the Digital Empire legacy browser publisher."""
import os

IG_USERNAME = os.environ.get("DIGITAL_EMPIRE_IG_USERNAME", "digitalempireagency.e")
IG_PASSWORD = os.environ.get("DIGITAL_EMPIRE_IG_PASSWORD", "")

COPYWRITER_SYSTEM_PROMPT = """
Scrivi una caption perfetta, umanizzata ed emozionante per un carosello Instagram.
Il tuo obiettivo è fare leva sul problema del cliente e proporre una soluzione verificabile.
Struttura: 90% formazione e valore concreto, 10% call to action.
"""

DEFAULT_HASHTAGS = "#digitalempire #cro #landingpage #ottimizzazione #business #imprenditoria"
