
import sys
sys.path.insert(0, '/home/user/workflow_architecture')
from core import Flow

PLAYWRIGHT_OPERATIONS_FLOW = Flow(
    name="PLAYWRIGHT_OPERATIONS_FLOW",
    start_condition="""Ogni volta ResearchEcosystem VisualEcosystem richiede operazioni Playwright real operational tool integration""",
    phases=[{'phase_id': 1, 'name': 'Navigation NavigatorMicroAgent AmazonPageNavigator ReviewSiteNavigator VisualNavigator real tool navigate_amazon_keyword_search navigate_review_site'}, {'phase_id': 2, 'name': 'Data Capture Extraction DataCaptureMicroAgent AmazonDetailExtractor ReviewDataCapture VisualCapture extract_data selectors title author ratings'}, {'phase_id': 3, 'name': 'Screenshot Raw Data ScreenshotMicroAgent screenshot raw_data saving'}, {'phase_id': 4, 'name': 'Save Results SaveAgent VisualSaveAgent SaveMicroAgent VisualSaveMicroAgent save_results visual_save results sources URLs notes graphics cover'}, {'phase_id': 5, 'name': 'Error Handling Self-Healing ErrorHandlerAgent handle_error retry alternative strategies timeout++ user_agent rotate max 3 escalate DetectionTeam'}],
    decision_gates=[{'gate_id': 'PW_DG1_Navigation_Success', 'logic': 'navigation result page_loaded_flag True', 'on_pass': 'Data Capture', 'on_fail': 'RetryExecutor retry via ErrorHandlerAgent adjusted params'}, {'gate_id': 'PW_DG2_Save_Success', 'logic': 'save confirmation saved_ref valid via SaveValidator', 'on_pass': 'flow complete', 'on_fail': 'retry save'}],
    rollback_points=['checkpoint_before navigation', 'last valid ResearchCheckpoint', 'SelfHealingCheckpoint before Playwright operation'],
    completion_criteria="""navigation success page loaded data captured extraction success screenshot if needed ref valid save confirmation saved_ref valid via Validator error handling retry escalate logged all saved results sources URLs notes useful material via Playwright saved confirmed""",
    involved_ecosystems=['ResearchEcosystem', 'VisualEcosystem', 'MemoryEcosystem', 'SelfHealingEcosystem', 'PlaywrightOperationsSubEcosystem'],
    sub_flows=['NavigationSubFlow', 'ExtractionSubFlow', 'SaveSubFlow']
)

print(f"Flow dedicated file PLAYWRIGHT_OPERATIONS_FLOW - phases {len(PLAYWRIGHT_OPERATIONS_FLOW.phases)} gates {len(PLAYWRIGHT_OPERATIONS_FLOW.decision_gates)}")
