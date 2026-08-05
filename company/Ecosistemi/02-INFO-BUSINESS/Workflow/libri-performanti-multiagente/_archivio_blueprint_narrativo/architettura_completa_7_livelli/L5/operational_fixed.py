import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent


KeywordGeneratorAgent = Agent(
    name="KeywordGeneratorAgent",
    role="Genera variazioni keyword Amazon search seed important_notes",
    hierarchy_level=5,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOps" if "PlaywrightOps" != "None" else None,
    inputs=["seed_keywords", "important_notes"],
    outputs=["keyword_variations"],
    decision_logic="""Genera variazioni keyword Amazon search basata su seed historical success patterns FeedbackRegistry""",
    connections={"reports_to": ["AmazonKeywordResearchLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

AmazonSearchAgent = Agent(
    name="AmazonSearchAgent",
    role="Esegue ricerche Amazon via Playwright tool real navigation",
    hierarchy_level=5,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOps" if "PlaywrightOps" != "None" else None,
    inputs=["keyword_variations"],
    outputs=["search_results_raw"],
    decision_logic="""Per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via NavigatorMicroAgent atomic""",
    connections={"reports_to": ["AmazonKeywordResearchLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

AmazonDataExtractorAgent = Agent(
    name="AmazonDataExtractorAgent",
    role="Estrae dati libri titoli autori via Playwright capture",
    hierarchy_level=5,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOps" if "PlaywrightOps" != "None" else None,
    inputs=["search_results_raw"],
    outputs=["extracted_book_metadata"],
    decision_logic="""Use PlaywrightDataCaptureMicroAgent extract titles authors ratings prices categories save via PlaywrightSaveAgent""",
    connections={"reports_to": ["AmazonKeywordResearchLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

ReviewSiteFinderAgent = Agent(
    name="ReviewSiteFinderAgent",
    role="Trova siti analizzano Amazon reviews via Playwright",
    hierarchy_level=5,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewSub" if "ReviewSub" != "None" else None,
    inputs=["search_seed_review_sites"],
    outputs=["found_review_sites_list"],
    decision_logic="""Navigate via Playwright find sites analyze Amazon reviews Discover via Playwright operations collect URLs notes""",
    connections={"reports_to": ["ReviewAnalysisResearchLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

ReviewDataExtractorAgent = Agent(
    name="ReviewDataExtractorAgent",
    role="Estrae review analysis data da siti via Playwright",
    hierarchy_level=5,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewSub" if "ReviewSub" != "None" else None,
    inputs=["found_review_sites_list"],
    outputs=["review_analysis_raw_data"],
    decision_logic="""Extract review analysis data from found sites using PlaywrightDataCaptureMicroAgent Save via PlaywrightSaveAgent""",
    connections={"reports_to": ["ReviewAnalysisResearchLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

PlaywrightSaveAgent = Agent(
    name="PlaywrightSaveAgent",
    role="Gestisce save Playwright research visual",
    hierarchy_level=5,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PersistenceSub" if "PersistenceSub" != "None" else None,
    inputs=["data_to_save", "destination_ref"],
    outputs=["save_confirmation"],
    decision_logic="""Call playwright_tool.save_results save results sources URLs notes useful material Validate via SaveValidatorAgent Retry failure""",
    connections={"reports_to": ["DataPersistenceLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

ChapterWriterAgent = Agent(
    name="ChapterWriterAgent",
    role="Scrive capitoli singoli multiple instances parallele legge memoria continuity",
    hierarchy_level=5,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="WritingSub" if "WritingSub" != "None" else None,
    inputs=["chapter_definition", "second_level_plan", "memory_context"],
    outputs=["chapter_written_content"],
    decision_logic="""Write chapter per definition maintain consistency all previous decisions constraints via MemoryReaderAgent read continuity Log decisions""",
    connections={"reports_to": ["BookWritingLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

GraphicPromptCreatorAgent = Agent(
    name="GraphicPromptCreatorAgent",
    role="Crea prompt dettagliati grafiche",
    hierarchy_level=5,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicSub" if "GraphicSub" != "None" else None,
    inputs=["chapter_content", "graphic_requirements"],
    outputs=["graphic_prompts_detailed"],
    decision_logic="""Create prompts graphics generation detailed coherent chapter content not absurd sustainable""",
    connections={"reports_to": ["GraphicDesignLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

GraphicGeneratorAgent = Agent(
    name="GraphicGeneratorAgent",
    role="Genera grafiche using prompts salva via VisualPlaywrightSaveAgent",
    hierarchy_level=5,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicSub" if "GraphicSub" != "None" else None,
    inputs=["graphic_prompts"],
    outputs=["generated_graphics_raw"],
    decision_logic="""Generate graphics using prompts In architecture generation abstract but save via VisualPlaywrightSaveAgent visual_save""",
    connections={"reports_to": ["GraphicDesignLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

MemoryWriterAgent = Agent(
    name="MemoryWriterAgent",
    role="Gestisce scritture strutturate memoria - sistema attivo",
    hierarchy_level=5,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub" if "CoreMemorySub" != "None" else None,
    inputs=["write_requests", "data_to_write", "category"],
    outputs=["write_confirmation"],
    decision_logic="""Write structured data memory per category checkpoints decisions plans hierarchies important_notes Validate via MemoryValidatorAgent before storage Create checkpoint via CheckpointManagerAgent""",
    connections={"reports_to": ["MemoryManagementLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

MemoryReaderAgent = Agent(
    name="MemoryReaderAgent",
    role="Gestisce letture memoria - sistema attivo",
    hierarchy_level=5,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CoreMemorySub" if "CoreMemorySub" != "None" else None,
    inputs=["read_requests", "category", "requester_id"],
    outputs=["read_response_with_timestamp"],
    decision_logic="""Retrieve relevant memory on request any team serve context timestamp Read categories Integration protocol every ecosystem memory connector""",
    connections={"reports_to": ["MemoryManagementLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

RetryExecutorAgent = Agent(
    name="RetryExecutorAgent",
    role="Esegue retry adjusted params real recovery",
    hierarchy_level=5,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub" if "RecoverySub" != "None" else None,
    inputs=["recovery_plan_retry", "failed_operation_ref"],
    outputs=["retry_execution_result"],
    decision_logic="""Execute retry operation adjusted params increased timeout user_agent rotate alternative selector new keywords memory reread Log RecoveryLog Max 3 retries""",
    connections={"reports_to": ["RecoveryLeader"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L5"
)

ALL_L5 = [KeywordGeneratorAgent,AmazonSearchAgent,AmazonDataExtractorAgent,ReviewSiteFinderAgent,ReviewDataExtractorAgent,PlaywrightSaveAgent,ChapterWriterAgent,GraphicPromptCreatorAgent,GraphicGeneratorAgent,MemoryWriterAgent,MemoryReaderAgent,RetryExecutorAgent]
print("Fixed file validated")
