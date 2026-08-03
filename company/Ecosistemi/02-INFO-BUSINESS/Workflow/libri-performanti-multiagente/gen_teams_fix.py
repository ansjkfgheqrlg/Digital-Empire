import os
base="/home/user/architettura_completa_7_livelli"
teams_defs_simple = [
    ("AmazonKeywordResearchTeam","ResearchEcosystem","AmazonResearchLeader"),
    ("ReviewAnalysisResearchTeam","ResearchEcosystem","ReviewResearchLeader"),
    ("DataPersistenceTeam","ResearchEcosystem","DataPersistenceLeader"),
    ("KeywordExpansionTeam","ResearchEcosystem","KeywordExpansionLeader"),
    ("SearchOptimizationTeam","ResearchEcosystem","SearchOptimizationLeader"),
    ("QualificationAnalysisTeam","QualificationEcosystem","QualificationLeader"),
    ("QualificationDecisionTeam","QualificationEcosystem","QualificationDecisionLeader"),
    ("StructurePlanningTeam","PlanningEcosystem","StructurePlanningLeader"),
    ("ProductionReadinessTeam","PlanningEcosystem","ProductionReadinessLeader"),
    ("ContentPlanningTeam","PlanningEcosystem","ContentPlanningLeader"),
    ("BookWritingTeam","ProductionEcosystem","BookWritingLeader"),
    ("ProductionQualityTeam","ProductionEcosystem","ProductionQualityLeader"),
    ("EditingTeam","ProductionEcosystem","EditingLeader"),
    ("GraphicDesignTeam","VisualEcosystem","GraphicDesignLeader"),
    ("CoverDesignTeam","VisualEcosystem","CoverDesignLeader"),
    ("VisualPlaywrightOperationsTeam","VisualEcosystem","VisualPlaywrightLeader"),
    ("VisualQualityTeam","VisualEcosystem","VisualQualityLeader"),
    ("MemoryManagementTeam","MemoryEcosystem","MemoryManagerLeader"),
    ("CheckpointSubEcosystem","MemoryEcosystem","CheckpointSubLeader"),
    ("DecisionLogSubEcosystem","MemoryEcosystem","DecisionLogSubLeader"),
    ("DetectionTeam","SelfHealingEcosystem","DetectionLeader"),
    ("DiagnosisTeam","SelfHealingEcosystem","DiagnosisLeader"),
    ("RecoveryTeam","SelfHealingEcosystem","RecoveryLeader"),
    ("FeedbackCollectionTeam","AutoImprovementEcosystem","FeedbackCollectionLeader"),
    ("ImprovementPlanningTeam","AutoImprovementEcosystem","ImprovementPlanningLeader"),
    ("ImprovementExecutionTeam","AutoImprovementEcosystem","ImprovementExecutionLeader"),
]

content = "import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')\nfrom core import Team\nTEAMS=[]\n"
for name, eco, leader in teams_defs_simple:
    content += f'''
TEAMS.append(Team(
    name="{name}",
    ecosystem="{eco}",
    sub_ecosystem="{name.replace('Team','Sub')}",
    leader_agent="{leader}",
    member_agents=["{leader}MemberA","{leader}MemberB","{leader}MemberC"],
    responsibilities=["Responsabilita principale {name} in {eco}", "Gestisce flusso interno", "Valida output", "Crea checkpoint", "Gestisce self-healing retry rollback", "Esegue handoff 8-step via Memory broker"],
    input_source="Handoff package da ecosistema precedente + memory {eco}",
    output_target="Prossimo team/ecosistema + memory {eco} + checkpoint",
    internal_communication_protocol={{"type": "sequential_parallel_hybrid", "flow": "Leader trigger members in ordine o parallelo, validator valida, skill applicata (BookNicheDecisionSkill, QualificationDecisionSkill, SelfHealingSkill, VideoStructureDesignSkill etc), checkpoint via CheckpointManagerAgent, self-healing retry rollback su failure, memory read/write via MemoryWriter/Reader", "playwright_integration": "real tool playwright_tool.navigate_amazon_keyword_search, extract_data, save_results, visual_save, handle_error if {eco}==Research o Visual", "skill_usage": ["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill"]}},
    external_handoff_protocol={{"protocol_name": "{name} handoff 8 steps", "steps": ["1 Source crea package structured output decisions risks checkpoint ref", "2 Memory logs handoff via MemoryWriterAgent", "3 Source leader conferma ready scrive checkpoint", "4 Target leader conferma receipt legge memory via MemoryReaderAgent", "5 Target valida completeness via Validator", "6 Se fail SelfHealing flow Detection->Diagnosis->Recovery", "7 Se pass target inizia lavoro", "8 Memory logs handoff completion"], "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True}},
    hierarchy_level=3
))
'''
content += '\nprint(f"TEAMS EXPANDED: {len(TEAMS)} teams")\n'
with open(f"{base}/Teams/all_teams_expanded.py","w") as f:
    f.write(content)
print("Teams fixed")
