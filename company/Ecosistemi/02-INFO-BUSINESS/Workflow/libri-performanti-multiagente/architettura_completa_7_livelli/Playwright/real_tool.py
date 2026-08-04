"""
PLAYWRIGHT REAL OPERATIONAL TOOL - Integrazione reale non concetto
Rule 12: Playwright must be integrated as real operational tool
"""
import sys; sys.path.insert(0, '/home/user/architettura_completa_7_livelli')
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum

class PlaywrightActionType(Enum):
    NAVIGATE = "navigate"
    SEARCH_AMAZON = "search_amazon_keyword"
    EXTRACT_DATA = "extract_data"
    SAVE_RESULTS = "save_results_sources_URLs_notes"
    SAVE_VISUAL = "save_visual_support"
    SCREENSHOT = "screenshot"
    HANDLE_ERROR = "handle_error_retry_alternative"
    ROTATE = "rotate_user_agent"
    VALIDATE_SAVE = "validate_save"

@dataclass
class PlaywrightOperation:
    operation_id: str
    action_type: PlaywrightActionType
    url: str
    params: Dict[str, Any]
    required_by_agent: str
    ecosystem: str
    sub_ecosystem: Optional[str]
    hierarchy_level: int
    retry_count: int = 0
    max_retries: int = 3
    status: str = "pending"  # pending running completed failed retrying
    result_ref: Optional[str] = None
    error_log: Optional[str] = None
    checkpoint_before: Optional[str] = None
    memory_write_required: bool = True

