from pathlib import Path
import re, collections, hashlib, json

f=Path(__file__).resolve().parent.parent/'ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.2.md'
p=f.read_text(encoding='utf-8', errors='strict'); lines=p.splitlines(); checks=[]
def ck(name, cond, detail=''):
    if not cond: raise AssertionError(f'{name}: {detail}')
    checks.append(name)

# Identity, scope, status, parentage.
ck('title',p.startswith('# NERVE-SOLVE Orchestration Layer v2.2 — Architettura definitiva di produzione'))
ck('date','**Data:** 15 agosto 2026' in p)
ck('Layer 1 only','**Ambito vincolante:** Layer 1 — NERVE-SOLVE' in p)
ck('design baseline candidate','`DESIGN BASELINE CANDIDATE v2.2`' in p[:1500])
ck('execution E1 and v2.2 unauthorized','`E1 — LOCAL FOUNDATION`' in p[:1500] and 'v2.2 constitutional activation `UNAUTHORIZED`' in p[-1500:])
ck('readiness blocked','**Production readiness:** `BLOCKED`' in p[:1000] and 'production readiness `BLOCKED`' in p[-1000:])
ck('implementation split','Component A resta implementato' in p[:1500] and 'B–T `NOT_STARTED`' in p[:1500])
for link in ['SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.2.md','PIANO_PRODUZIONE_Orchestration_Layer_v2.1_APEX7_L7.md','NERVE-SOLVE_v2.1_audit_e_blueprint.md','INGESTION_REPORT_PROBLEM_SOLVING_NERVE-SOLVE_v2.2.md','implementation/plans/NS-A_MIGRATION_v2.1_TO_v2.2_PROPOSAL.md']:
    ck('local link '+link,link in p and (f.parent/link).exists())
ck('identity before mission',p.index('## 0. Identità') < p.index('## 2. Missione operativa'))
ck('first person identity','**IO SONO NERVE-SOLVE.**' in p and 'IO ABITO' in p and 'IO NON SONO' in p)
ck('not skill/checklist','IO NON SONO una skill, un workshop, una checklist' in p)

# DNA exactly ten and falsifiable.
dna_sec=p.split('## 1. DNA nervoso — dieci principi, non undici',1)[1].split('### 1.1',1)[0]
dna=re.findall(r'^(\d+)\. \*\*(IO [^*]+)\*\*',dna_sec,re.M)
ck('exactly 10 DNA principles',[x[0] for x in dna]==[str(i) for i in range(10)],dna)
for i,label in dna: ck(f'DNA {i} first person visceral',label.startswith('IO ') and len(label)>8,label)
fals=p.split('### 1.1 Falsificabilità dei principi',1)[1].split('### 1.2',1)[0]
fals_rows=re.findall(r'^\| ([0-9]) \|',fals,re.M)
ck('10 falsifiers',fals_rows==[str(i) for i in range(10)],fals_rows)
ck('explicit hierarchy','sicurezza, legalità, autorità e integrità' in p and 'Nessun principio inferiore compensa' in p)

# Layer boundaries and anti-invasion.
for x in ['Layer 2 quantitativo/finanziario','Layer 3 specialistico/regolato','`OUT_OF_LAYER`','costruisce HandoffContract','non ne costruisce le competenze interne','Non sostituiscono le fasi del Builder Control Plane']:
    ck('boundary '+x,x in p)
ck('three mandatory interfaces','P-1 Triage Gate' in p and 'P10 Pre-delivery Validation' in p and 'P12 Closure' in p)
ck('works imperfect inputs','input imperfetti' in p.lower() and 'ASK/VERIFY/ESCALATE' in p)
ck('bounded autonomy','Autonomia senza supervisione costante' in p and 'può procedere autonomamente' in p)

# Local links, text hygiene, fences.
local=[]
for u in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p):
    if not re.match(r'https?://',u) and not u.startswith('#'): local.append(u.split('#')[0])
ck('5 local links',len(local)==5,local)
ck('all local links resolve',all((f.parent/u).exists() for u in local),local)
ck('balanced fences',len(re.findall(r'^```',p,re.M))==48)
ck('no placeholders',not re.search(r'\b(?:TODO|TBD|FIXME|PLACEHOLDER|LOREM IPSUM)\b',p,re.I))
ck('clean encoding','\x00' not in p and '\r' not in p and p.endswith('\n'))

