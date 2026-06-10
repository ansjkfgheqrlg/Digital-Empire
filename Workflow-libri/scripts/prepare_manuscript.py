"""
prepare_manuscript.py — Converte LIBRO 1.md nel formato corretto per la pipeline

- Ristruttura i titoli: ## PERSONAGGIO → # Capitolo N - PERSONAGGIO
- Mantiene i capitoli gruppo (CAPITOLO 1 — GLI ESILIATI ecc.) come testo H3
- Aggiunge bold automaticamente ai paragrafi che non ne hanno già

Uso:
    python scripts/prepare_manuscript.py
"""

import re
import sys
from pathlib import Path

# ──────────────────────────────────────────────
# Parole comuni italiane da NON mettere in grassetto
# ──────────────────────────────────────────────
STOP_WORDS = {
    'il', 'la', 'lo', 'i', 'gli', 'le', 'un', 'una', 'uno',
    'e', 'ed', 'ma', 'se', 'per', 'con', 'da', 'di', 'del',
    'della', 'dei', 'degli', 'delle', 'in', 'al', 'alla', 'ai',
    'agli', 'alle', 'sul', 'sulla', 'sui', 'sugli', 'sulle',
    'nel', 'nella', 'nei', 'negli', 'nelle', 'dal', 'dalla',
    'dai', 'dagli', 'dalle', 'che', 'chi', 'cui', 'non', 'si',
    'è', 'era', 'sono', 'fu', 'poi', 'già', 'così', 'anche',
    'come', 'questo', 'questa', 'questi', 'queste', 'quello',
    'quella', 'quelli', 'quelle', 'suo', 'sua', 'suoi', 'sue',
    'loro', 'tutto', 'tutte', 'tutti', 'aveva', 'hanno', 'avere',
    'essere', 'sarà', 'sarebbe', 'erano', 'avevano', 'quando',
    'dove', 'perché', 'però', 'dopo', 'prima', 'ancora', 'sempre',
    'mai', 'più', 'meno', 'molto', 'poco', 'troppo', 'ogni',
    'suo', 'sua', 'loro', 'nostro', 'vostro', 'proprio', 'stesso',
    'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette',
    'otto', 'nove', 'dieci', 'anni', 'anno', 'mesi', 'giorni',
    'volta', 'volte', 'modo', 'parte', 'cosa', 'nulla', 'niente',
    'qualcosa', 'qualcuno', 'chiunque', 'qualsiasi', 'tale',
    'allora', 'quindi', 'invece', 'mentre', 'durante', 'verso',
    'senza', 'fino', 'tra', 'fra', 'sopra', 'sotto', 'dentro',
    'fuori', 'contro', 'oltre', 'secondo', 'lungo', 'attraverso',
    'fare', 'fece', 'fatto', 'fare', 'disse', 'disse', 'aveva',
    'aveva', 'poteva', 'doveva', 'voleva', 'sapeva', 'andò',
    'tornò', 'rimase', 'diventò', 'divenne', 'ottenne', 'prese',
    'mise', 'portò', 'scrisse', 'costruì', 'morì', 'visse',
    'nato', 'nata', 'figlio', 'figlia', 'padre', 'madre', 'uomo',
    'donna', 'uomini', 'donne', 'persona', 'persone', 'vita',
    'morte', 'guerra', 'pace', 'città', 'paese', 'mondo', 'terra',
    'cielo', 'sole', 'mare', 'notte', 'giorno', 'tempo', 'storia',
    'nome', 'parola', 'voce', 'mente', 'cuore', 'occhi', 'mano',
    'mani', 'corpo', 'testa', 'piedi', 'propria', 'proprio',
    'era', 'li', 'ne', 'ci', 'vi', 'mi', 'ti', 'lo', 'la',
    'gli', 'le', 'ce', 've', 'me', 'te', 'se', 'ci', 'vi',
    'solo', 'sola', 'soli', 'sole', 'stava', 'stanno', 'stata',
    'stato', 'stati', 'essere', 'avuto', 'mai', 'poi', 'ora',
    'adesso', 'oggi', 'ieri', 'domani', 'qui', 'là', 'lì',
    'qua', 'su', 'giù', 'avanti', 'indietro', 'destra', 'sinistra',
    'grande', 'piccolo', 'nuovo', 'vecchio', 'primo', 'ultimo',
    'altro', 'altra', 'altri', 'altre', 'stesso', 'stessa',
    'nessuno', 'nessuna', 'qualche', 'certo', 'certa', 'certi',
}


