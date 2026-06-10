"""
Genera la tabella HTML per la chiamata a freddo.
Legge tutti i lead con telefono e crea lead_chiamata_freddo.html
"""
import csv
import glob

output_files = glob.glob('output/*.csv')
lead = []

for f in sorted(output_files):
    try:
        with open(f, encoding='utf-8') as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                tel = row.get('TELEFONO', '').strip()
                pronto = row.get('PRONTO_OUTREACH', '').strip()
                if tel and pronto in ('Sì', 'Si', 'Sì'):
                    lead.append(row)
    except Exception:
        continue

def sort_key(r):
    fascia_ord = {'A': 0, 'B': 1, 'C': 2}.get(r.get('FASCIA', 'C'), 2)
    for campo in ('SCORE_PRIORITÀ', 'SCORE_PRIORITÀ', 'SCORE_PRIORITA', 'SCORE_PRIORIT\u00c0'):
        val = r.get(campo, '')
        if val:
            try:
                return (fascia_ord, -int(val))
            except ValueError:
                pass
    return (fascia_ord, 0)

lead.sort(key=sort_key)

righe = []
for i, r in enumerate(lead, 1):
    nome    = r.get('NOME_BUSINESS', '?')
    citta   = r.get('CITTÀ', '') or r.get('CITT\u00c0', '') or r.get('CITTA', '')
    cat     = r.get('CATEGORIA', '')
    tel     = r.get('TELEFONO', '')
    rating  = r.get('RATING_GOOGLE', '')
    recens  = r.get('N_RECENSIONI', '')
    fascia  = r.get('FASCIA', '')
    score   = ''
    for campo in ('SCORE_PRIORITÀ', 'SCORE_PRIORITÀ', 'SCORE_PRIORITA', 'SCORE_PRIORIT\u00c0'):
        if r.get(campo, ''):
            score = r[campo]
            break

    colore = {'A': '#22c55e', 'B': '#3b82f6', 'C': '#94a3b8'}.get(fascia, '#94a3b8')
    stelle = f'⭐ {rating}' if rating else '—'
    rec_txt = f'{recens} rec.' if recens else ''

    righe.append(f"""
    <tr>
      <td class="n">{i}</td>
      <td>
        <strong>{nome}</strong><br>
        <small>{citta}</small>
      </td>
      <td><span class="tag">{cat}</span></td>
      <td class="tel"><a href="tel:{tel}">{tel}</a></td>
      <td>{stelle}<br><small>{rec_txt}</small></td>
      <td><span class="fascia" style="background:{colore}">{fascia}</span><br><small>{score}pt</small></td>
      <td><button class="btn-check" onclick="segna(this,{i})">Da chiamare</button></td>
      <td class="note-cell"><input class="nota" placeholder="Note..." onchange="salvaNota({i}, this.value)"></td>
    </tr>""")

righe_html = '\n'.join(righe)
totale = len(lead)