# Markdown tables.
def pipes(s):return len(re.findall(r'(?<!\\)\|',s))
tables=[];i=0
while i<len(lines):
    if lines[i].startswith('|'):
        j=i
        while j<len(lines) and lines[j].startswith('|'):j+=1
        tables.append((i+1,lines[i:j]));i=j
    else:i+=1
bad=[]
for n,b in tables:
    delim=len(b)>=2 and bool(re.match(r'^\|(?:\s*:?-{3,}:?\s*\|)+\s*$',b[1]))
    counts={pipes(x) for x in b}
    if not delim or len(counts)!=1:bad.append((n,delim,counts))
ck('40 valid tables',len(tables)==40 and not bad,(len(tables),bad))
heads=re.findall(r'^(#{1,6})\s+(.+?)\s*$',p,re.M)
hc=collections.Counter((len(a),b) for a,b in heads)
ck('no duplicate exact headings',not [x for x,n in hc.items() if n>1])

# Mentality and thought flows.
mental=p.split('## 8. Mentality Flow — passo per passo',1)[1].split('### 8.1',1)[0]
ms=re.findall(r'^\| \*\*(M\d+) — ',mental,re.M)
ck('12 ordered mentality steps',ms==[f'M{i}' for i in range(12)],ms)
thought=p.split('## 11. Thought Flow — state by state',1)[1].split('### 11.1',1)[0]
ts=re.findall(r'^\| \*\*(T\d+) — ',thought,re.M)
ck('12 ordered thought states',ts==[f'T{i}' for i in range(12)],ts)
for x in ['strongest_objection','disconfirming_evidence_refs','alternative_models','consequence_if_wrong','decision_rule','falsifiers','reopen_phase']:
    ck('decision trace field '+x,x in p)
for x in ['non richiede, non persiste e non espone','catene di pensiero private','motivi concisi, non monologo interno','no private CoT']:
    ck('private reasoning boundary '+x,x in p)
ck('thought flow uses public artifacts','protocollo metacognitivo tipizzato e auditabile' in p)
ck('anti-rumination','NO_INFORMATION_GAIN' in p and 'no-change detector' in p)

# Depth and phases.
for d in ['D0 — COMPRESSED','D1 — STANDARD','D2 — DEEP','D3 — CRITICAL']:
    ck('depth '+d,d in p)
phase_sec=p.split('## 13. Fasi canoniche P-1…P12',1)[1].split('### 13.1',1)[0]
phase_rows=re.findall(r'^\| \*\*(P(?:-1|\d+)) — ([^*]+)\*\* \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$',phase_sec,re.M)
expected=['P-1']+[f'P{i}' for i in range(13)]
ck('14 ordered canonical phases',[x[0] for x in phase_rows]==expected,[x[0] for x in phase_rows])
for phase,name,inp,out,gate,back in phase_rows:
    ck(phase+' input',bool(inp.strip()))
    ck(phase+' output',bool(out.strip()))
    ck(phase+' exit gate',bool(gate.strip()))
    ck(phase+' backtrack',('→' in back or 'backtrack' in back.lower() or 'fase' in back.lower()),back)
for phase in expected:
    ck(phase+' detailed section',f'### {phase} —' in p)
ck('mandatory phases cannot compress away','P-1 Triage Gate;' in p and 'P10 Pre-delivery Validation;' in p and 'P12 Closure.' in p)
ck('OLA compatibility mapping','### 15.2 Compatibilità con il ciclo OLA v2.2' in p)
for ola in ['`-1 TRIAGE GATE`','`0 FRAME & SELECT`','`1 PLAN`','`2 BUILD / REFINE`','`3 DETERMINISTIC VERIFY`','`4 SEMANTIC REVIEW`','`5 APEX QUALITY GATE`','`6 RELEASE & CLOSURE`']:
    ck('OLA mapping '+ola,ola in p)
ck('no delivery/deploy collision','P11 `DELIVERY` non equivale a deploy produttivo' in p)