def find_bold_candidates(text: str) -> list:
    """
    Trova parole candidate per il grassetto in un paragrafo.
    Priorità: parole con maiuscola (nomi propri), parole lunghe significative.
    Restituisce lista di (start_idx, end_idx, word) ordinata per priorità.
    """
    # Trova tutte le parole
    candidates = []
    for m in re.finditer(r'\b([A-Za-zÀ-ÿ][a-zà-ÿA-ZÀ-Ÿ\'\-]{3,})\b', text):
        word = m.group(1)
        word_lower = word.lower()
        if word_lower in STOP_WORDS:
            continue
        # Non mettere in grassetto parole già in * * o ** **
        pos = m.start()
        if pos > 0 and text[pos-1] in ('*', '_'):
            continue
        candidates.append((m.start(), m.end(), word))
    return candidates


def add_bold_to_paragraph(para: str) -> str:
    """
    Aggiunge bold a 1-2 parole in un paragrafo che non ne ha già.
    Non tocca paragrafi che iniziano con * o ** (leggi, applicazioni).
    Non tocca paragrafi con -- (separatori).
    """
    stripped = para.strip()

    # Non toccare se già ha bold
    if '**' in stripped:
        return para

    # Non toccare heading-like o separatori
    if stripped.startswith('#') or re.match(r'^-{3,}$', stripped):
        return para

    # Non toccare se è corsivo (applicazione oggi)
    if stripped.startswith('*') and stripped.endswith('*'):
        return para

    # Non toccare paragrafi molto corti (< 40 caratteri)
    if len(stripped) < 40:
        return para

    # Trova candidati
    candidates = find_bold_candidates(stripped)

    if not candidates:
        return para

    # Prende il primo candidato buono (parola significativa)
    # Priorità a parole maiuscole (nomi propri) e parole lunghe
    def score(c):
        word = c[2]
        s = 0
        if word[0].isupper():
            s += 10  # nome proprio
        s += min(len(word), 15)  # lunghezza (più lunga = più importante)
        return s

    sorted_candidates = sorted(candidates, key=score, reverse=True)

    # Seleziona 1 o 2 parole da mettere in grassetto
    selected = []

    # Prima parola: il candidato migliore entro i primi 2/3 del paragrafo
    first_third = len(stripped) * 2 // 3
    early_candidates = [(s, e, w) for s, e, w in sorted_candidates if s < first_third]

    if early_candidates:
        best = early_candidates[0]
        selected.append(best)

        # Seconda parola (opzionale): altro candidato significativo non troppo vicino
        remaining = [(s, e, w) for s, e, w in sorted_candidates
                     if (s, e, w) != best and abs(s - best[0]) > 20]
        if remaining:
            second = remaining[0]
            selected.append(second)
    elif sorted_candidates:
        selected.append(sorted_candidates[0])

    if not selected:
        return para

    # Applica i bold (in ordine inverso per non spostare gli indici)
    result = stripped
    for start, end, word in sorted(selected, key=lambda x: x[0], reverse=True):
        # Verifica che la parola sia ancora lì (non già in **  **)
        if result[start:end] == word:
            result = result[:start] + f'**{word}**' + result[end:]

    return result


