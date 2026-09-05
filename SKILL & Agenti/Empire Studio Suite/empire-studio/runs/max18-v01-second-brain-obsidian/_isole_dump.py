import json, os, sys, io

BASE = os.path.dirname(os.path.abspath(__file__))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

atoms = json.load(open(os.path.join(BASE, 'atoms.json'), encoding='utf-8'))
byid = {a['id']: a for a in atoms}

ISOLE = [
    ['KA-130','KA-131','KA-132','KA-133','KA-134','KA-136','KA-139','KA-142','KA-143'],
    ['KA-148','KA-158','KA-159','KA-160','KA-164','KA-165','KA-166','KA-167'],
    ['KA-118','KA-119','KA-123','KA-124','KA-125','KA-126'],
    ['KA-068','KA-069','KA-070','KA-071','KA-072'],
    ['KA-135','KA-137','KA-138','KA-140','KA-141'],
    ['KA-120','KA-121','KA-127','KA-128'],
    ['KA-005','KA-006'],
    ['KA-007','KA-008'],
]

out = []
for i, isola in enumerate(ISOLE, 1):
    out.append('=' * 70)
    out.append('ISOLA %d (%d atomi)' % (i, len(isola)))
    out.append('=' * 70)
    for aid in isola:
        a = byid[aid]
        c = ' '.join(str(a.get('contenuto', '')).split())
        out.append('[%s] tipo=%s fonte=%s' % (aid, a.get('tipo', ''), a.get('fonte', '')))
        out.append('  ancora: %s' % ' '.join(str(a.get('ancora', '')).split())[:160])
        out.append('  %s' % c)
        rel = a.get('relazioni', []) or []
        out.append('  rel: %s' % ', '.join('%s->%s' % (r.get('tipo'), r.get('verso')) for r in rel))
        out.append('')

open(os.path.join(BASE, '_isole_dump.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('scritto _isole_dump.txt', len('\n'.join(out)), 'char')