# Aggregate and invariants.
for field in ['constitution_hash: sha256','phase_policy_hash: sha256','authority_state: CONFIRMED | LIMITED | UNKNOWN | DENIED','problem_structure:','representation: EQUATION | PROCESS | CONCEPTUAL | GRAPH | HYBRID','coverage_status: PROVISIONAL | SUPPORTED | NOT_PROVEN','epistemic_items: []','decision_trace_ref','execution_commitment_ref','memory_permission: NONE | SESSION | PERSISTENT','last_material_delta_hash']:
    ck('aggregate '+field,field in p)
inv=p.split('## 18. Invarianti di stato',1)[1].split('## 19.',1)[0]
inv_rows=re.findall(r'^(\d+)\. ',inv,re.M)
ck('14 state invariants',inv_rows==[str(i) for i in range(1,15)],inv_rows)

# Components A-T.
comp_sec=p.split('## 21. Schede dei componenti',1)[1].split('# PARTE VIII',1)[0]
components=re.findall(r'^### ([A-T])\. ([^\n]+)',comp_sec,re.M)
ck('20 ordered components',[x[0] for x in components]==[chr(ord('A')+i) for i in range(20)],components)
for letter,name in components:
    start=comp_sec.index(f'### {letter}. {name}')
    nexts=[comp_sec.find(f'### {chr(c)}. ',start+1) for c in range(ord('A'),ord('T')+1)];nexts=[x for x in nexts if x!=-1]
    sec=comp_sec[start:min(nexts) if nexts else len(comp_sec)]
    for tag in ['**Scopo:**','**Input:**','**Output:**','**Stato:**','**Failure:**','**Non fa:**']:
        ck(f'component {letter} {tag}',tag in sec)

# Function catalog exact uniqueness and essential operations.
func_rows=re.findall(r'^\| ([A-Z]+\d+) \| `([^`]+)` \|',p,re.M)
ids=[x[0] for x in func_rows]; fnames=[x[1] for x in func_rows]
ck('216 logical function rows',len(func_rows)==216,len(func_rows))
ck('216 unique function IDs',len(set(ids))==216,[x for x,n in collections.Counter(ids).items() if n>1])
ck('216 unique function names',len(set(fnames))==216,[x for x,n in collections.Counter(fnames).items() if n>1])
for fid,fname in func_rows:
    ck('function nonempty '+fid,bool(fname and re.match(r'^[a-z][a-z0-9_]+$',fname)),fname)
for essential in ['load_constitution','open_case','resolve_action_authority','select_depth','build_request_contract','choose_structure_representation','construct_problem_structure','contextualize_structure_checks','assess_structure_overlap_coverage','version_problem_structure','create_system_map','add_epistemic_item','choose_information_action','select_lens_plan','seek_disconfirming_evidence','generate_candidate_options','define_decision_rule','build_execution_commitment_proposal','record_external_commitment_response','generate_strongest_objection','compute_gate_decision','publish_delivery','reopen_case','build_handoff_contract','execute_tool_task','register_evidence','query_memory','transition_phase','reconcile_unknown_outcome','evaluate_phase_entry_policy','emit_audit_record']:
    ck('essential function '+essential,essential in fnames)

# Decision, validation and output semantics.
for x in ['Nessuna percentuale di successo viene emessa','CONDITIONAL = solo non-blocking','BLOCKED = almeno un blocking FAIL o NOT_PROVEN','no private CoT','assumption-as-fact blocks','nessun reviewer semantico sovrascrive un test deterministico bloccante']:
    ck('decision/validation '+x,x in p)
for x in ['RequestEnvelope','HandoffContract','ToolTask','ValidationRun','Command API','Query API','Event catalog']:
    ck('contract '+x,x in p)

# Data and durability.
db=p.split('## 45. Tabelle PostgreSQL',1)[1].split('## 46.',1)[0]
dbtables=re.findall(r'^\| `([a-z_]+)` \|',db,re.M)
ck('37 db tables',len(dbtables)==37 and len(set(dbtables))==37,dbtables)
for t in ['nerve_case','case_transition','phase_run','epistemic_item','contradiction','problem_structure','problem_structure_check','decision_record','execution_commitment_proposal','decision_trace','validation_run','closure_record','authority_decision','case_lease','inbox_message','outbox_event','audit_record']:
    ck('db table '+t,t in dbtables)
