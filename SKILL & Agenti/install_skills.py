import zipfile, os

base = r'C:\Users\Utente\Desktop\qui tutto\Digital Empire\SKILL & Agenti'
skills_dir = r'C:\Users\Utente\.claude\skills'
commands_dir = r'C:\Users\Utente\.claude\commands'
os.makedirs(commands_dir, exist_ok=True)

# 1. PLAYWRIGHT
print('Installazione playwright...')
with zipfile.ZipFile(f'{base}/playwright-main.zip') as z:
    for member in z.namelist():
        if member.startswith('playwright-main/.claude/skills/playwright-dev/'):
            rel = member.replace('playwright-main/.claude/skills/', '')
            if rel:
                dest = os.path.join(skills_dir, rel)
                if member.endswith('/'):
                    os.makedirs(dest, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    with z.open(member) as src, open(dest, 'wb') as dst:
                        dst.write(src.read())
print('  OK -> playwright-dev')

# 2. IMPECCABLE
print('Installazione impeccable...')
with zipfile.ZipFile(f'{base}/impeccable-main.zip') as z:
    for member in z.namelist():
        if member.startswith('impeccable-main/.agents/skills/impeccable/'):
            rel = member.replace('impeccable-main/.agents/skills/', '')
            if rel:
                dest = os.path.join(skills_dir, rel)
                if member.endswith('/'):
                    os.makedirs(dest, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    with z.open(member) as src, open(dest, 'wb') as dst:
                        dst.write(src.read())
print('  OK -> impeccable')

# 3. CLI-PRINTING-PRESS
print('Installazione cli-printing-press...')
installed = set()
with zipfile.ZipFile(f'{base}/cli-printing-press-main.zip') as z:
    for member in z.namelist():
        if member.startswith('cli-printing-press-main/skills/') and 'testdata' not in member:
            rel = member.replace('cli-printing-press-main/skills/', '')
            if rel:
                dest = os.path.join(skills_dir, rel)
                installed.add(rel.split('/')[0])
                if member.endswith('/'):
                    os.makedirs(dest, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    with z.open(member) as src, open(dest, 'wb') as dst:
                        dst.write(src.read())
print(f'  OK -> {sorted(installed)}')

# 4. CONTEXT-ENGINEERING
print('Installazione Context-Engineering commands...')
with zipfile.ZipFile(f'{base}/Context-Engineering-main.zip') as z:
    for member in z.namelist():
        if member.startswith('Context-Engineering-main/.claude/commands/') and not member.endswith('/'):
            filename = os.path.basename(member)
            dest = os.path.join(commands_dir, filename)
            with z.open(member) as src, open(dest, 'wb') as dst:
                dst.write(src.read())
            print(f'  -> {filename}')

print('\nTutte le skill installate con successo!')
input('Premi Invio per chiudere...')
