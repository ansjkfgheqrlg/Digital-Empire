#!/usr/bin/env python3
"""
generate_skill.py — CC-Master v2.0
Genera lo scaffolding completo per una nuova skill Claude Code.

Uso:
  python generate_skill.py --name mia-skill --description "Descrizione breve" --triggers "frase1,frase2,frase3"
  python generate_skill.py --name mia-skill --description "..." --triggers "..." --has-scripts --has-references
  python generate_skill.py --name mia-skill --description "..." --triggers "..." --output-path "C:\\percorso\\custom"
"""

import argparse
import os
import re
import sys


def sanitize_name(name: str) -> str:
    """Converte il nome in formato lowercase-hyphens."""
    name = name.lower().strip()
    name = re.sub(r'[^a-z0-9\-]', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')


def build_description(name: str, description: str, triggers: list[str]) -> str:
    """Costruisce una description 'pushy' seguendo il pattern cc-master."""
    trigger_str = ', '.join(f'"{t.strip()}"' for t in triggers)
    return (
        f"{description}. "
        f"Usa questa skill quando l'utente vuole {description.lower().rstrip('.')}. "
        f"Trigger: {trigger_str}. "
        f"Output: risultato strutturato e production-ready."
    )


def generate_skill_md(name: str, description: str, triggers: list[str],
                      has_scripts: bool, has_references: bool) -> str:
    """Genera il contenuto del file SKILL.md."""
    trigger_list = '\n'.join(f'- "{t.strip()}"' for t in triggers)

    scripts_section = ""
    if has_scripts:
        scripts_section = """
## Esecuzione Script

Esegui lo script principale per generare output strutturato:

```bash
python scripts\\main.py --input "dati" --output "output.md"
```
"""

    references_section = ""
    if has_references:
        references_section = """
## Dati di Riferimento

Questa skill usa i seguenti file di riferimento:
- `references\\framework.md` — framework e linee guida
- `references\\examples.md` — esempi concreti

Leggi questi file prima di produrre l'output per garantire coerenza.
"""

    return f"""---
name: {name}
description: {description}
---

## Obiettivo

[Descrivi qui l'obiettivo principale della skill in 2-3 frasi. Cosa trasforma? Da cosa a cosa?]

## Quando Usare

Attiva questa skill quando l'utente usa una di queste frasi (o varianti simili):

{trigger_list}

**Non usare per:** [delimita qui cosa questa skill NON deve fare]

## Prerequisiti

[Lista le informazioni o condizioni necessarie prima di eseguire la skill]
- [ ] [prerequisito 1]
- [ ] [prerequisito 2]
{references_section}
## Processo

Segui questi step nell'ordine indicato:

1. **[STEP 1 — ANALISI]**
   - [Cosa analizzare]
   - [Come analizzarlo]

2. **[STEP 2 — ELABORAZIONE]**
   - [Cosa elaborare]
   - [Criteri di qualità]

3. **[STEP 3 — OUTPUT]**
   - [Come strutturare l'output]
   - [Formato finale]

4. **[STEP 4 — VERIFICA]**
   - [ ] [criterio 1]
   - [ ] [criterio 2]
   - [ ] [criterio 3]
{scripts_section}
## Output

**Formato:** [Markdown | JSON | file .md | altro]
**Struttura:** [descrivi la struttura dell'output prodotto]
**Qualità:** [standard minimi accettabili]

---

## Installazione

Copia l'intera cartella `{name}/` in:

**Globale** (disponibile in tutti i progetti):
```
C:\\Users\\Utente\\.claude\\skills\\
```

**Locale** (solo questo progetto):
```
.claude\\skills\\   ← nella root del progetto
```

Riavvia Claude Code per attivare la skill.
"""


def generate_main_py() -> str:
    """Genera il template dello script Python principale."""
    return '''#!/usr/bin/env python3
"""
main.py — Script principale della skill
Uso: python main.py --input "dati" --output "output.md"
"""
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Skill script principale')
    parser.add_argument('--input', required=True, help='Dati di input')
    parser.add_argument('--output', default='output.md', help='File di output (default: output.md)')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown',
                        help='Formato output (default: markdown)')
    args = parser.parse_args()

    print(f"[INFO] Elaborazione input: {args.input}")

    result = process(args.input, args.format)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"[OK] Output salvato in: {args.output}")


def process(input_data: str, format: str) -> str:
    """
    Logica principale della skill.
    TODO: Implementa qui la logica specifica della skill.
    """
    if format == 'json':
        import json
        return json.dumps({"input": input_data, "output": "TODO"}, indent=2, ensure_ascii=False)
    else:
        return f"""# Output

## Input Ricevuto
{input_data}

## Risultato
[TODO: implementa la logica di elaborazione qui]

---
*Generato da skill script*
"""


if __name__ == '__main__':
    main()
'''


def generate_framework_md(skill_name: str) -> str:
    """Genera il file framework.md di riferimento."""
    return f"""# Framework — {skill_name}

## Linee Guida

[Inserisci qui le linee guida specifiche per questa skill]

## Tono e Stile

- **Tono:** [formale / informale / professionale]
- **Persona:** [in quale persona scrivere l'output]
- **Lunghezza:** [breve / media / dettagliata]

## Struttura Output

[Descrivi la struttura esatta dell'output che questa skill deve produrre]

## Esempi

### Esempio 1 — Input
[input di esempio]

### Esempio 1 — Output
[output corrispondente di esempio]

## Vincoli

**Sempre:**
- [vincolo positivo 1]
- [vincolo positivo 2]

**Mai:**
- [vincolo negativo 1]
- [vincolo negativo 2]
"""


def main():
    parser = argparse.ArgumentParser(
        description='Genera scaffolding completo per una nuova skill Claude Code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python generate_skill.py --name report-settimanale --description "Genera report settimanale KPI" --triggers "fai il report,report settimanale,weekly report"
  python generate_skill.py --name analisi-competitor --description "Analizza competitor" --triggers "analizza competitor,ricerca competitor" --has-scripts --has-references
        """
    )
    parser.add_argument('--name', required=True, help='Nome della skill (verrà convertito in lowercase-hyphens)')
    parser.add_argument('--description', required=True, help='Descrizione breve della skill (1-2 frasi)')
    parser.add_argument('--triggers', required=True, help='Frasi trigger separate da virgola (es: "frase1,frase2,frase3")')
    parser.add_argument('--has-scripts', action='store_true', help='Crea cartella scripts/ con template Python')
    parser.add_argument('--has-references', action='store_true', help='Crea cartella references/ con framework.md')
    parser.add_argument('--output-path', default=None, help='Percorso di destinazione (default: cartella corrente)')

    args = parser.parse_args()

    # Sanitizza nome
    name = sanitize_name(args.name)
    if name != args.name:
        print(f"[INFO] Nome convertito: '{args.name}' → '{name}'")

    # Parsing triggers
    triggers = [t.strip() for t in args.triggers.split(',') if t.strip()]
    if len(triggers) < 2:
        print("[WARN] Raccomandati almeno 3 trigger phrases per una description efficace")

    # Determina output path
    base_path = args.output_path or os.getcwd()
    skill_path = os.path.join(base_path, name)

    if os.path.exists(skill_path):
        print(f"[ERROR] La cartella '{skill_path}' esiste già. Scegli un nome diverso o rimuovi prima la cartella.")
        sys.exit(1)

    # Crea struttura cartelle
    os.makedirs(skill_path)
    if args.has_scripts:
        os.makedirs(os.path.join(skill_path, 'scripts'))
    if args.has_references:
        os.makedirs(os.path.join(skill_path, 'references'))

    # Genera description completa
    full_description = build_description(name, args.description, triggers)

    # Scrivi SKILL.md
    skill_md_content = generate_skill_md(name, full_description, triggers,
                                          args.has_scripts, args.has_references)
    with open(os.path.join(skill_path, 'SKILL.md'), 'w', encoding='utf-8') as f:
        f.write(skill_md_content)

    # Scrivi scripts/main.py (se richiesto)
    if args.has_scripts:
        with open(os.path.join(skill_path, 'scripts', 'main.py'), 'w', encoding='utf-8') as f:
            f.write(generate_main_py())

    # Scrivi references/framework.md (se richiesto)
    if args.has_references:
        with open(os.path.join(skill_path, 'references', 'framework.md'), 'w', encoding='utf-8') as f:
            f.write(generate_framework_md(name))

    # Report finale
    print(f"\n✓ Skill '{name}' creata con successo!")
    print(f"\nStruttura creata in: {skill_path}")
    print(f"  {name}/")
    print(f"  └── SKILL.md")
    if args.has_scripts:
        print(f"  └── scripts/")
        print(f"      └── main.py")
    if args.has_references:
        print(f"  └── references/")
        print(f"      └── framework.md")
    print(f"\nProssimi passi:")
    print(f"  1. Apri {skill_path}\\SKILL.md e completa le sezioni [TODO]")
    if args.has_scripts:
        print(f"  2. Implementa la logica in scripts\\main.py")
    print(f"  3. Installa la skill in C:\\Users\\Utente\\.claude\\skills\\")
    print(f"  4. Riavvia Claude Code")


if __name__ == '__main__':
    main()