def process_manuscript(input_path: str, output_path: str):
    """
    Processo principale:
    1. Legge LIBRO 1.md
    2. Rinumera ## PERSONAGGIO → # Capitolo N - PERSONAGGIO
    3. Trasforma intestazioni gruppo in H3 embedded
    4. Aggiunge bold ai paragrafi
    5. Scrive input/manuscript.md
    """
    src = Path(input_path)
    if not src.exists():
        print(f"ERRORE: File non trovato: {input_path}")
        sys.exit(1)

    content = src.read_text(encoding='utf-8')
    lines = content.splitlines()

    output_lines = []
    chapter_num = 0
    current_group = ""  # nome del capitolo gruppo corrente
    in_intro = False
    in_finale = False

    # Buffer paragrafo corrente
    para_buffer = []

    def flush_para():
        """Svuota il buffer del paragrafo, applicando bold se necessario"""
        nonlocal para_buffer
        if para_buffer:
            para_text = ' '.join(para_buffer)
            processed = add_bold_to_paragraph(para_text)
            output_lines.append(processed)
            para_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Heading di PRIMO LIVELLO: # CAPITOLO N — NOME o # INTRO/PAGINA FINALE ──
        if stripped.startswith('# '):
            flush_para()

            # INTRO
            if re.match(r'^#\s+INTRO\s*$', stripped, re.IGNORECASE):
                in_intro = True
                in_finale = False
                output_lines.append('')
                output_lines.append('# Capitolo 0 - Introduzione')
                output_lines.append('')
                i += 1
                continue

            # PAGINA FINALE
            if re.match(r'^#\s+PAGINA\s+FINALE\s*$', stripped, re.IGNORECASE):
                in_intro = False
                in_finale = True
                output_lines.append('')
                output_lines.append('---')
                output_lines.append('')
                i += 1
                continue

            # Capitolo gruppo: # CAPITOLO N — NOME GRUPPO
            cap_match = re.match(r'^#\s+CAPITOLO\s+\d+\s+[—–-]+\s+(.+)$', stripped, re.IGNORECASE)
            if cap_match:
                current_group = cap_match.group(1).strip()
                # Non diventa un # Capitolo nel PDF — diventa testo H3 inserito alla fine
                i += 1
                continue

            # Capitolo 7 conclusione
            if re.match(r'^#\s+CAPITOLO\s+7', stripped, re.IGNORECASE):
                current_group = "La Tua Legge"
                output_lines.append('')
                chapter_num += 1
                output_lines.append(f'# Capitolo {chapter_num} - La Legge 49')
                output_lines.append('')
                i += 1
                continue

            # Altro H1 generico
            output_lines.append('')
            output_lines.append(stripped)
            output_lines.append('')
            i += 1
            continue

        # ── Heading di SECONDO LIVELLO: ## PERSONAGGIO (nome personaggio) ──
        if stripped.startswith('## '):
            flush_para()
            char_name = stripped[3:].strip()
            chapter_num += 1
            output_lines.append('')
            output_lines.append(f'# Capitolo {chapter_num} - {char_name}')
            if current_group:
                output_lines.append(f'### *{current_group}*')
            output_lines.append('')
            i += 1
            continue

        # ── Heading di TERZO LIVELLO: ### Sottotitolo ──
        if stripped.startswith('### '):
            flush_para()
            output_lines.append(stripped)
            output_lines.append('')
            i += 1
            continue

        # ── Separatore --- ──
        if re.match(r'^-{3,}$', stripped):
            flush_para()
            output_lines.append('---')
            output_lines.append('')
            i += 1
            continue

        # ── Riga vuota ──
        if not stripped:
            flush_para()
            output_lines.append('')
            i += 1
            continue

        # ── Riga di testo ──
        # Gestisci righe speciali che devono stare da sole
        # (LEGGE N°X, Applicazione oggi, grassetti di sezione)
        if stripped.startswith('**LEGGE'):
            flush_para()
            output_lines.append(stripped)
            output_lines.append('')
            i += 1
            continue

        if stripped.startswith('*Applicazione oggi:'):
            flush_para()
            output_lines.append(stripped)
            output_lines.append('')
            i += 1
            continue

        # Riga con &nbsp;
        if '&nbsp;' in stripped:
            flush_para()
            output_lines.append(stripped)
            i += 1
            continue

        # Riga con linee per la firma (______)
        if re.match(r'^_{10,}', stripped):
            flush_para()
            output_lines.append(stripped)
            i += 1
            continue

        # Riga normale — accumula nel buffer
        para_buffer.append(stripped)
        i += 1

    # Svuota eventuale buffer residuo
    flush_para()

    # Scrivi output
    dst = Path(output_path)
    dst.parent.mkdir(parents=True, exist_ok=True)

    # Pulisci righe vuote multiple consecutive
    final_lines = []
    prev_empty = False
    for line in output_lines:
        is_empty = line.strip() == ''
        if is_empty and prev_empty:
            continue
        final_lines.append(line)
        prev_empty = is_empty

    dst.write_text('\n'.join(final_lines) + '\n', encoding='utf-8')

    # Report
    print(f"OK - Manoscritto scritto in: {output_path}")
    print(f"   Capitoli trovati: {chapter_num}")
    print(f"   Righe output: {len(final_lines)}")


if __name__ == "__main__":
    import os

    # Assumi working dir = root del progetto
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent

    input_file = project_dir / "LIBRO 1.md"
    output_file = project_dir / "input" / "manuscript.md"

    print(f"Lettura: {input_file}")
    print(f"Scrittura: {output_file}")
    print()

    process_manuscript(str(input_file), str(output_file))
