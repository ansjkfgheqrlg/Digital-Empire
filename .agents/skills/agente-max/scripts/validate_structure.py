#!/usr/bin/env python3
"""
validate_structure.py — CC-Master v2.0
Valida la struttura di skill, agenti e plugin Claude Code contro le specifiche del manuale.

Uso:
  python validate_structure.py --target "C:\\percorso\\skill-name" --type skill
  python validate_structure.py --target "C:\\percorso\\agente.md" --type agent
  python validate_structure.py --target "C:\\percorso\\plugin" --type plugin
  python validate_structure.py --target "C:\\Users\\Utente\\.claude" --type all
  python validate_structure.py --target "." --type skill --strict --fix-suggestions
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ValidationResult:
    category: str  # 'OK', 'WARN', 'FAIL'
    message: str
    fix: Optional[str] = None


@dataclass
class ComponentReport:
    name: str
    path: str
    component_type: str
    results: list[ValidationResult] = field(default_factory=list)
    score: int = 0
    max_score: int = 100

    @property
    def status(self) -> str:
        if self.score >= 80:
            return 'VERDE ✅'
        elif self.score >= 60:
            return 'GIALLO ⚠️'
        else:
            return 'ROSSO ❌'

    @property
    def fail_count(self) -> int:
        return sum(1 for r in self.results if r.category == 'FAIL')

    @property
    def warn_count(self) -> int:
        return sum(1 for r in self.results if r.category == 'WARN')

    @property
    def ok_count(self) -> int:
        return sum(1 for r in self.results if r.category == 'OK')


def parse_yaml_frontmatter(content: str) -> tuple[dict, str]:
    """Estrae il frontmatter YAML e il body del file."""
    if not content.startswith('---'):
        return {}, content

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return {}, content

    frontmatter_str = content[3:end_idx].strip()
    body = content[end_idx + 3:].strip()

    # Parse semplice YAML (chiave: valore)
    frontmatter = {}
    current_key = None
    current_multiline = []

    for line in frontmatter_str.split('\n'):
        if line.startswith(' ') or line.startswith('\t'):
            # Continuazione multiline
            if current_key:
                current_multiline.append(line.strip())
        elif ':' in line:
            # Salva il precedente
            if current_key and current_multiline:
                frontmatter[current_key] = '\n'.join(current_multiline)

            parts = line.split(':', 1)
            current_key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''
            if value:
                frontmatter[current_key] = value
                current_key = None
                current_multiline = []
            else:
                current_multiline = []

    # Salva l'ultimo
    if current_key and current_multiline:
        frontmatter[current_key] = '\n'.join(current_multiline)

    return frontmatter, body


def validate_skill(path: str, show_fixes: bool = False) -> ComponentReport:
    """Valida una skill (cartella con SKILL.md o file .md diretto)."""
    # Determina il file principale
    if os.path.isdir(path):
        skill_md = os.path.join(path, 'SKILL.md')
        skill_name = os.path.basename(path)
    elif os.path.isfile(path) and path.endswith('.md'):
        skill_md = path
        skill_name = os.path.basename(path).replace('.md', '')
    else:
        report = ComponentReport(name='?', path=path, component_type='skill')
        report.results.append(ValidationResult('FAIL', 'Percorso non valido: deve essere una cartella o un file .md'))
        return report

    report = ComponentReport(name=skill_name, path=path, component_type='skill')
    score = 0

    # Leggi il file
    if not os.path.exists(skill_md):
        report.results.append(ValidationResult('FAIL', 'SKILL.md non trovato nella cartella'))
        report.score = 0
        return report

    with open(skill_md, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    frontmatter, body = parse_yaml_frontmatter(content)
    lines = body.split('\n')

    # === YAML FRONTMATTER CHECKS ===
    # name (10 punti)
    if 'name' in frontmatter:
        score += 10
        report.results.append(ValidationResult('OK', f"Campo 'name' presente: '{frontmatter['name']}'"))

        # Verifica formato lowercase-hyphens
        name_val = frontmatter['name']
        if name_val != name_val.lower() or ' ' in name_val:
            report.results.append(ValidationResult('WARN', f"'name' dovrebbe essere lowercase-hyphens (es: 'mia-skill')",
                                                    fix=f"Cambia name in: '{name_val.lower().replace(' ', '-')}'"))
    else:
        report.results.append(ValidationResult('FAIL', "Campo 'name' mancante nel frontmatter",
                                                fix="Aggiungi: name: nome-skill"))

    # description (20 punti)
    if 'description' in frontmatter:
        desc = frontmatter['description']
        if len(desc) >= 80:
            score += 20
            report.results.append(ValidationResult('OK', f"'description' presente ({len(desc)} caratteri)"))
        elif len(desc) >= 40:
            score += 10
            report.results.append(ValidationResult('WARN', f"'description' troppo corta ({len(desc)} caratteri, raccomandati ≥80)",
                                                    fix="Aggiungi trigger phrases e delimita cosa la skill NON fa"))
        else:
            score += 5
            report.results.append(ValidationResult('WARN', f"'description' molto corta ({len(desc)} caratteri)",
                                                    fix="Espandi con: cosa fa, trigger phrases in italiano, cosa NON fa, output"))
    else:
        report.results.append(ValidationResult('FAIL', "Campo 'description' mancante nel frontmatter",
                                                fix="Aggiungi: description: [descrizione con trigger phrases]"))

    # Trigger phrases in italiano (20 punti)
    if 'description' in frontmatter:
        desc = frontmatter['description']
        # Cerca pattern tipici di trigger: "Trigger:", frasi in italiano
        has_triggers = (
            'Trigger:' in desc or
            'trigger:' in desc or
            re.search(r'"[^"]{5,}"', desc) is not None or
            any(word in desc.lower() for word in ['quando', 'quando l\'utente', 'usa questa'])
        )
        if has_triggers:
            score += 20
            report.results.append(ValidationResult('OK', "Trigger phrases identificate nella description"))
        else:
            report.results.append(ValidationResult('WARN', "Nessuna trigger phrase trovata nella description",
                                                    fix='Aggiungi: Trigger: "frase1", "frase2", "frase3"'))

    # === BODY CHECKS ===
    # Forma imperativa (20 punti)
    imperative_violations = []
    second_person_patterns = [
        r'\btu devi\b', r'\btu dovresti\b', r'\btu puoi\b', r'\byou should\b',
        r'\byou must\b', r'\byou need to\b', r'\bdovresti\b', r'\bdevi\b'
    ]
    for pattern in second_person_patterns:
        matches = re.findall(pattern, body, re.IGNORECASE)
        if matches:
            imperative_violations.extend(matches)

    if not imperative_violations:
        score += 20
        report.results.append(ValidationResult('OK', "Body in forma imperativa (nessuna seconda persona trovata)"))
    else:
        report.results.append(ValidationResult('FAIL',
                                                f"Seconda persona trovata nel body: {imperative_violations[:3]}",
                                                fix="Sostituisci 'tu devi fare X' con forma imperativa 'Fai X'"))

    # Lunghezza body (15 punti)
    body_lines = len(lines)
    if body_lines <= 200:
        score += 15
        report.results.append(ValidationResult('OK', f"Body: {body_lines} righe (✅ ≤200)"))
    elif body_lines <= 500:
        score += 10
        report.results.append(ValidationResult('WARN', f"Body: {body_lines} righe (⚠️ tra 200 e 500)",
                                                fix="Considera di spostare contenuto dettagliato in references/framework.md"))
    else:
        report.results.append(ValidationResult('FAIL', f"Body: {body_lines} righe (❌ >500 — troppo lungo)",
                                                fix="Sposta il contenuto eccedente in references/ e linkalo da SKILL.md"))

    # Sezione installazione (15 punti)
    has_install = (
        'Installazione' in body or
        'installazione' in body or
        r'.claude\skills' in body or
        r'.claude/skills' in body
    )
    if has_install:
        score += 15
        report.results.append(ValidationResult('OK', "Sezione di installazione presente"))
    else:
        report.results.append(ValidationResult('WARN', "Sezione installazione assente",
                                                fix="Aggiungi alla fine: ## Installazione\nCopia in C:\\Users\\Utente\\.claude\\skills\\"))

    report.score = min(score, 100)
    return report


def validate_agent(path: str, show_fixes: bool = False) -> ComponentReport:
    """Valida un file agente .md."""
    if not os.path.isfile(path) or not path.endswith('.md'):
        report = ComponentReport(name='?', path=path, component_type='agent')
        report.results.append(ValidationResult('FAIL', 'Percorso non valido: deve essere un file .md'))
        return report

    agent_name = os.path.basename(path).replace('.md', '')
    report = ComponentReport(name=agent_name, path=path, component_type='agent')
    score = 0

    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    frontmatter, body = parse_yaml_frontmatter(content)

    # === FRONTMATTER CHECKS ===
    # name (10 punti)
    if 'name' in frontmatter:
        score += 10
        report.results.append(ValidationResult('OK', f"'name' presente: '{frontmatter['name']}'"))
    else:
        report.results.append(ValidationResult('FAIL', "'name' mancante nel frontmatter",
                                                fix="Aggiungi: name: nome-agente"))

    # description (15 punti)
    if 'description' in frontmatter:
        desc = frontmatter['description']
        if 'Use this agent when' in desc or 'Use when' in desc:
            score += 15
            report.results.append(ValidationResult('OK', "Description inizia con pattern 'Use this agent when'"))
        else:
            score += 5
            report.results.append(ValidationResult('WARN', "Description non segue il pattern 'Use this agent when...'",
                                                    fix="Inizia la description con: Use this agent when [condizioni]..."))
    else:
        report.results.append(ValidationResult('FAIL', "'description' mancante",
                                                fix="Aggiungi description con pattern 'Use this agent when...'"))

    # Esempi nella description (15 punti)
    if 'description' in frontmatter:
        example_count = frontmatter.get('description', '').count('<example>')
        if example_count >= 2:
            score += 15
            report.results.append(ValidationResult('OK', f"Description ha {example_count} blocchi <example>"))
        elif example_count == 1:
            score += 8
            report.results.append(ValidationResult('WARN', "Description ha solo 1 blocco <example> (minimi: 2)",
                                                    fix="Aggiungi un secondo esempio con un caso d'uso diverso"))
        else:
            report.results.append(ValidationResult('FAIL', "Nessun blocco <example> trovato nella description",
                                                    fix="Aggiungi almeno 2 blocchi <example>...</example>"))

    # model (10 punti)
    valid_models = ['opus', 'sonnet', 'haiku', 'claude-opus-4-6', 'claude-sonnet-4-6', 'claude-haiku-4-5-20251001']
    if 'model' in frontmatter:
        if any(m in frontmatter['model'] for m in valid_models):
            score += 10
            report.results.append(ValidationResult('OK', f"'model' valido: '{frontmatter['model']}'"))
        else:
            report.results.append(ValidationResult('WARN', f"'model' non riconosciuto: '{frontmatter['model']}'",
                                                    fix=f"Usa uno di: {valid_models[:3]}"))
    else:
        report.results.append(ValidationResult('WARN', "'model' non specificato",
                                                fix="Aggiungi: model: sonnet"))

    # tools (10 punti)
    if 'tools' in frontmatter:
        score += 10
        report.results.append(ValidationResult('OK', "'tools' presente nel frontmatter"))
    else:
        report.results.append(ValidationResult('WARN', "'tools' non specificato",
                                                fix="Aggiungi: tools: [\"Read\", \"Write\", \"Edit\"]"))

    # === BODY CHECKS ===
    # Seconda persona nel system prompt (20 punti)
    has_identity = 'IDENTITY' in body or 'Identity' in body or '## IDENTITY' in body
    if has_identity:
        score += 10
        report.results.append(ValidationResult('OK', "Sezione IDENTITY presente"))
    else:
        report.results.append(ValidationResult('FAIL', "Sezione IDENTITY assente nel system prompt",
                                                fix="Aggiungi: ## IDENTITY\nYou are [nome], a specialized expert in [dominio]..."))

    has_process = 'PROCESS' in body or 'Process' in body or '## PROCESS' in body
    if has_process:
        score += 10
        report.results.append(ValidationResult('OK', "Sezione PROCESS presente"))
    else:
        report.results.append(ValidationResult('WARN', "Sezione PROCESS assente",
                                                fix="Aggiungi: ## PROCESS\n1. [step]\n2. [step]..."))

    has_constraints = 'CONSTRAINTS' in body or 'Constraints' in body or 'Never:' in body
    if has_constraints:
        score += 10
        report.results.append(ValidationResult('OK', "Sezione CONSTRAINTS presente (Never:/Always:)"))
    else:
        report.results.append(ValidationResult('WARN', "Sezione CONSTRAINTS assente",
                                                fix="Aggiungi: ## CONSTRAINTS\nNever:\n- ...\nAlways:\n- ..."))

    report.score = min(score, 100)
    return report


def validate_plugin(path: str, show_fixes: bool = False) -> ComponentReport:
    """Valida la struttura di un plugin Claude Code."""
    report = ComponentReport(name=os.path.basename(path), path=path, component_type='plugin')
    score = 0

    if not os.path.isdir(path):
        report.results.append(ValidationResult('FAIL', 'Il percorso non è una cartella'))
        return report

    # plugin.json (30 punti)
    plugin_json = os.path.join(path, '.claude-plugin', 'plugin.json')
    if os.path.exists(plugin_json):
        score += 15
        report.results.append(ValidationResult('OK', ".claude-plugin/plugin.json trovato"))

        import json
        try:
            with open(plugin_json, 'r', encoding='utf-8') as f:
                plugin_data = json.load(f)

            required_fields = ['name', 'version', 'description']
            for field_name in required_fields:
                if field_name in plugin_data:
                    score += 5
                    report.results.append(ValidationResult('OK', f"plugin.json: campo '{field_name}' presente"))
                else:
                    report.results.append(ValidationResult('FAIL', f"plugin.json: campo '{field_name}' mancante",
                                                            fix=f'Aggiungi "{field_name}": "..." in plugin.json'))
        except json.JSONDecodeError as e:
            report.results.append(ValidationResult('FAIL', f"plugin.json non è JSON valido: {e}"))
    else:
        report.results.append(ValidationResult('FAIL', '.claude-plugin/plugin.json non trovato',
                                                fix="Crea la cartella .claude-plugin/ e il file plugin.json"))

    # agents/ (20 punti)
    agents_dir = os.path.join(path, 'agents')
    if os.path.isdir(agents_dir):
        agents = [f for f in os.listdir(agents_dir) if f.endswith('.md')]
        if agents:
            score += 20
            report.results.append(ValidationResult('OK', f"agents/ trovata con {len(agents)} agente/i: {agents}"))
        else:
            score += 10
            report.results.append(ValidationResult('WARN', "agents/ esiste ma è vuota"))
    else:
        report.results.append(ValidationResult('WARN', "agents/ non trovata",
                                                fix="Crea la cartella agents/ e aggiungi almeno un agente .md"))

    # knowledge/ (20 punti)
    knowledge_dir = os.path.join(path, 'knowledge')
    if os.path.isdir(knowledge_dir):
        kb_files = [f for f in os.listdir(knowledge_dir) if f.endswith('.md')]
        if kb_files:
            score += 20
            report.results.append(ValidationResult('OK', f"knowledge/ trovata con {len(kb_files)} file"))
        else:
            score += 10
            report.results.append(ValidationResult('WARN', "knowledge/ esiste ma è vuota"))
    else:
        report.results.append(ValidationResult('WARN', "knowledge/ non trovata (opzionale ma raccomandato)"))

    # skills/ (15 punti)
    skills_dir = os.path.join(path, 'skills')
    if os.path.isdir(skills_dir):
        skill_files = [f for f in os.listdir(skills_dir) if f.endswith('.md')]
        if skill_files:
            score += 15
            report.results.append(ValidationResult('OK', f"skills/ trovata con {len(skill_files)} skill interne"))
        else:
            score += 5
            report.results.append(ValidationResult('WARN', "skills/ esiste ma è vuota"))
    else:
        report.results.append(ValidationResult('WARN', "skills/ non trovata",
                                                fix="Crea la cartella skills/ con le skill specializzate del plugin"))

    report.score = min(score, 100)
    return report


def print_component_report(report: ComponentReport, show_fixes: bool = False) -> None:
    """Stampa il report di un singolo componente."""
    print(f"\n{'─' * 55}")
    print(f"  {report.component_type.upper()}: {report.name}")
    print(f"  Path: {report.path}")
    print(f"{'─' * 55}")

    for result in report.results:
        icon = {'OK': '✅', 'WARN': '⚠️', 'FAIL': '❌'}.get(result.category, '?')
        print(f"  {icon} {result.message}")
        if show_fixes and result.fix and result.category != 'OK':
            print(f"     → FIX: {result.fix}")

    print(f"\n  SCORE: {report.score}/100  |  STATUS: {report.status}")
    print(f"  OK: {report.ok_count}  WARN: {report.warn_count}  FAIL: {report.fail_count}")


def main():
    parser = argparse.ArgumentParser(
        description='Valida struttura di skill, agenti e plugin Claude Code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi:
  python validate_structure.py --target "C:\\skill\\mia-skill" --type skill
  python validate_structure.py --target "C:\\.claude\\agents\\mio-agente.md" --type agent
  python validate_structure.py --target "C:\\.claude\\plugins\\cc-master" --type plugin
  python validate_structure.py --target "C:\\.claude\\plugins\\cc-master" --type plugin --strict --fix-suggestions
        """
    )
    parser.add_argument('--target', required=True,
                        help='Percorso della skill/agente/plugin da validare')
    parser.add_argument('--type', required=True, choices=['skill', 'agent', 'plugin', 'all'],
                        help='Tipo di componente da validare')
    parser.add_argument('--strict', action='store_true',
                        help='Exit code 1 se ci sono FAIL (utile per CI/CD)')
    parser.add_argument('--fix-suggestions', action='store_true',
                        help='Mostra suggerimenti per correggere ogni problema')

    args = parser.parse_args()

    if not os.path.exists(args.target):
        print(f"[ERROR] Percorso non trovato: {args.target}")
        sys.exit(1)

    print('\n' + '═' * 55)
    print('  VALIDATION REPORT — CC-Master v2.0')
    print('═' * 55)

    reports = []

    if args.type == 'skill':
        reports.append(validate_skill(args.target, args.fix_suggestions))

    elif args.type == 'agent':
        reports.append(validate_agent(args.target, args.fix_suggestions))

    elif args.type == 'plugin':
        reports.append(validate_plugin(args.target, args.fix_suggestions))

    elif args.type == 'all':
        # Cerca tutti i componenti nella directory target
        target_dir = args.target

        # Agenti
        agents_dir = os.path.join(target_dir, 'agents')
        if os.path.isdir(agents_dir):
            for f in os.listdir(agents_dir):
                if f.endswith('.md'):
                    reports.append(validate_agent(os.path.join(agents_dir, f), args.fix_suggestions))

        # Skill
        skills_dir = os.path.join(target_dir, 'skills')
        if os.path.isdir(skills_dir):
            for f in os.listdir(skills_dir):
                if f.endswith('.md'):
                    reports.append(validate_skill(os.path.join(skills_dir, f), args.fix_suggestions))

        # Plugin stesso
        if os.path.isdir(os.path.join(target_dir, '.claude-plugin')):
            reports.append(validate_plugin(target_dir, args.fix_suggestions))

    for report in reports:
        print_component_report(report, args.fix_suggestions)

    # Summary finale
    if len(reports) > 1:
        avg_score = sum(r.score for r in reports) // len(reports)
        total_fails = sum(r.fail_count for r in reports)
        total_warns = sum(r.warn_count for r in reports)
        total_ok = sum(r.ok_count for r in reports)

        print(f"\n{'═' * 55}")
        print(f"  OVERALL SUMMARY ({len(reports)} componenti)")
        print(f"  Score medio: {avg_score}/100")
        print(f"  OK: {total_ok}  WARN: {total_warns}  FAIL: {total_fails}")
        print('═' * 55)

    total_fails_all = sum(r.fail_count for r in reports)
    if args.strict and total_fails_all > 0:
        print(f"\n[STRICT MODE] {total_fails_all} FAIL trovati — exit code 1")
        sys.exit(1)


if __name__ == '__main__':
    main()
