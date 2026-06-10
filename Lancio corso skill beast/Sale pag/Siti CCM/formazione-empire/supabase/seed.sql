-- ============================================================
-- Formazione Empire — Seed CCM (v2, no DO blocks)
-- Esegui DOPO la migrazione 0001. Idempotente: puoi rilanciarlo.
-- ============================================================

-- ============================================================
-- 1. CORSO CCM
-- ============================================================
insert into public.courses (slug, title, subtitle, tagline, description, status, sort_order)
values (
  'claude-code-mastery',
  'Claude Code Mastery',
  'Il sistema completo per dominare Claude Code e costruirci un business reale',
  'Da zero a System Architect AI',
  '9 moduli, 32+ lezioni, 3 progetti portfolio, 15+ skill riutilizzabili, 8 risorse premium. Il corso più completo in italiano per trasformare Claude Code in un''arma professionale.',
  'available',
  0
)
on conflict (slug) do update set
  title = excluded.title,
  subtitle = excluded.subtitle,
  tagline = excluded.tagline,
  description = excluded.description,
  status = excluded.status;
-- ============================================================
-- 2. MODULI (9)
-- ============================================================
insert into public.modules (course_id, slug, title, subtitle, description, sort_order)
select c.id, m.slug, m.title, m.subtitle, m.description, m.sort_order
from (values
  ('setup-rapido',
   'Setup Rapido & Primo Agente',
   'Da zero al tuo primo operatore AI in 10 minuti',
   'Installazione guidata No-Code dell''intero ecosistema AI: Claude Code, Projects, Cowork, Perplexity, Manus. Il tuo primo operatore AI funzionante entro la fine del modulo.',
   0),
  ('framework-icro',
   'Fondamenta: Framework I.C.R.O.',
   'Il framework per risultati deterministici con Claude',
   'La Lingua di Claude: impara il framework I.C.R.O. per ottenere output consistenti e professionali. Context Management avanzato e comandi per pilotare Claude con precisione chirurgica.',
   1),
  ('skill-builder',
   'Skill Builder: Sistemi Riutilizzabili',
   'La tua libreria personale di 15+ skill AI',
   'L''AI come specialista: costruisci skill riutilizzabili con il framework S.K.I.L.L. Trigger proattivi, librerie custom, e la creazione della tua libreria personale di 15+ skill operative.',
   2),
  ('workflow-agenti',
   'Workflow & Agenti Collaborativi',
   'Orchestrazione multi-agente e mindset dell''architetto',
   'Framework W.O.R.K. per flussi multi-step. Orchestrazione di agenti in sequenziale vs parallelo. Sviluppa il mindset dell''architetto AI per progettare sistemi scalabili.',
   3),
  ('progetti-portfolio',
   'Progetti Reali: Il Portfolio',
   'Tre progetti completi per il tuo portfolio professionale',
   'Costruiamo insieme 3 progetti reali di livello enterprise che puoi mostrare ai clienti o usare per te stesso: Content System, Report Enterprise, Business Process Automation.',
   4),
  ('monetizzazione',
   'Monetizzazione & Business',
   'Trasforma le skill in un business reale',
   'Come vendere le competenze appena acquisite: freelance, agenzia AI, prodotti digitali, automazioni, consulenze. Definizione offerta, pricing strategico, outreach con il Metodo D.A.N.',
   5),
  ('claude-code-avanzato',
   'Claude Code Avanzato',
   'Sub-agenti, hook, MCP server — l''arsenale completo',
   'Costruzione di flussi end-to-end. Orchestrazione multi-agente su progetti complessi. Sub-agenti, hook, MCP server per estensioni custom. Tecniche avanzate di context engineering.',
   6),
  ('cowork-avanzato',
   'Claude Cowork Avanzato',
   'Automazione processi aziendali e web',
   'Automazione di qualsiasi processo aziendale. Azioni sul web (browsing, form, scraping controllato). Pipeline ibride Cowork + Projects + Perplexity + Manus.',
   7),
  ('ricerca-mercato',
   'Ricerca di Mercato',
   'La skill più importante per il futuro',
   'Come leggere il mercato prima di costruire. Metodo di validazione: segnali reali di domanda vs rumore. Scovare nicchie scoperte e offerte già pagate dal mercato.',
   8)
) as m(slug, title, subtitle, description, sort_order)
cross join public.courses c
where c.slug = 'claude-code-mastery'
on conflict (course_id, slug) do update set
  title = excluded.title,
  subtitle = excluded.subtitle,
  description = excluded.description,
  sort_order = excluded.sort_order;