for x in ['fencing token','outbox ripubblica','UNKNOWN_OUTCOME','retry solo con errore classificato','resume rivalida policy']:
    ck('durability '+x,x in p)

# Security, autonomy, failure and ops.
roles=p.split('## 52. Ruoli agentici',1)[1].split('## 53.',1)[0]
role_rows=[x for x in re.findall(r'^\| ([^|]+) \| ([^|]+) \| ([^|]+) \|$',roles,re.M) if x[0].strip() != 'Ruolo']
ck('12 agent roles',len(role_rows)==12,len(role_rows))
ck('no God Agent','Non esiste un God Agent' in p)
for threat in ['prompt injection in input/source','framework injection/falso MECE','action-bias/urgency pressure','authority spoofing','chain-of-thought extraction','memory poisoning','cross-tenant retrieval','phase bypass','infinite reflection']:
    ck('threat '+threat,threat in p)
modes=re.findall(r'^\| `(NORMAL|DEGRADED_NO_TOOLS|DEGRADED_NO_MEMORY|READ_ONLY|PAUSED_SAFE|EMERGENCY_CONTAINMENT)` \|',p,re.M)
ck('6 operating modes',modes==['NORMAL','DEGRADED_NO_TOOLS','DEGRADED_NO_MEMORY','READ_ONLY','PAUSED_SAFE','EMERGENCY_CONTAINMENT'],modes)
ks=re.findall(r'^\| `(KS-[^`]+)` \|',p,re.M)
ck('9 unique kill switches',len(ks)==9 and len(set(ks))==9,ks)
ck('STOP/START asymmetry','STOP può essere attivato' in p and 'START/EXPAND richiede prova' in p)
ck('telemetry no CoT','Log vietato:' in p and '- chain-of-thought privata;' in p)

# Tests, ADRs, future plans and public critique.
cases=p.split('## 65. Suite cognitiva minima',1)[1].split('## 66.',1)[0]
case_rows=[x for x in cases.splitlines() if x.startswith('| ') and not x.startswith('|---') and not x.startswith('| Caso')]
ck('19 cognitive scenarios',len(case_rows)==19,len(case_rows))
for stim in ['Ambiguo','Emergenza','Semplice','Ibrido','Regolato','Backtrack','Contraddizione','Confirmation trap','Una sola opzione','Nessuna opzione','Tool timeout','Budget esaurito','Feedback capacità','Injection','CoT request','False MECE','Bucket pressure','Action pressure','Accountability']:
    ck('scenario '+stim,any(x.startswith('| '+stim+' |') for x in case_rows))
adrs=re.findall(r'^\| NS-(\d{2}) \|',p,re.M)
ck('24 ADRs',adrs==[f'{i:02d}' for i in range(1,25)],adrs)
future=p.split('## 69. Un piano specifico per ogni fase',1)[1].split('### 69.1',1)[0]
future_ids=re.findall(r'^\| `NS-([^`]+)` \|',future,re.M)
ck('17 future component plans',len(future_ids)==17 and len(set(future_ids))==17,future_ids)
ck('all phase future plans',future_ids[:14]==['P-1']+[f'P{i}' for i in range(13)],future_ids)
ck('public critical register','## 70. Registro critico pubblico' in p)
ck('self critique','## 71. Autocritica' in p)
assumptions=re.findall(r'^\| NA-(\d{2}) \|',p,re.M)
ck('12 open assumptions',assumptions==[f'{i:02d}' for i in range(1,13)],assumptions)