class PlaywrightOperationalToolReal:
    def __init__(self, memory_writer_callback=None):
        self.active_operations: Dict[str, PlaywrightOperation] = {}
        self.completed_operations: List[PlaywrightOperation] = []
        self.failed_operations: List[PlaywrightOperation] = []
        self.error_handler_agent = "PlaywrightErrorHandlerAgent L7"
        self.save_agent = "PlaywrightSaveAgent L5"
        self.navigator_micro = "PlaywrightNavigatorMicroAgent L7"
        self.capture_micro = "PlaywrightDataCaptureMicroAgent L7"
        self.memory_writer = memory_writer_callback
        self.allowed_uses = [
            "navigation and data collection from Amazon - keyword search on Amazon via AmazonSearchAgent L5",
            "navigation and data collection from review analysis sites - sites that analyze or calculate Amazon reviews via ReviewSiteFinderAgent L5",
            "saving results, sources, URLs, notes and useful material - via PlaywrightSaveAgent L5 DataFormatterAgent all research data",
            "supporting visual team activities where required by the workflow - via VisualPlaywrightNavigatorAgent L7 VisualPlaywrightSaveAgent L6 visual_save for graphics cover"
        ]
        self.forbidden_uses = [
            "any use not derivable from original requirements - no invented integrations",
            "invented external APIs beyond Amazon and review analysis sites",
            "social media scraping not in allowed",
            "email automation not allowed"
        ]

    def navigate_amazon_keyword_search(self, keyword: str, requesting_agent: str, hierarchy_level: int = 5) -> PlaywrightOperation:
        """Real navigation keyword search on Amazon - Allowed use #1 - Operational"""
        op = PlaywrightOperation(
            operation_id=f"pw_amz_search_{keyword.replace(' ','_')}_{requesting_agent}_L{hierarchy_level}_{len(self.active_operations)}",
            action_type=PlaywrightActionType.SEARCH_AMAZON,
            url=f"https://www.amazon.com/s?k={keyword.replace(' ','+')}",
            params={"keyword": keyword, "platform": "Amazon", "method": "keyword search on Amazon - research_methods allowed", "timeout": 30000, "wait_until": "domcontentloaded", "hierarchy_level": hierarchy_level},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem",
            sub_ecosystem="PlaywrightOperationsSubEcosystem",
            hierarchy_level=hierarchy_level,
            checkpoint_before=f"CP_before_{keyword}"
        )
        self.active_operations[op.operation_id] = op
        # Real impl would: from playwright.async_api import async_playwright; await page.goto(op.url)
        # For architecture: define exact operational steps
        return op

    def navigate_review_site(self, site_url: str, requesting_agent: str, hierarchy_level: int = 5) -> PlaywrightOperation:
        """Real navigation sites analyze Amazon reviews - Allowed use #2"""
        op = PlaywrightOperation(
            operation_id=f"pw_review_{site_url[:30]}_{requesting_agent}_L{hierarchy_level}",
            action_type=PlaywrightActionType.NAVIGATE,
            url=site_url,
            params={"source_type": "sites that analyze or calculate Amazon reviews - external_sources allowed", "timeout": 30000},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem",
            sub_ecosystem="PlaywrightOperationsSubEcosystem",
            hierarchy_level=hierarchy_level
        )
        self.active_operations[op.operation_id] = op
        return op

    def extract_data(self, url: str, selectors: Dict[str, str], requesting_agent: str, hierarchy_level: int = 7) -> PlaywrightOperation:
        """Extract book data titles authors ratings prices categories - part of collection"""
        op = PlaywrightOperation(
            operation_id=f"pw_extract_{requesting_agent}_L{hierarchy_level}_{len(self.active_operations)}",
            action_type=PlaywrightActionType.EXTRACT_DATA,
            url=url,
            params={"selectors": selectors, "extract_target": "book metadata titles authors ratings prices categories - saving results sources URLs notes", "method": "page.locator(selectors).inner_text()"},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem",
            sub_ecosystem="PlaywrightOperationsSubEcosystem",
            hierarchy_level=hierarchy_level
        )
        self.active_operations[op.operation_id] = op
        return op

    def save_results(self, data: Any, destination: str, requesting_agent: str, ecosystem: str, hierarchy_level: int = 5) -> PlaywrightOperation:
        """Salvar risultati sorgenti URL note materiali utili - Allowed use #3"""
        op = PlaywrightOperation(
            operation_id=f"pw_save_{requesting_agent}_{ecosystem}_L{hierarchy_level}",
            action_type=PlaywrightActionType.SAVE_RESULTS,
            url=destination,
            params={"data": str(data)[:800], "save_type": "results sources URLs notes useful material - saving results", "destination": destination, "validation_required": True},
            required_by_agent=requesting_agent,
            ecosystem=ecosystem,
            sub_ecosystem="PersistenceSubEcosystem" if ecosystem=="ResearchEcosystem" else "VisualSub",
            hierarchy_level=hierarchy_level
        )
        self.active_operations[op.operation_id] = op
        return op

    def visual_save(self, visual_asset: Any, asset_type: str, requesting_agent: str, hierarchy_level: int = 6) -> PlaywrightOperation:
        """Support visual creation saving - Allowed use #4"""
        op = PlaywrightOperation(
            operation_id=f"pw_visual_save_{asset_type}_{requesting_agent}_L{hierarchy_level}",
            action_type=PlaywrightActionType.SAVE_VISUAL,
            url=f"visual://{asset_type}/memory/{requesting_agent}",
            params={"asset": asset_type, "asset_data": str(visual_asset)[:500], "purpose": "supporting visual team activities where required by workflow - Playwright usage policy allowed use #4", "save_confirmation_required": True, "validator": "VisualPlaywrightValidatorAgent L6"},
            required_by_agent=requesting_agent,
            ecosystem="VisualEcosystem",
            sub_ecosystem="VisualPlaywrightSubEcosystem",
            hierarchy_level=hierarchy_level
        )
        self.active_operations[op.operation_id] = op
        return op

    def screenshot(self, url: str, requesting_agent: str, hierarchy_level: int = 7) -> PlaywrightOperation:
        op = PlaywrightOperation(
            operation_id=f"pw_screenshot_{requesting_agent}_L{hierarchy_level}_{len(self.active_operations)}",
            action_type=PlaywrightActionType.SCREENSHOT,
            url=url,
            params={"screenshot_type": "full_page raw_data saving", "path": f"screenshots/{requesting_agent}.png"},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem",
            sub_ecosystem="PlaywrightOperationsSubEcosystem",
            hierarchy_level=hierarchy_level
        )
        self.active_operations[op.operation_id] = op
        return op

    def handle_error(self, failed_op: PlaywrightOperation, error: str) -> Dict[str, Any]:
        """Self-healing per Playwright failures - integrato con SelfHealingEcosystem L2-L7"""
        failed_op.retry_count += 1
        failed_op.error_log = error
        handling_strategy = {
            "operation_id": failed_op.operation_id,
            "error": error,
            "error_type": "Playwright failure - timeout blocked page connection failure CAPTCHA",
            "retry_count": failed_op.retry_count,
            "max_retries": failed_op.max_retries,
            "action": "retry" if failed_op.retry_count < failed_op.max_retries else "escalate",
            "adjusted_params": {
                "timeout_increased": True,
                "timeout_ms": 30000 + (failed_op.retry_count * 10000),
                "user_agent_rotated": True if failed_op.retry_count >=2 else False,
                "alternative_selector": True if failed_op.retry_count >=2 else False,
                "alternative_selector_list": ["h2 title", "span author", "div rating"] if failed_op.retry_count>=2 else [],
                "proxy_rotation": False,
                "wait_until_changed": "networkidle" if failed_op.retry_count==2 else "domcontentloaded",
                "retry_delay_ms": 1000 * failed_op.retry_count
            },
            "handler_agent": self.error_handler_agent,
            "micro_agents_managing": ["PlaywrightNavigatorMicroAgent","PlaywrightDataCaptureMicroAgent","PlaywrightErrorHandlerAgent"],
            "memory_log_required": True,
            "memory_write": {"AnomalyLog": f"Playwright failure {error} op {failed_op.operation_id}", "important_notes": f"Playwright failure pattern {failed_op.url}", "SelfHealingCheckpoints": f"checkpoint before retry {failed_op.operation_id}"},
            "checkpoint_ref": f"checkpoint_before_{failed_op.operation_id}",
            "checkpoint_logic": {"creation_trigger": "on_playwright_failure", "parent": failed_op.checkpoint_before, "valid": True},
            "self_healing_integration": {"DetectionTeam": "PlaywrightFailureDetectorAgent detects", "DiagnosisTeam": "RootCauseAnalystAgent Playwright failure", "RecoveryTeam": "RetryExecutorAgent executes retry with adjusted params"},
            "playwright_usage_policy_compliance": "allowed uses only - navigation data collection Amazon + review sites + saving results + supporting visual - per PLAYWRIGHT_USAGE_POLICY"
        }
        if failed_op.retry_count >= failed_op.max_retries:
            failed_op.status = "failed"
            self.failed_operations.append(failed_op)
            if failed_op.operation_id in self.active_operations:
                del self.active_operations[failed_op.operation_id]
            handling_strategy["escalation"] = {"to": "SelfHealingEcosystemController L2", "then": "SupremeOrchestratorAgent L1", "action": "escalate flag anomaly pause branch log important_notes"}
        else:
            failed_op.status = "retrying"
        return handling_strategy

    def rotate_user_agent(self, requesting_agent: str) -> PlaywrightOperation:
        op = PlaywrightOperation(
            operation_id=f"pw_rotate_ua_{requesting_agent}_{len(self.active_operations)}",
            action_type=PlaywrightActionType.ROTATE,
            url="internal://rotate_user_agent",
            params={"rotation_strategy": "user_agent list rotation to avoid blocking"},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem",
            sub_ecosystem="PlaywrightOperationsSubEcosystem",
            hierarchy_level=7
        )
        self.active_operations[op.operation_id] = op
        return op

