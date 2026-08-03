"""
Generator per architettura completa espansa 7 livelli
Crea 170+ agenti, 25+ team, 18 skill, 35 memory, 8 ecosistemi + sub-ecosistemi
"""

import os, json, textwrap
base = "/home/user/architettura_completa_7_livelli"
os.makedirs(base, exist_ok=True)

# ---- Helpers to create agent definition string
def agent_def(name, role, level, team, eco, sub_eco, inputs, outputs, logic, reports_to, manages, reads, writes, skills=None, playwright=None):
    level_names = {
        1: "L1_SUPREME_ORCHESTRATOR",
        2: "L2_ECOSYSTEM_CONTROLLER",
        3: "L3_TEAM_LEADER",
        4: "L4_SENIOR_AGENT",
        5: "L5_OPERATIONAL_AGENT",
        6: "L6_SUPPORT_AGENT",
        7: "L7_MICRO_AGENT"
    }
    return f'''
{name} = Agent(
    name="{name}",
    role="{role}",
    hierarchy_level={level},
    team="{team}",
    ecosystem="{eco}",
    sub_ecosystem={f'"{sub_eco}"' if sub_eco else 'None'},
    inputs={inputs},
    outputs={outputs},
    decision_logic="""{logic}""",
    connections={{"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]}},
    memory_access={{"read": reads, "write": writes}},
    self_healing_behavior={{"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True}},
    playwright_usage={f'"{playwright}"' if playwright else 'None'},
    skill_usage={skills if skills else []},
    level_name="{level_names[level]}"
)
'''

# ---- LEVEL 1
L1_content = '''
from core import Agent
SupremeOrchestratorAgent = Agent(
    name="SupremeOrchestratorAgent",
    role="Supreme Orchestrator L1 - unico top-level, vede tutto, decide macro, override qualsiasi decisione, gestisce stato globale, inizia cicli, valida gerarchie",
    hierarchy_level=1,
    team="SupremeOrchestratorTeam",
    ecosystem="Global",
    sub_ecosystem=None,
    inputs=["reports_from_L2_controllers", "memory_ecosystem_state", "self_healing_escalations", "auto_improvement_signals", "final_outputs_all_ecosystems", "hierarchy_validation_reports"],
    outputs=["global_state", "macro_decisions", "override_commands", "cycle_initiation_signals", "hierarchy_updates", "CP0_INIT"],
    decision_logic="""SE riceve escalation self-healing severity CRITICAL ALLORA override decisione lower + trigger rollback a ultimo checkpoint globale valido + log in hierarchies. SE GO_rate <20% ALLORA aggiusta BookNicheDecisionSkill thresholds via ThresholdUpdaterAgent + aumenta retry Research. SE nuovo ciclo ALLORA crea CP0_INIT via CheckpointManagerAgent, scrive hierarchies via HierarchyManagerAgent, broadcast start a tutti i controller L2. Sempre monitora stall via StallDetectorAgent. Authority override senza soglia.""",
    connections={"reports_to": [], "manages": ["ResearchEcosystemController","QualificationEcosystemController","PlanningEcosystemController","ProductionEcosystemController","VisualEcosystemController","MemoryEcosystemController","SelfHealingEcosystemController","AutoImprovementEcosystemController"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","AnomalyLog","PerformanceHistory","FeedbackRegistry"], "write": ["hierarchies","checkpoints","important_notes"]},
    self_healing_behavior={"on_failure": "top level non self-heala, riceve escalation, manual_override_and_global_rollback", "checkpoint_before": True},
    level_name="L1_SUPREME_ORCHESTRATOR"
)
ALL_L1 = [SupremeOrchestratorAgent]
'''

with open(f"{base}/L1/supreme.py","w") as f:
    f.write("import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"+L1_content)

# ---- LEVEL 2 - 8 controllers
L2_agents = [
    ("ResearchEcosystemController","Controlla ResearchEcosystem, gestisce 5 team, keyword search Amazon + review sites, riporta a L1","ResearchEcosystem"),
    ("QualificationEcosystemController","Controlla QualificationEcosystem, piano qualifica dettagliato, reproducibilita assurdita velocita","QualificationEcosystem"),
    ("PlanningEcosystemController","Controlla PlanningEcosystem, second-level plan con video_structure REQUIRED preservato verbatim","PlanningEcosystem"),
    ("ProductionEcosystemController","Controlla ProductionEcosystem, scrittura intero libro coerente con second-level plan","ProductionEcosystem"),
    ("VisualEcosystemController","Controlla VisualEcosystem, grafiche prompt cover con Playwright support","VisualEcosystem"),
    ("MemoryEcosystemController","Controlla MemoryEcosystem attivo con agenti gestione validazione checkpoint - non storage passivo","MemoryEcosystem"),
    ("SelfHealingEcosystemController","Controlla SelfHealingEcosystem real active always-on healing con Detection Diagnosis Recovery","SelfHealingEcosystem"),
    ("AutoImprovementEcosystemController","Controlla AutoImprovementEcosystem real continuous improvement che impara da outcomes","AutoImprovementEcosystem"),
]

L2_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"
for name, role, eco in L2_agents:
    L2_content += agent_def(
        name=name,
        role=role+f" L2 Ecosystem Controller - {eco} - gestisce team, alloca risorse, valida handoff, report a Supreme",
        level=2,
        team="EcosystemControlTeam",
        eco=eco,
        sub_eco=None,
        inputs=["cycle_start_signal","memory_hierarchies","important_notes_feedback","checkpoints","team_status_reports","self_healing_reports"],
        outputs=["ecosystem_status","resource_allocation","go_signal","reports_to_L1","handoff_validation"],
        logic=f"SE nuovo ciclo ALLORA leggi important_notes LearningLog pattern successo fallimento, alloca a team leader L3, trigger flow interno. SE team riporta empty result o anomaly ALLORA trigger SelfHealing via PlaywrightErrorHandlerAgent. SE output validato con checkpoint ALLORA marca phase complete, crea checkpoint via CheckpointManagerAgent, inicia handoff a prossimo ecosistema via Memory broker protocol 8 step. SE 3 fallimenti ALLORA escalate a SupremeOrchestratorAgent. Controller {eco}",
        reports_to=["SupremeOrchestratorAgent"],
        manages=[f"{eco}Leader1", f"{eco}Leader2"] if eco!="MemoryEcosystem" else ["MemoryManagerLeader"],
        reads=["checkpoints","decisions","plans","hierarchies","important_notes","FeedbackRegistry","BookOpportunityRegistry"],
        writes=["checkpoints","decisions","hierarchies","important_notes"],
        skills=["BookNicheDecisionSkill","SelfHealingSkill","QualificationDecisionSkill","MemoryReadWriteSkill","CheckpointManagementSkill"],
        playwright="supervises PlaywrightOperationsSubEcosystem real tool"
    )
L2_content += "\nALL_L2 = [ResearchEcosystemController,QualificationEcosystemController,PlanningEcosystemController,ProductionEcosystemController,VisualEcosystemController,MemoryEcosystemController,SelfHealingEcosystemController,AutoImprovementEcosystemController]\n"

with open(f"{base}/L2/controllers.py","w") as f:
    f.write(L2_content)

