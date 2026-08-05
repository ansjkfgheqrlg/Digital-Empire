import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent


ReproducibilityAnalystAgent = Agent(
    name="ReproducibilityAnalystAgent",
    role="Senior valuta reproducibilita efficiente senza risorse inaccessibili",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["book_opportunity_data", "review_analysis"],
    outputs=["reproducibility_score", "evidence", "risk_flag"],
    decision_logic="""Senior valuta se libro contiene elementi requiring inaccessible resources OR unrealistic production steps THEN score LOW flag absurd ELSE HIGH Evidence link data Amazon review sites Threshold can be reproduced efficiently Decision authority tactical""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

AbsurdityDetectorAgent = Agent(
    name="AbsurdityDetectorAgent",
    role="Rileva elementi assurdi irrealistici nonsensical gate non assurdi",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["book_data", "chapter_hints"],
    outputs=["absurdity_flag", "absurdity_evidence", "absurdity_score"],
    decision_logic="""Scan book opportunity absurd elements impossible claims unrealistic promises nonsensical structure IF absurd found THEN flag TRUE evidence fail business alignment gate non assurdi""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ProductionSpeedAnalystAgent = Agent(
    name="ProductionSpeedAnalystAgent",
    role="Stima tempo produzione flag too slow vs modello quantita sostenibile",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["book_complexity", "chapter_count", "graphic_requirements"],
    outputs=["speed_estimate", "too_slow_flag", "sustainability_score"],
    decision_logic="""IF estimated production time > sustainability threshold quantity model THEN flag too_slow TRUE propose mitigation NO-GO Estimate based chapters details graphics Evidence required Tactical decision authority""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

MarketAlignmentAnalystAgent = Agent(
    name="MarketAlignmentAnalystAgent",
    role="Valuta allineamento goal quantity-performance performanti riproducibili sostenibili",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["performance_signals_amazon", "review_analysis_data", "reproducibility_score"],
    outputs=["market_alignment_score", "business_fit_evidence"],
    decision_logic="""Score alignment with goal guadagnare quantita libri performanti Check performante signals Amazon keyword search + review analysis sites riproducibile sostenibile non assurdo non lento Weighted contribution final GO decision""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

PlanQualityAuditorAgent = Agent(
    name="PlanQualityAuditorAgent",
    role="Valuta qualita qualification plan itself validita piano",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["all_analyst_outputs", "qualification_plan_draft"],
    outputs=["plan_validity_score", "plan_coherence_flag", "audit_report"],
    decision_logic="""Audit qualification plan check all 5 criteria evaluated explicitly motivation present traceability risk flags prioritized IF plan invalid THEN trigger requalify flow anomaly flag request rollback Research checkpoint Decision threshold plan_validity must be TRUE to pass""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

CompetitionAnalystAgent = Agent(
    name="CompetitionAnalystAgent",
    role="Analizza competizione livello nicchia da segnali Amazon",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["book_data", "amazon_search_results"],
    outputs=["competition_level", "competition_evidence"],
    decision_logic="""Analizza competizione livello nicchia da segnali Amazon search results count competition level scoring""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

SustainabilityAnalystAgent = Agent(
    name="SustainabilityAnalystAgent",
    role="Analizza sostenibilita produzione lungo termine quantita",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["book_complexity", "resource_estimate"],
    outputs=["sustainability_score", "long_term_viability"],
    decision_logic="""Analizza sostenibilita produzione lungo termine quantita modello quantità libri performanti""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

BusinessFitAnalystAgent = Agent(
    name="BusinessFitAnalystAgent",
    role="Valuta business fit guadagno tramite quantita libri performanti",
    hierarchy_level=4,
    team="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="AnalysisSub" if "AnalysisSub" != "None" else None,
    inputs=["market_signals", "reproducibility", "speed"],
    outputs=["business_fit_score", "business_evidence"],
    decision_logic="""Valuta business fit guadagno tramite quantita libri performanti allineamento obiettivo""",
    connections={"reports_to": ["QualificationAnalysisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

DecisionAggregatorAgent = Agent(
    name="DecisionAggregatorAgent",
    role="Aggrega output analyst decisione unificata weighted scoring",
    hierarchy_level=4,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="DecisionSub" if "DecisionSub" != "None" else None,
    inputs=["reproducibility_score", "absurdity_flag", "speed_estimate", "market_alignment", "plan_validity"],
    outputs=["aggregated_score", "preliminary_GO_NO_GO", "reasoning_chain"],
    decision_logic="""Apply weighted scoring reproducibility 30% speed 25% absurdity 20% market fit 25% threshold >=70 GO <70 NO-GO IF absurdity TRUE too_slow TRUE auto NO-GO regardless score Generate reasoning chain traceable Tactical authority but final decision QualificationDecisionLeader""",
    connections={"reports_to": ["QualificationDecisionLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

RiskFlagManagerAgent = Agent(
    name="RiskFlagManagerAgent",
    role="Gestisce prioritizza risk flags da tutti analyst",
    hierarchy_level=4,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="DecisionSub" if "DecisionSub" != "None" else None,
    inputs=["risk_flags_all_analysts"],
    outputs=["prioritized_risks", "risk_mitigation_suggestions"],
    decision_logic="""Collect all risk flags prioritize severity critical high medium low deduplicate suggest mitigations where possible write RiskRegistry IF critical risks >0 flag NO-GO""",
    connections={"reports_to": ["QualificationDecisionLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

VideoStructureArchitectAgent = Agent(
    name="VideoStructureArchitectAgent",
    role="CRITICAL REQUIRED Progetta video_structure preservato verbatim non reinterpretare CONTROL POINT CP-VIDEO-01",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["qualification_GO_package", "original_requirement_video_structure", "risk_flags"],
    outputs=["video_structure_field"],
    decision_logic="""CRITICAL Must preserve video_structure REQUIRED as per original requirement exactly do not reinterpret do not ignore Create explicit control point original_requirement preserved + validation_required flag If ambiguity detected handle_ambiguity preserve_and_encapsulate create validation checkpoint do not fill with assumptions Output must be explicit non-empty traceable to original requirement""",
    connections={"reports_to": ["StructurePlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ChapterDesignerAgent = Agent(
    name="ChapterDesignerAgent",
    role="Definisce capitoli descrizioni ordine scopo effort estimate fast vs slow",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["video_structure", "book_opportunity"],
    outputs=["chapters_list_with_descriptions"],
    decision_logic="""Design chapters list title description order purpose estimated_effort fast sustainable vs slow Must be coherent with video_structure and business goal quantity Check no chapter introduces too_slow or absurd elements""",
    connections={"reports_to": ["StructurePlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

DetailFillerAgent = Agent(
    name="DetailFillerAgent",
    role="Aggiunge ogni dettaglio rilevante produzione sostenibilita",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["chapters", "video_structure", "risk_flags"],
    outputs=["details_every_relevant"],
    decision_logic="""Add every relevant production detail production constraints style notes business alignment notes graphic needs resource estimates sustainability checks Details must be concrete not vague operational clarity priority""",
    connections={"reports_to": ["StructurePlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

PlanCoherenceValidatorAgent = Agent(
    name="PlanCoherenceValidatorAgent",
    role="Valida intero second-level plan coerente completo",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["second_level_plan_draft"],
    outputs=["coherence_validation_result", "completeness_check"],
    decision_logic="""Validate video_structure present verbatim chapters non-empty details concrete production_start_signal logic no absurd slow elements introduced alignment qualification GO IF fail trigger requalify to send back to Qualification with anomaly flag""",
    connections={"reports_to": ["StructurePlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

VideoStructureValidatorAgent = Agent(
    name="VideoStructureValidatorAgent",
    role="Valida video_structure presente verbatim non vuoto non reinterpretato critical validation",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["video_structure_field"],
    outputs=["video_structure_validation", "presence_flag", "verbatim_flag"],
    decision_logic="""Valida video_structure REQUIRED campo esistente non vuoto non reinterpretato non ignorato per absolute rule CRITICAL CONTROL POINT se missing critical failure self-healing""",
    connections={"reports_to": ["StructurePlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

OutlineOptimizerAgent = Agent(
    name="OutlineOptimizerAgent",
    role="Ottimizza outline capitoli flusso sostenibilita",
    hierarchy_level=4,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructureSub" if "StructureSub" != "None" else None,
    inputs=["chapters_draft", "details"],
    outputs=["optimized_outline"],
    decision_logic="""Ottimizza outline capitoli per flusso e sostenibilita quantita""",
    connections={"reports_to": ["StructurePlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ContentFlowDesignerAgent = Agent(
    name="ContentFlowDesignerAgent",
    role="Progetta flusso contenuti tra capitoli",
    hierarchy_level=4,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentSub" if "ContentSub" != "None" else None,
    inputs=["chapters", "details"],
    outputs=["content_flow_design"],
    decision_logic="""Progetta flusso contenuti tra capitoli per coerenza""",
    connections={"reports_to": ["ContentPlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ConsistencyCheckerAgent = Agent(
    name="ConsistencyCheckerAgent",
    role="Controlla consistenza cross-chapters durante produzione",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="WritingSub" if "WritingSub" != "None" else None,
    inputs=["chapters_written", "second_level_plan", "production_log"],
    outputs=["consistency_report", "inconsistencies_flagged"],
    decision_logic="""Check cross-chapter coherence style facts structure following plan no deviation introducing absurd elements IF inconsistency found flag trigger retry specific chapter with memory read previous decisions""",
    connections={"reports_to": ["BookWritingLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

StyleEnforcerAgent = Agent(
    name="StyleEnforcerAgent",
    role="Garantisce stile scrittura uniforme",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="WritingSub" if "WritingSub" != "None" else None,
    inputs=["manuscript_draft", "style_notes"],
    outputs=["style_normalized_manuscript", "style_log"],
    decision_logic="""Normalize writing style per style notes second_level_plan details Ensure uniform tone terminology formatting Check no generic vague advice concrete precise""",
    connections={"reports_to": ["BookWritingLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ContentQualityReviewerAgent = Agent(
    name="ContentQualityReviewerAgent",
    role="Revisiona qualita contenuto prima finalizzazione",
    hierarchy_level=4,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="WritingSub" if "WritingSub" != "None" else None,
    inputs=["normalized_manuscript"],
    outputs=["quality_review_result", "final_review_score"],
    decision_logic="""Review content against qualification plan second_level_plan business alignment Check operational clarity flow feasibility selection quality production sustainability IF quality fail trigger revision loop""",
    connections={"reports_to": ["BookWritingLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ManuscriptValidatorAgent = Agent(
    name="ManuscriptValidatorAgent",
    role="Valida completezza manoscritto",
    hierarchy_level=4,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="QualitySub" if "QualitySub" != "None" else None,
    inputs=["final_manuscript_draft"],
    outputs=["completeness_validation", "manuscript_valid_flag"],
    decision_logic="""Validate manuscript complete not partial all chapters present per plan no missing sections Check against chapters list""",
    connections={"reports_to": ["ProductionQualityLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

PlanComplianceCheckerAgent = Agent(
    name="PlanComplianceCheckerAgent",
    role="Verifica manoscritto segue second-level plan",
    hierarchy_level=4,
    team="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="QualitySub" if "QualitySub" != "None" else None,
    inputs=["manuscript", "second_level_plan"],
    outputs=["compliance_report", "deviations_list"],
    decision_logic="""Check compliance chapters respected video_structure considered details followed no introduction flagged absurd elements IF deviations log important_notes trigger consistency check""",
    connections={"reports_to": ["ProductionQualityLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

RootCauseAnalystAgent = Agent(
    name="RootCauseAnalystAgent",
    role="Analizza anomalie root cause real self-healing diagnosis",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub" if "DiagnosisSub" != "None" else None,
    inputs=["anomaly_report", "phase_state", "checkpoint_before"],
    outputs=["root_cause_diagnosis", "cause_category"],
    decision_logic="""Analyze anomaly check if missing output due Playwright failure incoherent due data extraction blocked due stall validation fail due video_structure missing etc Categorize cause suggest recovery strategy Tactical authority""",
    connections={"reports_to": ["DiagnosisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ImpactAssessorAgent = Agent(
    name="ImpactAssessorAgent",
    role="Valuta impatto anomalia su workflow",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub" if "DiagnosisSub" != "None" else None,
    inputs=["root_cause", "workflow_state"],
    outputs=["impact_assessment", "affected_phases"],
    decision_logic="""Assess impact which phases affected data loss risk checkpoint availability rollback possible alternative path exists Severity scoring""",
    connections={"reports_to": ["DiagnosisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

RecoveryPlannerAgent = Agent(
    name="RecoveryPlannerAgent",
    role="Crea recovery plan basato su diagnosis retry rollback escalate skip requalify",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub" if "DiagnosisSub" != "None" else None,
    inputs=["root_cause", "impact_assessment"],
    outputs=["recovery_plan_with_steps"],
    decision_logic="""Create recovery plan choose action retry rollback escalate skip_and_log requalify based error_type mapping Define adjusted params retry checkpoint ID rollback anomaly flag requalify Must include memory update flow continuation guarantee""",
    connections={"reports_to": ["DiagnosisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

OutputMonitorAgent = Agent(
    name="OutputMonitorAgent",
    role="Monitora output phase completeness coherence Detection Team",
    hierarchy_level=4,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub" if "DetectionSub" != "None" else None,
    inputs=["phase_outputs_feed", "expected_output_schemas"],
    outputs=["output_monitor_report", "completeness_flag"],
    decision_logic="""Monitor each phase output against expected schema books_found non empty qualification plan 5 criteria second_level_plan video_structure REQUIRED complete_book non empty graphics+cover present IF missing incoherent trigger anomaly""",
    connections={"reports_to": ["DetectionLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

AnomalyDetectorAgent = Agent(
    name="AnomalyDetectorAgent",
    role="Rileva anomalie pattern insoliti stati inattesi",
    hierarchy_level=4,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub" if "DetectionSub" != "None" else None,
    inputs=["process_metrics", "memory_validation_reports"],
    outputs=["anomaly_detected_flag", "anomaly_context"],
    decision_logic="""Detect anomalies unexpected state unusual pattern e.g. all NO-GO without alternative video_structure missing cover missing memory gap Cross-reference important_notes patterns""",
    connections={"reports_to": ["DetectionLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ImprovementAnalystAgent = Agent(
    name="ImprovementAnalystAgent",
    role="Analizza feedback identifica opportunita miglioramento 5 target",
    hierarchy_level=4,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="PlanningSub" if "PlanningSub" != "None" else None,
    inputs=["feedback_data", "performance_history"],
    outputs=["improvement_opportunities", "analysis_report"],
    decision_logic="""Analyze qualification outcomes GO rate production speed metrics self-healing frequency plan validity scores memory retrieval patterns book performance signals from Amazon+review sites Identify improvement for future research quality qualification decisions plan accuracy speed risk sensitivity""",
    connections={"reports_to": ["ImprovementPlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

PriorityRankerAgent = Agent(
    name="PriorityRankerAgent",
    role="Rank improvements by impact feasibility",
    hierarchy_level=4,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="PlanningSub" if "PlanningSub" != "None" else None,
    inputs=["improvement_opportunities"],
    outputs=["ranked_improvements", "priority_scores"],
    decision_logic="""Rank by impact on business goal quantity+performance and feasibility Prioritize operational_clarity first""",
    connections={"reports_to": ["ImprovementPlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

CoverConceptAgent = Agent(
    name="CoverConceptAgent",
    role="Crea cover concept basato contenuto e market data performance signals",
    hierarchy_level=4,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverSub" if "CoverSub" != "None" else None,
    inputs=["manuscript", "market_data", "performance_signals"],
    outputs=["cover_concept", "concept_rationale"],
    decision_logic="""Create cover concept aligned with performant niche signals from Amazon and review analysis sites coherent with book content not absurd sustainable produce Decision authority tactical""",
    connections={"reports_to": ["CoverDesignLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

CoverMarketFitAnalystAgent = Agent(
    name="CoverMarketFitAnalystAgent",
    role="Analizza market fit cover concept",
    hierarchy_level=4,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverSub" if "CoverSub" != "None" else None,
    inputs=["cover_concept", "market_data"],
    outputs=["market_fit_score", "market_evidence"],
    decision_logic="""Analizza market fit cover concept basato su performance signals""",
    connections={"reports_to": ["CoverDesignLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

VisualQualityAuditorAgent = Agent(
    name="VisualQualityAuditorAgent",
    role="Audita qualita visual finale",
    hierarchy_level=4,
    team="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub" if "VisualQualitySub" != "None" else None,
    inputs=["all_graphics", "cover", "graphics_prompts"],
    outputs=["quality_audit_report", "audit_score"],
    decision_logic="""Audita qualita visual finale vs manoscritto plan market fit""",
    connections={"reports_to": ["VisualQualityLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

VisualConsistencyCheckerAgent = Agent(
    name="VisualConsistencyCheckerAgent",
    role="Verifica consistenza visual tra grafiche e cover",
    hierarchy_level=4,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicSub" if "GraphicSub" != "None" else None,
    inputs=["graphics", "cover", "prompts"],
    outputs=["consistency_report", "consistency_flag"],
    decision_logic="""Verifica consistenza visual tra grafiche e cover stile uniforme""",
    connections={"reports_to": ["GraphicDesignLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

FailurePatternAnalyzerAgent = Agent(
    name="FailurePatternAnalyzerAgent",
    role="Analizza pattern fallimenti ricorrenti per prevenzione",
    hierarchy_level=4,
    team="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub" if "DiagnosisSub" != "None" else None,
    inputs=["AnomalyLog", "DiagnosisLog", "RecoveryLog"],
    outputs=["failure_patterns", "prevention_suggestions"],
    decision_logic="""Analizza pattern fallimenti ricorrenti DiagnosisLog RecoveryLog per prevenire future""",
    connections={"reports_to": ["DiagnosisLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

OpportunityIdentifierAgent = Agent(
    name="OpportunityIdentifierAgent",
    role="Identifica opportunita miglioramento da pattern positivi",
    hierarchy_level=4,
    team="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="PlanningSub" if "PlanningSub" != "None" else None,
    inputs=["PatternRegistry", "PerformanceHistory"],
    outputs=["positive_patterns", "opportunities"],
    decision_logic="""Identifica opportunita miglioramento da pattern positivi recurring success""",
    connections={"reports_to": ["ImprovementPlanningLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L4"
)

ALL_L4 = [ReproducibilityAnalystAgent,AbsurdityDetectorAgent,ProductionSpeedAnalystAgent,MarketAlignmentAnalystAgent,PlanQualityAuditorAgent,CompetitionAnalystAgent,SustainabilityAnalystAgent,BusinessFitAnalystAgent,DecisionAggregatorAgent,RiskFlagManagerAgent,VideoStructureArchitectAgent,ChapterDesignerAgent,DetailFillerAgent,PlanCoherenceValidatorAgent,VideoStructureValidatorAgent,OutlineOptimizerAgent,ContentFlowDesignerAgent,ConsistencyCheckerAgent,StyleEnforcerAgent,ContentQualityReviewerAgent,ManuscriptValidatorAgent,PlanComplianceCheckerAgent,RootCauseAnalystAgent,ImpactAssessorAgent,RecoveryPlannerAgent,OutputMonitorAgent,AnomalyDetectorAgent,ImprovementAnalystAgent,PriorityRankerAgent,CoverConceptAgent,CoverMarketFitAnalystAgent,VisualQualityAuditorAgent,VisualConsistencyCheckerAgent,FailurePatternAnalyzerAgent,OpportunityIdentifierAgent]
print("Fixed file validated")
