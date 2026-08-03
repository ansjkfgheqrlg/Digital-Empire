import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

ReproducibilityAnalystAgent = Agent(
    name="ReproducibilityAnalystAgent",
    role="Analizza se libro riproducibile efficientemente senza risorse inaccessibili L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ReproducibilityAnalystAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

AbsurdityDetectorAgent = Agent(
    name="AbsurdityDetectorAgent",
    role="Rileva elementi assurdi irrealistici nonsensical - gate non assurdi L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior AbsurdityDetectorAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ProductionSpeedAnalystAgent = Agent(
    name="ProductionSpeedAnalystAgent",
    role="Stima tempo produzione flag too slow vs modello quantita sostenibile L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ProductionSpeedAnalystAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

MarketAlignmentAnalystAgent = Agent(
    name="MarketAlignmentAnalystAgent",
    role="Valuta allineamento goal quantity-performance: performanti riproducibili sostenibili L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior MarketAlignmentAnalystAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

PlanQualityAuditorAgent = Agent(
    name="PlanQualityAuditorAgent",
    role="Valuta qualita qualification plan itself, validita piano L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior PlanQualityAuditorAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

CompetitionAnalystAgent = Agent(
    name="CompetitionAnalystAgent",
    role="Analizza competizione livello nicchia da segnali Amazon L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior CompetitionAnalystAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

SustainabilityAnalystAgent = Agent(
    name="SustainabilityAnalystAgent",
    role="Analizza sostenibilita produzione lungo termine quantita L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior SustainabilityAnalystAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

BusinessFitAnalystAgent = Agent(
    name="BusinessFitAnalystAgent",
    role="Valuta business fit guadagno tramite quantita libri performanti L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationAnalysisTeam",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior BusinessFitAnalystAgent in QualificationAnalysisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationAnalysisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

DecisionAggregatorAgent = Agent(
    name="DecisionAggregatorAgent",
    role="Aggrega output analyst in decisione unificata weighted scoring L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationDecisionTeam",
    hierarchy_level=4,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationDecisionSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior DecisionAggregatorAgent in QualificationDecisionTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationDecisionTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

RiskFlagManagerAgent = Agent(
    name="RiskFlagManagerAgent",
    role="Gestisce prioritizza risk flags da tutti analyst L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - QualificationDecisionTeam",
    hierarchy_level=4,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationDecisionSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior RiskFlagManagerAgent in QualificationDecisionTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a QualificationDecisionTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

VideoStructureArchitectAgent = Agent(
    name="VideoStructureArchitectAgent",
    role="CRITICAL REQUIRED - Progetta video_structure preservato verbatim non reinterpretare - CONTROL POINT CP-VIDEO-01 L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - StructurePlanningTeam",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior VideoStructureArchitectAgent in StructurePlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a StructurePlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ChapterDesignerAgent = Agent(
    name="ChapterDesignerAgent",
    role="Definisce capitoli con descrizioni ordine scopo effort estimate fast vs slow L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - StructurePlanningTeam",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ChapterDesignerAgent in StructurePlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a StructurePlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

DetailFillerAgent = Agent(
    name="DetailFillerAgent",
    role="Aggiunge ogni dettaglio rilevante produzione per sostenibilita L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - StructurePlanningTeam",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior DetailFillerAgent in StructurePlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a StructurePlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

PlanCoherenceValidatorAgent = Agent(
    name="PlanCoherenceValidatorAgent",
    role="Valida intero second-level plan coerente completo L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - StructurePlanningTeam",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior PlanCoherenceValidatorAgent in StructurePlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a StructurePlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

VideoStructureValidatorAgent = Agent(
    name="VideoStructureValidatorAgent",
    role="Valida video_structure presente verbatim non vuoto non reinterpretato - critical validation L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - StructurePlanningTeam",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior VideoStructureValidatorAgent in StructurePlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a StructurePlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

OutlineOptimizerAgent = Agent(
    name="OutlineOptimizerAgent",
    role="Ottimizza outline capitoli per flusso e sostenibilita L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - StructurePlanningTeam",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior OutlineOptimizerAgent in StructurePlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a StructurePlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ContentFlowDesignerAgent = Agent(
    name="ContentFlowDesignerAgent",
    role="Progetta flusso contenuti tra capitoli L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ContentPlanningTeam",
    hierarchy_level=4,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentPlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ContentFlowDesignerAgent in ContentPlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ContentPlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ConsistencyCheckerAgent = Agent(
    name="ConsistencyCheckerAgent",
    role="Controlla consistenza cross-chapters durante produzione L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - BookWritingTeam",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ConsistencyCheckerAgent in BookWritingTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a BookWritingTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

StyleEnforcerAgent = Agent(
    name="StyleEnforcerAgent",
    role="Garantisce stile scrittura uniforme L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - BookWritingTeam",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior StyleEnforcerAgent in BookWritingTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a BookWritingTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ContentQualityReviewerAgent = Agent(
    name="ContentQualityReviewerAgent",
    role="Revisiona qualita contenuto prima finalizzazione L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - BookWritingTeam",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ContentQualityReviewerAgent in BookWritingTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a BookWritingTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

WritingProgressTrackerAgent = Agent(
    name="WritingProgressTrackerAgent",
    role="Traccia progresso scrittura capitoli paralleli L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - BookWritingTeam",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior WritingProgressTrackerAgent in BookWritingTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a BookWritingTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ManuscriptValidatorAgent = Agent(
    name="ManuscriptValidatorAgent",
    role="Valida completezza manoscritto L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ProductionQualityTeam",
    hierarchy_level=4,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="ProductionQualitySub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ManuscriptValidatorAgent in ProductionQualityTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ProductionQualityTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

PlanComplianceCheckerAgent = Agent(
    name="PlanComplianceCheckerAgent",
    role="Verifica manoscritto segue second-level plan L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ProductionQualityTeam",
    hierarchy_level=4,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="ProductionQualitySub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior PlanComplianceCheckerAgent in ProductionQualityTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ProductionQualityTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

QualityMetricsCalculatorAgent = Agent(
    name="QualityMetricsCalculatorAgent",
    role="Calcola metriche qualita produzione L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ProductionQualityTeam",
    hierarchy_level=4,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="ProductionQualitySub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior QualityMetricsCalculatorAgent in ProductionQualityTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ProductionQualityTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

KeywordQualityAnalystAgent = Agent(
    name="KeywordQualityAnalystAgent",
    role="Analizza qualita keyword Amazon search signals L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - AmazonKeywordResearchTeam",
    hierarchy_level=4,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior KeywordQualityAnalystAgent in AmazonKeywordResearchTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a AmazonKeywordResearchTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

NicheCompetitionAnalystAgent = Agent(
    name="NicheCompetitionAnalystAgent",
    role="Analizza competizione nicchia da dati Amazon L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - AmazonKeywordResearchTeam",
    hierarchy_level=4,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior NicheCompetitionAnalystAgent in AmazonKeywordResearchTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a AmazonKeywordResearchTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ReviewSentimentAnalystAgent = Agent(
    name="ReviewSentimentAnalystAgent",
    role="Analizza sentiment review data da review sites L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ReviewAnalysisResearchTeam",
    hierarchy_level=4,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ReviewSentimentAnalystAgent in ReviewAnalysisResearchTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ReviewAnalysisResearchTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

RootCauseAnalystAgent = Agent(
    name="RootCauseAnalystAgent",
    role="Analizza anomalie root cause - real self-healing diagnosis L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - DiagnosisTeam",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior RootCauseAnalystAgent in DiagnosisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a DiagnosisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ImpactAssessorAgent = Agent(
    name="ImpactAssessorAgent",
    role="Valuta impatto anomalia su workflow L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - DiagnosisTeam",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ImpactAssessorAgent in DiagnosisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a DiagnosisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

RecoveryPlannerAgent = Agent(
    name="RecoveryPlannerAgent",
    role="Crea recovery plan basato su diagnosis retry rollback escalate skip requalify L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - DiagnosisTeam",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior RecoveryPlannerAgent in DiagnosisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a DiagnosisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

OutputMonitorAgent = Agent(
    name="OutputMonitorAgent",
    role="Monitora output phase completeness coherence - Detection Team L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - DetectionTeam",
    hierarchy_level=4,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior OutputMonitorAgent in DetectionTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a DetectionTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

AnomalyDetectorAgent = Agent(
    name="AnomalyDetectorAgent",
    role="Rileva anomalie pattern insoliti stati inattesi L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - DetectionTeam",
    hierarchy_level=4,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior AnomalyDetectorAgent in DetectionTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a DetectionTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ImprovementAnalystAgent = Agent(
    name="ImprovementAnalystAgent",
    role="Analizza feedback identifica opportunita miglioramento 5 target L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ImprovementPlanningTeam",
    hierarchy_level=4,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementPlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior ImprovementAnalystAgent in ImprovementPlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ImprovementPlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

PriorityRankerAgent = Agent(
    name="PriorityRankerAgent",
    role="Rank improvements by impact feasibility L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ImprovementPlanningTeam",
    hierarchy_level=4,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementPlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior PriorityRankerAgent in ImprovementPlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ImprovementPlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

CoverConceptAgent = Agent(
    name="CoverConceptAgent",
    role="Crea cover concept basato contenuto e market data performance signals L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - CoverDesignTeam",
    hierarchy_level=4,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior CoverConceptAgent in CoverDesignTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a CoverDesignTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

CoverMarketFitAnalystAgent = Agent(
    name="CoverMarketFitAnalystAgent",
    role="Analizza market fit cover concept L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - CoverDesignTeam",
    hierarchy_level=4,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior CoverMarketFitAnalystAgent in CoverDesignTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a CoverDesignTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

VisualQualityAuditorAgent = Agent(
    name="VisualQualityAuditorAgent",
    role="Audita qualita visual finale L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - VisualQualityTeam",
    hierarchy_level=4,
    team="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior VisualQualityAuditorAgent in VisualQualityTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a VisualQualityTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

VisualConsistencyCheckerAgent = Agent(
    name="VisualConsistencyCheckerAgent",
    role="Verifica consistenza visual tra grafiche e cover L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - GraphicDesignTeam",
    hierarchy_level=4,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior VisualConsistencyCheckerAgent in GraphicDesignTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a GraphicDesignTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

FailurePatternAnalyzerAgent = Agent(
    name="FailurePatternAnalyzerAgent",
    role="Analizza pattern fallimenti ricorrenti per prevenzione L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - DiagnosisTeam",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior FailurePatternAnalyzerAgent in DiagnosisTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a DiagnosisTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

OpportunityIdentifierAgent = Agent(
    name="OpportunityIdentifierAgent",
    role="Identifica opportunita miglioramento da pattern positivi L4 Senior Agent - decision-making authority tactical senza escalation se impact < team_level e no cross-team effect - ImprovementPlanningTeam",
    hierarchy_level=4,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementPlanningSub",
    inputs=['handoff_package', 'book_opportunity_data', 'review_analysis', 'raw_data_ref', 'analyst_outputs', 'phase_state', 'feedback_data'],
    outputs=['evaluation_score', 'evidence', 'risk_flag', 'validation_result', 'audit_report', 'aggregated_decision'],
    decision_logic="""Come senior OpportunityIdentifierAgent in ImprovementPlanningTeam: valuta con evidence da Amazon keyword search + review sites analysis, score descrittivo con motivazione traceabile, flag rischi, verifica coerenza con business goal quantity-performance, decide tactical authority senza escalation a ImprovementPlanningTeam leader se threshold non superato. Per VideoStructureArchitectAgent: CRITICAL preserva video_structure REQUIRED verbatim handle_ambiguity preserve_and_encapsulate create validation checkpoint forbidden fill_with_assumptions.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'QualificationDecisionSkill', 'SelfHealingSkill', 'VideoStructureDesignSkill', 'ChapterDesignSkill', 'AnomalyDetectionSkill', 'RecoveryExecutionSkill'],
    level_name="L4_SENIOR_AGENT"
)

ALL_L4 = [ReproducibilityAnalystAgent,AbsurdityDetectorAgent,ProductionSpeedAnalystAgent,MarketAlignmentAnalystAgent,PlanQualityAuditorAgent,CompetitionAnalystAgent,SustainabilityAnalystAgent,BusinessFitAnalystAgent,DecisionAggregatorAgent,RiskFlagManagerAgent,VideoStructureArchitectAgent,ChapterDesignerAgent,DetailFillerAgent,PlanCoherenceValidatorAgent,VideoStructureValidatorAgent,OutlineOptimizerAgent,ContentFlowDesignerAgent,ConsistencyCheckerAgent,StyleEnforcerAgent,ContentQualityReviewerAgent,WritingProgressTrackerAgent,ManuscriptValidatorAgent,PlanComplianceCheckerAgent,QualityMetricsCalculatorAgent,KeywordQualityAnalystAgent,NicheCompetitionAnalystAgent,ReviewSentimentAnalystAgent,RootCauseAnalystAgent,ImpactAssessorAgent,RecoveryPlannerAgent,OutputMonitorAgent,AnomalyDetectorAgent,ImprovementAnalystAgent,PriorityRankerAgent,CoverConceptAgent,CoverMarketFitAnalystAgent,VisualQualityAuditorAgent,VisualConsistencyCheckerAgent,FailurePatternAnalyzerAgent,OpportunityIdentifierAgent]