html = """<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<title>Lead Chiamata a Freddo — Digital Empire (""" + str(totale) + """ contatti)</title>
<style>
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; background:#0f172a; color:#e2e8f0; }
header { background:#1e293b; padding:20px 32px; border-bottom:1px solid #334155; display:flex; justify-content:space-between; align-items:center; }
h1 { font-size:18px; font-weight:700; color:#f1f5f9; }
h1 span { color:#22c55e; }
.meta { color:#64748b; font-size:13px; margin-top:4px; }
.stats { display:flex; gap:24px; }
.stat .n { font-size:22px; font-weight:700; color:#22c55e; display:block; text-align:center; }
.stat .l { font-size:11px; color:#64748b; text-transform:uppercase; letter-spacing:1px; text-align:center; }
.bar { height:4px; background:#1e293b; }
.fill { height:100%; background:#22c55e; width:0%; transition:width .3s; }
.filters { padding:14px 32px; background:#1e293b; border-bottom:1px solid #0f172a; display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
.fb { padding:5px 14px; border-radius:20px; border:1px solid #334155; background:transparent; color:#94a3b8; cursor:pointer; font-size:12px; }
.fb.on { background:#3b82f6; border-color:#3b82f6; color:#fff; }
.src { margin-left:auto; padding:6px 12px; border-radius:8px; border:1px solid #334155; background:#0f172a; color:#e2e8f0; font-size:13px; width:220px; }
.container { padding:20px 32px; }
table { width:100%; border-collapse:collapse; background:#1e293b; border-radius:10px; overflow:hidden; font-size:13px; }
th { padding:10px 14px; text-align:left; font-size:11px; text-transform:uppercase; letter-spacing:1px; color:#64748b; background:#0f172a; border-bottom:1px solid #334155; }
td { padding:10px 14px; border-bottom:1px solid #ffffff08; vertical-align:middle; }
tr:hover td { background:#ffffff06; }
tr.done td { opacity:.35; }
td.n { color:#475569; width:36px; }
td.tel a { color:#38bdf8; text-decoration:none; font-family:monospace; font-size:12px; }
td.tel a:hover { text-decoration:underline; }
.tag { background:#1e3a5f; color:#7dd3fc; padding:2px 8px; border-radius:8px; font-size:11px; }
.fascia { display:inline-block; padding:2px 8px; border-radius:10px; font-size:11px; font-weight:700; color:#fff; }
.btn-check { padding:5px 12px; border-radius:8px; border:1px solid #334155; background:transparent; color:#94a3b8; cursor:pointer; font-size:12px; white-space:nowrap; }
.btn-check.chiamato { background:#22c55e22; border-color:#22c55e; color:#22c55e; }
.btn-check.interessato { background:#f59e0b22; border-color:#f59e0b; color:#f59e0b; }
.btn-check.non-int { background:#ef444422; border-color:#ef4444; color:#ef4444; }
.nota { background:#0f172a; border:1px solid #334155; color:#e2e8f0; padding:4px 8px; border-radius:6px; font-size:12px; width:100%; }
td.note-cell { min-width:160px; }
.counter { position:fixed; bottom:20px; right:20px; background:#1e293b; border:1px solid #334155; padding:12px 18px; border-radius:12px; font-size:13px; color:#e2e8f0; box-shadow:0 8px 32px rgba(0,0,0,.5); text-align:center; }
.counter b { font-size:20px; color:#22c55e; display:block; }
</style>
</head>
<body>

<header>
  <div>
    <h1>Chiamata a Freddo &mdash; <span>Vendita Sito Web</span></h1>
    <div class="meta">Digital Empire Team &middot; """ + str(totale) + """ lead senza sito &middot; ordinati per priorità</div>
  </div>
  <div class="stats">
    <div class="stat"><span class="n" id="s-tot">""" + str(totale) + """</span><span class="l">Totali</span></div>
    <div class="stat"><span class="n" id="s-chi" style="color:#22c55e">0</span><span class="l">Chiamati</span></div>
    <div class="stat"><span class="n" id="s-int" style="color:#f59e0b">0</span><span class="l">Interessati</span></div>
    <div class="stat"><span class="n" id="s-ni" style="color:#ef4444">0</span><span class="l">Non int.</span></div>
  </div>
</header>

<div class="bar"><div class="fill" id="prog"></div></div>

<div class="filters">
  <button class="fb on" onclick="filtra('tutti',this)">Tutti (""" + str(totale) + """)</button>
  <button class="fb" onclick="filtra('A',this)">Fascia A (2)</button>
  <button class="fb" onclick="filtra('B',this)">Fascia B (243)</button>
  <button class="fb" onclick="filtra('da-chiamare',this)">Da chiamare</button>
  <button class="fb" onclick="filtra('interessati',this)">Interessati</button>
  <input type="text" class="src" id="src" placeholder="Cerca nome, città, categoria..." oninput="cerca()">
</div>

<div class="container">
<table id="tbl">
<thead>
<tr>
  <th>#</th><th>Business</th><th>Categoria</th><th>Telefono</th>
  <th>Google Maps</th><th>Fascia</th><th>Stato</th><th>Note</th>
</tr>
</thead>
<tbody>
""" + righe_html + """
</tbody>
</table>
</div>

<div class="counter">
  <b id="c-chiamati">0</b>
  chiamati oggi
</div>

<script>
const TOT = """ + str(totale) + """;
const STATI = JSON.parse(localStorage.getItem('caf_stati') || '{}');
const NOTE  = JSON.parse(localStorage.getItem('caf_note')  || '{}');

const S_LABEL = ['Da chiamare', '✓ Chiamato', '★ Interessato', '✗ Non int.'];
const S_CLASS = ['', 'chiamato', 'interessato', 'non-int'];

function segna(btn, i) {
  const curr = STATI[i] || 0;
  const next = (curr + 1) % 4;
  STATI[i] = next;
  localStorage.setItem('caf_stati', JSON.stringify(STATI));
  btn.textContent = S_LABEL[next];
  btn.className = 'btn-check ' + S_CLASS[next];
  btn.closest('tr').classList.toggle('done', next === 3);
  aggiornaStats();
}

function salvaNota(i, val) {
  NOTE[i] = val;
  localStorage.setItem('caf_note', JSON.stringify(NOTE));
}

function aggiornaStats() {
  const vals = Object.values(STATI);
  const chi = vals.filter(s => s >= 1).length;
  const int = vals.filter(s => s === 2).length;
  const ni  = vals.filter(s => s === 3).length;
  document.getElementById('s-chi').textContent = chi;
  document.getElementById('s-int').textContent = int;
  document.getElementById('s-ni').textContent  = ni;
  document.getElementById('c-chiamati').textContent = chi;
  document.getElementById('prog').style.width = (chi / TOT * 100) + '%';
}

function filtra(tipo, btn) {
  document.querySelectorAll('.fb').forEach(b => b.classList.remove('on'));
  btn.classList.add('on');
  document.querySelectorAll('#tbl tbody tr').forEach(row => {
    const idx = parseInt(row.children[0].textContent);
    const fascia = row.children[5].querySelector('.fascia').textContent.trim();
    const stato = STATI[idx] || 0;
    let show = true;
    if (tipo === 'A') show = fascia === 'A';
    else if (tipo === 'B') show = fascia === 'B';
    else if (tipo === 'da-chiamare') show = stato === 0;
    else if (tipo === 'interessati') show = stato === 2;
    row.style.display = show ? '' : 'none';
  });
}

function cerca() {
  const q = document.getElementById('src').value.toLowerCase();
  document.querySelectorAll('#tbl tbody tr').forEach(row => {
    row.style.display = row.textContent.toLowerCase().includes(q) ? '' : 'none';
  });
}

window.addEventListener('load', () => {
  Object.entries(STATI).forEach(([i, s]) => {
    const rows = document.querySelectorAll('#tbl tbody tr');
    const row = rows[parseInt(i) - 1];
    if (!row) return;
    const btn = row.querySelector('.btn-check');
    btn.textContent = S_LABEL[s];
    btn.className = 'btn-check ' + S_CLASS[s];
    if (s === 3) row.classList.add('done');
  });
  Object.entries(NOTE).forEach(([i, nota]) => {
    const rows = document.querySelectorAll('#tbl tbody tr');
    const row = rows[parseInt(i) - 1];
    if (row) row.querySelector('.nota').value = nota;
  });
  aggiornaStats();
});
</script>
</body>
</html>"""

with open('lead_chiamata_freddo.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Tabella creata: lead_chiamata_freddo.html ({totale} lead)')
