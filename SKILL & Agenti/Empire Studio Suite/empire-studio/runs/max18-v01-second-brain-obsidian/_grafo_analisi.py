import json, os, sys, io

BASE = os.path.dirname(os.path.abspath(__file__))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

atoms = json.load(open(os.path.join(BASE, 'atoms.json'), encoding='utf-8'))
ids = [a['id'] for a in atoms]
idset = set(ids)

# archi esistenti
existing = set()
for a in atoms:
    for r in a.get('relazioni', []) or []:
        v = r.get('verso')
        if v in idset:
            existing.add((a['id'], v))

extra_path = os.path.join(BASE, 'atoms-archi-trasversali.json')
extra = []
if os.path.exists(extra_path):
    try:
        extra = json.load(open(extra_path, encoding='utf-8'))
    except Exception as e:
        print('ERRORE lettura archi trasversali:', e)

def components(edges, nodes):
    par = {n: n for n in nodes}
    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            par[ra] = rb
    for (a, b) in edges:
        if a in par and b in par:
            union(a, b)
    comp = {}
    for n in nodes:
        comp.setdefault(find(n), []).append(n)
    return sorted(comp.values(), key=len, reverse=True)

def degree_orphans(edges, nodes):
    deg = {n: 0 for n in nodes}
    for (a, b) in edges:
        if a in deg: deg[a] += 1
        if b in deg: deg[b] += 1
    return [n for n in nodes if deg[n] == 0]

mode = sys.argv[1] if len(sys.argv) > 1 else 'stato'

if mode == 'stato':
    comps = components(existing, ids)
    print('ATOMI:', len(ids))
    print('ARCHI esistenti:', len(existing))
    print('COMPONENTI:', len(comps))
    print('dimensioni:', [len(c) for c in comps])
    print('ORFANI:', degree_orphans(existing, ids))
    # dump indice compatto
    with open(os.path.join(BASE, '_indice_atomi.txt'), 'w', encoding='utf-8') as f:
        for a in atoms:
            c = ' '.join(str(a.get('contenuto', '')).split())[:260]
            f.write('%s | %s | %s | %s\n' % (a['id'], a.get('tipo', ''), a.get('_origine', ''), c))
    # dump per componente
    with open(os.path.join(BASE, '_componenti.txt'), 'w', encoding='utf-8') as f:
        for i, c in enumerate(comps, 1):
            f.write('--- COMPONENTE %d (%d atomi) ---\n' % (i, len(c)))
            f.write(', '.join(sorted(c)) + '\n\n')
    print('scritti _indice_atomi.txt e _componenti.txt')

elif mode == 'verifica':
    VALID = {'motiva', 'quantificato-da', 'esempio-di', 'corretto-da', 'precede', 'parte-di', 'contraddice'}
    errs = []
    seen = set()
    new_edges = set()
    for i, e in enumerate(extra):
        da, verso, tipo = e.get('da'), e.get('verso'), e.get('tipo')
        if da not in idset: errs.append('#%d id inesistente da=%s' % (i, da))
        if verso not in idset: errs.append('#%d id inesistente verso=%s' % (i, verso))
        if tipo not in VALID: errs.append('#%d tipo non valido: %s' % (i, tipo))
        if da == verso: errs.append('#%d self-loop %s' % (i, da))
        if not str(e.get('perche', '')).strip(): errs.append('#%d perche vuoto' % i)
        k = (da, verso)
        if k in existing: errs.append('#%d DOPPIONE di atoms.json: %s->%s' % (i, da, verso))
        if k in seen or (verso, da) in seen: errs.append('#%d doppione interno: %s->%s' % (i, da, verso))
        seen.add(k)
        new_edges.add(k)
    all_edges = existing | new_edges
    comps = components(all_edges, ids)
    orph = degree_orphans(all_edges, ids)
    print('ARCHI NUOVI:', len(extra))
    print('ERRORI:', len(errs))
    for x in errs[:40]: print('  ', x)
    print('--- RISULTATO FINALE ---')
    print('COMPONENTI CONNESSE:', len(comps))
    print('dimensioni componenti:', [len(c) for c in comps])
    print('ORFANI (grado 0):', len(orph), orph)
    if len(comps) > 1:
        for c in comps[1:]:
            print('  isola residua:', sorted(c))