-- ============================================================
-- 3. LEZIONI (32)
-- ============================================================
insert into public.lessons (module_id, slug, title, description, long_description, duration_minutes, sort_order)
select m.id, l.slug, l.title, l.description, l.long_description, l.duration_minutes, l.sort_order
from (values
  -- Modulo 0: Setup Rapido
  ('setup-rapido', 'ecosistema',
   'L''ecosistema: Claude Code, Projects, Cowork, Perplexity, Manus',
   'Panoramica completa degli strumenti che useremo.',
   'In questa lezione introduttiva facciamo una mappatura completa dell''ecosistema AI che utilizzeremo durante tutto il corso. Vedrai cos''è Claude Code, come si differenzia da Projects e Cowork, il ruolo di Perplexity e come Manus si integra nel workflow. Al termine avrai una visione chiara di quando usare ogni strumento.',
   12, 0),
  ('setup-rapido', 'installazione-guidata',
   'Installazione GUIDATA (No-Code approach)',
   'Installa tutto senza scrivere una riga di codice.',
   'Guida passo-passo per installare tutti gli strumenti dell''ecosistema senza necessità di competenze tecniche. Ogni comando viene spiegato nel dettaglio con screenshot e video demo. Troubleshooting dei problemi più comuni.',
   18, 1),
  ('setup-rapido', 'primo-operatore',
   'Il tuo primo operatore AI in 10 minuti',
   'Costruisci il tuo primo agente AI funzionante.',
   'Passiamo dalla teoria alla pratica. Costruiamo insieme il tuo primo operatore AI: un assistente che analizza testi e produce report strutturati. Vedrai il potere di un singolo prompt ben strutturato.',
   22, 2),
  -- Modulo 1: Framework ICRO
  ('framework-icro', 'lingua-claude',
   'La ''Lingua'' di Claude: Context Mastery',
   'Come pensa Claude e come parlargli.',
   'Capire come Claude processa il contesto è la differenza tra output mediocri e output eccellenti. In questa lezione smontiamo il modo in cui il modello ragiona e ti do i principi per comunicare con lui in modo ottimale.',
   25, 0),
  ('framework-icro', 'icro',
   'Framework I.C.R.O. per risultati deterministici',
   'Input, Context, Role, Output — il sistema completo.',
   'I.C.R.O. = Input, Context, Role, Output. Il framework proprietario che uso per ogni mia skill, agente e prompt professionale. Esempi pratici applicati a 5 use-case diversi.',
   32, 1),
  ('framework-icro', 'context-management',
   'Comandi Avanzati & Context Management',
   'Slash commands, memoria, context engineering.',
   'Tutti i comandi avanzati di Claude Code che fanno la differenza: /compact, /clear, /resume, memoria persistente, gestione del context window. Come evitare context rot e far lavorare Claude su task lunghi.',
   28, 2),
  -- Modulo 2: Skill Builder
  ('skill-builder', 'skill-framework',
   'L''AI come specialista (Framework S.K.I.L.L.)',
   'Dallo script alla skill riutilizzabile.',
   'Il salto di qualità: smettere di scrivere prompt one-shot e iniziare a costruire skill. Framework S.K.I.L.L. = Scope, Knowledge, Instructions, Limits, Links. Architettura di una skill professionale.',
   30, 0),
  ('skill-builder', 'trigger-proattivi',
   'Trigger Proattivi e Librerie Custom',
   'Skill che si attivano da sole al momento giusto.',
   'Come configurare trigger proattivi affinché le skill si attivino automaticamente al rilevamento del contesto giusto. Librerie condivise, skill namespaces, gestione versioni.',
   26, 1),
  ('skill-builder', 'tua-libreria',
   'Creazione della tua Libreria di 15+ Skill',
   'Costruiamo insieme 15 skill pronte all''uso.',
   'Workshop completo: costruiamo 15 skill operative che puoi usare immediatamente nel tuo business. Content creation, data analysis, customer support, sales outreach, research e molto altro.',
   75, 2),
  -- Modulo 3: Workflow & Agenti
  ('workflow-agenti', 'work-framework',
   'Framework W.O.R.K. per flussi multi-step',
   'Da skill singole a workflow articolati.',
   'Quando un task richiede più passaggi coordinati, servono i workflow. Framework W.O.R.K. = Workflow, Orchestration, Routing, Kernel. Casi d''uso reali nel business.',
   34, 0),
  ('workflow-agenti', 'orchestrazione',
   'Orchestrazione Agenti (Sequenziali vs Paralleli)',
   'Quando usare un agente solo, quando più agenti insieme.',
   'Trade-off tra sequenziale e parallelo. Come distribuire task complessi su più agenti specializzati. Gestione dipendenze e sincronizzazione.',
   38, 1),
  ('workflow-agenti', 'mindset-architetto',
   'Il Mindset dell''Architetto AI',
   'Pensare in sistemi, non in prompt.',
   'La transizione mentale da ''utente di AI'' ad ''architetto AI''. Come progettare sistemi AI scalabili, manutenibili, e aggiornabili. Principi di software engineering applicati al prompt engineering.',
   22, 2),
  -- Modulo 4: Progetti Portfolio
  ('progetti-portfolio', 'content-system',
   'Progetto 1: Content System Completo',
   'Sistema di content generation end-to-end.',
   'Sistema AI che genera post, thread, articoli e newsletter partendo da un singolo topic. Pipeline completa con ricerca, outline, writing, editing, repurposing multi-piattaforma.',
   90, 0),
  ('progetti-portfolio', 'report-enterprise',
   'Progetto 2: Analisi & Report Enterprise',
   'Sistema di analisi dati e report professionali.',
   'Sistema AI che analizza dataset, genera insight, e produce report PDF multi-pagina di livello consulenziale. Ideale per agenzie e consulenti.',
   85, 1),
  ('progetti-portfolio', 'automation',
   'Progetto 3: Business Process Automation',
   'Automazione processi aziendali completi.',
   'Sistema che automatizza un intero processo aziendale: lead qualification, email outreach, CRM update, calendar booking, follow-up. Tutto orchestrato da agenti AI.',
   100, 2),
  -- Modulo 5: Monetizzazione
  ('monetizzazione', 'vendere-skill',
   'Come vendere le competenze appena acquisite',
   '5 modelli di business applicabili da subito.',
   'Panoramica dei 5 modelli di business più redditizi per chi sa usare Claude Code professionalmente. Pro, contro, time-to-first-money di ognuno.',
   28, 0),
  ('monetizzazione', 'offerta-pricing',
   'Definizione offerta & pricing strategico',
   'Come posizionare e prezzare il tuo valore.',
   'Metodologia per costruire un''offerta chiara e differenziata. Pricing strategico basato sul valore, non sul tempo. Esempi reali di offerte a 3k, 5k, 10k €.',
   35, 1),
  ('monetizzazione', 'metodo-dan',
   'Il Metodo D.A.N. per l''Outreach',
   'Messaggi di outreach che convertono davvero.',
   'D.A.N. = Diagnosi, Aspirazione, Next Step. Il framework che uso per scrivere messaggi di outreach con tassi di risposta del 20%+. Template e script reali.',
   30, 2),
  ('monetizzazione', 'prima-call',
   'Script di Chiusura e Prima Call con Cliente',
   'Come gestire la prima call e chiudere il deal.',
   'Struttura della prima call: discovery, presentation, close. Script testati e ottimizzati. Come gestire obiezioni comuni.',
   32, 3),
  -- Modulo 6: Claude Code Avanzato
  ('claude-code-avanzato', 'flussi-end-to-end',
   'Costruzione di interi flussi di lavoro end-to-end',
   'Dal trigger iniziale al deliverable finale.',
   'Progettazione di flussi di lavoro completi che partono da un singolo trigger (email, form, evento) e producono un deliverable finale senza intervento umano.',
   48, 0),
  ('claude-code-avanzato', 'multi-agente-complessi',
   'Orchestrazione multi-agente su progetti complessi',
   'Quando servono 5+ agenti coordinati.',
   'Scenari reali dove serve orchestrare 5, 10 o più agenti su progetti complessi. Pattern di coordinazione, shared state, checkpointing.',
   52, 1),
  ('claude-code-avanzato', 'sub-agenti-hook-mcp',
   'Sub-agenti, hook e MCP server per estensioni custom',
   'Estendi Claude Code con tool custom.',
   'Sub-agenti specializzati con tool set ristretti. Hook per automatizzare azioni su eventi. MCP server per integrare qualsiasi API o tool esterno.',
   55, 2),
  ('claude-code-avanzato', 'context-engineering-advanced',
   'Tecniche avanzate di context engineering',
   'Ottimizzazione del context window per task lunghi.',
   'Come mantenere Claude performante su task di ore o giorni. Context compaction strategica, memory files, checkpoint & resume patterns.',
   40, 3),
  -- Modulo 7: Cowork Avanzato
  ('cowork-avanzato', 'processi-aziendali',
   'Automazione di qualsiasi processo aziendale',
   'Mappa il processo e automatizzalo.',
   'Metodologia per mappare un processo aziendale esistente e automatizzarlo con Cowork. Dal process mining all''implementazione.',
   42, 0),
  ('cowork-avanzato', 'azioni-web',
   'Automazione di azioni sul web',
   'Browsing, form, scraping controllato.',
   'Come far eseguire a Claude azioni reali sul web: compilare form, estrarre dati, navigare dashboard, interagire con SaaS tools.',
   38, 1),
  ('cowork-avanzato', 'pipeline-ibride',
   'Pipeline ibride Cowork + Projects + Perplexity + Manus',
   'Il meglio di ogni strumento in un''unica pipeline.',
   'Quando usare quale strumento. Pipeline ibride che sfruttano i punti di forza di ogni tool. Case study reali.',
   45, 2),
  ('cowork-avanzato', 'workflow-autoesecutivi',
   'Workflow auto-esecutivi che lavorano mentre dormi',
   'Scheduler, cron, trigger remoti.',
   'Come configurare workflow che si eseguono automaticamente su schedule, eventi esterni, webhook. Il tuo business che lavora 24/7.',
   36, 3),
  -- Modulo 8: Ricerca di Mercato
  ('ricerca-mercato', 'cosa-funziona',
   'Come cercare sul mercato ciò che funziona DAVVERO',
   'Distinguere il rumore dai segnali.',
   'Dove guardare per trovare prodotti, servizi, offerte che il mercato sta già comprando. Strumenti e fonti per la ricerca di mercato seria.',
   32, 0),
  ('ricerca-mercato', 'validazione',
   'Metodo di validazione: segnali reali vs rumore',
   'Come capire se c''è vera domanda.',
   'Framework per validare un''idea in massimo 7 giorni. Segnali di domanda reale vs hype. Test a basso costo per validare prima di costruire.',
   30, 1),
  ('ricerca-mercato', 'nicchie-scoperte',
   'Scovare nicchie scoperte e offerte pagate dal mercato',
   'Dove il gold rush è ancora aperto.',
   'Tecnica per trovare nicchie ancora poco presidiate ma con buona capacità di spesa. Come identificare offerte che i clienti già pagano ma sottoserviti.',
   28, 2),
  ('ricerca-mercato', 'leggere-mercato',
   'Leggere il mercato prima di costruire',
   'La skill che cambia la tua carriera.',
   'La mentalità del market-first builder. Come smettere di costruire cose che nessuno vuole e iniziare a servire domanda esistente con offerte superiori.',
   35, 3)
) as l(module_slug, slug, title, description, long_description, duration_minutes, sort_order)
join public.modules m on m.slug = l.module_slug
join public.courses c on c.id = m.course_id and c.slug = 'claude-code-mastery'
on conflict (module_id, slug) do update set
  title = excluded.title,
  description = excluded.description,
  long_description = excluded.long_description,
  duration_minutes = excluded.duration_minutes,
  sort_order = excluded.sort_order;

