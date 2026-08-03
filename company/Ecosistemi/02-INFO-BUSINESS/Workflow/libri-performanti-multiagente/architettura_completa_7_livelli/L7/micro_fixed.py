import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from core import Agent


PlaywrightNavigatorMicroAgent = Agent(
    name="PlaywrightNavigatorMicroAgent",
    role="Micro singola navigazione pagina via Playwright tool atomic",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="NavigationSub" if "NavigationSub" != "None" else None,
    inputs=["navigation_request", "url", "timeout_params"],
    outputs=["navigation_result"],
    decision_logic="""Atomic task single Playwright navigation Execute playwright_tool.navigate_amazon_keyword_search or navigate_review_site Report success fail Spawned AmazonSearchAgent auto-terminated""",
    connections={"reports_to": ["PlaywrightOperationsSubEcosystem", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

PlaywrightDataCaptureMicroAgent = Agent(
    name="PlaywrightDataCaptureMicroAgent",
    role="Micro cattura dati specifici pagine via Playwright",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="ExtractionSub" if "ExtractionSub" != "None" else None,
    inputs=["extraction_request", "selectors", "url"],
    outputs=["captured_data"],
    decision_logic="""Atomic task single data extraction using selectors Execute playwright_tool.extract_data Spawned DataExtractor agents""",
    connections={"reports_to": ["PlaywrightOperationsSubEcosystem", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

PlaywrightErrorHandlerAgent = Agent(
    name="PlaywrightErrorHandlerAgent",
    role="Gestisce errori Playwright-specific timeouts blocked CAPTCHAs retry alternative core self-healing Playwright",
    hierarchy_level=7,
    team="PlaywrightOperationsSubEcosystem",
    ecosystem="ResearchEcosystem",
    sub_ecosystem="NavigationSub" if "NavigationSub" != "None" else None,
    inputs=["playwright_error", "failed_operation", "retry_count"],
    outputs=["error_handling_strategy"],
    decision_logic="""Handle Playwright errors timeouts blocked pages connection failures CAPTCHAs Strategy retry adjusted params timeout++ user_agent rotate alternative selector Use playwright_tool.handle_error Max 3 retries then escalate Logs AnomalyLog""",
    connections={"reports_to": ["PlaywrightOperationsSubEcosystem", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

VisualPlaywrightNavigatorAgent = Agent(
    name="VisualPlaywrightNavigatorAgent",
    role="Gestisce navigazione Playwright visual tasks",
    hierarchy_level=7,
    team="VisualPlaywrightOperationsTeam",
    ecosystem="VisualEcosystem",
    sub_ecosystem="PlaywrightSub" if "PlaywrightSub" != "None" else None,
    inputs=["visual_navigation_request"],
    outputs=["visual_navigation_result"],
    decision_logic="""Atomic navigation visual team support tasks save via Playwright support usage""",
    connections={"reports_to": ["VisualPlaywrightOperationsLeader", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

ErrorDetectorAgent = Agent(
    name="ErrorDetectorAgent",
    role="Rileva errori eccezioni fallimenti processi",
    hierarchy_level=7,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub" if "DetectionSub" != "None" else None,
    inputs=["process_logs", "exception_feed"],
    outputs=["error_detected_report"],
    decision_logic="""Atomic detection scan logs errors exceptions failures Part DetectionTeam""",
    connections={"reports_to": ["DetectionLeader", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

StallDetectorAgent = Agent(
    name="StallDetectorAgent",
    role="Rileva processi stalled frozen",
    hierarchy_level=7,
    team="DetectionTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="DetectionSub" if "DetectionSub" != "None" else None,
    inputs=["process_heartbeat_feed", "phase_timeout_thresholds"],
    outputs=["stall_detected_report"],
    decision_logic="""Detect stalled processes no heartbeat phase timeout exceeded Trigger recovery Spawned continuously""",
    connections={"reports_to": ["DetectionLeader", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

AlternativePathAgent = Agent(
    name="AlternativePathAgent",
    role="Trova esegue percorsi alternativi quando retry rollback fail",
    hierarchy_level=7,
    team="RecoveryTeam",
    ecosystem="SelfHealingEcosystem",
    sub_ecosystem="RecoverySub" if "RecoverySub" != "None" else None,
    inputs=["failed_recovery_attempts", "workflow_state"],
    outputs=["alternative_path_execution"],
    decision_logic="""Find alternative path different keyword strategy skip_and_log non-critical graphic requalify send item back qualification anomaly flag Execute alternative Real recovery agent""",
    connections={"reports_to": ["RecoveryLeader", "PlaywrightErrorHandlerAgent"], "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]},
    memory_access={"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]},
    self_healing_behavior={"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback ultimo checkpoint valido escalate controller se 3 fallimenti", "max_retries": 3},
    playwright_usage=None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill"],
    level_name="L7"
)

ALL_L7 = [PlaywrightNavigatorMicroAgent,PlaywrightDataCaptureMicroAgent,PlaywrightErrorHandlerAgent,VisualPlaywrightNavigatorAgent,ErrorDetectorAgent,StallDetectorAgent,AlternativePathAgent]
print("Fixed file validated")