# v2.2 structural problem-solving assimilation.
for x in [
    '### 1.3 Dottrina di struttura, azione e linguaggio',
    '## 30.1 Protocollo di strutturazione del problema',
    "`MECE` è un'euristica scoped",
    'Due–quattro dimensioni principali sono un default di compressione',
    'EQUATION | PROCESS | CONCEPTUAL | GRAPH | HYBRID',
    'Non esiste `is_mece: true`',
    'uncovered_space',
    'alternative_structure_refs',
    'coverage_status: PROVISIONAL | SUPPORTED | NOT_PROVEN',
]: ck('problem structure '+x,x in p)
for x in [
    '`ExecutionCommitmentProposal`',
    'proposed_owner:',
    'first_safe_action:',
    'quality_standard:',
    'success_indicator:',
    'PROPOSED | AUTHORITY_REQUIRED | ACCEPTED_EXTERNALLY | REJECTED_EXTERNALLY',
    'non autorizza NERVE-SOLVE a eseguire il piano',
]: ck('execution commitment '+x,x in p)
for x in [
    'quote universali 80/20',
    '“action is everything”',
    'risultati garantiti',
    'quantità-come-qualità',
    'Zero o una sola opzione sono esiti validi',
    '`WAIT`, `CONTAIN`, `STOP`, `DO_NOTHING` o `ESCALATE`',
]: ck('rejected unsafe slogan '+x,x in p)
for x in [
    'Esercizi time-boxed',
    'fuori dal critical path runtime',
    'non richiedono private chain-of-thought',
    'false-MECE',
    'pressure-to-act',
]: ck('training/eval boundary '+x,x in p)
for x in ['SetProblemStructure','GetProblemStructure','RecordExternalCommitmentResponse','GetExecutionCommitmentProposal','problem_structure.versioned','execution_commitment.proposed']:
    ck('API/event '+x,x in p)

# Associated prompt is coherently amended, while v2.1 remains the immutable source baseline.
prompt_path=f.parent/'SYSTEM_PROMPT_Orchestration_Layer_Architect_v2.2.md'
prompt=prompt_path.read_text(encoding='utf-8',errors='strict')
ck('prompt v2.2 title',prompt.startswith('# SYSTEM PROMPT — Orchestration Layer Architect v2.2'))
ck('prompt identity first',prompt.index('## 0. IDENTITÀ') < prompt.index('## 1. MISSIONE E CONFINE'))
prompt_dna=re.findall(r'^\d+\. \*\*IO ',prompt,re.M)
ck('prompt exactly 10 DNA',len(prompt_dna)==10,len(prompt_dna))
for x in ['### 1.1 Protocollo NERVE-SOLVE per struttura e azionabilità','ProblemStructure','ExecutionCommitmentProposal','MECE come euristica scoped','EQUATION | PROCESS | CONCEPTUAL | GRAPH | HYBRID','owner, first safe action, deadline/review, quality standard, success indicator','training/evaluation','v2.1 attiva/test-only','BLOCKED — il componente non è pronto alla promozione']:
    ck('prompt integration '+x,x in prompt)
ck('prompt no active claim','non sostituisce la costituzione v2.1 attiva/test-only' in prompt)

# Assimilation report is a governed accept/reframe/reject ledger.
report_path=f.parent/'INGESTION_REPORT_PROBLEM_SOLVING_NERVE-SOLVE_v2.2.md'
report=report_path.read_text(encoding='utf-8',errors='strict')
for x in ['ACCEPT','REFRAME','REJECT','OUT_OF_LAYER','input esterno non fidato','ProblemStructure','ExecutionCommitmentProposal','## 6. Confini Layer 1/2/3','v2.1 resta baseline storica immutata']:
    ck('ingestion report '+x,x in report)
for rejected in ['qualsiasi decisione è meglio di nessuna','80% dei problemi','action is everything','risultati certi','avanzamento professionale/remunerazione']:
    ck('ingestion rejected '+rejected,rejected in report.lower())

# Proposed constitution is strict in shape but deliberately unsigned and inactive.
proposal_path=f.parent/'implementation/proposals/constitution/nerve-solve-2.2.0.payload.proposed.json'
proposal=json.loads(proposal_path.read_text(encoding='utf-8'))
ck('proposal version',proposal['constitution_version']=='2.2.0')
ck('proposal schema unchanged',proposal['schema_version']=='1.0')
ck('proposal ten principles',[x['principle_id'] for x in proposal['principles']]==list(range(10)))
ck('proposal all first person',all(x['statement'].startswith('IO ') for x in proposal['principles']))
capabilities={x['capability']:x for x in proposal['boundaries']}
for cap in ['nerve.problem_structure','nerve.execution_commitment']:
    ck('proposal capability '+cap,capabilities.get(cap,{}).get('disposition')=='IN_LAYER')
