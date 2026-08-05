import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

KeywordGeneratorAgent = Agent(
    name="KeywordGeneratorAgent",
    role="Genera variazioni keyword per Amazon search da seed + important_notes patterns L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational KeywordGeneratorAgent in AmazonKeywordResearchTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

AmazonSearchAgent = Agent(
    name="AmazonSearchAgent",
    role="Esegue ricerche Amazon via Playwright operational tool real navigation L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational AmazonSearchAgent in AmazonKeywordResearchTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

AmazonDataExtractorAgent = Agent(
    name="AmazonDataExtractorAgent",
    role="Estrae dati libri titoli autori ratings prezzi categorie via Playwright capture L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational AmazonDataExtractorAgent in AmazonKeywordResearchTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ReviewSiteFinderAgent = Agent(
    name="ReviewSiteFinderAgent",
    role="Trova siti che analizzano Amazon reviews via Playwright navigation L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ReviewSiteFinderAgent in ReviewAnalysisResearchTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ReviewDataExtractorAgent = Agent(
    name="ReviewDataExtractorAgent",
    role="Estrae dati analisi review da siti trovati via Playwright L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ReviewDataExtractorAgent in ReviewAnalysisResearchTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

PlaywrightSaveAgent = Agent(
    name="PlaywrightSaveAgent",
    role="Gestisce tutte le operazioni save Playwright research e visual L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational PlaywrightSaveAgent in DataPersistenceTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

DataFormatterAgent = Agent(
    name="DataFormatterAgent",
    role="Formatta dati in structured_output pronto per qualifica L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational DataFormatterAgent in DataPersistenceTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

RawDataArchiverAgent = Agent(
    name="RawDataArchiverAgent",
    role="Archivia raw data da Playwright con refs e screenshot L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational RawDataArchiverAgent in DataPersistenceTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

KeywordVariationGeneratorAgent = Agent(
    name="KeywordVariationGeneratorAgent",
    role="Genera variazioni keyword avanzate per retry quando empty result L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="KeywordExpansionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational KeywordVariationGeneratorAgent in KeywordExpansionTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

SemanticKeywordExpanderAgent = Agent(
    name="SemanticKeywordExpanderAgent",
    role="Espande keyword semanticamente da LearningLog patterns L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="KeywordExpansionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational SemanticKeywordExpanderAgent in KeywordExpansionTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

LongTailKeywordAgent = Agent(
    name="LongTailKeywordAgent",
    role="Genera long-tail keywords per nicchie meno competitive L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="KeywordExpansionTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="KeywordExpansionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational LongTailKeywordAgent in KeywordExpansionTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

SearchStrategyOptimizerAgent = Agent(
    name="SearchStrategyOptimizerAgent",
    role="Ottimizza strategia search per ridurre blocchi Playwright L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="SearchOptimizationTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="SearchOptimizationSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational SearchStrategyOptimizerAgent in SearchOptimizationTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

QualificationReportWriterAgent = Agent(
    name="QualificationReportWriterAgent",
    role="Scrive report qualifica finale strutturato con GO NO-GO L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationDecisionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational QualificationReportWriterAgent in QualificationDecisionTeam QualificationEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

DecisionQualityCheckerAgent = Agent(
    name="DecisionQualityCheckerAgent",
    role="Verifica qualita decisione traceability motivazione L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="QualificationDecisionTeam",
    ecosystem="QualificationEcosystem",
    sub_ecosystem="QualificationDecisionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational DecisionQualityCheckerAgent in QualificationDecisionTeam QualificationEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ContentDetailArchitectAgent = Agent(
    name="ContentDetailArchitectAgent",
    role="Progetta dettagli contenuti per sustainable production L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentPlanningSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ContentDetailArchitectAgent in ContentPlanningTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ReadinessCheckerAgent = Agent(
    name="ReadinessCheckerAgent",
    role="Verifica prerequisiti produzione met - second-level plan complete L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ProductionReadinessSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ReadinessCheckerAgent in ProductionReadinessTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ResourceEstimatorAgent = Agent(
    name="ResourceEstimatorAgent",
    role="Stima risorse necessarie tempo capitoli grafica cover L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ProductionReadinessSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ResourceEstimatorAgent in ProductionReadinessTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ProductionStartSignalAgent = Agent(
    name="ProductionStartSignalAgent",
    role="Emette segnale formale start produzione TRUE timestamp - marks actual start production flow L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ProductionReadinessSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ProductionStartSignalAgent in ProductionReadinessTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

RiskMitigationPlannerAgent = Agent(
    name="RiskMitigationPlannerAgent",
    role="Pianifica mitigazione rischi identificati in RiskRegistry L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ProductionReadinessTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ProductionReadinessSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational RiskMitigationPlannerAgent in ProductionReadinessTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ChapterWriterAgent = Agent(
    name="ChapterWriterAgent",
    role="Scrive capitoli singoli multiple instances parallele, legge memoria per continuity L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ChapterWriterAgent in BookWritingTeam ProductionEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ChapterDependencyManagerAgent = Agent(
    name="ChapterDependencyManagerAgent",
    role="Gestisce dipendenze tra capitoli per scrittura parallela L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="BookWritingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="BookWritingSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ChapterDependencyManagerAgent in BookWritingTeam ProductionEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

EditingCoordinatorAgent = Agent(
    name="EditingCoordinatorAgent",
    role="Coordina editing finale L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="EditingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational EditingCoordinatorAgent in EditingTeam ProductionEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

FinalProofreaderAgent = Agent(
    name="FinalProofreaderAgent",
    role="Proofreading finale manoscritto L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="EditingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational FinalProofreaderAgent in EditingTeam ProductionEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

GraphicPromptCreatorAgent = Agent(
    name="GraphicPromptCreatorAgent",
    role="Crea prompt dettagliati per generazione grafiche L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational GraphicPromptCreatorAgent in GraphicDesignTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

GraphicGeneratorAgent = Agent(
    name="GraphicGeneratorAgent",
    role="Genera grafiche usando prompt + salva via VisualPlaywrightSaveAgent visual_save L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational GraphicGeneratorAgent in GraphicDesignTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

CoverPromptCreatorAgent = Agent(
    name="CoverPromptCreatorAgent",
    role="Crea prompt dettagliato cover generation L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational CoverPromptCreatorAgent in CoverDesignTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

CoverGeneratorAgent = Agent(
    name="CoverGeneratorAgent",
    role="Genera cover + salva via Playwright - asset critico L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational CoverGeneratorAgent in CoverDesignTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

MemoryWriterAgent = Agent(
    name="MemoryWriterAgent",
    role="Gestisce scritture strutturate memoria da tutti ecosistemi - sistema attivo L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational MemoryWriterAgent in MemoryManagementTeam MemoryEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

MemoryReaderAgent = Agent(
    name="MemoryReaderAgent",
    role="Gestisce letture memoria da tutti ecosistemi con context timestamp - sistema attivo L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational MemoryReaderAgent in MemoryManagementTeam MemoryEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

RetryExecutorAgent = Agent(
    name="RetryExecutorAgent",
    role="Esegue retry con adjusted params real recovery - timeout++ user_agent rotate L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational RetryExecutorAgent in RecoveryTeam SelfHealingEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

OutcomeCollectorAgent = Agent(
    name="OutcomeCollectorAgent",
    role="Raccoglie outcomes da cicli completati per auto-improvement L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational OutcomeCollectorAgent in FeedbackCollectionTeam AutoImprovementEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ParameterAdjusterAgent = Agent(
    name="ParameterAdjusterAgent",
    role="Aggiusta parametri workflow basati su improvement plan L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementExecutionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ParameterAdjusterAgent in ImprovementExecutionTeam AutoImprovementEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ResourceAllocationPlannerAgent = Agent(
    name="ResourceAllocationPlannerAgent",
    role="Pianifica allocazione risorse per capitoli L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentPlanningSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ResourceAllocationPlannerAgent in ContentPlanningTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

CrossReferenceCheckerAgent = Agent(
    name="CrossReferenceCheckerAgent",
    role="Verifica cross-reference tra capitoli e piano L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="EditingTeam",
    ecosystem="ProductionEcosystem",
    sub_ecosystem="EditingSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational CrossReferenceCheckerAgent in EditingTeam ProductionEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

GraphicStyleEnforcerAgent = Agent(
    name="GraphicStyleEnforcerAgent",
    role="Impone stile uniforme grafiche L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational GraphicStyleEnforcerAgent in GraphicDesignTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

VisualQualityReviewerAgent = Agent(
    name="VisualQualityReviewerAgent",
    role="Legato ma usato in L5 variant - quality review operational L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational VisualQualityReviewerAgent in GraphicDesignTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

OutcomeAnalyzerAgent = Agent(
    name="OutcomeAnalyzerAgent",
    role="Analizza outcomes per feedback collection L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational OutcomeAnalyzerAgent in FeedbackCollectionTeam AutoImprovementEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ContentFlowDesignerAgent = Agent(
    name="ContentFlowDesignerAgent",
    role="Disegna flusso contenuti second-level plan L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="StructurePlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="StructurePlanningSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ContentFlowDesignerAgent in StructurePlanningTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

PlaywrightRotationManagerAgent = Agent(
    name="PlaywrightRotationManagerAgent",
    role="Gestisce rotazione Playwright per evitare blocchi L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="SearchOptimizationTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="SearchOptimizationSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational PlaywrightRotationManagerAgent in SearchOptimizationTeam ResearchEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

CheckpointCreatorAgent = Agent(
    name="CheckpointCreatorAgent",
    role="Crea checkpoint via CheckpointManagerAgent - parte Memory sub-ecosystem L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational CheckpointCreatorAgent in CheckpointSubEcosystem MemoryEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

DecisionLogWriterAgent = Agent(
    name="DecisionLogWriterAgent",
    role="Scrive decisioni log immutable - Memory sub-ecosystem L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionLogSubEcosystem",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational DecisionLogWriterAgent in DecisionLogSubEcosystem MemoryEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

LearningLoggerAgent = Agent(
    name="LearningLoggerAgent",
    role="Logga learning in LearningLog - auto-improvement execution L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ImprovementExecutionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="ImprovementExecutionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational LearningLoggerAgent in ImprovementExecutionTeam AutoImprovementEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

CycleOutcomeAnalyzerAgent = Agent(
    name="CycleOutcomeAnalyzerAgent",
    role="Analizza outcome ciclo completo L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational CycleOutcomeAnalyzerAgent in FeedbackCollectionTeam AutoImprovementEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ContentDetailArchitectAgent2 = Agent(
    name="ContentDetailArchitectAgent2",
    role="Second instance detail architect for redundancy L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="ContentPlanningTeam",
    ecosystem="PlanningEcosystem",
    sub_ecosystem="ContentPlanningSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational ContentDetailArchitectAgent2 in ContentPlanningTeam PlanningEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage=None,
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

VisualPlaywrightSaveAgent = Agent(
    name="VisualPlaywrightSaveAgent",
    role="Salva visual outputs via Playwright support - operational variant L5 Operational Agent - esegue core tasks research writing evaluation graphic creation data collection Playwright operations, segue istruzioni senior e leader, report output",
    hierarchy_level=5,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    inputs=['internal_flow_trigger', 'handoff_package', 'keyword_variations', 'search_results_raw', 'extraction_request', 'write_requests', 'chapter_definition', 'second_level_plan', 'memory_context', 'anomaly_report', 'feedback_data', 'improvement_plan'],
    outputs=['search_results_raw', 'extracted_book_metadata', 'review_data_raw', 'formatted_structured_output', 'save_confirmation', 'keyword_variations', 'evaluation_outputs', 'chapter_written_content', 'graphic_prompts', 'graphics_raw', 'cover_raw', 'memory_write_confirmation', 'read_response', 'retry_execution_result', 'collected_outcomes', 'parameter_adjustments'],
    decision_logic="""Come operational VisualPlaywrightSaveAgent in VisualPlaywrightOperationsTeam VisualEcosystem: esegue task core con Playwright tool reale se richiesto (navigate_amazon_keyword_search, extract_data, save_results, visual_save), gestisce retry su failure via PlaywrightErrorHandlerAgent, scrive checkpoint via CheckpointManagerAgent, legge/scrive memoria via MemoryWriter/Reader, applica skill pertinente. Per AmazonSearchAgent: per ogni keyword chiama playwright_tool.navigate_amazon_keyword_search via PlaywrightNavigatorMicroAgent atomic. Per ChapterWriterAgent: legge memoria via MemoryReaderAgent per context continuity, scrive ProductionCheckpoints per chapter.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="navigation and data collection from Amazon + saving results sources URLs notes + supporting visual activities",
    skill_usage=['BookNicheDecisionSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'SelfHealingSkill', 'BookWritingConsistencySkill', 'GraphicPromptEngineeringSkill'],
    level_name="L5_OPERATIONAL_AGENT"
)

ALL_L5 = [KeywordGeneratorAgent,AmazonSearchAgent,AmazonDataExtractorAgent,ReviewSiteFinderAgent,ReviewDataExtractorAgent,PlaywrightSaveAgent,DataFormatterAgent,RawDataArchiverAgent,KeywordVariationGeneratorAgent,SemanticKeywordExpanderAgent,LongTailKeywordAgent,SearchStrategyOptimizerAgent,QualificationReportWriterAgent,DecisionQualityCheckerAgent,ContentDetailArchitectAgent,ReadinessCheckerAgent,ResourceEstimatorAgent,ProductionStartSignalAgent,RiskMitigationPlannerAgent,ChapterWriterAgent,ChapterDependencyManagerAgent,EditingCoordinatorAgent,FinalProofreaderAgent,GraphicPromptCreatorAgent,GraphicGeneratorAgent,CoverPromptCreatorAgent,CoverGeneratorAgent,MemoryWriterAgent,MemoryReaderAgent,RetryExecutorAgent,OutcomeCollectorAgent,ParameterAdjusterAgent,ResourceAllocationPlannerAgent,CrossReferenceCheckerAgent,GraphicStyleEnforcerAgent,VisualQualityReviewerAgent,OutcomeAnalyzerAgent,ContentFlowDesignerAgent,PlaywrightRotationManagerAgent,CheckpointCreatorAgent,DecisionLogWriterAgent,LearningLoggerAgent,CycleOutcomeAnalyzerAgent,ContentDetailArchitectAgent2,VisualPlaywrightSaveAgent]
