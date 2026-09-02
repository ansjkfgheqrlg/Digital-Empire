"""Fix bad/short agent descriptions with manually-curated ones."""
import os
import re

AGENTS_DIR = os.path.dirname(os.path.abspath(__file__)) + "/agents"

# Manual description overrides for agents with bad auto-extracted descriptions
OVERRIDES = {
    # APEX-7
    "apex-analyst": "Analista di APEX-7. Trova pattern nei dati, connette informazioni disperse in insight utili. Lavora in parallelo con Writer. Attiva per analisi profonde, ricerca pattern, sintesi dati.",
    "apex-critic": "Critico di APEX-7. Trova falle e debolezze in ogni output prima della consegna. Identifica problemi che costerebbero di piu' se scoperti dopo. Attiva per review, quality check, stress test.",
    "apex-gate-agent": "Gate agent di APEX-7. Ultimo controllo prima che un output raggiunga l'utente. Non crea ne' migliora, solo valuta e decide pass/fail. Attiva per gate finale, approvazione output.",
    "apex-meta-agent": "Meta agent di APEX-7. Osserva il sistema dall'esterno, vede pattern che i singoli agenti non vedono. Interviene quando il sistema si inceppa, evolve il sistema. Attiva per audit di sistema, ottimizzazione workflow.",
    "apex-orchestrator": "Orchestratore di APEX-7. Coordina tutti gli agenti del sistema, decide il flusso, instanzia e monitora. Sistema nervoso centrale di APEX-7. Attiva per orchestrazione multi-agente, coordinamento task.",
    "apex-planner": "Planner di APEX-7. Trasforma obiettivi vaghi in piani chirurgici. Non esegue mai, pianifica con ossessione per il dettaglio. Attiva per pianificazione, decomposizione task, strategia.",
    "apex-refiner": "Refiner di APEX-7. Riceve output difettosi e li rende eccellenti con precisione chirurgica. Preserva cio' che funziona, sostituisce cio' che non funziona. Attiva per raffinamento output, correzione mirata.",
    "apex-writer": "Writer di APEX-7. Trasforma piani e analisi in output concreti e di valore. Ogni parola deve guadagnarsi il suo posto. Attiva per scrittura, produzione contenuti, output finali.",

    # Context Engineering Commands
    "alignment.agent": "Agente di allineamento per Context Engineering. Verifica che il lavoro rispetti gli obiettivi originali, mantiene coerenza tra fasi. Attiva per alignment check, verifica coerenza, goal tracking.",
    "architect-agent": "Architetto per Context Engineering. Progetta l'architettura completa di agenti AI, definisce componenti, interazioni, flussi dati. Attiva per design architetturale, progettazione sistemi agenti.",
    "build-implementation": "Builder per Context Engineering. Scrive codice Python di automazione robusto e production-ready. Attiva per implementazione codice, build di automazioni, sviluppo software.",
    "cli.agent": "Agente CLI per Context Engineering. Gestisce operazioni da linea di comando, script eseguibili, interfacce terminale. Attiva per task CLI, scripting, automazione terminale.",
    "comms.agent": "Agente comunicazioni per Context Engineering. Gestisce comunicazioni strutturate tra agenti, formatta messaggi, coordina handoff. Attiva per comunicazione inter-agente, reporting.",
    "data.agent": "Agente dati per Context Engineering. Gestisce acquisizione, trasformazione e analisi dati. Attiva per data processing, ETL, analisi dataset.",
    "deploy.agent": "Agente deploy per Context Engineering. Gestisce deployment di sistemi e automazioni. Attiva per deploy, rilascio, messa in produzione.",
    "deploy-cloud": "Agente deploy cloud per Context Engineering. Deploya sistemi nel cloud (AWS, GCP, Vercel, etc.). Attiva per cloud deployment, infrastructure, hosting.",
    "doc.agent": "Agente documentazione per Context Engineering. Genera e mantiene documentazione tecnica di qualita'. Attiva per documentazione, README, guide tecniche.",
    "legal.agent": "Agente legale per Context Engineering. Verifica conformita' legale, licenze, termini di servizio. Attiva per compliance, legal review, licenze software.",
    "lit.agent": "Agente letteratura per Context Engineering. Ricerca e sintetizza letteratura tecnica e accademica. Attiva per research literature, paper review, stato dell'arte.",
    "marketing.agent": "Agente marketing per Context Engineering. Crea materiali marketing per prodotti tecnici. Attiva per marketing copy, product marketing, positioning.",
    "meta.agent": "Meta agente per Context Engineering. Coordina e ottimizza il sistema di agenti stesso. Attiva per meta-ottimizzazione, system improvement, agent coordination.",
    "monitor.agent": "Agente monitoring per Context Engineering. Monitora sistemi in produzione, rileva anomalie. Attiva per monitoring, alerting, health check.",
    "optimize.agent": "Agente ottimizzazione per Context Engineering. Ottimizza performance, costi, qualita' dei sistemi. Attiva per optimization, performance tuning, cost reduction.",
    "research.agent": "Agente ricerca per Context Engineering. Esplora codebase e riferimenti esterni prima della progettazione. Attiva per codebase exploration, research, analisi preliminare.",
    "review-and-heal": "Agente review e self-healing per Context Engineering. Fa review, testing e auto-riparazione dei sistemi. Attiva per code review, testing, self-healing, bug fixing.",
    "security.agent": "Agente sicurezza per Context Engineering. Verifica sicurezza del codice, vulnerabilita', secret exposure. Attiva per security audit, vulnerability scan, secret detection.",
    "test.agent": "Agente testing per Context Engineering. Scrive e esegue test per ogni implementazione non triviale. Attiva per unit test, integration test, test automation.",

    # Content Forge 2.0
    "cf-conductor": "Conductor di Content Forge 2.0. Orchestratore principale della pipeline di trasformazione contenuti. Gestisce tutti i sub-agenti, tracking stato, trace. Attiva per orchestrazione content forge, pipeline gestione.",
    "cf-ingestion-agent": "Agente ingestione di Content Forge 2.0. Acquisisce e preprocessa contenuti grezzi (PDF, video, testi). Attiva per ingestione contenuti, preprocessing, parsing documenti.",
    "cf-knowledge-graph-agent": "Agente knowledge graph di Content Forge 2.0. Assembla il grafo della conoscenza da atoms JSON, dedup, gerarchia, edges, cluster. Attiva per graph building, knowledge mapping.",
    "cf-phase-planner-agent": "Phase planner di Content Forge 2.0. Genera piani per fasi successive quando le soglie di failure sono raggiunte. Attiva per phase planning, failure recovery, pipeline advancement.",
    "cf-agent-builder-agent": "Agent builder di Content Forge 2.0. Costruisce nuovi agenti per la pipeline forge. Attiva per creazione agenti, agent scaffolding.",
    "cf-agent-depth-agent": "Depth agent di Content Forge 2.0. Approfondisce analisi su contenuti specifici per massima profondita'. Attiva per deep analysis, content depth, approfondimento.",
    "cf-analyst-agent": "Analista di Content Forge 2.0. Analizza contenuti estratti per pattern, insight, struttura. Attiva per content analysis, pattern extraction.",
    "cf-coverage-verifier-agent": "Coverage verifier di Content Forge 2.0. Verifica che tutti i contenuti sorgente siano stati processati senza lacune. Attiva per coverage check, completeness verification.",
    "cf-custom-builder-agent": "Custom builder di Content Forge 2.0. Costruisce output personalizzati secondo specifiche custom. Attiva per custom output, build personalizzati.",
    "cf-doc-builder-agent": "Doc builder di Content Forge 2.0. Costruisce documentazione strutturata dai contenuti processati. Attiva per document generation, report building.",
    "cf-failure-detector-agent": "Failure detector di Content Forge 2.0. Rileva fallimenti nella pipeline e diagnostica cause. Attiva per error detection, failure analysis, diagnostica.",
    "cf-formula-validator-agent": "Formula validator di Content Forge 2.0. Valida formule, framework e strutture logiche nei contenuti. Attiva per formula check, logic validation.",
    "cf-humanizer-agent": "Humanizer di Content Forge 2.0. Rende i contenuti generati piu' naturali e umani, elimina tone robotico. Attiva per humanization, tone adjustment, naturalezza.",
    "cf-mkd-builder-agent": "MKD builder di Content Forge 2.0. Costruisce file MKD (master knowledge document) strutturati. Attiva per MKD generation, knowledge document building.",
    "cf-orchestration-builder-agent": "Orchestration builder di Content Forge 2.0. Costruisce workflow di orchestrazione per pipeline complesse. Attiva per workflow building, pipeline design.",
    "cf-question-designer-agent": "Question designer di Content Forge 2.0. Progetta domande per quiz, assessment, verifiche di comprensione. Attiva per question design, quiz creation.",
    "cf-reference-expander-agent": "Reference expander di Content Forge 2.0. Espande riferimenti e citazioni con contesto completo. Attiva per reference expansion, citation enrichment.",
    "cf-skill-builder-agent": "Skill builder di Content Forge 2.0. Costruisce skill Claude Code dai contenuti processati. Attiva per skill creation, skill packaging.",
    "cf-skill-depth-agent": "Skill depth agent di Content Forge 2.0. Approfondisce skill con conoscenza aggiuntiva e casi d'uso. Attiva per skill enrichment, depth enhancement.",
    "cf-target-advisor-agent": "Target advisor di Content Forge 2.0. Consiglia il target output ottimale per i contenuti processati. Attiva per target recommendation, output format advice.",
    "cf-target-schema-validator-agent": "Target schema validator di Content Forge 2.0. Valida che l'output rispetti lo schema target specificato. Attiva per schema validation, output conformity check.",
    "cf-team-builder-agent": "Team builder di Content Forge 2.0. Costruisce configurazioni team multi-agente per task specifici. Attiva per team configuration, multi-agent setup.",
    "cf-triage-agent": "Triage agent di Content Forge 2.0. Classifica e smista contenuti in ingresso verso la pipeline appropriata. Attiva per content triage, classification, routing.",
    "cf-wiki-builder-agent": "Wiki builder di Content Forge 2.0. Costruisce pagine wiki strutturate dai contenuti processati. Attiva per wiki generation, knowledge base building.",
    "cf-workflow-builder-agent": "Workflow builder di Content Forge 2.0. Costruisce workflow automatizzati dai contenuti processati. Attiva per workflow generation, automation building.",

    # Board/C-Suite remaining
    "chief-forge": "Chief Forge di Digital Empire. Factory di skill, agenti e team. Owner della lista P0 skill, MKD mandatory, supervisiona ecosistema 07-FORGE e guilds. Attiva per creazione agenti, skill, team, quality gate skill.",
    "cmo-empire": "CMO di Digital Empire. Owner standard APSOC, brand voice, copy gate. Supervisiona 03-CONTENT-FACTORY e 04-MARKETING. Attiva per strategy marketing, brand voice, copy review, APSOC gate.",
    "cro-empire": "CRO di Digital Empire. Revenue blockers, conversion, lancio prodotti. Supervisiona 01-AGENCY e 02-INFO-BUSINESS. Attiva per revenue pipeline, pricing, lancio prodotti, deal review.",

    # MBA agents
    "mba-conductor": "Conductor di Master Build Architecture. Orchestratore principale per progettazione architetture software complete. Attiva per architettura software, system design, progettazione complessa.",
    "mba-agent-spec-builder": "Agent spec builder di Master Build Architecture. Costruisce specifiche complete per agenti (system prompt, tools, playbook, evals, failure modes, memory). Attiva per agent specification, agent design.",
    "mba-anti-pattern-hunter": "Anti-pattern hunter di Master Build Architecture. Cerca e identifica anti-pattern nel design architetturale. Attiva per anti-pattern detection, design review, quality audit.",
    "mba-context-boundary-architect": "Context boundary architect di Master Build Architecture. Progetta i confini dei contesti in architetture complesse. Attiva per context design, boundary definition, DDD.",
    "mba-coverage-verifier-agent": "Coverage verifier di Master Build Architecture. Verifica copertura completa delle specifiche architetturali. Attiva per coverage check, spec completeness.",
    "mba-failure-detector-agent": "Failure detector di Master Build Architecture. Rileva potenziali punti di fallimento nell'architettura. Attiva per failure analysis, risk detection.",
    "mba-failure-mode-validator-agent": "Failure mode validator di Master Build Architecture. Valida che tutti i failure mode siano gestiti correttamente. Attiva per failure mode validation, resilience check.",
    "mba-ingestion-agent": "Ingestion agent di Master Build Architecture. Acquisisce requisiti e contesto per la progettazione architetturale. Attiva per requirements gathering, context ingestion.",
    "mba-memory-ecosystem-builder": "Memory ecosystem builder di Master Build Architecture. Progetta sistemi di memoria e persistenza per agenti. Attiva per memory design, persistence architecture.",
    "mba-plan-builder": "Plan builder di Master Build Architecture. Costruisce piani di implementazione dettagliati dall'architettura. Attiva per implementation planning, roadmap building.",
    "mba-principle-codifier": "Principle codifier di Master Build Architecture. Codifica principi architetturali in regole verificabili. Attiva per principle definition, architectural rules.",
    "mba-principles-manager": "Principles manager di Master Build Architecture. Gestisce e mantiene il catalogo dei principi architetturali. Attiva per principles management, architectural governance.",
    "mba-ruflo-swarm-extractor": "Ruflo swarm extractor di Master Build Architecture. Estrae pattern di swarm orchestration dall'architettura. Attiva per swarm extraction, multi-agent pattern mining.",
    "mba-skill-depth-agent": "Skill depth agent di Master Build Architecture. Approfondisce skill con conoscenza architetturale. Attiva per skill enrichment, architectural knowledge.",
    "mba-swarm-builder": "Swarm builder di Master Build Architecture. Costruisce configurazioni swarm multi-agente. Attiva per swarm design, multi-agent orchestration setup.",
    "mba-target-schema-validator-agent": "Target schema validator di Master Build Architecture. Valida output contro schema target. Attiva per schema validation, output verification.",
    "mba-topology-designer": "Topology designer di Master Build Architecture. Progetta la topologia di comunicazione tra agenti. Attiva per topology design, agent communication patterns.",

    # YouTube Factory
    "ytf-conductor": "Conductor di YouTube Automation Factory. Orchestratore principale della fabbrica YouTube, unico che parla con l'utente, coordina tutti i sub-agenti. Attiva per produzione video YouTube, orchestrazione pipeline.",
    "ytf-niche-gate": "Niche gate di YouTube Automation Factory. Gate di controllo che BLOCCA nicchie non validate. Controllo indipendente dalla scout. Attiva per nicchia validation, market fit check.",
    "ytf-qa-audio-video": "QA audio/video di YouTube Automation Factory. BLOCCA il passaggio se il video non supera canoni di qualita' audio/video. Controllo indipendente dal producer. Attiva per quality check video, audio verification.",
    "ytf-seo-gate": "SEO gate di YouTube Automation Factory. BLOCCA la pubblicazione se i metadati non sono a norma SEO. Controllo indipendente dal metadata optimizer. Attiva per SEO validation, metadata check.",
    "ytf-memory-keeper": "Memory keeper di YouTube Automation Factory. Mantiene la memoria persistente della fabbrica, checkpoints, learned rules. Attiva per memory management, knowledge persistence.",
    "ytf-metadata-optimizer": "Metadata optimizer di YouTube Automation Factory. Ottimizza titoli, descrizioni, tag per massimo SEO e CTR. Attiva per metadata optimization, SEO copywriting.",
    "ytf-niche-scout": "Niche scout di YouTube Automation Factory. Cerca e valuta nicchie profittevoli per canali YouTube automation. Attiva per niche research, market analysis.",
    "ytf-performance-auditor": "Performance auditor di YouTube Automation Factory. Audita performance dei video pubblicati, identifica pattern di successo. Attiva per performance analysis, video analytics.",
    "ytf-script-writer": "Script writer di YouTube Automation Factory. Scrive script per video YouTube ottimizzati per retention. Attiva per scriptwriting, video scripting.",
    "ytf-self-improver": "Self-improver di YouTube Automation Factory. Analizza performance passate e migliora i processi della fabbrica. Attiva per self-improvement, process optimization.",
    "ytf-seo-analyst": "SEO analyst di YouTube Automation Factory. Analizza keyword, trend, competitor per strategia SEO YouTube. Attiva per YouTube SEO, keyword research.",
    "ytf-thumbnail-designer": "Thumbnail designer di YouTube Automation Factory. Progetta thumbnail ad alto CTR per video YouTube. Attiva per thumbnail design, visual optimization.",
    "ytf-video-hunter": "Video hunter di YouTube Automation Factory. Cerca video sorgente da cui creare contenuti originali. Attiva per content sourcing, video research.",
    "ytf-video-producer": "Video producer di YouTube Automation Factory. Produce video finali assemblando script, audio, visual. Attiva per video production, assembly, rendering.",

    # YouTube Launch
    "ytl-brand-designer": "Brand designer di YouTube Channel Launch. Progetta identita' visiva del canale (logo, colori, banner). Attiva per brand design, visual identity.",
    "ytl-channel-architect": "Channel architect di YouTube Channel Launch. Progetta struttura del canale (categorie, playlist, about). Attiva per channel setup, architecture planning.",
    "ytl-channel-seo": "Channel SEO di YouTube Channel Launch. Ottimizza il canale per discovery (keywords, about, tags). Attiva per channel SEO, discoverability.",
    "ytl-launch-gate": "Launch gate di YouTube Channel Launch. Gate finale prima del lancio, verifica tutto sia pronto. Attiva per launch readiness, pre-launch check.",
    "ytl-monetization-planner": "Monetization planner di YouTube Channel Launch. Pianifica strategia di monetizzazione del canale. Attiva per monetization strategy, revenue planning.",

    # YouTube Compliance
    "ytc-compliance-gate": "Compliance gate di YouTube Compliance Shield. Gate finale di conformita' prima della pubblicazione. Attiva per compliance check, publication readiness.",
    "ytc-copyright-scanner": "Copyright scanner di YouTube Compliance Shield. Scansiona contenuti per violazioni copyright. Attiva per copyright check, content originality.",
    "ytc-originality-auditor": "Originality auditor di YouTube Compliance Shield. Audita originalita' dei contenuti per evitare strike. Attiva per originality audit, uniqueness verification.",
    "ytc-policy-checker": "Policy checker di YouTube Compliance Shield. Verifica conformita' alle policy YouTube (community guidelines, ToS). Attiva per policy check, guideline compliance.",

    # Outreach
    "outreach-case-study-forge": "Case study forge di Outreach Team. Crea case study professionali da delivery completate con metriche verificate. Attiva per case study creation, social proof.",
    "outreach-followup-sequencer": "Follow-up sequencer di Outreach Team. Progetta sequenze di follow-up per prospect non rispondenti. Attiva per follow-up sequences, drip campaigns.",
    "outreach-message-writer": "Message writer di Outreach Team. Scrive messaggi outreach personalizzati per ogni canale (email, LinkedIn, IG). Attiva per outreach copy, cold messaging.",
    "outreach-rule-keeper": "Rule keeper di Outreach Team. Vigila sul rispetto delle regole outreach (anti-spam, tone, compliance). Attiva per outreach compliance, rule enforcement.",

    # Website Creator
    "web-copy-writer": "Copy writer di Website Creator. Scrive copy per landing page e siti web. Attiva per web copy, landing page text, website content.",
    "web-section-coder": "Section coder di Website Creator. Codifica sezioni HTML/CSS/JS per siti web. Attiva per web development, section coding, frontend.",
    "web-web-master": "Web master di Website Creator. Coordina la creazione completa del sito, gestisce struttura e deploy. Attiva per website management, site orchestration.",

    # Backbone
    "bb-handoff-router": "Handoff Router del Backbone. Instrada handoff tra ecosistemi, verifica schema HC-v1. Attiva per routing inter-ecosistema, handoff management.",
    "bb-memory-writer": "Memory Writer del Backbone. Scrive e legge AgentDB per tutti i 10 namespace ecosistema. Attiva per memory persistence, AgentDB operations.",

    # Guilds
    "guild-copy-apsoc": "Copy-APSOC Guild leader. Governa lo standard APSOC per il copy in tutto l'Impero. Attiva per APSOC review, copy standard, quality assurance copy.",
    "guild-cost": "Cost Guild leader. Governa le policy di costo e ottimizzazione budget. Attiva per cost optimization, budget policy, spending review.",
    "guild-design": "Design Guild leader. Governa gli standard di design e UX. Attiva per design review, UX standards, visual consistency.",
    "guild-prompt": "Prompt Guild leader. Governa gli standard di prompt engineering. Attiva per prompt review, prompt optimization, prompt quality.",
    "guild-quality": "Quality Guild leader. Governa gli standard di qualita' cross-empire. Attiva per quality review, standards enforcement, QA.",

    # Sentinels
    "sentinel-brandvoice": "BrandVoice Sentinel. Vigila su claim senza prova, tono passivo, canoni mensili promessi, frasi generiche Barnum. Attiva su ogni output verso l'esterno (email, social, landing, ads).",
    "sentinel-cost": "Cost Sentinel. Vigila su ogni spesa API/crediti, attiva dry-run se sopra soglia. Attiva su ogni operazione che costa denaro.",
    "sentinel-drift": "Drift Sentinel. Vigila su modifiche a sistemi attivi senza ADR. Blocca modifiche architetturali non documentate. Attiva su ogni modifica a company/, .claude/, sistemi produzione.",
    "sentinel-quality": "Quality Sentinel. Vigila su APSOC score sotto 80, output senza proof. Attiva su ogni deliverable prima della consegna.",
    "sentinel-security": "Security Sentinel. Vigila su segreti nel repo, credenziali esposte, PII. Attiva su ogni commit e scansioni periodiche.",

    # Empire Style
    "empire-style": "Trasforma un sito esistente nello stile premium Digital Empire (ccm-style). Applica design system, colori, tipografia, animazioni. Attiva per restyling siti, brand application.",
}

def fix_description(filepath, filename, new_desc):
    """Replace the description in frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith("---"):
        return False

    second_dash = content.find("---", 3)
    if second_dash == -1:
        return False

    front = content[3:second_dash]
    body = content[second_dash:]

    # Replace description line
    new_front = re.sub(
        r'^description:.*$',
        f'description: "{new_desc}"',
        front,
        count=1,
        flags=re.MULTILINE
    )

    new_content = "---" + new_front + body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    fixed = 0
    skipped = 0

    for filename in sorted(os.listdir(AGENTS_DIR)):
        if not filename.endswith('.md'):
            continue

        name = filename.replace('.md', '')
        filepath = os.path.join(AGENTS_DIR, filename)

        if name in OVERRIDES:
            success = fix_description(filepath, filename, OVERRIDES[name])
            if success:
                fixed += 1
                print(f"FIXED: {filename}")
            else:
                print(f"FAIL:  {filename}")
        else:
            skipped += 1

    print(f"\nFixed: {fixed} | Skipped: {skipped}")

if __name__ == "__main__":
    main()