# ---- LEVEL 3 - 25 leaders
L3_leaders = [
    ("AmazonResearchLeader","AmazonKeywordResearchTeam","ResearchEcosystem","PlaywrightOps","Gestisce keyword generation, search, extraction, validation, BookNicheDecisionSkill",["KeywordGeneratorAgent","AmazonSearchAgent","AmazonDataExtractorAgent","AmazonResultsValidatorAgent","KeywordQualityAnalystAgent","NicheCompetitionAnalystAgent"]),
    ("ReviewResearchLeader","ReviewAnalysisResearchTeam","ResearchEcosystem","ReviewSubEcosystem","Gestisce review site discovery, extraction, normalization, validation",["ReviewSiteFinderAgent","ReviewDataExtractorAgent","ReviewScoreNormalizerAgent","ReviewDataValidatorAgent","ReviewSentimentAnalystAgent"]),
    ("DataPersistenceLeader","DataPersistenceTeam","ResearchEcosystem","PersistenceSubEcosystem","Garantisce salvataggio via Playwright, formatting, validation, checkpoint CP1",["PlaywrightSaveAgent","DataFormatterAgent","SaveValidatorAgent","RawDataArchiverAgent"]),
    ("KeywordExpansionLeader","KeywordExpansionTeam","ResearchEcosystem","ExpansionSubEcosystem","Leader team espansione keyword quando empty result, genera variazioni da LearningLog",["KeywordVariationGeneratorAgent","SemanticKeywordExpanderAgent","LongTailKeywordAgent"]),
    ("SearchOptimizationLeader","SearchOptimizationTeam","ResearchEcosystem","OptimizationSub","Ottimizza strategie search Amazon, riduce blocchi Playwright",["SearchStrategyOptimizerAgent","PlaywrightRotationManagerAgent"]),
    ("QualificationLeader","QualificationAnalysisTeam","QualificationEcosystem","AnalysisSub","Gestisce 8 analyst senior, coordinate flusso valutazione 5 criteri",["ReproducibilityAnalystAgent","AbsurdityDetectorAgent","ProductionSpeedAnalystAgent","MarketAlignmentAnalystAgent","PlanQualityAuditorAgent","CompetitionAnalystAgent","SustainabilityAnalystAgent","BusinessFitAnalystAgent"]),
    ("QualificationDecisionLeader","QualificationDecisionTeam","QualificationEcosystem","DecisionSub","Aggrega decisioni, gestisce rischi, scrive report finale GO/NO-GO",["DecisionAggregatorAgent","RiskFlagManagerAgent","QualificationReportWriterAgent","DecisionQualityCheckerAgent"]),
    ("StructurePlanningLeader","StructurePlanningTeam","PlanningEcosystem","StructureSub","Gestisce video_structure REQUIRED preservato verbatim, chapters, details, coherence - CONTROL POINT CRITICO",["VideoStructureArchitectAgent","ChapterDesignerAgent","DetailFillerAgent","PlanCoherenceValidatorAgent","VideoStructureValidatorAgent","OutlineOptimizerAgent"]),
    ("ProductionReadinessLeader","ProductionReadinessTeam","PlanningEcosystem","ReadinessSub","Verifica prerequisiti produzione, stima risorse, emette start signal",["ReadinessCheckerAgent","ResourceEstimatorAgent","ProductionStartSignalAgent","RiskMitigationPlannerAgent"]),
    ("ContentPlanningLeader","ContentPlanningTeam","PlanningEcosystem","ContentSub","Leader pianificazione contenuti dettagliata per produzione sostenibile",["ContentDetailArchitectAgent","ContentFlowDesignerAgent","ResourceAllocationPlannerAgent"]),
    ("BookWritingLeader","BookWritingTeam","ProductionEcosystem","WritingSub","Gestisce chapter writers paralleli, consistenza, stile, qualità",["ChapterWriterAgent","ConsistencyCheckerAgent","StyleEnforcerAgent","ContentQualityReviewerAgent","ChapterDependencyManagerAgent","WritingProgressTrackerAgent"]),
    ("ProductionQualityLeader","ProductionQualityTeam","ProductionEcosystem","QualitySub","Valida manoscritto completezza, compliance piano, approvazione finale",["ManuscriptValidatorAgent","PlanComplianceCheckerAgent","FinalApprovalAgent","QualityMetricsCalculatorAgent"]),
    ("EditingLeader","EditingTeam","ProductionEcosystem","EditingSub","Leader editing finale, uniformità, correzione",["EditingCoordinatorAgent","FinalProofreaderAgent","CrossReferenceCheckerAgent"]),
    ("GraphicDesignLeader","GraphicDesignTeam","VisualEcosystem","GraphicSub","Gestisce creazione prompt grafiche, generazione, quality review revision loop",["GraphicPromptCreatorAgent","GraphicGeneratorAgent","GraphicQualityReviewerAgent","GraphicRevisionAgent","GraphicStyleEnforcerAgent","VisualConsistencyCheckerAgent"]),
    ("CoverDesignLeader","CoverDesignTeam","VisualEcosystem","CoverSub","Gestisce cover concept basato contenuto e market data, prompt, generazione, review critica",["CoverConceptAgent","CoverPromptCreatorAgent","CoverGeneratorAgent","CoverQualityReviewerAgent","CoverRevisionAgent","CoverMarketFitAnalystAgent"]),
    ("VisualPlaywrightLeader","VisualPlaywrightOperationsTeam","VisualEcosystem","PlaywrightSub","Gestisce navigazione Playwright e salvataggio visual tasks",["VisualPlaywrightNavigatorAgent","VisualPlaywrightSaveAgent","VisualPlaywrightValidatorAgent"]),
    ("VisualQualityLeader","VisualQualityTeam","VisualEcosystem","VisualQualitySub","Leader qualità visual, approva grafica e cover finali",["VisualQualityAuditorAgent","FinalVisualApprovalAgent"]),
    ("MemoryManagerLeader","MemoryManagementTeam","MemoryEcosystem","CoreMemorySub","Gestisce tutti gli agenti memoria, read/write protocols, checkpoint logic, validazione - SISTEMA ATTIVO",["MemoryWriterAgent","MemoryReaderAgent","MemoryValidatorAgent","CheckpointManagerAgent","DecisionLoggerAgent","PlanStorageAgent","HierarchyManagerAgent","ImportantNotesAgent"]),
    ("CheckpointSubLeader","CheckpointSubEcosystem","MemoryEcosystem","CheckpointSub","Leader sub-ecosistema checkpoint creation storage restoration",["CheckpointCreatorAgent","CheckpointValidatorAgent","CheckpointRestorerAgent","CheckpointPrunerAgent"]),
    ("DecisionLogSubLeader","DecisionLogSubEcosystem","MemoryEcosystem","DecisionSub","Leader sub-ecosistema logging decisioni immutable",["DecisionLogWriterAgent","DecisionLogReaderAgent","DecisionTraceabilityAgent"]),
    ("DetectionLeader","DetectionTeam","SelfHealingEcosystem","DetectionSub","Gestisce output monitoring, error detection, anomaly detection, stall detection",["OutputMonitorAgent","ErrorDetectorAgent","AnomalyDetectorAgent","StallDetectorAgent","PlaywrightFailureDetectorAgent","MemoryFailureDetectorAgent"]),
    ("DiagnosisLeader","DiagnosisTeam","SelfHealingEcosystem","DiagnosisSub","Gestisce root cause analysis, impact assessment, recovery planning",["RootCauseAnalystAgent","ImpactAssessorAgent","RecoveryPlannerAgent","FailurePatternAnalyzerAgent"]),
    ("RecoveryLeader","RecoveryTeam","SelfHealingEcosystem","RecoverySub","Gestisce retry rollback alternative path validation - real recovery",["RetryExecutorAgent","RollbackExecutorAgent","AlternativePathAgent","RecoveryValidatorAgent","EscalationManagerAgent"]),
    ("FeedbackCollectionLeader","FeedbackCollectionTeam","AutoImprovementEcosystem","FeedbackSub","Gestisce outcome collection, metrics, pattern detection - real improvement",["OutcomeCollectorAgent","PerformanceMetricsAgent","PatternDetectorAgent","CycleOutcomeAnalyzerAgent"]),
    ("ImprovementPlanningLeader","ImprovementPlanningTeam","AutoImprovementEcosystem","PlanningSub","Analizza feedback, rank priorities, scrive improvement plans",["ImprovementAnalystAgent","PriorityRankerAgent","ImprovementPlanWriterAgent","OpportunityIdentifierAgent"]),
    ("ImprovementExecutionLeader","ImprovementExecutionTeam","AutoImprovementEcosystem","ExecutionSub","Adjust parameters, update thresholds, optimize workflows - execution reale",["ParameterAdjusterAgent","ThresholdUpdaterAgent","WorkflowOptimizerAgent","LearningLoggerAgent"]),
]

L3_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"
for name, team, eco, sub, role, manages in L3_leaders:
    L3_content += agent_def(
        name=name,
        role=f"{role} L3 Team Leader - {team} in {eco} - manages team, coordina lavoro interno, intra-team comm, report a controller, gestisce handoff 8-step",
        level=3,
        team=team,
        eco=eco,
        sub_eco=sub,
        inputs=["cycle_signal","handoff_package_from_previous_ecosystem","memory_hierarchies","important_notes","team_member_status","checkpoint_refs"],
        outputs=["team_status","internal_flow_trigger","handoff_ready_package","checkpoint_creation_request","reports_to_L2"],
        logic=f"Come leader {team} in {eco}: trigger internal flow {manages} in ordine o parallelo dove possibile, monitora output per completeness coherence, valida via validator agent, applica skill pertinenti, crea checkpoint via CheckpointManagerAgent, gestisce self-healing retry rollback se failure, inizia handoff protocol a prossimo team/ecosystem con memory broker validation. Gestisce sub-ecosystem {sub} se presente. Report a {eco}Controller.",
        reports_to=[f"{eco}Controller"],
        manages=manages,
        reads=["checkpoints","decisions","plans","hierarchies","important_notes","BookOpportunityRegistry","FeedbackRegistry","LearningLog"],
        writes=["checkpoints","decisions","important_notes","AnomalyLog"],
        skills=["BookNicheDecisionSkill","QualificationDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill","CheckpointManagementSkill","VideoStructureDesignSkill","ChapterDesignSkill","BookWritingConsistencySkill"]
    )
L3_content += "\nALL_L3 = [" + ",".join([n for n,_,_,_,_,_ in L3_leaders]) + "]\n"
with open(f"{base}/L3/leaders.py","w") as f:
    f.write(L3_content)