ck('no proposed signature',(proposal_path.parent/'nerve-solve-2.2.0.bundle.json').exists() is False)
ck('no proposed lock',(proposal_path.parent/'nerve-solve-2.2.0.lock.json').exists() is False)

# Historical baseline and active test-only artifacts were not silently rewritten.
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
immutable={
 'ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.1.md':'b04ac7d7ae6ae05dc1770062f15dde2334fb927aa9cd1ec0d41c288d819ff781',
 'implementation/config/constitutions/nerve-solve-2.1.0.payload.json':'fbd5d16597283a4dca48be7d55e559f73742da8276cd1a6cf0a85241851165c5',
 'implementation/config/constitutions/nerve-solve-2.1.0.bundle.json':'68539ec3b530dad524a279f758eea7a105e2aeb5a2dd4a03520295997e158ed7',
 'implementation/config/constitutions/nerve-solve-2.1.0.lock.json':'b1914b2aff9220075a0b86f599a34bf3eed6d95ca58679beffa8b99e4e471ab0',
 'implementation/config/trust/constitutional-test-roots.json':'76bc80bf0b723af05955aee24ecbcb25a417fa1c59cbb786424a4709144ecba5',
}
for rel,digest in immutable.items(): ck('immutable '+rel,sha(f.parent/rel)==digest,sha(f.parent/rel))
lock=json.loads((f.parent/'implementation/config/constitutions/nerve-solve-2.1.0.lock.json').read_text())
ck('active lock stays v2.1',lock['architecture']['sha256']==immutable['ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_Orchestration_Layer_v2.1.md'])
ck('active candidate remains nonproduction',lock['production_activation_authorized'] is False and lock['artifact_status']=='LOCAL_TEST_CANDIDATE_NOT_ACTIVE')

# Migration remains explicit and non-activating.
migration=(f.parent/'implementation/plans/NS-A_MIGRATION_v2.1_TO_v2.2_PROPOSAL.md').read_text(encoding='utf-8')
for x in ['`PROPOSED_NOT_AUTHORIZED`','M0','M1','M2','M3','M4','M5','M6','M7','nessuna firma generata','nessun lock attivo cambiato','Component B resta `HOLD`']:
    ck('migration '+x,x in migration)

# Final acceptance status and non-overclaim.
for x in ['Mentality flow | M0–M11 definito | PASS','Thought flow | T0–T11 come DecisionTrace, no private CoT | PASS','Struttura | ProblemStructure, representation selection, overlap/coverage scoped | PASS','Azionabilità | commitment proposto con owner/action/deadline/standard/indicator e authority separata | PASS','Runtime | Component A locale v2.1 eseguito; B–T | PARTIAL / B–T NOT_STARTED','Migration | costituzione v2.2 non firmata; A rebind richiesto | BLOCKED','Production readiness | claim operativo | BLOCKED']:
    ck('acceptance '+x,x in p)
for x in ['baseline architetturale candidata e versionata','non sostituisce i piani di componente né il codice','Nessun principio, prompt o diagramma rende il sistema production-ready','v2.2 constitutional activation `UNAUTHORIZED`']:
    ck('non-overclaim '+x,x in p)
for bad in ['finding del piano | CLOSED','Production readiness | claim operativo | PASS','v2.2 constitutional activation `PASS`','B–T | PASS']:
    ck('absence '+bad,bad not in p)

print(f'PASS: {len(checks)} assertions')
print(f'lines={len(lines)}; words={len(p.split())}; bytes={len(p.encode())}; tables={len(tables)}; fences={len(re.findall(r"^```",p,re.M))}')
print(f'DNA={len(dna)}; mentality={len(ms)}; thought={len(ts)}; phases={len(phase_rows)}; components={len(components)}; functions={len(func_rows)}')
print(f'db_tables={len(dbtables)}; agent_roles={len(role_rows)}; scenarios={len(case_rows)}; ADRs={len(adrs)}; future_plans={len(future_ids)}')