-- ============================================================
-- 4. RISORSE GLOBALI (course-level) — prima le puliamo per idempotenza
-- ============================================================
delete from public.resources
where course_id = (select id from public.courses where slug = 'claude-code-mastery');

insert into public.resources (course_id, title, type, size_label, href, sort_order)
select c.id, r.title, r.type, r.size_label, r.href, r.sort_order
from (values
  ('Libreria completa delle 15 Skill', 'zip', '620 KB', '#', 0),
  ('Framework I.C.R.O. — Guida Completa', 'pdf', '4.2 MB', '#', 1),
  ('Framework S.K.I.L.L. — Guida Completa', 'pdf', '3.8 MB', '#', 2),
  ('Framework W.O.R.K. — Guida Completa', 'pdf', '3.6 MB', '#', 3),
  ('Metodo D.A.N. — Script Outreach', 'pdf', '2.4 MB', '#', 4),
  ('Template Prima Call con Cliente', 'pdf', '1.8 MB', '#', 5),
  ('Cheatsheet Comandi Claude Code', 'pdf', '1.2 MB', '#', 6),
  ('3 Progetti Portfolio (codice + prompt)', 'zip', '4.5 MB', '#', 7)
) as r(title, type, size_label, href, sort_order)
cross join public.courses c
where c.slug = 'claude-code-mastery';

-- ============================================================
-- 5. CORSI VETRINA (coming-soon)
-- ============================================================
insert into public.courses (slug, title, subtitle, tagline, description, status, sort_order) values
  ('cro-mastery', 'CRO Copy Mastery',
   'Scrivere copy che converte — il sistema Digital Empire',
   'Il sistema di copywriting che ha generato 7 cifre',
   'Il framework completo di Digital Empire per scrivere sale page, email, ads e VSL che convertono davvero. Dal mindset agli script reali.',
   'coming-soon', 10),
  ('launch-mastery', 'Launch Mastery',
   'Il playbook per lanciare e vendere prodotti digitali',
   'Da idea a primo €10k in 30 giorni',
   'Il sistema end-to-end per lanciare un info-prodotto: validation, offerta, funnel, sale page, ads, email sequence, community.',
   'coming-soon', 11)
on conflict (slug) do update set
  title = excluded.title,
  status = excluded.status;

-- ============================================================
-- 6. VERIFICA (output rapido per confermare)
-- ============================================================
select
  (select count(*) from public.courses) as courses_count,
  (select count(*) from public.modules) as modules_count,
  (select count(*) from public.lessons) as lessons_count,
  (select count(*) from public.resources) as resources_count;
