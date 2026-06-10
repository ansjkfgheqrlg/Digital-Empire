#!/usr/bin/env python3
"""
generate_agent.py — CC-Master v2.0
Genera lo scaffolding completo per un nuovo agente Claude Code.

Uso:
  python generate_agent.py --name mio-agente --domain "analisi finanziaria" --model sonnet
  python generate_agent.py --name mio-agente --domain "..." --model opus --color blue --tools "Read,Write,Edit"
  python generate_agent.py --name mio-agente --domain "..." --model sonnet --trigger-phrases "frase1|frase2" --output-path "C:\\percorso"
"""

import argparse
import os
import re
import sys


VALID_MODELS = ['opus', 'sonnet', 'haiku',
                'claude-opus-4-6', 'claude-sonnet-4-6', 'claude-haiku-4-5-20251001']
VALID_COLORS = ['magenta', 'blue', 'green', 'yellow', 'red', 'cyan', 'orange', 'purple', 'white']
VALID_TOOLS = ['Read', 'Write', 'Edit', 'Glob', 'Grep', 'Bash', 'WebSearch',
               'WebFetch', 'TodoWrite', 'NotebookEdit', 'Agent']
HIGH_RISK_TOOLS = ['Bash', 'Agent']


def sanitize_name(name: str) -> str:
    """Converte il nome in formato lowercase-hyphens."""
    name = name.lower().strip()
    name = re.sub(r'[^a-z0-9\-]', '-', name)
    name = re.sub(r'-+', '-', name)
    return name.strip('-')


def generate_description(name: str, domain: str, trigger_phrases: list[str]) -> str:
    """Genera la description con pattern 'Use this agent when...' e 2 esempi."""
    phrase1 = trigger_phrases[0] if trigger_phrases else f"aiutami con {domain}"
    phrase2 = trigger_phrases[1] if len(trigger_phrases) > 1 else f"{domain} per il mio progetto"

    trigger_str = ', '.join(f'"{t.strip()}"' for t in trigger_phrases)

    return f"""Use this agent when the user needs expert help with {domain}, or any task requiring deep specialization in this domain. Also activate when the user says {trigger_str} or any variation.

<example>
Context: User needs specialized help with {domain}.
user: "{phrase1}"
assistant: "Attivo {name} — l'esperto specializzato in {domain} per questo task."
<commentary>
This is the primary use case for {name}. The agent provides specialized expertise in {domain}.
</commentary>
</example>

<example>
Context: User has a specific task requiring {domain} expertise.
user: "{phrase2}"
assistant: "{name} gestisce questo — ha il processo e le competenze specifiche per {domain}."
<commentary>
Any task requiring deep {domain} knowledge should route through {name}.
</commentary>
</example>"""


def generate_agent_md(name: str, domain: str, model: str, color: str,
                      tools: list[str], trigger_phrases: list[str]) -> str:
    """Genera il file completo dell'agente."""
    description = generate_description(name, domain, trigger_phrases)
    tools_str = str(tools).replace("'", '"')

    return f"""---
name: {name}
description: {description}

model: {model}
color: {color}
tools: {tools_str}
---

## IDENTITY

You are {name}, a specialized expert in {domain} for Digital Empire.
You are not a general assistant — you are focused exclusively on {domain}.

Your fundamental principle: [inserisci qui il principio cardine di questo agente — es: "Produce only production-ready output, never approximations"]

## MISSION

Transform the user's {domain} requests into precise, professional, production-ready results.

[Espandi qui la missione in 2-3 frasi: cosa trasformi, da cosa a cosa, per chi, con quale risultato atteso]

## PROCESS

1. **ORIENT** — Analyze what exactly the user needs within the {domain} domain.
   → Gate: Ensure the request is actually within your domain before proceeding.

2. **GATHER** — Collect all necessary information before acting.
   - What inputs are needed?
   - What files/data should be read first?
   - What is missing?
   → Gate: Do not proceed until all inputs are available.

3. **PLAN** — Outline the approach before executing.
   - For any task creating/modifying files: present the plan first
   - For questions: identify the precise answer
   → Gate: User must see the plan (implicit or explicit approval)

4. **EXECUTE** — Produce the actual output.
   - Use Write/Edit tools to create real files, not descriptions
   - Use TodoWrite for tasks with 3+ steps
   - Mark each TodoWrite item completed immediately after finishing

5. **VERIFY** — Run the quality checklist before delivering.
   - [ ] Output matches what was planned
   - [ ] All files are complete, not placeholder/partial
   - [ ] Instructions for use/installation are included

## OUTPUT CONTRACT

For **[tipo output 1]**: [formato, struttura, lunghezza, qualità minima]
For **[tipo output 2]**: [formato, struttura, lunghezza, qualità minima]

Before delivering any output, verify:
- [ ] [criterio qualità 1 specifico per {domain}]
- [ ] [criterio qualità 2]
- [ ] [criterio qualità 3]

## CONSTRAINTS

Never:
- Act outside the {domain} domain (route to appropriate agent instead)
- Create or modify files without presenting a plan first
- Deliver partial or placeholder output
- [aggiungi vincoli specifici del dominio]

Always:
- Produce real, production-ready files — not descriptions of what to create
- Include installation or usage instructions with every deliverable
- Use Windows paths with backslashes (C:\\Users\\Utente\\...)
- [aggiungi vincoli positivi specifici del dominio]
"""