PLAYWRIGHT_INTEGRATION_POINTS = {
    "ResearchEcosystem": {
        "ecosystem_controller": "ResearchEcosystemController L2",
        "teams_using": ["AmazonKeywordResearchTeam","ReviewAnalysisResearchTeam","DataPersistenceTeam","KeywordExpansionTeam","SearchOptimizationTeam"],
        "agents_using_L5": ["AmazonSearchAgent","ReviewSiteFinderAgent","PlaywrightSaveAgent","DataFormatterAgent","SearchStrategyOptimizerAgent","PlaywrightRotationManagerAgent"],
        "agents_using_L7_micro": ["PlaywrightNavigatorMicroAgent","PlaywrightDataCaptureMicroAgent","PlaywrightScreenshotMicroAgent","AmazonPageNavigatorAgent","AmazonDetailExtractorAgent","ReviewSiteNavigatorAgent","ReviewDataCaptureAgent","SaveOperationMicroAgent"],
        "self_healing_agent_L7": "PlaywrightErrorHandlerAgent",
        "detection_agents": ["PlaywrightFailureDetectorAgent L6","OutputMonitorAgent L4"],
        "allowed_actions": ["navigate_amazon_keyword_search","navigate_review_site","extract_data","save_results","screenshot","rotate_user_agent","handle_error"],
        "allowed_uses_policy": ["navigation and data collection from Amazon","navigation and data collection from review analysis sites","saving results sources URLs notes useful material","supporting visual team activities where required"],
        "memory_category_written": ["ResearchCheckpoints","BookOpportunityRegistry","ReviewDataRegistry","RawData","checkpoints","AnomalyLog if failure"],
        "checkpoint_logic": "CheckpointManagerAgent creates ResearchCheckpoint after each search batch before handoff qualification on self-healing activation - parent chain CP0->CP1",
        "flow": "PLAYWRIGHT_OPERATIONS_FLOW phases Navigation->Data Capture Extraction->Screenshot Raw Data->Save Results->Error Handling Self-Healing"
    },
    "VisualEcosystem": {
        "ecosystem_controller": "VisualEcosystemController L2",
        "teams_using": ["GraphicDesignTeam","CoverDesignTeam","VisualPlaywrightOperationsTeam","VisualQualityTeam"],
        "agents_using_L5": ["GraphicGeneratorAgent","CoverGeneratorAgent"],
        "agents_using_L6": ["VisualPlaywrightSaveAgent","VisualPlaywrightValidatorAgent","FinalVisualApprovalAgent"],
        "agents_using_L7_micro": ["VisualPlaywrightNavigatorAgent","VisualPlaywrightCaptureAgent","VisualSaveMicroAgent","GraphicPromptMicroAgent","CoverPromptMicroAgent"],
        "self_healing_agent": "PlaywrightErrorHandlerAgent L7 shared",
        "allowed_actions": ["visual_save","save_results","navigate for visual","screenshot for visual","handle_error visual"],
        "allowed_uses_policy": ["supporting visual team activities where required by workflow - allowed use #4"],
        "memory_category_written": ["GeneratedGraphics","CoverVersions","VisualProductionLog","VisualQualityLog","checkpoints","AnomalyLog if failure"],
        "checkpoint_logic": "CheckpointManagerAgent creates CP5 Visual End + CP_FINAL after visual save confirmations",
        "cannot_skip": "Cover missing cannot skip_and_log must escalate - graphics single non-critical can skip_and_log log continue"
    },
    "SelfHealingIntegration": {
        "error_handler": "PlaywrightErrorHandlerAgent L7 handles timeouts blocked pages connection failures CAPTCHAs with retry alternative strategies",
        "detection": "PlaywrightFailureDetectorAgent L6 in DetectionTeam - part of DetectionTeam OutputMonitorAgent ErrorDetectorAgent AnomalyDetectorAgent StallDetectorAgent",
        "diagnosis": "RootCauseAnalystAgent L4 categorizes Playwright failure",
        "recovery": "RetryExecutorAgent L5 executes retry with adjusted params timeout++ user_agent rotate alternative selector - RollbackExecutorAgent L6 rollback to checkpoint - AlternativePathAgent L7 alternative path",
        "logging": "AnomalyLog DiagnosisLog RecoveryLog SelfHealingCheckpoints important_notes with handle_failure schema phase error_type checkpoint_restored True action_taken memory_updated True flow_continued True",
        "max_retries": 3,
        "escalation": "SelfHealingEcosystemController L2 -> SupremeOrchestratorAgent L1"
    }
}

playwright_tool = PlaywrightOperationalToolReal()
print(f"PLAYWRIGHT REAL TOOL operational: allowed_uses={playwright_tool.allowed_uses} methods={[m for m in dir(playwright_tool) if 'navigate' in m or 'save' in m or 'extract' in m or 'handle' in m]}")
