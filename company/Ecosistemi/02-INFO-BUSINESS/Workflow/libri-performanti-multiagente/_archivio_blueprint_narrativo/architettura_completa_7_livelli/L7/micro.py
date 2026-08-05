import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent

PlaywrightNavigatorMicroAgent = Agent(
    name="PlaywrightNavigatorMicroAgent",
    role="Micro gestisce singola navigazione pagina via Playwright tool - atomic task spawned managed higher L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOperationsSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro PlaywrightNavigatorMicroAgent L7 in PlaywrightOperationsSubEcosystem ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic navigation data capture screenshot error handling",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

PlaywrightDataCaptureMicroAgent = Agent(
    name="PlaywrightDataCaptureMicroAgent",
    role="Micro cattura dati specifici da pagine via Playwright - atomic extraction selectors L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOperationsSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro PlaywrightDataCaptureMicroAgent L7 in PlaywrightOperationsSubEcosystem ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic navigation data capture screenshot error handling",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

PlaywrightScreenshotMicroAgent = Agent(
    name="PlaywrightScreenshotMicroAgent",
    role="Micro fa screenshot quando necessario raw_data saving via Playwright L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOperationsSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro PlaywrightScreenshotMicroAgent L7 in PlaywrightOperationsSubEcosystem ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic navigation data capture screenshot error handling",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

PlaywrightErrorHandlerAgent = Agent(
    name="PlaywrightErrorHandlerAgent",
    role="Gestisce errori Playwright-specific timeouts blocked pages CAPTCHAs connection failures retry alternative - core self-healing Playwright L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="PlaywrightOperationsSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro PlaywrightErrorHandlerAgent L7 in PlaywrightOperationsSubEcosystem ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic navigation data capture screenshot error handling",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

VisualPlaywrightNavigatorAgent = Agent(
    name="VisualPlaywrightNavigatorAgent",
    role="Micro gestisce navigazione Playwright per task visual L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro VisualPlaywrightNavigatorAgent L7 in VisualPlaywrightOperationsTeam VisualEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic navigation data capture screenshot error handling",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

VisualPlaywrightCaptureAgent = Agent(
    name="VisualPlaywrightCaptureAgent",
    role="Micro cattura dati visual pages L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro VisualPlaywrightCaptureAgent L7 in VisualPlaywrightOperationsTeam VisualEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic navigation data capture screenshot error handling",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

ErrorDetectorAgent = Agent(
    name="ErrorDetectorAgent",
    role="Micro rileva errori eccezioni fallimenti in tutti processi - Detection Team L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro ErrorDetectorAgent L7 in DetectionTeam SelfHealingEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

StallDetectorAgent = Agent(
    name="StallDetectorAgent",
    role="Micro rileva processi stalled frozen no heartbeat timeout - Detection Team L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro StallDetectorAgent L7 in DetectionTeam SelfHealingEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

AlternativePathAgent = Agent(
    name="AlternativePathAgent",
    role="Micro trova esegue percorsi alternativi quando retry rollback fail real recovery L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro AlternativePathAgent L7 in RecoveryTeam SelfHealingEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

AmazonPageNavigatorAgent = Agent(
    name="AmazonPageNavigatorAgent",
    role="Atomic navigator specifica per pagine Amazon search results L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro AmazonPageNavigatorAgent L7 in AmazonKeywordResearchTeam ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

AmazonDetailExtractorAgent = Agent(
    name="AmazonDetailExtractorAgent",
    role="Atomic extractor dettagli libro singola pagina Amazon L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="AmazonKeywordResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="AmazonKeywordResearchSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro AmazonDetailExtractorAgent L7 in AmazonKeywordResearchTeam ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

ReviewSiteNavigatorAgent = Agent(
    name="ReviewSiteNavigatorAgent",
    role="Atomic navigator per review analysis sites navigation L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro ReviewSiteNavigatorAgent L7 in ReviewAnalysisResearchTeam ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

ReviewDataCaptureAgent = Agent(
    name="ReviewDataCaptureAgent",
    role="Atomic capture review analysis data singola site L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="ReviewAnalysisResearchTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ReviewAnalysisResearchSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro ReviewDataCaptureAgent L7 in ReviewAnalysisResearchTeam ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

SaveOperationMicroAgent = Agent(
    name="SaveOperationMicroAgent",
    role="Atomic singola operazione save via Playwright save_results L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="DataPersistenceTeam",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="DataPersistenceSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro SaveOperationMicroAgent L7 in DataPersistenceTeam ResearchEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

ValidationCheckMicroAgent = Agent(
    name="ValidationCheckMicroAgent",
    role="Atomic singolo check validazione schema output phase L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro ValidationCheckMicroAgent L7 in DetectionTeam SelfHealingEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

MemoryReadMicroAgent = Agent(
    name="MemoryReadMicroAgent",
    role="Atomic singola lettura memoria via MemoryReaderAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro MemoryReadMicroAgent L7 in MemoryManagementTeam MemoryEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

MemoryWriteMicroAgent = Agent(
    name="MemoryWriteMicroAgent",
    role="Atomic singola scrittura memoria via MemoryWriterAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="MemoryManagementTeam",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="MemoryManagementSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro MemoryWriteMicroAgent L7 in MemoryManagementTeam MemoryEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

CheckpointCreateMicroAgent = Agent(
    name="CheckpointCreateMicroAgent",
    role="Atomic creazione checkpoint singolo via CheckpointManagerAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro CheckpointCreateMicroAgent L7 in CheckpointSubEcosystem MemoryEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

CheckpointRestoreMicroAgent = Agent(
    name="CheckpointRestoreMicroAgent",
    role="Atomic restore checkpoint singolo via CheckpointManagerAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="CheckpointSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="CheckpointSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro CheckpointRestoreMicroAgent L7 in CheckpointSubEcosystem MemoryEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

DecisionLogMicroAgent = Agent(
    name="DecisionLogMicroAgent",
    role="Atomic logging singola decisione via DecisionLoggerAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="DecisionLogSubEcosystem",
    ecosystem="MemoryEcosystem",
    sub_ecosystem="DecisionLogSubEcosystem",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro DecisionLogMicroAgent L7 in DecisionLogSubEcosystem MemoryEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

GraphicPromptMicroAgent = Agent(
    name="GraphicPromptMicroAgent",
    role="Atomic creazione singolo prompt grafica via PromptCreator L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="GraphicDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="GraphicDesignSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro GraphicPromptMicroAgent L7 in GraphicDesignTeam VisualEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

CoverPromptMicroAgent = Agent(
    name="CoverPromptMicroAgent",
    role="Atomic creazione singolo prompt cover L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="CoverDesignTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="CoverDesignSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro CoverPromptMicroAgent L7 in CoverDesignTeam VisualEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

VisualSaveMicroAgent = Agent(
    name="VisualSaveMicroAgent",
    role="Atomic singolo save visual via VisualPlaywrightSaveAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="VisualPlaywrightOperationsSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro VisualSaveMicroAgent L7 in VisualPlaywrightOperationsTeam VisualEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

MetricCaptureMicroAgent = Agent(
    name="MetricCaptureMicroAgent",
    role="Atomic cattura metrica singola performance per auto-improvement L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro MetricCaptureMicroAgent L7 in FeedbackCollectionTeam AutoImprovementEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

PatternCheckMicroAgent = Agent(
    name="PatternCheckMicroAgent",
    role="Atomic check pattern singolo via PatternDetectorAgent L7 Micro Agent - small single-purpose atomic task single API call single Playwright navigation single data extraction single validation check - spawned managed by higher L3-L6 auto-terminated after task",
    hierarchy_level=7,
    team="FeedbackCollectionTeam",
    ecosystem="AutoImprovementEcosystem",
    sub_ecosystem="FeedbackCollectionSub",
    inputs=['atomic_task_request', 'navigation_request_url_timeout_params', 'extraction_request_selectors_url', 'screenshot_request_url', 'error_failed_operation_retry_count', 'save_request_data_destination', 'validation_request_expected_schema', 'memory_read_write_request_category_requester'],
    outputs=['atomic_result_flag', 'navigation_result_page_loaded', 'captured_data_extraction_success', 'screenshot_ref', 'error_handling_strategy_retry_or_escalate', 'save_confirmation_saved_ref', 'validation_result_completeness_flag', 'memory_read_response_write_confirmation'],
    decision_logic="""Come micro PatternCheckMicroAgent L7 in FeedbackCollectionTeam AutoImprovementEcosystem: esegue task atomico singolo - una navigazione Playwright, una estrazione dati, uno screenshot, un check validazione, una lettura scrittura memoria atomica. Spawned on demand da L3-L6 agents (es. AmazonSearchAgent spawna PlaywrightNavigatorMicroAgent per ogni keyword), esegue via playwright_tool real operational se Playwright, reporta success/fail, auto-terminated dopo task. Per PlaywrightErrorHandlerAgent: gestisce errori Playwright timeouts blocked pages connection failures CAPTCHAs con retry adjusted params timeout increased user_agent rotated alternative selector - core self-healing Playwright. Memoria: scrive checkpoint prima/dopo.""",
    connections={"reports_to": reports_to, "manages": manages, "collaborates_with": ["MemoryManagerLeader", "MemoryReaderAgent", "CheckpointManagerAgent"]},
    memory_access={"read": reads, "write": writes},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes, rollback a ultimo checkpoint valido via CheckpointManagerAgent, escalate a controller se 3 fallimenti", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True},
    playwright_usage="atomic validation memory check",
    skill_usage=['SelfHealingSkill', 'PlaywrightNavigationSkill', 'PlaywrightDataExtractionSkill', 'PlaywrightSaveSkill', 'MemoryReadWriteSkill', 'CheckpointManagementSkill', 'AnomalyDetectionSkill'],
    level_name="L7_MICRO_AGENT"
)

ALL_L7 = [PlaywrightNavigatorMicroAgent,PlaywrightDataCaptureMicroAgent,PlaywrightScreenshotMicroAgent,PlaywrightErrorHandlerAgent,VisualPlaywrightNavigatorAgent,VisualPlaywrightCaptureAgent,ErrorDetectorAgent,StallDetectorAgent,AlternativePathAgent,AmazonPageNavigatorAgent,AmazonDetailExtractorAgent,ReviewSiteNavigatorAgent,ReviewDataCaptureAgent,SaveOperationMicroAgent,ValidationCheckMicroAgent,MemoryReadMicroAgent,MemoryWriteMicroAgent,CheckpointCreateMicroAgent,CheckpointRestoreMicroAgent,DecisionLogMicroAgent,GraphicPromptMicroAgent,CoverPromptMicroAgent,VisualSaveMicroAgent,MetricCaptureMicroAgent,PatternCheckMicroAgent]
