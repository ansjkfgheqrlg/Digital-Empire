#!/usr/bin/env python3
"""
context_calculator.py — CC-Master v2.0
Calcola il consumo stimato di contesto per ogni componente dell'ecosistema Claude Code.

Soglie dal Capitolo 23 del manuale Claude Code per il Business:
  Verde:  pre-occupato <20%, durante lavoro <50%, MCP <5%, skill <1%
  Giallo: pre-occupato 20-35%, durante lavoro 50-70%, MCP 5-15%, skill 1-3%
  Rosso:  pre-occupato >35%, durante lavoro >70%, MCP >15%, skill >3%

Uso:
  python context_calculator.py
  python context_calculator.py --claude-dir "C:\\percorso\\custom\\.claude"
  python context_calculator.py --model opus --show-breakdown
  python context_calculator.py --export-json report.json
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# Stima token: ~250 token per KB (testo italiano formattato)
TOKENS_PER_KB = 250

# Contesto massimo per modello
CONTEXT_WINDOWS = {
    'sonnet': 200_000,
    'opus': 200_000,
    'haiku': 200_000,
}

# System prompt Anthropic (stima fissa)
SYSTEM_PROMPT_TOKENS = 20_000

# Soglie (dal Capitolo 23)
THRESHOLDS = {
    'pre_occupied': {'green': 20, 'yellow': 35},
    'during_work': {'green': 50, 'yellow': 70},
    'skill': {'green': 1, 'yellow': 3},
    'mcp': {'green': 5, 'yellow': 15},
    'messages': {'green': 40, 'yellow': 60},
}

# Pesi MCP noti (percentuale del contesto 200K)
KNOWN_MCP_WEIGHTS = {
    'clickup': 27.0,
    'chrome-dev-tool': 0.1,
    'chrome_dev_tool': 0.1,
    'github': 6.0,
    'notion': 12.0,
    'filesystem': 1.5,
    'sequential-thinking': 2.5,
    'brave-search': 1.5,
    'memory': 2.0,
    'puppeteer': 3.0,
}


@dataclass
class Component:
    name: str
    category: str  # 'system', 'claude_md', 'agent', 'skill', 'mcp', 'plugin', 'memory'
    path: str
    size_bytes: int = 0
    tokens_estimated: int = 0
    notes: str = ''


@dataclass
class Report:
    model: str
    context_window: int
    components: list[Component] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)


def status_label(value: float, thresholds: dict) -> str:
    """Restituisce etichetta Verde/Giallo/Rosso."""
    if value <= thresholds['green']:
        return 'Verde ✅'
    elif value <= thresholds['yellow']:
        return 'Giallo ⚠️'
    else:
        return 'Rosso ❌'


def estimate_tokens(size_bytes: int) -> int:
    """Stima i token da dimensione file in bytes."""
    kb = size_bytes / 1024
    return int(kb * TOKENS_PER_KB)


def scan_directory(path: str, category: str, extensions: tuple = ('.md',)) -> list[Component]:
    """Scansiona una directory e restituisce componenti trovati."""
    components = []
    if not os.path.exists(path):
        return components

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath) and any(filename.endswith(ext) for ext in extensions):
            size = os.path.getsize(filepath)
            comp = Component(
                name=filename.replace('.md', ''),
                category=category,
                path=filepath,
                size_bytes=size,
                tokens_estimated=estimate_tokens(size)
            )
            components.append(comp)

    return components


def scan_plugins(plugins_dir: str) -> list[Component]:
    """Scansiona i plugin installati."""
    components = []
    if not os.path.exists(plugins_dir):
        return components

    for plugin_name in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, plugin_name)
        if not os.path.isdir(plugin_path):
            continue

        # Calcola dimensione totale del plugin
        total_size = 0
        for root, dirs, files in os.walk(plugin_path):
            for f in files:
                fp = os.path.join(root, f)
                total_size += os.path.getsize(fp)

        comp = Component(
            name=plugin_name,
            category='plugin',
            path=plugin_path,
            size_bytes=total_size,
            tokens_estimated=estimate_tokens(total_size),
            notes='Plugin completo (agents + skills + knowledge)'
        )
        components.append(comp)

    return components


def parse_mcp_from_settings(settings_path: str) -> list[Component]:
    """Estrae i MCP dalla configurazione settings.json."""
    components = []
    if not os.path.exists(settings_path):
        return components

    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    except (json.JSONDecodeError, IOError):
        return components

    mcp_servers = settings.get('mcpServers', {})
    context_window = 200_000  # default

    for mcp_name, mcp_config in mcp_servers.items():
        if mcp_config.get('disabled', False):
            continue

        # Cerca peso noto
        normalized_name = mcp_name.lower().replace('-', '_')
        weight_pct = None
        for known_name, known_weight in KNOWN_MCP_WEIGHTS.items():
            if known_name in normalized_name or normalized_name in known_name:
                weight_pct = known_weight
                break

        tokens = int((weight_pct / 100 * context_window)) if weight_pct else 5000
        notes = f'{weight_pct:.1f}% del contesto' if weight_pct else 'peso stimato (sconosciuto)'

        comp = Component(
            name=mcp_name,
            category='mcp',
            path=settings_path,
            size_bytes=0,
            tokens_estimated=tokens,
            notes=notes
        )
        components.append(comp)

    return components


def generate_report(claude_dir: str, model: str) -> Report:
    """Genera il report completo del consumo di contesto."""
    context_window = CONTEXT_WINDOWS.get(model, 200_000)
    report = Report(model=model, context_window=context_window)

    # 1. System prompt Anthropic (fisso)
    report.components.append(Component(
        name='System Prompt Anthropic',
        category='system',
        path='(built-in)',
        size_bytes=0,
        tokens_estimated=SYSTEM_PROMPT_TOKENS,
        notes='Stima fissa — non modificabile'
    ))

    # 2. CLAUDE.md globale
    global_claude_md = os.path.join(claude_dir, 'CLAUDE.md')
    if os.path.exists(global_claude_md):
        size = os.path.getsize(global_claude_md)
        report.components.append(Component(
            name='CLAUDE.md (global)',
            category='claude_md',
            path=global_claude_md,
            size_bytes=size,
            tokens_estimated=estimate_tokens(size)
        ))

    # 3. Agenti globali
    agents_dir = os.path.join(claude_dir, 'agents')
    report.components.extend(scan_directory(agents_dir, 'agent'))

    # 4. Skill globali
    skills_dir = os.path.join(claude_dir, 'skills')
    report.components.extend(scan_directory(skills_dir, 'skill'))

    # 5. Plugin
    plugins_dir = os.path.join(claude_dir, 'plugins')
    report.components.extend(scan_plugins(plugins_dir))

    # 6. MCP da settings.json
    settings_path = os.path.join(claude_dir, 'settings.json')
    report.components.extend(parse_mcp_from_settings(settings_path))

    # 7. Auto memory
    memory_file = os.path.join(claude_dir, 'MEMORY.md')
    if os.path.exists(memory_file):
        size = os.path.getsize(memory_file)
        report.components.append(Component(
            name='Auto Memory (MEMORY.md)',
            category='memory',
            path=memory_file,
            size_bytes=size,
            tokens_estimated=estimate_tokens(size)
        ))

    # Analisi issues e raccomandazioni
    total_tokens = sum(c.tokens_estimated for c in report.components)
    total_pct = (total_tokens / context_window) * 100

    mcp_tokens = sum(c.tokens_estimated for c in report.components if c.category == 'mcp')
    mcp_pct = (mcp_tokens / context_window) * 100

    skill_tokens = sum(c.tokens_estimated for c in report.components if c.category == 'skill')
    skill_pct = (skill_tokens / context_window) * 100

    if total_pct > 35:
        report.issues.append(f'Contesto pre-occupato al {total_pct:.1f}% — ROSSO (soglia: 35%)')
        report.recommendations.append('Riduci urgentemente il numero di componenti globali attivi')
    elif total_pct > 20:
        report.issues.append(f'Contesto pre-occupato al {total_pct:.1f}% — GIALLO (soglia: 20%)')
        report.recommendations.append('Considera di spostare MCP e skill pesanti a livello per-progetto')

    for comp in report.components:
        if comp.category == 'mcp':
            mcp_comp_pct = (comp.tokens_estimated / context_window) * 100
            if mcp_comp_pct > 15:
                report.issues.append(f"MCP '{comp.name}' occupa {mcp_comp_pct:.1f}% del contesto — troppo pesante")
                report.recommendations.append(
                    f"Sposta '{comp.name}' a configurazione per-progetto o considera alternativa skill"
                )

    if skill_pct > 3:
        report.issues.append(f'Skill totali occupano {skill_pct:.1f}% del contesto — ROSSO (soglia: 3%)')
        report.recommendations.append('Rimuovi skill globali non utilizzate in tutti i progetti')

    return report


def print_report(report: Report, show_breakdown: bool = False) -> None:
    """Stampa il report formattato."""
    context_window = report.context_window

    print('\n' + '═' * 60)
    print('  CONTEXT USAGE REPORT — CC-Master v2.0')
    print('═' * 60)
    print(f'  Model:          claude-{report.model}')
    print(f'  Context Window: {context_window:,} token')
    print(f'  Token per KB:   ~{TOKENS_PER_KB}')
    print('═' * 60)

    if show_breakdown:
        print('\nCOMPONENT BREAKDOWN:')
        print('─' * 60)

        categories_order = ['system', 'claude_md', 'plugin', 'agent', 'skill', 'mcp', 'memory']
        category_labels = {
            'system': 'Sistema',
            'claude_md': 'CLAUDE.md',
            'plugin': 'Plugin',
            'agent': 'Agente',
            'skill': 'Skill',
            'mcp': 'MCP',
            'memory': 'Memory'
        }

        for cat in categories_order:
            cat_components = [c for c in report.components if c.category == cat]
            if not cat_components:
                continue

            for comp in cat_components:
                pct = (comp.tokens_estimated / context_window) * 100
                bar = '█' * int(pct / 2)
                label = category_labels.get(cat, cat)
                notes = f'  [{comp.notes}]' if comp.notes else ''

                # Colore testuale
                if cat == 'mcp' and pct > 15:
                    status = '❌'
                elif cat == 'mcp' and pct > 5:
                    status = '⚠️'
                elif pct > 20:
                    status = '❌'
                else:
                    status = '✅'

                print(f'  {status} [{label:10}] {comp.name:<30} {comp.tokens_estimated:>7,} tok  {pct:5.1f}%{notes}')

        print('─' * 60)

    # Totali per categoria
    total_tokens = sum(c.tokens_estimated for c in report.components)
    total_pct = (total_tokens / context_window) * 100
    available_pct = 100 - total_pct

    print(f'\nSUMMARY:')
    print(f'  Contesto pre-occupato:  {total_tokens:>8,} tok  {total_pct:5.1f}%  {status_label(total_pct, THRESHOLDS["pre_occupied"])}')
    print(f'  Disponibile per lavoro: {context_window - total_tokens:>8,} tok  {available_pct:5.1f}%')

    mcp_tokens = sum(c.tokens_estimated for c in report.components if c.category == 'mcp')
    mcp_pct = (mcp_tokens / context_window) * 100
    if mcp_tokens > 0:
        print(f'  MCP totale:             {mcp_tokens:>8,} tok  {mcp_pct:5.1f}%  {status_label(mcp_pct, THRESHOLDS["mcp"])}')

    skill_tokens = sum(c.tokens_estimated for c in report.components if c.category == 'skill')
    skill_pct = (skill_tokens / context_window) * 100
    if skill_tokens > 0:
        print(f'  Skill totale:           {skill_tokens:>8,} tok  {skill_pct:5.1f}%  {status_label(skill_pct, THRESHOLDS["skill"])}')

    # Health status
    print()
    if not report.issues:
        print('  HEALTH STATUS: VERDE ✅ — Tutto nella norma')
    elif any('ROSSO' in i for i in report.issues):
        print('  HEALTH STATUS: ROSSO ❌ — Problemi critici rilevati')
    else:
        print('  HEALTH STATUS: GIALLO ⚠️ — Attenzione consigliata')

    if report.issues:
        print('\nISSUES:')
        for issue in report.issues:
            print(f'  [!] {issue}')

    if report.recommendations:
        print('\nRECOMMENDATIONS:')
        for i, rec in enumerate(report.recommendations, 1):
            print(f'  {i}. {rec}')

    print('\n' + '═' * 60)


def main():
    parser = argparse.ArgumentParser(
        description='Calcola consumo token ecosistema Claude Code con soglie manuale Cap.23',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python context_calculator.py
  python context_calculator.py --show-breakdown
  python context_calculator.py --model opus --show-breakdown
  python context_calculator.py --claude-dir "C:\\percorso\\.claude" --export-json report.json
        """
    )
    parser.add_argument('--claude-dir',
                        default=r'C:\Users\Utente\.claude',
                        help='Percorso cartella .claude (default: C:\\Users\\Utente\\.claude)')
    parser.add_argument('--model', default='sonnet', choices=['sonnet', 'opus', 'haiku'],
                        help='Modello Claude in uso (default: sonnet)')
    parser.add_argument('--show-breakdown', action='store_true',
                        help='Mostra breakdown dettagliato per ogni componente')
    parser.add_argument('--export-json', default=None, metavar='FILE',
                        help='Esporta il report in JSON')

    args = parser.parse_args()

    if not os.path.exists(args.claude_dir):
        print(f'[ERROR] Cartella .claude non trovata: {args.claude_dir}')
        print('        Specifica il percorso corretto con --claude-dir')
        sys.exit(1)

    print(f'[INFO] Scansione di: {args.claude_dir}')
    report = generate_report(args.claude_dir, args.model)
    print_report(report, show_breakdown=args.show_breakdown)

    if args.export_json:
        data = {
            'model': report.model,
            'context_window': report.context_window,
            'components': [
                {
                    'name': c.name,
                    'category': c.category,
                    'tokens': c.tokens_estimated,
                    'percent': round((c.tokens_estimated / report.context_window) * 100, 2),
                    'notes': c.notes
                }
                for c in report.components
            ],
            'issues': report.issues,
            'recommendations': report.recommendations
        }
        with open(args.export_json, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f'\n[OK] Report JSON esportato in: {args.export_json}')


if __name__ == '__main__':
    main()
