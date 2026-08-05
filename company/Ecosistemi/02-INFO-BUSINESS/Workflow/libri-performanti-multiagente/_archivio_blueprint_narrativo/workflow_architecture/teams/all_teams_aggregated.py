import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Team
TEAMS=[]

TEAMS.append(Team(
    name="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    leader_agent="AmazonResearchLeader",
    member_agents=["AmazonResearchLeaderMemberA","AmazonResearchLeaderMemberB","AmazonResearchLeaderMemberC"],
    responsibilities=["Responsabilita principale AmazonKeywordResearchTeam in ResearchEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ResearchEcosystem",
    output_target="Prossimo team/ecosistema + memory ResearchEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ResearchEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "AmazonKeywordResearchTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    leader_agent="ReviewResearchLeader",
    member_agents=["ReviewResearchLeaderMemberA","ReviewResearchLeaderMemberB","ReviewResearchLeaderMemberC"],
    responsibilities=["Responsabilita principale ReviewAnalysisResearchTeam in ResearchEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ResearchEcosystem",
    output_target="Prossimo team/ecosistema + memory ResearchEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ResearchEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "ReviewAnalysisResearchTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    leader_agent="DataPersistenceLeader",
    member_agents=["DataPersistenceLeaderMemberA","DataPersistenceLeaderMemberB","DataPersistenceLeaderMemberC"],
    responsibilities=["Responsabilita principale DataPersistenceTeam in ResearchEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ResearchEcosystem",
    output_target="Prossimo team/ecosistema + memory ResearchEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ResearchEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "DataPersistenceTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="KeywordExpansionSub",
    leader_agent="KeywordExpansionLeader",
    member_agents=["KeywordExpansionLeaderMemberA","KeywordExpansionLeaderMemberB","KeywordExpansionLeaderMemberC"],
    responsibilities=["Responsabilita principale KeywordExpansionTeam in ResearchEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ResearchEcosystem",
    output_target="Prossimo team/ecosistema + memory ResearchEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ResearchEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "KeywordExpansionTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="SearchOptimizationTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="SearchOptimizationSub",
    leader_agent="SearchOptimizationLeader",
    member_agents=["SearchOptimizationLeaderMemberA","SearchOptimizationLeaderMemberB","SearchOptimizationLeaderMemberC"],
    responsibilities=["Responsabilita principale SearchOptimizationTeam in ResearchEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ResearchEcosystem",
    output_target="Prossimo team/ecosistema + memory ResearchEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ResearchEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "SearchOptimizationTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="QualificationAnalysisTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationAnalysisSub",
    leader_agent="QualificationLeader",
    member_agents=["QualificationLeaderMemberA","QualificationLeaderMemberB","QualificationLeaderMemberC"],
    responsibilities=["Responsabilita principale QualificationAnalysisTeam in QualificationEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory QualificationEcosystem",
    output_target="Prossimo team/ecosistema + memory QualificationEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if QualificationEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "QualificationAnalysisTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationDecisionSub",
    leader_agent="QualificationDecisionLeader",
    member_agents=["QualificationDecisionLeaderMemberA","QualificationDecisionLeaderMemberB","QualificationDecisionLeaderMemberC"],
    responsibilities=["Responsabilita principale QualificationDecisionTeam in QualificationEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory QualificationEcosystem",
    output_target="Prossimo team/ecosistema + memory QualificationEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if QualificationEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "QualificationDecisionTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    leader_agent="StructurePlanningLeader",
    member_agents=["StructurePlanningLeaderMemberA","StructurePlanningLeaderMemberB","StructurePlanningLeaderMemberC"],
    responsibilities=["Responsabilita principale StructurePlanningTeam in PlanningEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory PlanningEcosystem",
    output_target="Prossimo team/ecosistema + memory PlanningEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if PlanningEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "StructurePlanningTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ProductionReadinessSub",
    leader_agent="ProductionReadinessLeader",
    member_agents=["ProductionReadinessLeaderMemberA","ProductionReadinessLeaderMemberB","ProductionReadinessLeaderMemberC"],
    responsibilities=["Responsabilita principale ProductionReadinessTeam in PlanningEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory PlanningEcosystem",
    output_target="Prossimo team/ecosistema + memory PlanningEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if PlanningEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "ProductionReadinessTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentPlanningSub",
    leader_agent="ContentPlanningLeader",
    member_agents=["ContentPlanningLeaderMemberA","ContentPlanningLeaderMemberB","ContentPlanningLeaderMemberC"],
    responsibilities=["Responsabilita principale ContentPlanningTeam in PlanningEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory PlanningEcosystem",
    output_target="Prossimo team/ecosistema + memory PlanningEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if PlanningEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "ContentPlanningTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    leader_agent="BookWritingLeader",
    member_agents=["BookWritingLeaderMemberA","BookWritingLeaderMemberB","BookWritingLeaderMemberC"],
    responsibilities=["Responsabilita principale BookWritingTeam in ProductionEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ProductionEcosystem",
    output_target="Prossimo team/ecosistema + memory ProductionEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ProductionEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "BookWritingTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="ProductionQualityTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="ProductionQualitySub",
    leader_agent="ProductionQualityLeader",
    member_agents=["ProductionQualityLeaderMemberA","ProductionQualityLeaderMemberB","ProductionQualityLeaderMemberC"],
    responsibilities=["Responsabilita principale ProductionQualityTeam in ProductionEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ProductionEcosystem",
    output_target="Prossimo team/ecosistema + memory ProductionEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ProductionEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "ProductionQualityTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="EditingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub",
    leader_agent="EditingLeader",
    member_agents=["EditingLeaderMemberA","EditingLeaderMemberB","EditingLeaderMemberC"],
    responsibilities=["Responsabilita principale EditingTeam in ProductionEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory ProductionEcosystem",
    output_target="Prossimo team/ecosistema + memory ProductionEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if ProductionEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "EditingTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    leader_agent="GraphicDesignLeader",
    member_agents=["GraphicDesignLeaderMemberA","GraphicDesignLeaderMemberB","GraphicDesignLeaderMemberC"],
    responsibilities=["Responsabilita principale GraphicDesignTeam in VisualEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory VisualEcosystem",
    output_target="Prossimo team/ecosistema + memory VisualEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if VisualEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "GraphicDesignTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    leader_agent="CoverDesignLeader",
    member_agents=["CoverDesignLeaderMemberA","CoverDesignLeaderMemberB","CoverDesignLeaderMemberC"],
    responsibilities=["Responsabilita principale CoverDesignTeam in VisualEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory VisualEcosystem",
    output_target="Prossimo team/ecosistema + memory VisualEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if VisualEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "CoverDesignTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    leader_agent="VisualPlaywrightLeader",
    member_agents=["VisualPlaywrightLeaderMemberA","VisualPlaywrightLeaderMemberB","VisualPlaywrightLeaderMemberC"],
    responsibilities=["Responsabilita principale VisualPlaywrightOperationsTeam in VisualEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory VisualEcosystem",
    output_target="Prossimo team/ecosistema + memory VisualEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if VisualEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "VisualPlaywrightOperationsTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="VisualQualityTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualQualitySub",
    leader_agent="VisualQualityLeader",
    member_agents=["VisualQualityLeaderMemberA","VisualQualityLeaderMemberB","VisualQualityLeaderMemberC"],
    responsibilities=["Responsabilita principale VisualQualityTeam in VisualEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory VisualEcosystem",
    output_target="Prossimo team/ecosistema + memory VisualEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if VisualEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "VisualQualityTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    leader_agent="MemoryManagerLeader",
    member_agents=["MemoryManagerLeaderMemberA","MemoryManagerLeaderMemberB","MemoryManagerLeaderMemberC"],
    responsibilities=["Responsabilita principale MemoryManagementTeam in MemoryEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory MemoryEcosystem",
    output_target="Prossimo team/ecosistema + memory MemoryEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if MemoryEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "MemoryManagementTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    leader_agent="CheckpointSubLeader",
    member_agents=["CheckpointSubLeaderMemberA","CheckpointSubLeaderMemberB","CheckpointSubLeaderMemberC"],
    responsibilities=["Responsabilita principale CheckpointSubEcosystem in MemoryEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory MemoryEcosystem",
    output_target="Prossimo team/ecosistema + memory MemoryEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if MemoryEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "CheckpointSubEcosystem handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionLogSubEcosystem",
    leader_agent="DecisionLogSubLeader",
    member_agents=["DecisionLogSubLeaderMemberA","DecisionLogSubLeaderMemberB","DecisionLogSubLeaderMemberC"],
    responsibilities=["Responsabilita principale DecisionLogSubEcosystem in MemoryEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory MemoryEcosystem",
    output_target="Prossimo team/ecosistema + memory MemoryEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if MemoryEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "DecisionLogSubEcosystem handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    leader_agent="DetectionLeader",
    member_agents=["DetectionLeaderMemberA","DetectionLeaderMemberB","DetectionLeaderMemberC"],
    responsibilities=["Responsabilita principale DetectionTeam in SelfHealingEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory SelfHealingEcosystem",
    output_target="Prossimo team/ecosistema + memory SelfHealingEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if SelfHealingEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "DetectionTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="DiagnosisTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DiagnosisSub",
    leader_agent="DiagnosisLeader",
    member_agents=["DiagnosisLeaderMemberA","DiagnosisLeaderMemberB","DiagnosisLeaderMemberC"],
    responsibilities=["Responsabilita principale DiagnosisTeam in SelfHealingEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory SelfHealingEcosystem",
    output_target="Prossimo team/ecosistema + memory SelfHealingEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if SelfHealingEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "DiagnosisTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    leader_agent="RecoveryLeader",
    member_agents=["RecoveryLeaderMemberA","RecoveryLeaderMemberB","RecoveryLeaderMemberC"],
    responsibilities=["Responsabilita principale RecoveryTeam in SelfHealingEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory SelfHealingEcosystem",
    output_target="Prossimo team/ecosistema + memory SelfHealingEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if SelfHealingEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "RecoveryTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    leader_agent="FeedbackCollectionLeader",
    member_agents=["FeedbackCollectionLeaderMemberA","FeedbackCollectionLeaderMemberB","FeedbackCollectionLeaderMemberC"],
    responsibilities=["Responsabilita principale FeedbackCollectionTeam in AutoImprovementEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory AutoImprovementEcosystem",
    output_target="Prossimo team/ecosistema + memory AutoImprovementEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if AutoImprovementEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "FeedbackCollectionTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="ImprovementPlanningTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementPlanningSub",
    leader_agent="ImprovementPlanningLeader",
    member_agents=["ImprovementPlanningLeaderMemberA","ImprovementPlanningLeaderMemberB","ImprovementPlanningLeaderMemberC"],
    responsibilities=["Responsabilita principale ImprovementPlanningTeam in AutoImprovementEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory AutoImprovementEcosystem",
    output_target="Prossimo team/ecosistema + memory AutoImprovementEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if AutoImprovementEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "ImprovementPlanningTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

TEAMS.append(Team(
    name="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementExecutionSub",
    leader_agent="ImprovementExecutionLeader",
    member_agents=["ImprovementExecutionLeaderMemberA","ImprovementExecutionLeaderMemberB","ImprovementExecutionLeaderMemberC"],
    responsibilities=["Responsabilita principale ImprovementExecutionTeam in AutoImprovementEcosystem", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory AutoImprovementEcosystem",
    output_target="Prossimo team/ecosistema + memory AutoImprovementEcosystem + checkpoint",
    internal_communication_protocol={"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if AutoImprovementEcosystem==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]},
    external_handoff_protocol={"protocol_name": "ImprovementExecutionTeam handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True},
    hierarchy_level=3
))

print(f"TEAMS EXPANDED: {len(TEAMS)} teams")
