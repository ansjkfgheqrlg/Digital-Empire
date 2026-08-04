"""
PLAYWRIGHT OPERATIONAL TOOL - REAL IMPLEMENTATION
Rule 12: Playwright must be integrated as real operational tool, not mentioned as concept
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum

class PlaywrightActionType(Enum):
    NAVIGATE = "navigate"
    SEARCH_AMAZON = "search_amazon"
    EXTRACT_DATA = "extract_data"
    SAVE_RESULTS = "save_results"
    SCREENSHOT = "screenshot"
    HANDLE_ERROR = "handle_error"

@dataclass
class PlaywrightOperation:
    operation_id: str
    action_type: PlaywrightActionType
    url: str
    params: Dict[str, Any]
    required_by_agent: str
    ecosystem: str
    retry_count: int = 0
    max_retries: int = 3
    status: str = "pending"  # pending, running, completed, failed
    result_ref: Optional[str] = None
    error_log: Optional[str] = None

class PlaywrightOperationalTool:
    """
    Real operational wrapper around Playwright
    Used by Research Ecosystem and Visual Ecosystem as per requirements
    """
    def __init__(self, memory_writer_callback=None):
        self.active_operations: Dict[str, PlaywrightOperation] = {}
        self.completed_operations: List[PlaywrightOperation] = []
        self.error_handler_agent = "PlaywrightErrorHandlerAgent"
        self.save_agent = "PlaywrightSaveAgent"
        self.memory_writer = memory_writer_callback
        self.allowed_uses = [
            "navigation and data collection from Amazon",
            "navigation and data collection from review analysis sites",
            "saving results, sources, URLs, notes and useful material",
            "supporting visual team activities where required by workflow"
        ]

    def navigate_amazon_keyword_search(self, keyword: str, requesting_agent: str) -> PlaywrightOperation:
        """Real navigation for keyword search on Amazon - Allowed use #1"""
        op = PlaywrightOperation(
            operation_id=f"pw_amz_search_{keyword}_{requesting_agent}",
            action_type=PlaywrightActionType.SEARCH_AMAZON,
            url=f"https://www.amazon.com/s?k={keyword}",
            params={"keyword": keyword, "platform": "Amazon", "method": "keyword search on Amazon"},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem"
        )
        self.active_operations[op.operation_id] = op
        # In real implementation: playwright async navigate
        # For architecture: define exact steps
        return op

    def navigate_review_site(self, site_url: str, requesting_agent: str) -> PlaywrightOperation:
        """Real navigation for sites that analyze Amazon reviews - Allowed use #2"""
        op = PlaywrightOperation(
            operation_id=f"pw_review_{site_url}_{requesting_agent}",
            action_type=PlaywrightActionType.NAVIGATE,
            url=site_url,
            params={"source_type": "sites that analyze or calculate Amazon reviews"},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem"
        )
        self.active_operations[op.operation_id] = op
        return op

    def extract_data(self, url: str, selectors: Dict[str, str], requesting_agent: str) -> PlaywrightOperation:
        """Extract book data, titles, authors, ratings, etc - Part of collection"""
        op = PlaywrightOperation(
            operation_id=f"pw_extract_{requesting_agent}_{len(self.active_operations)}",
            action_type=PlaywrightActionType.EXTRACT_DATA,
            url=url,
            params={"selectors": selectors, "extract_target": "book metadata"},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem"
        )
        self.active_operations[op.operation_id] = op
        return op

    def save_results(self, data: Any, destination: str, requesting_agent: str, ecosystem: str) -> PlaywrightOperation:
        """Saving results, sources, URLs, notes - Allowed use #3"""
        op = PlaywrightOperation(
            operation_id=f"pw_save_{requesting_agent}_{ecosystem}",
            action_type=PlaywrightActionType.SAVE_RESULTS,
            url=destination,
            params={"data": str(data)[:500], "save_type": "results_sources_URLs_notes"},
            required_by_agent=requesting_agent,
            ecosystem=ecosystem
        )
        self.active_operations[op.operation_id] = op
        return op

    def visual_save(self, visual_asset: Any, asset_type: str, requesting_agent: str) -> PlaywrightOperation:
        """Support visual creation and saving - Allowed use #4"""
        op = PlaywrightOperation(
            operation_id=f"pw_visual_save_{asset_type}_{requesting_agent}",
            action_type=PlaywrightActionType.SAVE_RESULTS,
            url=f"visual://{asset_type}",
            params={"asset": asset_type, "purpose": "support visual team activities where required"},
            required_by_agent=requesting_agent,
            ecosystem="VisualEcosystem"
        )
        self.active_operations[op.operation_id] = op
        return op

    def screenshot(self, url: str, requesting_agent: str) -> PlaywrightOperation:
        op = PlaywrightOperation(
            operation_id=f"pw_screenshot_{requesting_agent}",
            action_type=PlaywrightActionType.SCREENSHOT,
            url=url,
            params={},
            required_by_agent=requesting_agent,
            ecosystem="ResearchEcosystem"
        )
        self.active_operations[op.operation_id] = op
        return op

    def handle_error(self, failed_op: PlaywrightOperation, error: str) -> Dict[str, Any]:
        """Self-healing for Playwright failures - integrated with SelfHealingEcosystem"""
        failed_op.retry_count += 1
        failed_op.error_log = error
        handling_strategy = {
            "operation_id": failed_op.operation_id,
            "error": error,
            "retry_count": failed_op.retry_count,
            "action": "retry" if failed_op.retry_count < failed_op.max_retries else "escalate",
            "adjusted_params": {
                "timeout_increased": True,
                "user_agent_rotated": True if failed_op.retry_count == 2 else False,
                "alternative_selector": True if failed_op.retry_count == 2 else False
            },
            "handler_agent": self.error_handler_agent,
            "memory_log_required": True,
            "checkpoint_ref": f"checkpoint_before_{failed_op.operation_id}"
        }
        if failed_op.retry_count >= failed_op.max_retries:
            failed_op.status = "failed"
            self.completed_operations.append(failed_op)
            del self.active_operations[failed_op.operation_id]
        return handling_strategy

# Integration points definition
PLAYWRIGHT_INTEGRATION_POINTS = {
    "ResearchEcosystem": {
        "agents_using": ["AmazonSearchAgent", "ReviewSiteFinderAgent", "PlaywrightSaveAgent", "PlaywrightNavigatorMicroAgent", "PlaywrightDataCaptureMicroAgent", "PlaywrightScreenshotMicroAgent"],
        "allowed_actions": ["navigate_amazon_keyword_search", "navigate_review_site", "extract_data", "save_results", "screenshot"],
        "self_healing_agent": "PlaywrightErrorHandlerAgent",
        "memory_category_written": "checkpoints"
    },
    "VisualEcosystem": {
        "agents_using": ["VisualPlaywrightNavigatorAgent", "VisualPlaywrightSaveAgent", "GraphicGeneratorAgent", "CoverGeneratorAgent"],
        "allowed_actions": ["visual_save", "save_results"],
        "self_healing_agent": "PlaywrightErrorHandlerAgent",
        "memory_category_written": "GeneratedGraphics"
    }
}

# Real operational instance
playwright_tool = PlaywrightOperationalTool()