# ---- LEVEL 4 Senior - 40 agents
L4_senior_list = [
    ("ReproducibilityAnalystAgent","Analizza se libro riproducibile efficientemente senza risorse inaccessibili","QualificationAnalysisTeam","QualificationEcosystem"),
    ("AbsurdityDetectorAgent","Rileva elementi assurdi irrealistici nonsensical - gate non assurdi","QualificationAnalysisTeam","QualificationEcosystem"),
    ("ProductionSpeedAnalystAgent","Stima tempo produzione flag too slow vs modello quantita sostenibile","QualificationAnalysisTeam","QualificationEcosystem"),
    ("MarketAlignmentAnalystAgent","Valuta allineamento goal quantity-performance: performanti riproducibili sostenibili","QualificationAnalysisTeam","QualificationEcosystem"),
    ("PlanQualityAuditorAgent","Valuta qualita qualification plan itself, validita piano","QualificationAnalysisTeam","QualificationEcosystem"),
    ("CompetitionAnalystAgent","Analizza competizione livello nicchia da segnali Amazon","QualificationAnalysisTeam","QualificationEcosystem"),
    ("SustainabilityAnalystAgent","Analizza sostenibilita produzione lungo termine quantita","QualificationAnalysisTeam","QualificationEcosystem"),
    ("BusinessFitAnalystAgent","Valuta business fit guadagno tramite quantita libri performanti","QualificationAnalysisTeam","QualificationEcosystem"),
    ("DecisionAggregatorAgent","Aggrega output analyst in decisione unificata weighted scoring","QualificationDecisionTeam","QualificationEcosystem"),
    ("RiskFlagManagerAgent","Gestisce prioritizza risk flags da tutti analyst","QualificationDecisionTeam","QualificationEcosystem"),
    ("VideoStructureArchitectAgent","CRITICAL REQUIRED - Progetta video_structure preservato verbatim non reinterpretare - CONTROL POINT CP-VIDEO-01","StructurePlanningTeam","PlanningEcosystem"),
    ("ChapterDesignerAgent","Definisce capitoli con descrizioni ordine scopo effort estimate fast vs slow","StructurePlanningTeam","PlanningEcosystem"),
    ("DetailFillerAgent","Aggiunge ogni dettaglio rilevante produzione per sostenibilita","StructurePlanningTeam","PlanningEcosystem"),
    ("PlanCoherenceValidatorAgent","Valida intero second-level plan coerente completo","StructurePlanningTeam","PlanningEcosystem"),
    ("VideoStructureValidatorAgent","Valida video_structure presente verbatim non vuoto non reinterpretato - critical validation","StructurePlanningTeam","PlanningEcosystem"),
    ("OutlineOptimizerAgent","Ottimizza outline capitoli per flusso e sostenibilita","StructurePlanningTeam","PlanningEcosystem"),
    ("ContentFlowDesignerAgent","Progetta flusso contenuti tra capitoli","ContentPlanningTeam","PlanningEcosystem"),
    ("ConsistencyCheckerAgent","Controlla consistenza cross-chapters durante produzione","BookWritingTeam","ProductionEcosystem"),
    ("StyleEnforcerAgent","Garantisce stile scrittura uniforme","BookWritingTeam","ProductionEcosystem"),
    ("ContentQualityReviewerAgent","Revisiona qualita contenuto prima finalizzazione","BookWritingTeam","ProductionEcosystem"),
    ("WritingProgressTrackerAgent","Traccia progresso scrittura capitoli paralleli","BookWritingTeam","ProductionEcosystem"),
    ("ManuscriptValidatorAgent","Valida completezza manoscritto","ProductionQualityTeam","ProductionEcosystem"),
    ("PlanComplianceCheckerAgent","Verifica manoscritto segue second-level plan","ProductionQualityTeam","ProductionEcosystem"),
    ("QualityMetricsCalculatorAgent","Calcola metriche qualita produzione","ProductionQualityTeam","ProductionEcosystem"),
    ("KeywordQualityAnalystAgent","Analizza qualita keyword Amazon search signals","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("NicheCompetitionAnalystAgent","Analizza competizione nicchia da dati Amazon","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("ReviewSentimentAnalystAgent","Analizza sentiment review data da review sites","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("RootCauseAnalystAgent","Analizza anomalie root cause - real self-healing diagnosis","DiagnosisTeam","SelfHealingEcosystem"),
    ("ImpactAssessorAgent","Valuta impatto anomalia su workflow","DiagnosisTeam","SelfHealingEcosystem"),
    ("RecoveryPlannerAgent","Crea recovery plan basato su diagnosis retry rollback escalate skip requalify","DiagnosisTeam","SelfHealingEcosystem"),
    ("OutputMonitorAgent","Monitora output phase completeness coherence - Detection Team","DetectionTeam","SelfHealingEcosystem"),
    ("AnomalyDetectorAgent","Rileva anomalie pattern insoliti stati inattesi","DetectionTeam","SelfHealingEcosystem"),
    ("ImprovementAnalystAgent","Analizza feedback identifica opportunita miglioramento 5 target","ImprovementPlanningTeam","AutoImprovementEcosystem"),
    ("PriorityRankerAgent","Rank improvements by impact feasibility","ImprovementPlanningTeam","AutoImprovementEcosystem"),
    ("CoverConceptAgent","Crea cover concept basato contenuto e market data performance signals","CoverDesignTeam","VisualEcosystem"),
    ("CoverMarketFitAnalystAgent","Analizza market fit cover concept","CoverDesignTeam","VisualEcosystem"),
    ("VisualQualityAuditorAgent","Audita qualita visual finale","VisualQualityTeam","VisualEcosystem"),
    ("VisualConsistencyCheckerAgent","Verifica consistenza visual tra grafiche e cover","GraphicDesignTeam","VisualEcosystem"),
    ("FailurePatternAnalyzerAgent","Analizza pattern fallimenti ricorrenti per prevenzione","DiagnosisTeam","SelfHealingEcosystem"),
    ("OpportunityIdentifierAgent","Identifica opportunita miglioramento da pattern positivi","ImprovementPlanningTeam","AutoImprovementEcosystem"),
]

L4_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"
for name, role, team, eco in L4_senior_list:
    sub = team.replace("Team","Sub")
    L4_content += agent_def(
        name=name,
        role=role+f" L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - {team}",
        level=4,
        team=team,
        eco=eco,
        sub_eco=sub,
        inputs=["handoff_package","book_opportunity_data","review_analysis","raw_data_ref","analyst_outputs","phase_state","feedback_data"],
        outputs=["evaluation_score","evidence","risk_flag","validation_result","audit_report","aggregated_decision"],
        logic=f"Come senior {name} in {team}: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a {team} leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.",
        reports_to=[team.replace("Team","Leader") if "Leader" not in team else "QualificationLeader"],
        manages=["L5 Operational agents", "L6 Support"],
        reads=["BookOpportunityRegistry","ReviewDataRegistry","QualificationCheckpoints","SecondLevelPlans","decisions","plans","important_notes","checkpoints","FeedbackRegistry"],
        writes=["QualificationCheckpoints","RiskRegistry","SecondLevelPlans","PlanningCheckpoints","DiagnosisLog","AnomalyLog","ImprovementPlans"],
        skills=["BookNicheDecisionSkill","QualificationDecisionSkill","SelfHealingSkill","VideoStructureDesignSkill","ChapterDesignSkill","AnomalyDetectionSkill","RecoveryExecutionSkill"],
        playwright=None
    )
L4_content += "\nALL_L4 = [" + ",".join([n for n,_,_,_ in L4_senior_list]) + "]\n"

with open(f"{base}/L4/senior.py","w") as f:
    f.write(L4_content)

# ---- LEVEL 5 Operational - 45 agents
L5_ops = [
    ("KeywordGeneratorAgent","Genera variazioni keyword per Amazon search da seed + important_notes patterns","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("AmazonSearchAgent","Esegue ricerche Amazon via Playwright operational tool real navigation","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("AmazonDataExtractorAgent","Estrae dati libri titoli autori ratings prezzi categorie via Playwright capture","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("ReviewSiteFinderAgent","Trova siti che analizzano Amazon reviews via Playwright navigation","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("ReviewDataExtractorAgent","Estrae dati analisi review da siti trovati via Playwright","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("PlaywrightSaveAgent","Gestisce tutte le operazioni save Playwright research e visual","DataPersistenceTeam","ResearchEcosystem"),
    ("DataFormatterAgent","Formatta dati in structured_output pronto per qualifica","DataPersistenceTeam","ResearchEcosystem"),
    ("RawDataArchiverAgent","Archivia raw data da Playwright con refs e screenshot","DataPersistenceTeam","ResearchEcosystem"),
    ("KeywordVariationGeneratorAgent","Genera variazioni keyword avanzate per retry quando empty result","KeywordExpansionTeam","ResearchEcosystem"),
    ("SemanticKeywordExpanderAgent","Espande keyword semanticamente da LearningLog patterns","KeywordExpansionTeam","ResearchEcosystem"),
    ("LongTailKeywordAgent","Genera long-tail keywords per nicchie meno competitive","KeywordExpansionTeam","ResearchEcosystem"),
    ("SearchStrategyOptimizerAgent","Ottimizza strategia search per ridurre blocchi Playwright","SearchOptimizationTeam","ResearchEcosystem"),
    ("QualificationReportWriterAgent","Scrive report qualifica finale strutturato con GO NO-GO","QualificationDecisionTeam","QualificationEcosystem"),
    ("DecisionQualityCheckerAgent","Verifica qualita decisione traceability motivazione","QualificationDecisionTeam","QualificationEcosystem"),
    ("ContentDetailArchitectAgent","Progetta dettagli contenuti per sustainable production","ContentPlanningTeam","PlanningEcosystem"),
    ("ReadinessCheckerAgent","Verifica prerequisiti produzione met - second-level plan complete","ProductionReadinessTeam","PlanningEcosystem"),
    ("ResourceEstimatorAgent","Stima risorse necessarie tempo capitoli grafica cover","ProductionReadinessTeam","PlanningEcosystem"),
    ("ProductionStartSignalAgent","Emette segnale formale start produzione TRUE timestamp - marks actual start production flow","ProductionReadinessTeam","PlanningEcosystem"),
    ("RiskMitigationPlannerAgent","Pianifica mitigazione rischi identificati in RiskRegistry","ProductionReadinessTeam","PlanningEcosystem"),
    ("ChapterWriterAgent","Scrive capitoli singoli multiple instances parallele, legge memoria per continuity","BookWritingTeam","ProductionEcosystem"),
    ("ChapterDependencyManagerAgent","Gestisce dipendenze tra capitoli per scrittura parallela","BookWritingTeam","ProductionEcosystem"),
    ("EditingCoordinatorAgent","Coordina editing finale","EditingTeam","ProductionEcosystem"),
    ("FinalProofreaderAgent","Proofreading finale manoscritto","EditingTeam","ProductionEcosystem"),
    ("GraphicPromptCreatorAgent","Crea prompt dettagliati per generazione grafiche","GraphicDesignTeam","VisualEcosystem"),
    ("GraphicGeneratorAgent","Genera grafiche usando prompt + salva via VisualPlaywrightSaveAgent visual_save","GraphicDesignTeam","VisualEcosystem"),
    ("CoverPromptCreatorAgent","Crea prompt dettagliato cover generation","CoverDesignTeam","VisualEcosystem"),
    ("CoverGeneratorAgent","Genera cover + salva via Playwright - asset critico","CoverDesignTeam","VisualEcosystem"),
    ("MemoryWriterAgent","Gestisce scritture strutturate memoria da tutti ecosistemi - sistema attivo","MemoryManagementTeam","MemoryEcosystem"),
    ("MemoryReaderAgent","Gestisce letture memoria da tutti ecosistemi con context timestamp - sistema attivo","MemoryManagementTeam","MemoryEcosystem"),
    ("RetryExecutorAgent","Esegue retry con adjusted params real recovery - timeout++ user_agent rotate","RecoveryTeam","SelfHealingEcosystem"),
    ("OutcomeCollectorAgent","Raccoglie outcomes da cicli completati per auto-improvement","FeedbackCollectionTeam","AutoImprovementEcosystem"),
    ("ParameterAdjusterAgent","Aggiusta parametri workflow basati su improvement plan","ImprovementExecutionTeam","AutoImprovementEcosystem"),
    ("ResourceAllocationPlannerAgent","Pianifica allocazione risorse per capitoli","ContentPlanningTeam","PlanningEcosystem"),
    ("CrossReferenceCheckerAgent","Verifica cross-reference tra capitoli e piano","EditingTeam","ProductionEcosystem"),
    ("GraphicStyleEnforcerAgent","Impone stile uniforme grafiche","GraphicDesignTeam","VisualEcosystem"),
    ("VisualQualityReviewerAgent","Legato ma usato in L5 variant - quality review operational","GraphicDesignTeam","VisualEcosystem"),
    ("OutcomeAnalyzerAgent","Analizza outcomes per feedback collection","FeedbackCollectionTeam","AutoImprovementEcosystem"),
    ("ContentFlowDesignerAgent","Disegna flusso contenuti second-level plan","StructurePlanningTeam","PlanningEcosystem"),
    ("PlaywrightRotationManagerAgent","Gestisce rotazione Playwright per evitare blocchi","SearchOptimizationTeam","ResearchEcosystem"),
    ("CheckpointCreatorAgent","Crea checkpoint via CheckpointManagerAgent - parte Memory sub-ecosystem","CheckpointSubEcosystem","MemoryEcosystem"),
    ("DecisionLogWriterAgent","Scrive decisioni log immutable - Memory sub-ecosystem","DecisionLogSubEcosystem","MemoryEcosystem"),
    ("LearningLoggerAgent","Logga learning in LearningLog - auto-improvement execution","ImprovementExecutionTeam","AutoImprovementEcosystem"),
    ("CycleOutcomeAnalyzerAgent","Analizza outcome ciclo completo","FeedbackCollectionTeam","AutoImprovementEcosystem"),
    ("ContentDetailArchitectAgent2","Second instance detail architect for redundancy","ContentPlanningTeam","PlanningEcosystem"),
    ("VisualPlaywrightSaveAgent","Salva visual outputs via Playwright support - operational variant","VisualPlaywrightOperationsTeam","VisualEcosystem"),
]

L5_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"
for name, role, team, eco in L5_ops:
    L5_content += agent_def(
        name=name,
        role=role+f" L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
        level=5,
        team=team,
        eco=eco,
        sub_eco=team.replace("Team","Sub"),
        inputs=["internal_flow_trigger","handoff_package","keyword_variations","search_results_raw","extraction_request","write_requests","chapter_definition","second_level_plan","memory_context","anomaly_report","feedback_data","improvement_plan"],
        outputs=["search_results_raw","extracted_book_metadata","review_data_raw","formatted_structured_output","save_confirmation","keyword_variations","evaluation_outputs","chapter_written_content","graphic_prompts","graphics_raw","cover_raw","memory_write_confirmation","read_response","retry_execution_result","collected_outcomes","parameter_adjustments"],
        logic=f"Come operational {name} in {team} {eco}: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.",
        reports_to=[team.replace("Team","Leader")],
        manages=["L6 Support","L7 Micro"],
        reads=["BookOpportunityRegistry","ReviewDataRegistry","SecondLevelPlans","decisions","plans","checkpoints","important_notes","FeedbackRegistry","LearningLog"],
        writes=["BookOpportunityRegistry","ResearchCheckpoints","ProductionCheckpoints","GraphicPrompts","GeneratedGraphics","CoverVersions","checkpoints","FeedbackRegistry","LearningLog"],
        skills=["BookNicheDecisionSkill","PlaywrightNavigationSkill","PlaywrightDataExtractionSkill","PlaywrightSaveSkill","MemoryReadWriteSkill","SelfHealingSkill","BookWritingConsistencySkill","GraphicPromptEngineeringSkill"],
        playwright="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities" if "Playwright" in name or "Search" in name or "Extractor" in name or "Save" in name or "Graphic" in name or "Cover" in name else None
    )
L5_content += "\nALL_L5 = [" + ",".join([n for n,_,_,_ in L5_ops]) + "]\n"

with open(f"{base}/L5/operational.py","w") as f:
    f.write(L5_content)

# ---- LEVEL 6 Support - 40 agents
L6_support = [
    ("DataFormatterAgent","Formatta dati per storage via Playwright save strutturato per qualifica","DataPersistenceTeam","ResearchEcosystem"),
    ("SaveValidatorAgent","Conferma salvataggi Playwright successo URL sorgente loggata raw_data accessibile","DataPersistenceTeam","ResearchEcosystem"),
    ("ReviewScoreNormalizerAgent","Normalizza diversi scoring systems in formato unificato","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("AmazonResultsValidatorAgent","Valida dati Amazon estratti completi coerenti titolo URL sorgente keyword","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("ReviewDataValidatorAgent","Valida completezza coerenza review data linkata a book opportunities","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("FinalApprovalAgent","Da approvazione finale produzione manoscritto completo validato","ProductionQualityTeam","ProductionEcosystem"),
    ("VisualPlaywrightSaveAgent","Salva output visual via Playwright support operational","VisualPlaywrightOperationsTeam","VisualEcosystem"),
    ("GraphicQualityReviewerAgent","Revisiona qualità grafiche generate score pass fail loop revisione","GraphicDesignTeam","VisualEcosystem"),
    ("CoverQualityReviewerAgent","Revisiona qualità cover critica pass fail non skippabile","CoverDesignTeam","VisualEcosystem"),
    ("HierarchyManagerAgent","Mantiene dati gerarchia 7 livelli agent_id name level team ecosystem reports_to manages","MemoryManagementTeam","MemoryEcosystem"),
    ("ImportantNotesAgent","Memorizza recupera note critiche flags - importante","MemoryManagementTeam","MemoryEcosystem"),
    ("PerformanceMetricsAgent","Calcola metriche performance per fase - feedback 6 segnali","FeedbackCollectionTeam","AutoImprovementEcosystem"),
    ("PatternDetectorAgent","Rileva pattern ricorrenti positivi negativi keyword too slow GO rate low","FeedbackCollectionTeam","AutoImprovementEcosystem"),
    ("ImprovementPlanWriterAgent","Scrive improvement plans prioritizzati","ImprovementPlanningTeam","AutoImprovementEcosystem"),
    ("ThresholdUpdaterAgent","Aggiorna soglie decisionali basate su learning GO threshold 70","ImprovementExecutionTeam","AutoImprovementEcosystem"),
    ("WorkflowOptimizerAgent","Ottimizza sequenze flow basate su dati performance","ImprovementExecutionTeam","AutoImprovementEcosystem"),
    ("MemoryValidatorAgent","Valida consistenza memoria rileva corruzione gaps - sistema attivo","MemoryManagementTeam","MemoryEcosystem"),
    ("CheckpointManagerAgent","Gestisce checkpoint creation storage restoration - core self-healing","MemoryManagementTeam","MemoryEcosystem"),
    ("DecisionLoggerAgent","Logga decisioni con full context reasoning immutable append-only","MemoryManagementTeam","MemoryEcosystem"),
    ("PlanStorageAgent","Memorizza recupera tutti i piani versioned not overwritten","MemoryManagementTeam","MemoryEcosystem"),
    ("GraphicRevisionAgent","Revisiona grafiche fail quality review loop","GraphicDesignTeam","VisualEcosystem"),
    ("CoverRevisionAgent","Revisiona cover se needed loop critico","CoverDesignTeam","VisualEcosystem"),
    ("RollbackExecutorAgent","Esegue rollback a checkpoint precedenti real recovery via CheckpointManager restore","RecoveryTeam","SelfHealingEcosystem"),
    ("RecoveryValidatorAgent","Valida recovery successo workflow continua senza data loss","RecoveryTeam","SelfHealingEcosystem"),
    ("CheckpointValidatorAgent","Valida checkpoint prima storage - Memory sub-ecosystem","CheckpointSubEcosystem","MemoryEcosystem"),
    ("CheckpointRestorerAgent","Esegue restore checkpoint su richiesta rollback - Memory sub","CheckpointSubEcosystem","MemoryEcosystem"),
    ("CheckpointPrunerAgent","Gestisce pruning checkpoint vecchi preservando traceability","CheckpointSubEcosystem","MemoryEcosystem"),
    ("DecisionLogReaderAgent","Legge log decisioni con traceability - Memory sub","DecisionLogSubEcosystem","MemoryEcosystem"),
    ("DecisionTraceabilityAgent","Verifica traceability decisioni reasoning chain - Memory sub","DecisionLogSubEcosystem","MemoryEcosystem"),
    ("VisualPlaywrightValidatorAgent","Valida salvataggi visual Playwright","VisualPlaywrightOperationsTeam","VisualEcosystem"),
    ("FinalVisualApprovalAgent","Approvazione finale visual - VisualQualityTeam","VisualQualityTeam","VisualEcosystem"),
    ("EscalationManagerAgent","Gestisce escalation a controller e Supreme dopo max retry fail","RecoveryTeam","SelfHealingEcosystem"),
    ("PlaywrightFailureDetectorAgent","Rileva fallimenti Playwright specifici timeout blocked","DetectionTeam","SelfHealingEcosystem"),
    ("MemoryFailureDetectorAgent","Rileva fallimenti memoria write failure corruption gap","DetectionTeam","SelfHealingEcosystem"),
    ("WritingQualityCheckerAgent","Controlla qualità scrittura uniformità","BookWritingTeam","ProductionEcosystem"),
    ("ContentValidationAgent","Valida contenuto manoscritto vs second-level plan details","ProductionQualityTeam","ProductionEcosystem"),
    ("VisualQualityAuditorAgent","Audita qualità visual finale cross-team","VisualQualityTeam","VisualEcosystem"),
    ("SearchQualityValidatorAgent","Valida qualità risultati search Amazon","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("NicheViabilityValidatorAgent","Valida fattibilità nicchia da BookNicheDecisionSkill","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("ProductionLogWriterAgent","Scrive production log decisioni durante scrittura","BookWritingTeam","ProductionEcosystem"),
]

L6_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"
for name, role, team, eco in L6_support:
    L6_content += agent_def(
        name=name,
        role=role+f" L6 Support Agent - funzioni supporto memory read/write checkpoint management data formatting validation logging monitoring",
        level=6,
        team=team,
        eco=eco,
        sub_eco=team.replace("Team","Sub"),
        inputs=["data_to_validate","memory_content_all_categories","checkpoint_refs","phase_outputs","save_operations","performance_metrics","historical_data","plan_validity","graphic_data","cover_data"],
        outputs=["validation_result","save_validation","consistency_report","checkpoint_created_confirmation","restored_checkpoint","read_response","decision_log_confirmation","plan_retrieval","quality_score","revision_loop_trigger","recovery_validation"],
        logic=f"Come support {name} in {team} {eco}: fornisce funzioni supporto - validazione completezza coerenza, checkpoint management creation storage restoration via CheckpointManagerAgent, memory validation gap corruption detection, logging monitoring, formatting data per storage. Per MemoryValidatorAgent: valida consistenza memoria across categories checkpoint align decisions plans hierarchies important_notes, flag corruption gaps trigger SelfHealing flow, trigger Memory Maintenance Flow periodic. Per CheckpointManagerAgent: gestisce creation triggers end phase before decision before handoff on self-healing, storage con parent ID valid flag, restoration via RollbackExecutorAgent request. Supporta L5 operational e L4 senior.",
        reports_to=[team.replace("Team","Leader")],
        manages=["L7 Micro"],
        reads=["checkpoints","decisions","plans","hierarchies","important_notes","BookOpportunityRegistry","ReviewDataRegistry","AnomalyLog","PerformanceHistory"],
        writes=["checkpoints","decisions","plans","important_notes","ResearchCheckpoints","ProductionCheckpoints","SelfHealingCheckpoints","AnomalyLog","RecoveryLog","FeedbackRegistry"],
        skills=["MemoryReadWriteSkill","CheckpointManagementSkill","SelfHealingSkill","AnomalyDetectionSkill","RecoveryExecutionSkill","FeedbackCollectionSkill"],
        playwright="support validation if involves Playwright save confirmation"
    )
L6_content += "\nALL_L6 = [" + ",".join([n for n,_,_,_ in L6_support]) + "]\n"

with open(f"{base}/L6/support.py","w") as f:
    f.write(L6_content)

# ---- LEVEL 7 Micro - 25 micro agents
L7_micro = [
    ("PlaywrightNavigatorMicroAgent","Micro gestisce singola navigazione pagina via Playwright tool - atomic task spawned managed higher","PlaywrightOperationsSubEcosystem","ResearchEcosystem"),
    ("PlaywrightDataCaptureMicroAgent","Micro cattura dati specifici da pagine via Playwright - atomic extraction selectors","PlaywrightOperationsSubEcosystem","ResearchEcosystem"),
    ("PlaywrightScreenshotMicroAgent","Micro fa screenshot quando necessario raw_data saving via Playwright","PlaywrightOperationsSubEcosystem","ResearchEcosystem"),
    ("PlaywrightErrorHandlerAgent","Gestisce errori Playwright-specific timeouts blocked pages CAPTCHAs connection failures retry alternative - core self-healing Playwright","PlaywrightOperationsSubEcosystem","ResearchEcosystem"),
    ("VisualPlaywrightNavigatorAgent","Micro gestisce navigazione Playwright per task visual","VisualPlaywrightOperationsTeam","VisualEcosystem"),
    ("VisualPlaywrightCaptureAgent","Micro cattura dati visual pages","VisualPlaywrightOperationsTeam","VisualEcosystem"),
    ("ErrorDetectorAgent","Micro rileva errori eccezioni fallimenti in tutti processi - Detection Team","DetectionTeam","SelfHealingEcosystem"),
    ("StallDetectorAgent","Micro rileva processi stalled frozen no heartbeat timeout - Detection Team","DetectionTeam","SelfHealingEcosystem"),
    ("AlternativePathAgent","Micro trova esegue percorsi alternativi quando retry rollback fail real recovery","RecoveryTeam","SelfHealingEcosystem"),
    ("AmazonPageNavigatorAgent","Atomic navigator specifica per pagine Amazon search results","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("AmazonDetailExtractorAgent","Atomic extractor dettagli libro singola pagina Amazon","AmazonKeywordResearchTeam","ResearchEcosystem"),
    ("ReviewSiteNavigatorAgent","Atomic navigator per review analysis sites navigation","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("ReviewDataCaptureAgent","Atomic capture review analysis data singola site","ReviewAnalysisResearchTeam","ResearchEcosystem"),
    ("SaveOperationMicroAgent","Atomic singola operazione save via Playwright save_results","DataPersistenceTeam","ResearchEcosystem"),
    ("ValidationCheckMicroAgent","Atomic singolo check validazione schema output phase","DetectionTeam","SelfHealingEcosystem"),
    ("MemoryReadMicroAgent","Atomic singola lettura memoria via MemoryReaderAgent","MemoryManagementTeam","MemoryEcosystem"),
    ("MemoryWriteMicroAgent","Atomic singola scrittura memoria via MemoryWriterAgent","MemoryManagementTeam","MemoryEcosystem"),
    ("CheckpointCreateMicroAgent","Atomic creazione checkpoint singolo via CheckpointManagerAgent","CheckpointSubEcosystem","MemoryEcosystem"),
    ("CheckpointRestoreMicroAgent","Atomic restore checkpoint singolo via CheckpointManagerAgent","CheckpointSubEcosystem","MemoryEcosystem"),
    ("DecisionLogMicroAgent","Atomic logging singola decisione via DecisionLoggerAgent","DecisionLogSubEcosystem","MemoryEcosystem"),
    ("GraphicPromptMicroAgent","Atomic creazione singolo prompt grafica via PromptCreator","GraphicDesignTeam","VisualEcosystem"),
    ("CoverPromptMicroAgent","Atomic creazione singolo prompt cover","CoverDesignTeam","VisualEcosystem"),
    ("VisualSaveMicroAgent","Atomic singolo save visual via VisualPlaywrightSaveAgent","VisualPlaywrightOperationsTeam","VisualEcosystem"),
    ("MetricCaptureMicroAgent","Atomic cattura metrica singola performance per auto-improvement","FeedbackCollectionTeam","AutoImprovementEcosystem"),
    ("PatternCheckMicroAgent","Atomic check pattern singolo via PatternDetectorAgent","FeedbackCollectionTeam","AutoImprovementEcosystem"),
]

L7_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Agent\n"
for name, role, team, eco in L7_micro:
    L7_content += agent_def(
        name=name,
        role=role+f" L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
        level=7,
        team=team,
        eco=eco,
        sub_eco=team.replace("Team","Sub"),
        inputs=["atomic_task_request","navigation_request_url_timeout_params","extraction_request_selectors_url","screenshot_request_url","error_failed_operation_retry_count","save_request_data_destination","validation_request_expected_schema","memory_read_write_request_category_requester"],
        outputs=["atomic_result_flag","navigation_result_page_loaded","captured_data_extraction_success","screenshot_ref","error_handling_strategy_retry_or_escalate","save_confirmation_saved_ref","validation_result_completeness_flag","memory_read_response_write_confirmation"],
        logic=f"Come micro {name} L7 in {team} {eco}: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.",
        reports_to=[team.replace("Team","Leader"),"PlaywrightErrorHandlerAgent","CheckpointManagerAgent"],
        manages=[],
        reads=["ResearchCheckpoints","checkpoints","AnomalyLog"] if "Playwright" in name or "Navigator" in name else ["checkpoints","important_notes"],
        writes=["ResearchCheckpoints","BookOpportunityRegistry","AnomalyLog","checkpoints"] if "Playwright" in name or "Capture" in name else ["checkpoints","important_notes"],
        skills=["SelfHealingSkill","PlaywrightNavigationSkill","PlaywrightDataExtractionSkill","PlaywrightSaveSkill","MemoryReadWriteSkill","CheckpointManagementSkill","AnomalyDetectionSkill"],
        playwright="atomic navigation data capture screenshot error handling" if "Playwright" in name else "atomic validation memory check"
    )
L7_content += "\nALL_L7 = [" + ",".join([n for n,_,_,_ in L7_micro]) + "]\n"

with open(f"{base}/L7/micro.py","w") as f:
    f.write(L7_content)

print("Generated L1-L7 expanded architecture files")
# ---- Generate skills expanded
skills_list = [
    ("BookNicheDecisionSkill","Decide quali libri e nicchie target basato su market signals Amazon + review sites","ResearchEcosystem,QualificationEcosystem,PlanningEcosystem","trigger quando enough data collected per valutare niche viability - books_found>0 review_sites>0 structured_output ready o feedback da AutoImprovement important_notes LearningLog"),
    ("QualificationDecisionSkill","Decide GO NO-GO con weighted scoring 5 criteri reproducibilità velocità assurdità market fit validità piano","QualificationEcosystem","trigger quando tutti analyst evaluations completate - reproducibility_score absurdity_flag speed_estimate market_alignment plan_validity disponibili"),
    ("SelfHealingSkill","Rileva gestisce recupera fallimenti in qualsiasi fase - trasversale riutilizzato da ogni team","all","trigger any anomaly error stall incoherent output - 8 triggers missing output incoherent blocked failed validation empty result no-go without alternative memory write failure Playwright failure - always active DetectionTeam"),
    ("VideoStructureDesignSkill","Progetta video_structure REQUIRED preservato verbatim - CRITICAL original requirement do not remove reinterpret","PlanningEcosystem","trigger quando qualification GO package valido + risk_flags + need second-level plan - CONTROL POINT CP-VIDEO-01 handle_ambiguity preserve_and_encapsulate"),
    ("ChapterDesignSkill","Definisce capitoli con descrizioni ordine scopo effort estimate sostenibile vs slow","PlanningEcosystem","trigger dopo video_structure presente verbatim validato via VideoStructureValidatorAgent"),
    ("SecondLevelPlanCoherenceSkill","Valida coerenza completezza second-level plan con video_structure chapters details","PlanningEcosystem","trigger quando second_level_plan draft completo"),
    ("ProductionReadinessSkill","Verifica prerequisiti produzione met stima risorse emette start signal TRUE marks actual start production flow","PlanningEcosystem","trigger quando second_level_plan draft validato PlanCoherenceValidator"),
    ("BookWritingConsistencySkill","Mantiene consistenza con decisioni precedenti vincoli e continuity via memory reading","ProductionEcosystem","trigger quando second_level_plan approvato production_start_signal TRUE + memory context required"),
    ("StyleEnforcementSkill","Garantisce stile uniforme scrittura cross-chapters","ProductionEcosystem","trigger dopo chapter writing consistency check"),
    ("GraphicPromptEngineeringSkill","Crea prompt dettagliati per generazione grafiche coerenti con chapter content non assurdi sostenibili","VisualEcosystem","trigger quando manuscript ready + chapter content + graphic needs from details"),
    ("CoverConceptDesignSkill","Crea cover concept basato su contenuto libro e market data performance signals","VisualEcosystem","trigger quando manuscript ready + market data + performance signals Amazon + review sites"),
    ("PlaywrightNavigationSkill","Gestisce navigazione reale Playwright su Amazon e review sites - operational real tool","ResearchEcosystem,VisualEcosystem","trigger quando search request o visual navigation request - usa PlaywrightOperationalTool navigate methods"),
    ("PlaywrightDataExtractionSkill","Estrae dati reali da pagine via Playwright selectors - atomic capture","ResearchEcosystem,VisualEcosystem","trigger quando navigation success + extraction request selectors"),
    ("PlaywrightSaveSkill","Salva risultati sorgenti URL note materiali via Playwright saving processes real operational","ResearchEcosystem,VisualEcosystem","trigger quando data_to_save ready destination ref"),
    ("MemoryReadWriteSkill","Gestisce lettura scrittura memoria attiva con protocolli validation checkpoint - active system not passive","MemoryEcosystem,all","trigger ogni read/write request da qualsiasi ecosystem via MemoryManagementTeam connector"),
    ("CheckpointManagementSkill","Crea memorizza ripristina checkpoint - core self-healing - creation triggers end phase before decision before handoff on healing","MemoryEcosystem,SelfHealingEcosystem,all","trigger end_of_each_phase before_major_decision before_handoff on_self_healing_activation per chapter in production"),
    ("AnomalyDetectionSkill","Rileva anomalie errori stalli output incoerenti - DetectionTeam OutputMonitor ErrorDetector AnomalyDetector StallDetector","SelfHealingEcosystem","trigger continuous monitoring all phase outputs completeness coherence process logs exception feed heartbeat feed"),
    ("RecoveryExecutionSkill","Esegue recovery retry rollback alternative path validation - real active healing","SelfHealingEcosystem","trigger quando diagnosis report con recovery plan available - retry adjusted params timeout++ user_agent rotate rollback to checkpoint alternative path skip_and_log"),
]

skills_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Skill\nSKILLS = []\n"
for name, func, eco_str, trigger in skills_list:
    ecos = eco_str.split(",")
    skills_content += f'''
{name} = Skill(
    name="{name}",
    owner_agents=["{name.replace('Skill','Leader')}","{name.replace('Skill','Agent')}","SupremeOrchestratorAgent","MemoryManagerLeader","SelfHealingEcosystemController"],
    trigger_condition="""{trigger}""",
    execution_steps=[
        "1. Riceve trigger condition valida con input necessari disponibili",
        "2. Legge memoria rilevante via MemoryReaderAgent con context timestamp - {func[:60]}",
        "3. Esegue logica specifica skill con operational tool se Playwright: navigate_amazon_keyword_search, navigate_review_site, extract_data, save_results, visual_save, screenshot, handle_error",
        "4. Valida output con validator agent pertinente (es. AmazonResultsValidator, PlanCoherenceValidator, GraphicQualityReviewer, MemoryValidator)",
        "5. Scrive risultato in memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent con parent ID valid flag",
        "6. Logga decisione traceability via DecisionLoggerAgent se GO NO-GO, production_start_signal, keyword_selection, niche_ranking",
        "7. Se fail attiva SelfHealingSkill detection diagnosis recovery - retry rollback escalate skip_and_log requalify - log in AnomalyLog DiagnosisLog RecoveryLog important_notes"
    ],
    success_criteria="Output valido non vuoto, validazione passata, checkpoint creato, memoria scritta, traceability loggata, workflow continua senza data loss per skill healing, almeno una measurable improvement per auto-improvement skills",
    failure_handling="Se fallisce dopo max retries (3 per healing, 3 cicli per niche), escalate a team leader L3 -> ecosistema controller L2 -> Supreme L1 con full context anomaly report, flag in important_notes pause branch se critical, rollback a ultimo checkpoint valido",
    retry_logic={{"max_retries": 3, "retry_strategy": ["retry con adjusted params timeout++ user_agent rotate alternative selector keyword expansion memory reread", "rollback a ultimo checkpoint valido via CheckpointManagerAgent", "escalate flag anomaly pause branch log important_notes", "skip_and_log broken step log continua dove possibile solo non-critical", "requalify rimanda a qualification con anomaly flag"], "checkpoint": "SelfHealingCheckpoint before after each retry", "memory_integration": "reads checkpoints decisions important_notes AnomalyLog writes AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes"}},
    used_in_ecosystems={ecos},
    hierarchy_levels=[1,2,3,4,5,6,7]
)
SKILLS.append({name})
'''

skills_content += "\nprint(f'SKILLS EXPANDED: {len(skills_list)} skills: '+str([s.name for s in SKILLS]))\n"
# Fix f-string escaping
skills_content = skills_content.replace("{len(skills_list)}","{len(SKILLS)}")

with open(f"{base}/Skills/all_skills_expanded.py","w") as f:
    f.write(skills_content)

print("Generated expanded skills")

# ---- Generate teams expanded
teams_defs = [
    ("AmazonKeywordResearchTeam","ResearchEcosystem","AmazonResearchLeader","Ricerca libri via keyword search Amazon estrazione validazione",["KeywordGeneratorAgent","AmazonSearchAgent","AmazonDataExtractorAgent","AmazonResultsValidatorAgent","KeywordQualityAnalystAgent","NicheCompetitionAnalystAgent","AmazonPageNavigatorAgent","AmazonDetailExtractorAgent","SearchQualityValidatorAgent","NicheViabilityValidatorAgent"],"ResearchDecisions + important_notes + FeedbackRegistry","DataPersistenceTeam + ReviewAnalysisResearchTeam + BookOpportunityRegistry","sequential_pipeline_with_feedback KeywordGenerator -> Search via NavigatorMicroAgent -> Extractor via CaptureMicroAgent -> Validator -> Leader decision -> loop if empty retry con adjusted keywords","handoff con package books_found raw extraction logs checkpoint CP + memory broker 8 step validation required checkpoint required memory logged self-healing on failure"),
    ("ReviewAnalysisResearchTeam","ResearchEcosystem","ReviewResearchLeader","Trova siti analizzano Amazon reviews estrae normalizza valida",["ReviewSiteFinderAgent","ReviewDataExtractorAgent","ReviewScoreNormalizerAgent","ReviewDataValidatorAgent","ReviewSentimentAnalystAgent","ReviewSiteNavigatorAgent","ReviewDataCaptureAgent"],"book opportunities da Amazon team + seed review sites","DataPersistenceTeam + ReviewDataRegistry","sequential SiteFinder -> Extractor -> Normalizer -> Validator -> Leader - self healing if no sites found ma continua se books found PlaywrightErrorHandler","handoff review analysis raw normalized scores site URLs"),
    ("DataPersistenceTeam","ResearchEcosystem","DataPersistenceLeader","Salva tutti dati via Playwright formatting validation checkpoint CP1",["PlaywrightSaveAgent","DataFormatterAgent","SaveValidatorAgent","RawDataArchiverAgent","SaveOperationMicroAgent"],"book opportunities + review data + raw","ResearchEcosystemController + QualificationEcosystem via memory + BookOpportunityRegistry ReviewDataRegistry ResearchCheckpoints","collect_and_save collect outputs -> Formatter formats structured_output ready qualifica -> PlaywrightSaveAgent saves via playwright_tool.save_results results sources URLs notes -> Validator validates -> Leader creates checkpoint CP1 ResearchCheckpoint","handoff Research->Qualification structured_output books_found review_sites_found raw_data BookOpportunityRegistry ReviewDataRegistry CP1 8 steps"),
    ("KeywordExpansionTeam","ResearchEcosystem","KeywordExpansionLeader","Espansione keyword quando empty result genera variazioni da LearningLog",["KeywordVariationGeneratorAgent","SemanticKeywordExpanderAgent","LongTailKeywordAgent"],"empty result trigger + important_notes + LearningLog","AmazonKeywordResearchTeam + retry cycle","feedback loop expansion: empty -> VariationGenerator -> SemanticExpander -> LongTail -> new keyword list -> AmazonSearchAgent retry","internal handoff a AmazonKeywordResearchTeam per retry"),
    ("SearchOptimizationTeam","ResearchEcosystem","SearchOptimizationLeader","Ottimizza strategie search Amazon riduce blocchi Playwright",["SearchStrategyOptimizerAgent","PlaywrightRotationManagerAgent"],"Playwright failure logs + AnomalyLog","AmazonKeywordResearchTeam + ReviewAnalysisResearchTeam","optimization loop: analyze failures -> StrategyOptimizer adjust -> RotationManager rotate user_agent timeout alternative selector -> retry","handoff ottimizzato strategy a search teams"),
    ("QualificationAnalysisTeam","QualificationEcosystem","QualificationLeader","Valuta reproducibilita assurdita velocita market alignment plan validity - 5 criteri",["ReproducibilityAnalystAgent","AbsurdityDetectorAgent","ProductionSpeedAnalystAgent","MarketAlignmentAnalystAgent","PlanQualityAuditorAgent","CompetitionAnalystAgent","SustainabilityAnalystAgent","BusinessFitAnalystAgent"],"Research handoff package structured_output + BookOpportunityRegistry ReviewDataRegistry + important_notes decisions history","QualificationDecisionTeam + QualificationCheckpoints + RiskRegistry","parallel_then_sequential_audit: 8 analyst parallel scann per book -> outputs to PlanQualityAuditor -> Auditor reviews entire qualification output -> QualificationLeader preliminary GO NO-GO + uses BookNicheDecisionSkill QualificationDecisionSkill","handoff analyst scores evidence risk flags plan validity a DecisionTeam"),
    ("QualificationDecisionTeam","QualificationEcosystem","QualificationDecisionLeader","Aggrega decisioni gestisce rischi scrive report finale GO NO-GO",["DecisionAggregatorAgent","RiskFlagManagerAgent","QualificationReportWriterAgent","DecisionQualityCheckerAgent"],"analyst_outputs + risk_flags","PlanningEcosystem if GO + QualificationDecisions + QualificationPlans + RiskRegistry + decisions memory","aggregation_and_reporting: Aggregator via QualificationDecisionSkill weighted repro 30% speed 25% absurdity 20% market 25% threshold 70 GO auto NO-GO if absurdity TRUE too_slow TRUE -> RiskManager prioritizes -> ReportWriter writes final report -> DecisionLeader approves - reasoning_chain logged via DecisionLoggerAgent","handoff Qual->Plan GO decision + qualification report + risk_flags + QualificationDecisions + CP2 solo GO avanza NO-GO archivia trigger new research"),
    ("StructurePlanningTeam","PlanningEcosystem","StructurePlanningLeader","Definisce video_structure REQUIRED preservato verbatim chapters details coherence - CONTROL POINT CRITICO",["VideoStructureArchitectAgent","ChapterDesignerAgent","DetailFillerAgent","PlanCoherenceValidatorAgent","VideoStructureValidatorAgent","OutlineOptimizerAgent","ContentFlowDesignerAgent"],"qualification GO package + qualification plan + risk_flags + decisions memory","ProductionReadinessTeam + ContentPlanningTeam + SecondLevelPlans + PlanningCheckpoints","sequential_critical_path: 1 VideoStructureArchitect designs video_structure REQUIRED preserve verbatim explicit control point handle_ambiguity preserve_and_encapsulate 2 ChapterDesigner creates chapters 3 DetailFiller adds details 4 PlanCoherenceValidator validates 5 StructureLeader approves - critical validation video_structure present verbatim if missing critical self-healing rollback to CP2","handoff second_level_plan draft con video_structure + chapters + details"),
    ("ProductionReadinessTeam","PlanningEcosystem","ProductionReadinessLeader","Verifica prerequisiti stima risorse emette start signal",["ReadinessCheckerAgent","ResourceEstimatorAgent","ProductionStartSignalAgent","RiskMitigationPlannerAgent"],"second_level_plan draft","ProductionEcosystem + ProductionStartSignals + PlanningCheckpoints + CP3","verification_and_signal: ReadinessChecker verifies prerequisites -> ResourceEstimator estimates -> RiskMitigationPlanner mitigazione -> ProductionStartSignalAgent emits TRUE timestamp - marks actual start production flow","handoff Plan->Prod second_level_plan complete video_structure REQUIRED + chapters + details + production_start_signal TRUE + CP3"),
    ("ContentPlanningTeam","PlanningEcosystem","ContentPlanningLeader","Pianificazione contenuti dettagliata per produzione sostenibile",["ContentDetailArchitectAgent","ContentFlowDesignerAgent","ResourceAllocationPlannerAgent","ContentDetailArchitectAgent2"],"second_level_plan draft chapters","ProductionReadinessTeam + details enriched","detail_enrichment: DetailArchitect enriches production_constraints style_notes business_alignment_notes graphic_needs sustainability_check -> FlowDesigner designs flow between chapters -> AllocationPlanner plans resources","handoff details arricchiti a ReadinessTeam"),
    ("BookWritingTeam","ProductionEcosystem","BookWritingLeader","Scrive intero libro coerente con second-level plan, continuity via memoria",["ChapterWriterAgent","ConsistencyCheckerAgent","StyleEnforcerAgent","ContentQualityReviewerAgent","ChapterDependencyManagerAgent","WritingProgressTrackerAgent","WritingQualityCheckerAgent","ProductionLogWriterAgent"],"second_level_plan + production_start_signal TRUE + memory context all decisions plans checkpoints hierarchies important_notes","ProductionQualityTeam + ProductionCheckpoints + ProductionLog","parallel_writing_then_sequential_review: 1 ChapterWriter instances per chapter parallel where possible respect dependencies 2 ConsistencyChecker cross-chapter 3 StyleEnforcer uniform style 4 ContentQualityReviewer final review 5 WritingLeader approves manuscript draft - memory read via MemoryReaderAgent continuity - checkpoint CP4 per chapter","handoff manuscript draft + production log + chapter checkpoints a QualityTeam"),
    ("ProductionQualityTeam","ProductionEcosystem","ProductionQualityLeader","Valida completezza compliance approvazione finale",["ManuscriptValidatorAgent","PlanComplianceCheckerAgent","FinalApprovalAgent","QualityMetricsCalculatorAgent","ContentValidationAgent"],"manuscript draft","VisualEcosystem + CompletedManuscripts + ProductionCheckpoints + CP4 final","validation_chain: ManuscriptValidator validates completeness -> PlanComplianceChecker checks follows second-level plan -> ContentValidation -> QualityMetrics -> FinalApprovalAgent final approval -> ProductionQualityLeader - self-healing if fail rollback to last chapter checkpoint CP4","handoff Prod->Visual completed manuscript + plan ref + production log + CP4 final memory broker 8 steps"),
    ("EditingTeam","ProductionEcosystem","EditingLeader","Editing finale uniformità correzione",["EditingCoordinatorAgent","FinalProofreaderAgent","CrossReferenceCheckerAgent"],"validated manuscript","ProductionQualityTeam final","editing_flow: Coordinator -> Proofreader -> CrossReferenceChecker -> FinalApproval","internal"),
    ("GraphicDesignTeam","VisualEcosystem","GraphicDesignLeader","Crea grafiche prompt review revision loop",["GraphicPromptCreatorAgent","GraphicGeneratorAgent","GraphicQualityReviewerAgent","GraphicRevisionAgent","GraphicStyleEnforcerAgent","VisualConsistencyCheckerAgent","GraphicPromptMicroAgent"],"manuscript + chapter definitions + details graphic needs","VisualPlaywrightOperationsTeam + VisualQualityTeam + GeneratedGraphics + GraphicPrompts + VisualProductionLog","creation_review_revision_loop: PromptCreator creates -> Generator generates via VisualPlaywrightSaveAgent using playwright_tool.visual_save support -> QualityReviewer reviews score -> IF failed RevisionAgent revises -> back to QualityReviewer IF passed approved and saved - loop until approved","handoff approved graphics + graphic prompts a Quality + FinalAssembly"),
    ("CoverDesignTeam","VisualEcosystem","CoverDesignLeader","Crea cover concept prompt generazione review critica non skippabile",["CoverConceptAgent","CoverPromptCreatorAgent","CoverGeneratorAgent","CoverQualityReviewerAgent","CoverRevisionAgent","CoverMarketFitAnalystAgent","CoverPromptMicroAgent"],"manuscript + market data + performance signals","VisualPlaywrightOperationsTeam + VisualQualityTeam + CoverVersions + final approved cover","concept_to_cover_loop: CoverConceptAgent concept content+market -> PromptCreator prompt -> Generator generates -> QualityReviewer reviews -> IF failed RevisionAgent revises loop until approved - critical cannot skip_and_log must escalate if fails","handoff final approved cover + versions + prompts"),
    ("VisualPlaywrightOperationsTeam","VisualEcosystem","VisualPlaywrightLeader","Gestisce navigazione Playwright e salvataggio visual tasks support",["VisualPlaywrightNavigatorAgent","VisualPlaywrightSaveAgent","VisualPlaywrightValidatorAgent","VisualPlaywrightCaptureAgent","VisualSaveMicroAgent"],"visual assets + save requests","VisualEcosystemController + GeneratedGraphics + CoverVersions + VisualProductionLog + save confirmations","navigator_then_save: Navigator navigation if needed -> SaveAgent saves via playwright_tool.visual_save -> Validator validates save - allowed use #4 supporting visual team activities - self-healing retry 2x skip_and_log non-critical escalate cover","handoff Visual->FinalAssembly all graphics + cover + graphic prompts saved confirmed + CP5 + CP_FINAL"),
    ("VisualQualityTeam","VisualEcosystem","VisualQualityLeader","Qualità visual finale approva grafiche e cover",["VisualQualityAuditorAgent","FinalVisualApprovalAgent"],"all graphics + cover + prompts","FinalAssembly + VisualProductionLog + CP_FINAL","quality_final: Auditor audits quality all visual vs manuscript plan market fit -> FinalVisualApproval approval -> VisualQualityLeader - creates CP5 CP_FINAL","handoff a FinalAssembly final package ready Amazon"),
    ("MemoryManagementTeam","MemoryEcosystem","MemoryManagerLeader","Gestisce memoria attiva read/write checkpoint decision plan hierarchy notes - SISTEMA ATTIVO NON PASSIVO",["MemoryWriterAgent","MemoryReaderAgent","MemoryValidatorAgent","CheckpointManagerAgent","DecisionLoggerAgent","PlanStorageAgent","HierarchyManagerAgent","ImportantNotesAgent","MemoryReadMicroAgent","MemoryWriteMicroAgent"],"read_requests + write_requests + checkpoint triggers + validation triggers + all ecosystems","all ecosystems memory responses + checkpoints + decisions + plans + hierarchies + important_notes + AnomalyLog triggers","active_memory_broker: ogni ecosystem ha memory connector -> requests routed: write -> Writer after validation by Validator, read -> Reader with context timestamp, checkpoint -> CheckpointManager auto at phase transitions, decisions -> DecisionLogger immutable append-only, plans -> PlanStorage versioned - always_active always_integrated","MemoryBrokerProtocol: Ecosystem sends read/write via connector -> Memory agents process -> Response data + timestamp -> Checkpoint auto at phase transition -> Validation by Validator -> If gap corruption trigger SelfHealing flow"),
    ("CheckpointSubEcosystem","MemoryEcosystem","CheckpointSubLeader","Sub-ecosistema gestione checkpoint creation storage restoration",["CheckpointCreatorAgent","CheckpointValidatorAgent","CheckpointRestorerAgent","CheckpointPrunerAgent","CheckpointCreateMicroAgent","CheckpointRestoreMicroAgent"],"checkpoint creation triggers + rollback requests + state snapshots","all ecosystems checkpoint_created_confirmation restored_checkpoint + SelfHealingCheckpoints","checkpoint_flow: Creator creates with parent ID valid flag - Validator validates completeness coherence - Restorer restores su richiesta rollback via RollbackExecutor - Pruner pruning vecchi preservando traceability - Micro agents atomic create restore - Core of self-healing - Memory Maintenance Flow triggers periodic","handoff a MemoryManagementTeam e SelfHealing"),
    ("DecisionLogSubEcosystem","MemoryEcosystem","DecisionLogSubLeader","Sub-ecosistema logging decisioni immutable traceability",["DecisionLogWriterAgent","DecisionLogReaderAgent","DecisionTraceabilityAgent","DecisionLogMicroAgent"],"decision_events reasoning_chains","decisions + QualificationDecisions + decision_log_confirmation decision_id + traceability","decision_log_flow: Writer logs decision_id phase team agent type value reasoning timestamp related_data immutable - Reader retrieves on request with traceability - TraceabilityAgent verifies reasoning chain - Micro atomic logging - hierarchical"),
    ("DetectionTeam","SelfHealingEcosystem","DetectionLeader","Monitora output completeness coherence detect errors anomalies stalled frozen - Detection real active",["OutputMonitorAgent","ErrorDetectorAgent","AnomalyDetectorAgent","StallDetectorAgent","PlaywrightFailureDetectorAgent","MemoryFailureDetectorAgent","ValidationCheckMicroAgent"],"phase_outputs_all_ecosystems + process_status_feeds + memory_validation_reports + heartbeat","DiagnosisTeam + AnomalyLog + important_notes + DetectionLeader report","parallel_monitoring: All detection agents parallel: OutputMonitor checks phase outputs vs expected schemas books_found non empty qualification plan 5 criteria second_level_plan video_structure REQUIRED complete_book non empty graphics+cover present - ErrorDetector scans logs errors exceptions - AnomalyDetector unusual patterns - StallDetector frozen no heartbeat - PlaywrightFailureDetector Playwright timeout blocked - MemoryFailureDetector memory write failure gaps - aggregate anomaly report severity location context checkpoint_before -> DiagnosisLeader","handoff Detection->Diagnosis anomaly reports severity context checkpoint_before 8 steps"),
    ("DiagnosisTeam","SelfHealingEcosystem","DiagnosisLeader","Analizza root cause impact crea recovery plan - real diagnosis active",["RootCauseAnalystAgent","ImpactAssessorAgent","RecoveryPlannerAgent","FailurePatternAnalyzerAgent"],"anomaly_reports","RecoveryTeam + DiagnosisLog + RecoveryLog plan","sequential_diagnosis: RootCauseAnalyst root cause categorization Playwright failure data extraction validation empty result memory stall etc - ImpactAssessor impact affected phases data loss risk checkpoint availability - FailurePatternAnalyzer recurring patterns - RecoveryPlanner creates recovery plan choosing action retry rollback escalate skip_and_log requalify with adjusted params checkpoint ID anomaly flag - mapping error_type to action per SelfHealingEngine","handoff Diagnosis->Recovery diagnosis report root cause impact recovery plan"),
    ("RecoveryTeam","SelfHealingEcosystem","RecoveryLeader","Esegue retry rollback alternative path validation - real recovery active always-on",["RetryExecutorAgent","RollbackExecutorAgent","AlternativePathAgent","RecoveryValidatorAgent","EscalationManagerAgent"],"recovery_plans","affected ecosystems resume signal + RecoveryLog + SelfHealingCheckpoints + escalation to controller if fails","retry_rollback_alternative_validate: RetryExecutor retries adjusted params increased timeout user_agent rotate alternative selector new keywords memory reread - IF fails RollbackExecutor rolls back to checkpoint via CheckpointManagerAgent restore - IF fails AlternativePath finds executes alternative path different keyword strategy skip non-critical graphic - RecoveryValidator validates recovery success without data loss - IF fails after max 3 EscalationManager escalates to controller SupremeOrchestrator - skill SelfHealingSkill - logging every recovery in RecoveryLog memory updated checkpoint restored flow continued handle_failure schema","handoff Recovery->AffectedEcosystem recovery confirmation or escalation + restored checkpoint + memory updated"),
    ("FeedbackCollectionTeam","AutoImprovementEcosystem","FeedbackCollectionLeader","Raccoglie outcomes calcola metrics rileva pattern - real improvement active",["OutcomeCollectorAgent","PerformanceMetricsAgent","PatternDetectorAgent","CycleOutcomeAnalyzerAgent","OutcomeAnalyzerAgent","MetricCaptureMicroAgent","PatternCheckMicroAgent"],"cycle_completion_signals + phase_outcome_logs + AnomalyLog + PerformanceHistory","ImprovementPlanningTeam + FeedbackRegistry + PerformanceHistory","collection_metrics_patterns: OutcomeCollector collects GO rate production speed internal time self-healing frequency plan validity scores memory retrieval patterns book performance signals from Amazon+review sites - MetricsAgent calculates metrics per 6 feedback signals qualification outcomes production speed metrics book performance signals self-healing activation frequency plan validity scores memory retrieval patterns - PatternDetector recurring patterns positive negative - no invented metrics only internal time + signals Amazon review sites","handoff FeedbackCollection->ImprovementPlanning structured feedback data metrics patterns"),
    ("ImprovementPlanningTeam","AutoImprovementEcosystem","ImprovementPlanningLeader","Analizza feedback rank priorities scrive improvement plans",["ImprovementAnalystAgent","PriorityRankerAgent","ImprovementPlanWriterAgent","OpportunityIdentifierAgent"],"feedback_data metrics patterns","ImprovementExecutionTeam + ImprovementPlans + ranked improvements","analyze_rank_write: ImprovementAnalyst analyzes feedback identifies opportunities for 5 targets future research quality future qualification decisions future plan accuracy production flow speed risk detection sensitivity - PriorityRanker ranks by impact feasibility aligned business goal quantity+performance - OpportunityIdentifier positive patterns - PlanWriter writes prioritized plan","handoff ImprovementPlanning->ImprovementExecution prioritized improvement plan analysis report"),
    ("ImprovementExecutionTeam","AutoImprovementEcosystem","ImprovementExecutionLeader","Adjust parameters update thresholds optimize workflows execution reale",["ParameterAdjusterAgent","ThresholdUpdaterAgent","WorkflowOptimizerAgent","LearningLoggerAgent"],"improvement_plans","all ecosystems updated parameters + LearningLog + PerformanceHistory + important_notes","adjust_update_optimize: ParameterAdjuster adjusts workflow params keyword strategies batch size retry limits - ThresholdUpdater updates decision thresholds GO threshold 70 based learning - WorkflowOptimizer optimizes flow sequences based performance data improve handoff validation reduce self-healing triggers fixing root causes - LearningLogger logs changes LearningLog important_notes per generate_improvement_signal schema source_phase outcome_summary improvement_suggestion target memory_write True - validation changes not introduce absurd too slow maintain operational clarity","handoff ImprovementExecution->AllEcosystems updated parameters threshold updates optimized flows learning logs read by Research Qualification before new cycle"),
]

teams_content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Team\nTEAMS = []\n"
for name, eco, leader, resp, members, inp_src, out_tgt, internal, external in teams_defs:
    teams_content += f'''
TEAMS.append(Team(
    name="{name}",
    ecosystem="{eco}",
    sub_ecosystem="{name.replace('Team','Sub')}",
    leader_agent="{leader}",
    member_agents={members},
    responsibilities={resp.split(", ") if isinstance(resp, str) else [resp]},
    input_source="{inp_src}",
    output_target="{out_tgt}",
    internal_communication_protocol={{"type": "{internal[:60]}", "flow": """{internal}""", "message_format": {{"sender":"agent_name","receiver":"next_agent","payload":"structured_data","timestamp":"ISO","checkpoint_ref":"CP"}}, "retry_policy": "on validator fail retry extractor, on empty trigger BookNicheDecisionSkill expand keywords, on failure self-healing retry rollback", "playwright_integration": "real operational tool playwright_tool methods navigate_amazon_keyword_search navigate_review_site extract_data save_results visual_save screenshot handle_error", "memory_write": "via MemoryWriterAgent + CheckpointManagerAgent + DecisionLoggerAgent", "skill_usage": "BookNicheDecisionSkill QualificationDecisionSkill SelfHealingSkill VideoStructureDesignSkill etc"}},
    external_handoff_protocol={{"protocol_name": "{name} to next Handoff", "steps": ["1. Source leader creates handoff package structured output decisions risks checkpoint ref","2. Package contents {name} specific","3. Memory logs handoff via MemoryWriterAgent","4. Source leader confirms ready writes checkpoint","5. Target leader confirms receipt reads memory via MemoryReaderAgent","6. Target validates completeness via Validator agent","7. If validation fails SelfHealing flow activates","8. If passes target begins work logs completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True, "description": """{external}"""}},
    hierarchy_level=3
))
'''

teams_content += f'\nprint(f"TEAMS EXPANDED: {{len(TEAMS)}} teams: "+str([t.name for t in TEAMS]))\n'

with open(f"{base}/Teams/all_teams_expanded.py","w") as f:
    f.write(teams_content)

print("Generated teams expanded 26 teams")