def main():
    parser = argparse.ArgumentParser(
        description='Genera scaffolding completo per un nuovo agente Claude Code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python generate_agent.py --name reviewer --domain "code review" --model sonnet --color blue --tools "Read,Grep,Glob"
  python generate_agent.py --name qa-tester --domain "quality assurance e testing" --model sonnet --trigger-phrases "testa questo|fai QA|verifica funzionamento"
  python generate_agent.py --name data-analyst --domain "analisi dati e business intelligence" --model opus --color yellow --tools "Read,Write,Edit,Bash"
        """
    )
    parser.add_argument('--name', required=True, help='Nome dell\'agente (verrà convertito in lowercase-hyphens)')
    parser.add_argument('--domain', required=True, help='Dominio specialistico dell\'agente (es: "code review", "analisi finanziaria")')
    parser.add_argument('--model', default='sonnet', choices=VALID_MODELS,
                        help='Modello Claude da usare (default: sonnet)')
    parser.add_argument('--color', default='blue', choices=VALID_COLORS,
                        help='Colore UI dell\'agente (default: blue)')
    parser.add_argument('--tools', default='Read,Write,Edit,TodoWrite',
                        help='Tool separati da virgola (default: Read,Write,Edit,TodoWrite)')
    parser.add_argument('--trigger-phrases', default='',
                        help='Frasi trigger separate da | (es: "frase1|frase2|frase3")')
    parser.add_argument('--output-path', default=None,
                        help='Percorso di destinazione (default: C:\\Users\\Utente\\.claude\\agents\\)')

    args = parser.parse_args()

    # Sanitizza nome
    name = sanitize_name(args.name)
    if name != args.name:
        print(f"[INFO] Nome convertito: '{args.name}' → '{name}'")

    # Parsing tools
    tools = [t.strip() for t in args.tools.split(',') if t.strip()]
    invalid_tools = [t for t in tools if t not in VALID_TOOLS]
    if invalid_tools:
        print(f"[WARN] Tool non riconosciuti: {invalid_tools}. Tool validi: {VALID_TOOLS}")

    # Warning per tool ad alto rischio
    risky = [t for t in tools if t in HIGH_RISK_TOOLS]
    if risky:
        print(f"[WARN] Tool ad alto rischio inclusi: {risky}")
        print("       Assicurati che siano necessari e aggiungi vincoli appropriati in CONSTRAINTS.")

    # Parsing trigger phrases
    trigger_phrases = []
    if args.trigger_phrases:
        trigger_phrases = [t.strip() for t in args.trigger_phrases.split('|') if t.strip()]
    if not trigger_phrases:
        trigger_phrases = [f"aiutami con {args.domain}", f"{args.domain} per il mio progetto"]
        print(f"[INFO] Nessuna trigger phrase specificata. Usate frasi di default. Considera di personalizzarle.")

    # Output path
    base_path = args.output_path or r'C:\Users\Utente\.claude\agents'
    output_file = os.path.join(base_path, f'{name}.md')

    if os.path.exists(output_file):
        print(f"[ERROR] Il file '{output_file}' esiste già.")
        print(f"        Usa un nome diverso o elimina prima il file esistente.")
        sys.exit(1)

    # Crea la cartella se non esiste
    os.makedirs(base_path, exist_ok=True)

    # Genera il file agente
    content = generate_agent_md(name, args.domain, args.model, args.color,
                                 tools, trigger_phrases)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # Report finale
    print(f"\n✓ Agente '{name}' creato con successo!")
    print(f"\nFile creato: {output_file}")
    print(f"\nConfigurazione:")
    print(f"  Model:  {args.model}")
    print(f"  Color:  {args.color}")
    print(f"  Tools:  {tools}")
    print(f"\nProssimi passi:")
    print(f"  1. Apri {output_file}")
    print(f"  2. Completa le sezioni IDENTITY, MISSION, OUTPUT CONTRACT, CONSTRAINTS")
    print(f"  3. Personalizza i [TODO] placeholder con il contenuto specifico del dominio")
    print(f"  4. Se necessario, sposta il file in .claude\\agents\\ del progetto specifico")
    print(f"  5. Riavvia Claude Code per attivare l'agente")
    print(f"\nPer invocare manualmente: @{name} nel prompt")


if __name__ == '__main__':
    main()
