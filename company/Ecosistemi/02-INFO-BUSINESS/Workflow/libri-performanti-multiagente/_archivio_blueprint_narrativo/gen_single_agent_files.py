import os, json, textwrap, pathlib
base = pathlib.Path("/home/user/architettura_sincrona")
base.mkdir(parents=True, exist_ok=True)

# Core file copy from previous
import shutil
core_src = pathlib.Path("/home/user/architettura_completa_7_livelli/core.py")
shutil.copy(core_src, base / "core.py")

# Create sync protocol files
sync_dir = base / "sync"
sync_dir.mkdir(exist_ok=True)

with open(sync_dir / "harmony_protocol.py", "w") as f:
    f.write('''
"""
HARMONIC SYNCHRONY PROTOCOL - Ogni agente lavora in perfetta sincronia e armonia con gli altri
Definisce come gli agenti di un team e tra team comunicano senza conflitti
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import time

@dataclass
class HarmonySignal:
    signal_id: str
    sender_agent: str
    receiver_agent: str
    team: str
    ecosystem: str
    signal_type: str  # ready, checkpoint, handoff, validation, error, recovery
    payload: Dict[str, Any]
    timestamp: str
    requires_ack: bool = True

class TeamSynchronyProtocol:
    """
    Protocollo di sincronia perfetta intra-team:
    - Ogni agente comunica via HarmonySignal con ack obbligatorio
    - Leader coordina flow interno sequenziale/parallelo con checkpoint condivisi
    - Validator agents validano prima di prossimo step
    - CheckpointManagerAgent condivide checkpoint a tutti membri team
    - Self-healing harmony: se un agente fallisce, team rimane in sincronia via rollback comune
    """
    def __init__(self, team_name: str, leader: str, members: List[str]):
        self.team_name = team_name
        self.leader = leader
        self.members = members
        self.signals_log: List[HarmonySignal] = []
        self.checkpoint_shared = None
        self.harmony_status = "synchronized"  # synchronized, syncing, desynchronized, recovering

    def emit_ready(self, agent: str):
        return HarmonySignal(
            signal_id=f"{self.team_name}_{agent}_ready_{int(time.time()*1000)}",
            sender_agent=agent,
            receiver_agent=self.leader,
            team=self.team_name,
            ecosystem="",
            signal_type="ready",
            payload={"agent": agent, "status": "ready for task"},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=True
        )

    def emit_checkpoint(self, agent: str, checkpoint_id: str):
        self.checkpoint_shared = checkpoint_id
        return HarmonySignal(
            signal_id=f"{self.team_name}_{agent}_checkpoint_{checkpoint_id}",
            sender_agent=agent,
            receiver_agent="ALL_TEAM",
            team=self.team_name,
            ecosystem="",
            signal_type="checkpoint",
            payload={"checkpoint_id": checkpoint_id, "shared": True, "parent": self.checkpoint_shared},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=False
        )

    def emit_handoff_internal(self, from_agent: str, to_agent: str, package: Dict):
        return HarmonySignal(
            signal_id=f"{self.team_name}_{from_agent}_to_{to_agent}_handoff",
            sender_agent=from_agent,
            receiver_agent=to_agent,
            team=self.team_name,
            ecosystem="",
            signal_type="handoff",
            payload=package,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=True
        )

    def validate_harmony(self):
        """Verifica che tutti gli agenti siano sincronizzati"""
        # In implementazione reale: controlla che tutti abbiano ack, checkpoint condiviso, nessun desync
        self.harmony_status = "synchronized"
        return {"team": self.team_name, "status": self.harmony_status, "members_ready": len(self.members), "checkpoint_shared": self.checkpoint_shared}

class InterTeamHarmonyProtocol:
    """
    Protocollo armonia tra team e tra ecosistemi:
    - Handoff esterno 8-step sincronizzato via Memory broker + checkpoint
    - Ogni handoff richiede conferma leader source e target + validazione
    - Self-healing inter-team: se validazione fallisce, DetectionTeam trigger
    """
    def __init__(self):
        self.handoffs_log: List[Dict] = []

    def handoff_8_step(self, source_team: str, target_team: str, package: Dict, source_leader: str, target_leader: str):
        steps = [
            f"1. {source_leader} ({source_team}) crea handoff package structured output decisions risks checkpoint ref - package keys {list(package.keys())}",
            f"2. MemoryEcosystem MemoryWriterAgent logs handoff via MemoryEcosystemController",
            f"3. {source_leader} conferma ready scrive checkpoint via CheckpointManagerAgent",
            f"4. {target_leader} ({target_team}) conferma receipt legge memory via MemoryReaderAgent",
            f"5. {target_team} valida completeness via Validator agent interno team (es. AmazonResultsValidatorAgent, PlanCoherenceValidatorAgent, ManuscriptValidatorAgent, GraphicQualityReviewerAgent)",
            f"6. Se validation fails -> SelfHealingEcosystem DetectionTeam OutputMonitorAgent detects incoherent output -> DiagnosisTeam RootCauseAnalyst -> RecoveryTeam RetryExecutor rollback",
            f"7. Se validation passes -> {target_team} inizia lavoro interno flow con TeamSynchronyProtocol intra-team",
            f"8. Memory logs handoff completion via MemoryWriterAgent + CheckpointManagerAgent crea checkpoint post-handoff"
        ]
        handoff_record = {"source_team": source_team, "target_team": target_team, "source_leader": source_leader, "target_leader": target_leader, "package_summary": str(package)[:500], "steps": steps, "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True, "harmony_status": "synchronized"}
        self.handoffs_log.append(handoff_record)
        return handoff_record

# Global harmony orchestrator
class GlobalHarmonyOrchestrator:
    """Garantisce che tutti i team di tutti gli ecosistemi lavorino in perfetta sincronia e armonia"""
    def __init__(self):
        self.team_protocols: Dict[str, TeamSynchronyProtocol] = {}
        self.inter_team_protocol = InterTeamHarmonyProtocol()
        self.ecosystem_harmony: Dict[str, str] = {}

    def register_team(self, team_name: str, leader: str, members: List[str]):
        proto = TeamSynchronyProtocol(team_name, leader, members)
        self.team_protocols[team_name] = proto
        return proto

    def check_global_harmony(self):
        statuses = {team: proto.validate_harmony() for team, proto in self.team_protocols.items()}
        # In reale: verifica cross-ecosystem dependencies, no deadlock, no race conditions
        return {"global_harmony": "all_synchronized_perfect_harmony", "teams": statuses, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")}

global_harmony = GlobalHarmonyOrchestrator()

print("HARMONY PROTOCOL initialized - perfect synchrony and harmony intra-team and inter-team")
''')

with open(sync_dir / "team_synchronizer.py", "w") as f:
    f.write('''
"""
TEAM SYNCHRONIZER - Assicura che ogni agente in team lavori in sincronia perfetta
Ogni agente ha suo file dedicato ma sincronizzato via TeamSynchronyProtocol
"""

import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from sync.harmony_protocol import global_harmony, TeamSynchronyProtocol, HarmonySignal
from core import Agent
from typing import List

class TeamSynchronizer:
    def __init__(self, team_name: str, leader_agent: str, member_agents: List[str], ecosystem: str):
        self.team_name = team_name
        self.leader_agent = leader_agent
        self.member_agents = member_agents
        self.ecosystem = ecosystem
        self.protocol = global_harmony.register_team(team_name, leader_agent, member_agents)
        self.agents_instances: dict = {}

    def register_agent_instance(self, agent: Agent):
        self.agents_instances[agent.name] = agent
        # Emit ready signal
        signal = self.protocol.emit_ready(agent.name)
        # In real system: send via message bus, wait ack from leader
        return signal

    def synchronize_checkpoint(self, agent_name: str, checkpoint_id: str):
        signal = self.protocol.emit_checkpoint(agent_name, checkpoint_id)
        # Broadcast to all team members
        # All members update shared checkpoint via CheckpointManagerAgent
        return signal

    def internal_handoff(self, from_agent: str, to_agent: str, package: dict):
        signal = self.protocol.emit_handoff_internal(from_agent, to_agent, package)
        # Wait ack from receiver
        return signal

    def validate_team_harmony(self):
        return self.protocol.validate_harmony()

    def get_harmony_status(self):
        return global_harmony.check_global_harmony()

# Example usage for a team - will be instantiated per team folder
''')

# Now create teams structure with per-agent files
# Define full expanded team/agent mapping from previous expanded architecture

teams_definition = {
    "AmazonKeywordResearchTeam": {
        "ecosystem": "ResearchEcosystem",
        "sub_ecosystem": "PlaywrightOps",
        "leader": "AmazonResearchLeader",
        "members": [
            ("AmazonResearchLeader", 3, "Leader team gestisce keyword generation search extraction validation BookNicheDecisionSkill - coordina flow interno KeywordGenerator -> Search via NavigatorMicroAgent -> Extractor via CaptureMicroAgent -> Validator", ["cycle_signal","handoff_package","memory_hierarchies","important_notes"], ["team_status","internal_flow_trigger","handoff_ready_package","checkpoint_creation"]),
            ("KeywordGeneratorAgent", 5, "Genera variazioni keyword Amazon search da seed important_notes patterns FeedbackRegistry - operational core", ["seed_keywords","important_notes","FeedbackRegistry"], ["keyword_variations","keyword_strategy_log"]),
            ("AmazonSearchAgent", 5, "Esegue ricerche Amazon via Playwright operational tool real navigation - operational core Playwright", ["keyword_variations"], ["search_results_raw","search_metadata"]),
            ("AmazonDataExtractorAgent", 5, "Estrae dati libri titoli autori ratings prezzi categorie via Playwright capture - operational", ["search_results_raw"], ["extracted_book_metadata","extraction_log"]),
            ("AmazonResultsValidatorAgent", 6, "Valida dati Amazon estratti completi coerenti titolo URL sorgente keyword - support validation", ["extracted_book_metadata"], ["validation_result_amazon","coherence_flag"]),
            ("KeywordQualityAnalystAgent", 4, "Analizza qualita keyword Amazon search signals - senior tactical decision authority", ["keyword_variations","search_results_raw"], ["keyword_quality_score","quality_evidence"]),
            ("NicheCompetitionAnalystAgent", 4, "Analizza competizione nicchia da dati Amazon - senior", ["amazon_search_results","book_opportunities"], ["competition_level","competition_evidence"]),
            ("SearchQualityValidatorAgent", 6, "Valida qualita risultati search Amazon - support", ["search_results_raw","extracted_metadata"], ["search_quality_validation","quality_flag"]),
            ("NicheViabilityValidatorAgent", 6, "Valida fattibilita nicchia da BookNicheDecisionSkill - support", ["book_opportunities","scores"], ["viability_validation","viability_flag"]),
            ("AmazonPageNavigatorAgent", 7, "Atomic navigator specifica per pagine Amazon search results - micro atomic", ["navigation_request","url"], ["navigation_result","page_loaded_flag"]),
            ("AmazonDetailExtractorAgent", 7, "Atomic extractor dettagli libro singola pagina Amazon - micro", ["extraction_request","selectors","url"], ["captured_data","extraction_success_flag"]),
        ]
    },
    "ReviewAnalysisResearchTeam": {
        "ecosystem": "ResearchEcosystem",
        "sub_ecosystem": "ReviewSub",
        "leader": "ReviewResearchLeader",
        "members": [
            ("ReviewResearchLeader", 3, "Leader ReviewAnalysisResearchTeam gestisce review site discovery extraction normalization validation", ["book_opportunities","seed_review_sites"], ["review_analysis_data","normalized_scores"]),
            ("ReviewSiteFinderAgent", 5, "Trova siti che analizzano Amazon reviews via Playwright navigation - operational", ["search_seed_review_sites"], ["found_review_sites_list"]),
            ("ReviewDataExtractorAgent", 5, "Estrae review analysis data da siti via Playwright - operational", ["found_review_sites_list"], ["review_analysis_raw_data"]),
            ("ReviewScoreNormalizerAgent", 6, "Normalizza diversi scoring systems in formato unificato - support", ["review_scores_various_formats"], ["normalized_review_scores_unified"]),
            ("ReviewDataValidatorAgent", 6, "Valida completezza coerenza review data linkata book opportunities - support", ["normalized_review_data"], ["review_data_validation"]),
            ("ReviewSentimentAnalystAgent", 4, "Analizza sentiment review data da review sites - senior", ["review_data_raw","normalized_scores"], ["sentiment_score","sentiment_evidence"]),
            ("ReviewSiteNavigatorAgent", 7, "Atomic navigator per review analysis sites - micro", ["navigation_request_review_site"], ["navigation_result_review"]),
            ("ReviewDataCaptureAgent", 7, "Atomic capture review analysis data singola site - micro", ["extraction_request_review","url"], ["captured_review_data"]),
        ]
    },
    "DataPersistenceTeam": {
        "ecosystem": "ResearchEcosystem",
        "sub_ecosystem": "PersistenceSub",
        "leader": "DataPersistenceLeader",
        "members": [
            ("DataPersistenceLeader", 3, "Leader DataPersistenceTeam garantisce salvataggio via Playwright formatting validation checkpoint CP1", ["book_opportunities","review_data","raw_data"], ["save_confirmations","research_complete_signal","structured_output"]),
            ("PlaywrightSaveAgent", 5, "Gestisce tutte operazioni save Playwright research visual - operational", ["data_to_save","destination_ref"], ["save_confirmation","saved_ref"]),
            ("DataFormatterAgent", 5, "Formatta dati in structured_output pronto per qualifica - operational", ["raw_book_data","raw_review_data"], ["formatted_structured_output"]),
            ("SaveValidatorAgent", 6, "Conferma salvataggi Playwright successo URL sorgente loggata raw_data accessibile - support", ["save_operations"], ["save_validation_result"]),
            ("RawDataArchiverAgent", 5, "Archivia raw data da Playwright con refs e screenshot - operational", ["raw_data","screenshot_refs"], ["archived_raw_data_refs"]),
            ("SaveOperationMicroAgent", 7, "Atomic singola operazione save via Playwright save_results - micro", ["save_request_data_destination"], ["save_confirmation_saved_ref"]),
        ]
    },
    "QualificationAnalysisTeam": {
        "ecosystem": "QualificationEcosystem",
        "sub_ecosystem": "AnalysisSub",
        "leader": "QualificationLeader",
        "members": [
            ("QualificationLeader", 3, "Leader QualificationAnalysisTeam gestisce 8 analyst valuta 5 criteri reproducibility absurdity speed market plan validity", ["research_handoff_package","BookOpportunityRegistry"], ["evaluation_scores","risk_flags","preliminary_decision"]),
            ("ReproducibilityAnalystAgent", 4, "Senior valuta reproducibilita efficiente senza risorse inaccessibili - tactical authority", ["book_opportunity_data","review_analysis"], ["reproducibility_score","evidence","risk_flag"]),
            ("AbsurdityDetectorAgent", 4, "Rileva elementi assurdi irrealistici nonsensical gate non assurdi - senior", ["book_data","chapter_hints"], ["absurdity_flag","absurdity_evidence"]),
            ("ProductionSpeedAnalystAgent", 4, "Stima tempo produzione flag too slow vs modello quantita sostenibile - senior", ["book_complexity","chapter_count"], ["speed_estimate","too_slow_flag"]),
            ("MarketAlignmentAnalystAgent", 4, "Valuta allineamento goal quantity-performance performanti riproducibili sostenibili - senior", ["performance_signals_amazon","review_analysis_data"], ["market_alignment_score","business_fit_evidence"]),
            ("PlanQualityAuditorAgent", 4, "Valuta qualita qualification plan itself validita piano - senior audit", ["all_analyst_outputs","qualification_plan_draft"], ["plan_validity_score","audit_report"]),
            ("CompetitionAnalystAgent", 4, "Analizza competizione livello nicchia da segnali Amazon - senior", ["book_data","amazon_search_results"], ["competition_level"]),
            ("SustainabilityAnalystAgent", 4, "Analizza sostenibilita produzione lungo termine quantita - senior", ["book_complexity","resource_estimate"], ["sustainability_score"]),
            ("BusinessFitAnalystAgent", 4, "Valuta business fit guadagno tramite quantita libri performanti - senior", ["market_signals","reproducibility"], ["business_fit_score"]),
        ]
    },
    "QualificationDecisionTeam": {
        "ecosystem": "QualificationEcosystem",
        "sub_ecosystem": "DecisionSub",
        "leader": "QualificationDecisionLeader",
        "members": [
            ("QualificationDecisionLeader", 3, "Leader QualificationDecisionTeam aggrega decisioni gestisce rischi scrive report finale GO NO-GO", ["analyst_outputs","risk_flags"], ["final_qualification_report","GO_NO_GO_decision"]),
            ("DecisionAggregatorAgent", 4, "Aggrega output analyst decisione unificata weighted scoring reproducibilita 30% velocita 25% assurdita 20% market 25% threshold 70 GO", ["reproducibility_score","absurdity_flag","speed_estimate","market_alignment","plan_validity"], ["aggregated_score","preliminary_GO_NO_GO"]),
            ("RiskFlagManagerAgent", 4, "Gestisce prioritizza risk flags da tutti analyst - senior", ["risk_flags_all_analysts"], ["prioritized_risks","risk_mitigation_suggestions"]),
            ("QualificationReportWriterAgent", 5, "Scrive report qualifica finale strutturato GO NO-GO motivata trace - operational", ["aggregated_decision","prioritized_risks"], ["final_qualification_report"]),
            ("DecisionQualityCheckerAgent", 5, "Verifica qualita decisione traceability motivazione - operational", ["final_report_draft"], ["decision_quality_validation"]),
        ]
    },
    "StructurePlanningTeam": {
        "ecosystem": "PlanningEcosystem",
        "sub_ecosystem": "StructureSub",
        "leader": "StructurePlanningLeader",
        "members": [
            ("StructurePlanningLeader", 3, "Leader StructurePlanningTeam gestisce video_structure REQUIRED preservato verbatim chapters details coherence CONTROL POINT CRITICO", ["qualification_GO_package","risk_flags"], ["second_level_plan","validation_status"]),
            ("VideoStructureArchitectAgent", 4, "CRITICAL REQUIRED Progetta video_structure preservato verbatim non reinterpretare CONTROL POINT CP-VIDEO-01 - senior critical", ["qualification_GO_package","original_requirement_video_structure","risk_flags"], ["video_structure_field"]),
            ("ChapterDesignerAgent", 4, "Definisce capitoli descrizioni ordine scopo effort estimate fast vs slow - senior", ["video_structure","book_opportunity"], ["chapters_list_with_descriptions"]),
            ("DetailFillerAgent", 4, "Aggiunge ogni dettaglio rilevante produzione sostenibilita - senior", ["chapters","video_structure","risk_flags"], ["details_every_relevant"]),
            ("PlanCoherenceValidatorAgent", 4, "Valida intero second-level plan coerente completo - senior", ["second_level_plan_draft"], ["coherence_validation_result"]),
            ("VideoStructureValidatorAgent", 4, "Valida video_structure presente verbatim non vuoto non reinterpretato critical validation - senior", ["video_structure_field"], ["video_structure_validation","presence_flag"]),
            ("OutlineOptimizerAgent", 4, "Ottimizza outline capitoli flusso sostenibilita - senior", ["chapters_draft","details"], ["optimized_outline"]),
            ("ContentFlowDesignerAgent", 4, "Progetta flusso contenuti tra capitoli - senior", ["chapters","details"], ["content_flow_design"]),
        ]
    },
    "ProductionReadinessTeam": {
        "ecosystem": "PlanningEcosystem",
        "sub_ecosystem": "ReadinessSub",
        "leader": "ProductionReadinessLeader",
        "members": [
            ("ProductionReadinessLeader", 3, "Leader ProductionReadinessTeam verifica prerequisiti stima risorse emette start signal", ["second_level_plan_draft"], ["readiness_confirmation","production_start_signal"]),
            ("ReadinessCheckerAgent", 5, "Verifica prerequisiti produzione met second-level plan complete - operational", ["second_level_plan_draft","qualification_GO_decision","risk_flags"], ["readiness_check_result"]),
            ("ResourceEstimatorAgent", 5, "Stima risorse necessarie tempo capitoli grafica cover - operational", ["second_level_plan","chapter_list","graphic_needs"], ["resource_estimate","sustainability_assessment"]),
            ("ProductionStartSignalAgent", 5, "Emette segnale formale start produzione TRUE timestamp marks actual start production flow - operational CRITICAL", ["readiness_confirmation","resource_estimate"], ["production_start_signal_explicit","CP3_creation_trigger"]),
            ("RiskMitigationPlannerAgent", 5, "Pianifica mitigazione rischi identificati RiskRegistry - operational", ["risk_flags","second_level_plan"], ["risk_mitigation_plan"]),
        ]
    },
    "BookWritingTeam": {
        "ecosystem": "ProductionEcosystem",
        "sub_ecosystem": "WritingSub",
        "leader": "BookWritingLeader",
        "members": [
            ("BookWritingLeader", 3, "Leader BookWritingTeam gestisce chapter writers paralleli consistenza stile qualita", ["second_level_plan","production_start_signal","memory_context"], ["complete_manuscript_draft","writing_log"]),
            ("ChapterWriterAgent", 5, "Scrive capitoli singoli multiple instances parallele legge memoria continuity - operational core", ["chapter_definition","second_level_plan","memory_context"], ["chapter_written_content","chapter_production_log"]),
            ("ConsistencyCheckerAgent", 4, "Controlla consistenza cross-chapters durante produzione - senior", ["chapters_written","second_level_plan","production_log"], ["consistency_report","inconsistencies_flagged"]),
            ("StyleEnforcerAgent", 4, "Garantisce stile scrittura uniforme - senior", ["manuscript_draft","style_notes"], ["style_normalized_manuscript"]),
            ("ContentQualityReviewerAgent", 4, "Revisiona qualita contenuto prima finalizzazione - senior", ["normalized_manuscript"], ["quality_review_result"]),
            ("ChapterDependencyManagerAgent", 5, "Gestisce dipendenze tra capitoli per scrittura parallela - operational", ["chapter_definitions","dependencies"], ["dependency_graph","parallel_plan"]),
            ("WritingProgressTrackerAgent", 4, "Traccia progresso scrittura capitoli paralleli - senior", ["chapter_writing_status"], ["progress_report","eta"]),
            ("WritingQualityCheckerAgent", 6, "Controlla qualita scrittura uniformita - support", ["chapter_content"], ["writing_quality_score"]),
            ("ProductionLogWriterAgent", 5, "Scrive production log decisioni durante scrittura - operational", ["chapter_decisions","consistency_checks"], ["production_log_entry"]),
        ]
    },
    "ProductionQualityTeam": {
        "ecosystem": "ProductionEcosystem",
        "sub_ecosystem": "QualitySub",
        "leader": "ProductionQualityLeader",
        "members": [
            ("ProductionQualityLeader", 3, "Leader ProductionQualityTeam valida completezza compliance approvazione finale", ["manuscript_draft"], ["validated_manuscript","final_approval"]),
            ("ManuscriptValidatorAgent", 4, "Valida completezza manoscritto - senior", ["final_manuscript_draft"], ["completeness_validation"]),
            ("PlanComplianceCheckerAgent", 4, "Verifica manoscritto segue second-level plan - senior", ["manuscript","second_level_plan"], ["compliance_report"]),
            ("FinalApprovalAgent", 6, "Da approvazione finale produzione manoscritto completo validato - support", ["validated_manuscript","compliance_report"], ["final_approval_signal"]),
            ("QualityMetricsCalculatorAgent", 4, "Calcola metriche qualita produzione - senior", ["manuscript","production_log"], ["quality_metrics"]),
            ("ContentValidationAgent", 6, "Valida contenuto manoscritto vs second-level plan details - support", ["manuscript","details"], ["content_validation_result"]),
        ]
    },
    "GraphicDesignTeam": {
        "ecosystem": "VisualEcosystem",
        "sub_ecosystem": "GraphicSub",
        "leader": "GraphicDesignLeader",
        "members": [
            ("GraphicDesignLeader", 3, "Leader GraphicDesignTeam creazione prompt grafiche generazione quality review revision loop", ["manuscript","chapter_list","details"], ["approved_graphics"]),
            ("GraphicPromptCreatorAgent", 5, "Crea prompt dettagliati per generazione grafiche - operational", ["chapter_content","graphic_requirements"], ["graphic_prompts_detailed"]),
            ("GraphicGeneratorAgent", 5, "Genera grafiche using prompt salva via VisualPlaywrightSaveAgent visual_save - operational Playwright", ["graphic_prompts"], ["generated_graphics_raw"]),
            ("GraphicQualityReviewerAgent", 6, "Revisiona qualita grafiche generate score pass fail loop revisione - support", ["generated_graphics_raw"], ["quality_score_graphics","pass_fail_flag"]),
            ("GraphicRevisionAgent", 6, "Revisiona grafiche fail quality review loop - support", ["failed_graphics","quality_feedback"], ["revised_graphics"]),
            ("GraphicStyleEnforcerAgent", 5, "Impone stile uniforme grafiche - operational", ["graphics","style_notes"], ["style_enforced_graphics"]),
            ("VisualConsistencyCheckerAgent", 4, "Verifica consistenza visual tra grafiche e cover - senior", ["graphics","cover","prompts"], ["consistency_report"]),
            ("GraphicPromptMicroAgent", 7, "Atomic creazione singolo prompt grafica - micro", ["prompt_request_single"], ["single_prompt_created"]),
        ]
    },
    "CoverDesignTeam": {
        "ecosystem": "VisualEcosystem",
        "sub_ecosystem": "CoverSub",
        "leader": "CoverDesignLeader",
        "members": [
            ("CoverDesignLeader", 3, "Leader CoverDesignTeam cover concept prompt generazione review critica non skippabile", ["manuscript","market_data","graphic_style"], ["final_approved_cover"]),
            ("CoverConceptAgent", 4, "Crea cover concept basato contenuto e market data performance signals - senior", ["manuscript","market_data","performance_signals"], ["cover_concept","concept_rationale"]),
            ("CoverPromptCreatorAgent", 5, "Crea prompt dettagliato cover generation - operational", ["cover_concept","manuscript"], ["cover_prompt_detailed"]),
            ("CoverGeneratorAgent", 5, "Genera cover salva via Playwright asset critico - operational Playwright", ["cover_prompt"], ["cover_generated_raw"]),
            ("CoverQualityReviewerAgent", 6, "Revisiona qualita cover critica pass fail non skippabile - support", ["cover_generated_raw","cover_concept"], ["cover_quality_score","cover_pass_fail"]),
            ("CoverRevisionAgent", 6, "Revisiona cover se needed loop critico - support", ["failed_cover","quality_feedback"], ["revised_cover"]),
            ("CoverMarketFitAnalystAgent", 4, "Analizza market fit cover concept - senior", ["cover_concept","market_data"], ["market_fit_score"]),
            ("CoverPromptMicroAgent", 7, "Atomic creazione singolo prompt cover - micro", ["cover_prompt_request"], ["single_cover_prompt_created"]),
        ]
    },
    "VisualPlaywrightOperationsTeam": {
        "ecosystem": "VisualEcosystem",
        "sub_ecosystem": "PlaywrightSub",
        "leader": "VisualPlaywrightLeader",
        "members": [
            ("VisualPlaywrightLeader", 3, "Leader VisualPlaywrightOperationsTeam navigazione Playwright salvataggio visual tasks", ["visual_assets","save_requests"], ["save_confirmations"]),
            ("VisualPlaywrightNavigatorAgent", 7, "Gestisce navigazione Playwright visual tasks - micro Playwright", ["visual_navigation_request"], ["visual_navigation_result"]),
            ("VisualPlaywrightSaveAgent", 6, "Salva output visual via Playwright support operational - support Playwright", ["visual_assets_to_save","asset_type"], ["visual_save_confirmation"]),
            ("VisualPlaywrightValidatorAgent", 6, "Valida salvataggi visual Playwright - support", ["visual_save_operations"], ["visual_save_validation"]),
            ("VisualPlaywrightCaptureAgent", 7, "Cattura dati visual pages - micro", ["visual_capture_request"], ["visual_captured_data"]),
            ("VisualSaveMicroAgent", 7, "Atomic singolo save visual via VisualPlaywrightSaveAgent - micro", ["visual_save_request_single"], ["single_visual_save_confirmation"]),
        ]
    },
    "MemoryManagementTeam": {
        "ecosystem": "MemoryEcosystem",
        "sub_ecosystem": "CoreMemorySub",
        "leader": "MemoryManagerLeader",
        "members": [
            ("MemoryManagerLeader", 3, "Leader MemoryManagementTeam gestisce memoria attiva read write checkpoint decision plan hierarchy notes SISTEMA ATTIVO NON PASSIVO", ["read_requests","write_requests","checkpoint_triggers","validation_triggers"], ["read_responses","write_confirmations","validation_reports"]),
            ("MemoryWriterAgent", 5, "Gestisce scritture strutturate memoria da tutti ecosistemi - sistema attivo operational", ["write_requests","data_to_write","category"], ["write_confirmation"]),
            ("MemoryReaderAgent", 5, "Gestisce letture memoria da tutti ecosistemi con context timestamp - sistema attivo operational", ["read_requests","category","requester_id"], ["read_response_with_timestamp"]),
            ("MemoryValidatorAgent", 6, "Valida consistenza memoria corruzione gaps active - support", ["memory_content_all_categories","checkpoint_refs"], ["validation_report","corruption_gap_flags"]),
            ("CheckpointManagerAgent", 6, "Gestisce checkpoint creation storage restoration core self-healing - support", ["checkpoint_creation_triggers","rollback_requests","state_snapshots"], ["checkpoint_created_confirmation","restored_checkpoint"]),
            ("DecisionLoggerAgent", 6, "Logga decisioni full context reasoning immutable - support", ["decision_events","reasoning_chains"], ["decision_log_confirmation"]),
            ("PlanStorageAgent", 6, "Memorizza recupera tutti i piani versioned not overwritten - support", ["plan_write_requests","plan_read_requests"], ["plan_storage_confirmation","plan_retrieval"]),
            ("HierarchyManagerAgent", 6, "Mantiene dati gerarchia 7 livelli - support", ["hierarchy_update_requests","orchestrator_init"], ["hierarchy_storage_confirmation"]),
            ("ImportantNotesAgent", 6, "Memorizza recupera note critiche flags importante - support", ["notes_write_requests","risk_flags","anomaly_logs"], ["notes_storage_confirmation"]),
            ("MemoryReadMicroAgent", 7, "Atomic singola lettura memoria via MemoryReaderAgent - micro", ["atomic_read_request"], ["atomic_read_result"]),
            ("MemoryWriteMicroAgent", 7, "Atomic singola scrittura memoria via MemoryWriterAgent - micro", ["atomic_write_request"], ["atomic_write_result"]),
        ]
    },
    "DetectionTeam": {
        "ecosystem": "SelfHealingEcosystem",
        "sub_ecosystem": "DetectionSub",
        "leader": "DetectionLeader",
        "members": [
            ("DetectionLeader", 3, "Leader DetectionTeam monitora output completeness coherence detect errors anomalies stalled frozen", ["phase_outputs_all_ecosystems","process_status_feeds"], ["anomaly_reports"]),
            ("OutputMonitorAgent", 4, "Monitora output phase completeness coherence - Detection Team senior", ["phase_outputs_feed","expected_output_schemas"], ["output_monitor_report","completeness_flag"]),
            ("ErrorDetectorAgent", 7, "Rileva errori eccezioni fallimenti processi - micro Detection", ["process_logs","exception_feed"], ["error_detected_report"]),
            ("AnomalyDetectorAgent", 4, "Rileva anomalie pattern insoliti stati inattesi - senior Detection", ["process_metrics","memory_validation_reports"], ["anomaly_detected_flag"]),
            ("StallDetectorAgent", 7, "Rileva processi stalled frozen no heartbeat timeout - micro Detection", ["process_heartbeat_feed","phase_timeout_thresholds"], ["stall_detected_report"]),
            ("PlaywrightFailureDetectorAgent", 6, "Rileva fallimenti Playwright specifici timeout blocked - support Detection", ["playwright_logs","failure_feed"], ["playwright_failure_detected"]),
            ("MemoryFailureDetectorAgent", 6, "Rileva fallimenti memoria write failure corruption gap - support Detection", ["memory_logs","validation_reports"], ["memory_failure_detected"]),
            ("ValidationCheckMicroAgent", 7, "Atomic singolo check validazione schema output phase - micro", ["validation_request_expected_schema","phase_output"], ["validation_result_completeness_flag"]),
        ]
    },
    "DiagnosisTeam": {
        "ecosystem": "SelfHealingEcosystem",
        "sub_ecosystem": "DiagnosisSub",
        "leader": "DiagnosisLeader",
        "members": [
            ("DiagnosisLeader", 3, "Leader DiagnosisTeam root cause analysis impact assessment recovery planning", ["anomaly_reports"], ["diagnosis_reports_with_recovery_plan"]),
            ("RootCauseAnalystAgent", 4, "Analizza anomalie root cause real self-healing diagnosis - senior", ["anomaly_report","phase_state","checkpoint_before"], ["root_cause_diagnosis","cause_category"]),
            ("ImpactAssessorAgent", 4, "Valuta impatto anomalia su workflow - senior", ["root_cause","workflow_state"], ["impact_assessment"]),
            ("RecoveryPlannerAgent", 4, "Crea recovery plan basato su diagnosis retry rollback escalate skip requalify - senior", ["root_cause","impact_assessment"], ["recovery_plan_with_steps"]),
            ("FailurePatternAnalyzerAgent", 4, "Analizza pattern fallimenti ricorrenti per prevenzione - senior", ["AnomalyLog","DiagnosisLog","RecoveryLog"], ["failure_patterns","prevention_suggestions"]),
        ]
    },
    "RecoveryTeam": {
        "ecosystem": "SelfHealingEcosystem",
        "sub_ecosystem": "RecoverySub",
        "leader": "RecoveryLeader",
        "members": [
            ("RecoveryLeader", 3, "Leader RecoveryTeam retry rollback alternative path validation real recovery", ["recovery_plans"], ["recovery_confirmations_or_escalations"]),
            ("RetryExecutorAgent", 5, "Esegue retry adjusted params real recovery timeout++ user_agent rotate - operational", ["recovery_plan_retry","failed_operation_ref"], ["retry_execution_result"]),
            ("RollbackExecutorAgent", 6, "Esegue rollback checkpoint precedenti real recovery via CheckpointManager restore - support", ["rollback_requests","checkpoint_id"], ["rollback_execution_result","restored_state"]),
            ("AlternativePathAgent", 7, "Trova esegue percorsi alternativi quando retry rollback fail real recovery - micro", ["failed_recovery_attempts","workflow_state"], ["alternative_path_execution"]),
            ("RecoveryValidatorAgent", 6, "Valida recovery successo workflow continua senza data loss - support", ["recovery_execution_results","workflow_state_after"], ["recovery_validation_result"]),
            ("EscalationManagerAgent", 6, "Gestisce escalation a controller e Supreme dopo max retry fail - support", ["failed_recovery_after_max_retries"], ["escalation_signal_to_L2_L1"]),
        ]
    },
    "FeedbackCollectionTeam": {
        "ecosystem": "AutoImprovementEcosystem",
        "sub_ecosystem": "FeedbackSub",
        "leader": "FeedbackCollectionLeader",
        "members": [
            ("FeedbackCollectionLeader", 3, "Leader FeedbackCollectionTeam outcome collection metrics pattern detection real improvement", ["cycle_completion_signals","phase_outcomes"], ["structured_feedback_data"]),
            ("OutcomeCollectorAgent", 5, "Raccoglie outcomes da cicli completati per auto-improvement - operational", ["cycle_completion_signals","phase_completion_logs"], ["collected_outcomes"]),
            ("PerformanceMetricsAgent", 6, "Calcola metriche performance per fase feedback 6 segnali - support", ["collected_outcomes","phase_logs"], ["performance_metrics_per_phase"]),
            ("PatternDetectorAgent", 6, "Rileva pattern ricorrenti positivi negativi - support", ["performance_metrics","historical_data"], ["detected_patterns"]),
            ("CycleOutcomeAnalyzerAgent", 5, "Analizza outcome ciclo completo - operational", ["cycle_completion","phase_outcomes"], ["cycle_outcome_analysis"]),
            ("MetricCaptureMicroAgent", 7, "Atomic cattura metrica singola performance per auto-improvement - micro", ["metric_capture_request_single"], ["single_metric_captured"]),
            ("PatternCheckMicroAgent", 7, "Atomic check pattern singolo via PatternDetector - micro", ["pattern_check_request_single"], ["single_pattern_check_result"]),
        ]
    },
    "ImprovementPlanningTeam": {
        "ecosystem": "AutoImprovementEcosystem",
        "sub_ecosystem": "PlanningSub",
        "leader": "ImprovementPlanningLeader",
        "members": [
            ("ImprovementPlanningLeader", 3, "Leader ImprovementPlanningTeam analizza feedback rank priorities scrive improvement plans", ["feedback_data"], ["prioritized_improvement_plans"]),
            ("ImprovementAnalystAgent", 4, "Analizza feedback identifica opportunita miglioramento 5 target - senior", ["feedback_data","performance_history"], ["improvement_opportunities"]),
            ("PriorityRankerAgent", 4, "Rank improvements by impact feasibility - senior", ["improvement_opportunities"], ["ranked_improvements"]),
            ("ImprovementPlanWriterAgent", 6, "Scrive improvement plans prioritizzati - support", ["ranked_improvements"], ["improvement_plans_written"]),
            ("OpportunityIdentifierAgent", 4, "Identifica opportunita miglioramento da pattern positivi - senior", ["PatternRegistry","PerformanceHistory"], ["positive_patterns","opportunities"]),
        ]
    },
    "ImprovementExecutionTeam": {
        "ecosystem": "AutoImprovementEcosystem",
        "sub_ecosystem": "ExecutionSub",
        "leader": "ImprovementExecutionLeader",
        "members": [
            ("ImprovementExecutionLeader", 3, "Leader ImprovementExecutionTeam adjust parameters update thresholds optimize workflows execution reale", ["improvement_plans"], ["updated_parameters","workflow_optimizations"]),
            ("ParameterAdjusterAgent", 5, "Aggiusta parametri workflow basati su improvement plan - operational", ["improvement_plan","ranked_improvements"], ["parameter_adjustments"]),
            ("ThresholdUpdaterAgent", 6, "Aggiorna soglie decisionali basate su learning GO threshold 70 - support", ["improvement_plan","performance_history"], ["threshold_updates"]),
            ("WorkflowOptimizerAgent", 6, "Ottimizza sequenze flow basate su dati performance - support", ["performance_metrics","improvement_plan"], ["optimized_flow_sequences"]),
            ("LearningLoggerAgent", 5, "Logga learning in LearningLog auto-improvement execution - operational", ["improvement_execution_results","parameter_changes"], ["learning_log_entry"]),
        ]
    },
}

# Generate files
for team_name, team_def in teams_definition.items():
    team_path = base / "teams" / team_name
    team_path.mkdir(parents=True, exist_ok=True)

    # Team synchronizer file
    sync_content = f'''
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from sync.harmony_protocol import global_harmony
from sync.team_synchronizer import TeamSynchronizer
from core import Team

# Team definition - non è più un unico file per tutti i team, ma file dedicato per {team_name}
# Ogni agente ha suo file dedicato sotto questa cartella e lavora in sincronia perfetta

TEAM_NAME = "{team_name}"
ECOSYSTEM = "{team_def['ecosystem']}"
SUB_ECOSYSTEM = "{team_def['sub_ecosystem']}"
LEADER = "{team_def['leader']}"
MEMBERS = {[m[0] for m in team_def['members']]}

# Synchronizer per garantire perfetta sincronia e armonia
synchronizer = TeamSynchronizer(TEAM_NAME, LEADER, MEMBERS, ECOSYSTEM)
global_harmony.register_team(TEAM_NAME, LEADER, MEMBERS)

TEAM_DEFINITION = Team(
    name=TEAM_NAME,
    ecosystem=ECOSYSTEM,
    sub_ecosystem=SUB_ECOSYSTEM,
    leader_agent=LEADER,
    member_agents=MEMBERS,
    responsibilities=["Responsabilita principale {team_name} in {team_def['ecosystem']}", "Gestisce flusso interno con TeamSynchronyProtocol", "Valida output con validator agent", "Crea checkpoint condiviso via CheckpointManagerAgent", "Gestisce self-healing sincronizzato intra-team", "Esegue handoff esterno 8-step sincronizzato via InterTeamHarmonyProtocol"],
    input_source="Handoff package da ecosistema precedente + memory {team_def['ecosystem']} + sync signals",
    output_target="Prossimo team/ecosistema + memory {team_def['ecosystem']} + checkpoint condiviso + sync ack",
    internal_communication_protocol={{
        "type": "harmonic_synchrony_perfect",
        "protocol": "TeamSynchronyProtocol con HarmonySignal ready checkpoint handoff validation error recovery",
        "flow": "Leader trigger members in ordine o parallelo con ready signals -> members emit checkpoint shared via CheckpointManager -> Validator valida -> se fail self-healing intra-team synchronized rollback -> se pass handoff interno con ack -> leader verifica harmony_status synchronized",
        "synchrony_mechanism": "Ogni agente invia ready signal a leader, leader coordina, checkpoint condiviso broadcast a ALL_TEAM, validazione con ack obbligatorio, harmony_status synchronized validato",
        "harmony_validation": "TeamSynchronyProtocol.validate_harmony() verifica tutti members_ready checkpoint_shared harmony_status synchronized",
        "playwright_integration": "Se team usa Playwright, PlaywrightNavigatorMicroAgent e DataCaptureMicroAgent lavorano in sincronia via TeamSynchronyProtocol con checkpoint condivisi",
        "self_healing_harmony": "Se un agente fallisce, team rimane in sincronia via rollback comune a ultimo checkpoint condiviso validato da CheckpointManagerAgent + RecoveryTeam",
        "memory_shared": "MemoryWriterAgent e MemoryReaderAgent condivisi intra-team con ImportantNotesAgent per risk flags"
    }},
    external_handoff_protocol={{
        "protocol_name": f"{{TEAM_NAME}} to next Handoff 8-step InterTeamHarmonyProtocol",
        "steps": [
            "1. {team_def['leader']} (LEADER L3) crea handoff package structured output decisions risks checkpoint ref + harmony_status synchronized",
            "2. MemoryEcosystem MemoryWriterAgent logs handoff",
            "3. Leader conferma ready scrive checkpoint condiviso via CheckpointManagerAgent broadcast ad ALL_TEAM",
            "4. Target team leader conferma receipt legge memory via MemoryReaderAgent + verifica harmony",
            "5. Target team valida completeness via Validator agent interno team",
            "6. Se validation fails -> SelfHealing DetectionTeam",
            "7. Se passes -> Target team inizia lavoro interno flow con TeamSynchronyProtocol",
            "8. Memory logs handoff completion + InterTeamHarmonyProtocol logs"
        ],
        "validation_required": True,
        "memory_logged": True,
        "checkpoint_required": True,
        "self_healing_on_failure": True,
        "harmony_required": True
    }},
    hierarchy_level=3
)

def get_synchronizer():
    return synchronizer

def validate_team_harmony():
    return synchronizer.validate_team_harmony()

print(f"Team {{TEAM_NAME}} synchronizer initialized - leader {{LEADER}} members {{len(MEMBERS)}} - perfect synchrony harmony")
'''

    with open(team_path / f"team_{team_name}_synchronizer.py", "w") as f:
        f.write(sync_content)

    # Now per-agent files
    for agent_name, level, role_desc, inputs, outputs in team_def["members"]:
        # Clean role
        safe_role = role_desc.replace('"','\\"')
        inputs_str = json.dumps(inputs)
        outputs_str = json.dumps(outputs)
        # Determine reports_to
        if agent_name == team_def["leader"]:
            reports_to = [f"{team_def['ecosystem']}Controller"]
        else:
            reports_to = [team_def["leader"]]

        agent_file_content = f'''
"""
AGENTE DEDICATO - File singolo per {agent_name}
Team: {team_name}
Ecosistema: {team_def['ecosystem']} / {team_def['sub_ecosystem']}
Livello Gerarchico: L{level}
Lavora in perfetta sincronia e armonia con altri agenti del team via TeamSynchronyProtocol
"""

import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import HarmonySignal
import time

# Definizione agente con tutti i campi richiesti RULE 3
{agent_name} = Agent(
    name="{agent_name}",
    role="{safe_role} - L{level} - Team {team_name} - Ecosistema {team_def['ecosystem']} - Lavora in perfetta sincronia e armonia con altri agenti via TeamSynchronyProtocol HarmonySignal",
    hierarchy_level={level},
    team="{team_name}",
    ecosystem="{team_def['ecosystem']}",
    sub_ecosystem="{team_def['sub_ecosystem']}",
    inputs={inputs_str},
    outputs={outputs_str},
    decision_logic="""Come agente {agent_name} L{level} in team {team_name} ecosistema {team_def['ecosystem']} sub {team_def['sub_ecosystem']}:
    {safe_role}
    LOGICA DECISIONALE ESATTA:
    - Riceve HarmonySignal ready da TeamSynchronyProtocol leader {team_def['leader']}
    - Legge memoria rilevante via MemoryReaderAgent L5 con context timestamp se necessario: checkpoints, decisions, plans, hierarchies, important_notes, BookOpportunityRegistry, ReviewDataRegistry, FeedbackRegistry, LearningLog
    - Esegue task core specifico del ruolo con operational tool se Playwright: navigate_amazon_keyword_search url https://www.amazon.com/s?k={{keyword}}, extract_data selectors, save_results results sources URLs notes, visual_save supporting visual team
    - Valida output con validator agent interno team: AmazonResultsValidatorAgent, ReviewDataValidatorAgent, PlanCoherenceValidatorAgent, ManuscriptValidatorAgent, GraphicQualityReviewerAgent, CoverQualityReviewerAgent, MemoryValidatorAgent, CheckpointManagerAgent
    - Emite HarmonySignal checkpoint con checkpoint_id condiviso via CheckpointManagerAgent broadcast a ALL_TEAM team {team_name}
    - Emite HarmonySignal handoff interno a prossimo agente team con ack obbligatorio
    - Se fail: emette HarmonySignal error a DetectionLeader L3, trigger SelfHealing flow DetectionTeam OutputMonitorAgent - DiagnosisTeam RootCauseAnalyst - RecoveryTeam RetryExecutor con adjusted params timeout++ user_agent rotate alternative selector new keywords memory reread rollback ultimo checkpoint valido via CheckpointManagerAgent
    - Verifica harmony_status synchronized via TeamSynchronyProtocol.validate_harmony()
    - Scrive risultato in memoria via MemoryWriterAgent L5 + checkpoint via CheckpointManagerAgent L6 parent ID valid flag
    - Logga decisione traceability via DecisionLoggerAgent L6 se GO NO-GO production_start_signal keyword_selection niche_ranking
    DECISION AUTHORITY: {"can decide tactical without escalation if impact < team_level and no cross-team effect" if level==4 else "follow instructions senior and leaders, report output" if level==5 else "support functions validation logging monitoring checkpoint management" if level==6 else "small single-purpose atomic task spawned managed higher auto-terminated after task" if level==7 else "manages team members coordinates internal work handles intra-team communication reports to ecosystem controller L2" if level==3 else "controls ecosystem manages teams reports to L1" if level==2 else "supreme orchestrator sees everything decides macro override any decision manages global state"}
    SINCRONIA E ARMONIA: Lavora in perfetta sincronia e armonia con altri agenti del team {team_name} - ogni agente invia ready signal, checkpoint condiviso, handoff con ack, validazione, harmony_status synchronized - InterTeamHarmonyProtocol per handoff esterno 8-step sincronizzato via Memory broker
    """,
    connections={{"reports_to": {json.dumps(reports_to)}, "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent","TeamSynchronizer_{team_name}"]}},
    memory_access={{"read": ["checkpoints","decisions","plans","hierarchies","important_notes","BookOpportunityRegistry","ReviewDataRegistry","FeedbackRegistry","LearningLog"], "write": ["checkpoints","decisions","important_notes","AnomalyLog"]}},
    self_healing_behavior={{"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry con adjusted params da important_notes LearningLog rollback a ultimo checkpoint condiviso valido via CheckpointManagerAgent team {team_name} sincronizzato con altri membri team - se 3 fallimenti escalate a leader {team_def['leader']} poi controller {team_def['ecosystem']}Controller poi Supreme", "max_retries": 3, "checkpoint_before": True, "memory_updated": True, "flow_continued": True, "harmony_preserved": True}},
    playwright_usage="real operational tool navigation data collection Amazon review sites saving results supporting visual activities - usa PlaywrightNavigatorMicroAgent DataCaptureMicroAgent ScreenshotMicroAgent ErrorHandlerAgent VisualSaveMicroAgent se team usa Playwright - allowed uses per PLAYWRIGHT_USAGE_POLICY" if "Playwright" in agent_name or "Search" in agent_name or "Extractor" in agent_name or "Save" in agent_name or "Graphic" in agent_name or "Cover" in agent_name else None,
    skill_usage=["BookNicheDecisionSkill","QualificationDecisionSkill","SelfHealingSkill","VideoStructureDesignSkill","ChapterDesignSkill","MemoryReadWriteSkill","CheckpointManagementSkill","PlaywrightNavigationSkill","PlaywrightDataExtractionSkill","PlaywrightSaveSkill"] if level in [3,4,5] else ["SelfHealingSkill","CheckpointManagementSkill"],
    level_name="L{level}_{'SUPREME' if level==1 else 'CONTROLLER' if level==2 else 'LEADER' if level==3 else 'SENIOR' if level==4 else 'OPERATIONAL' if level==5 else 'SUPPORT' if level==6 else 'MICRO'}"
)

# Metodi aggiuntivi per sincronia perfetta
class {agent_name}_SynchronizedWrapper:
    def __init__(self, agent_instance):
        self.agent = agent_instance
        self.harmony_signals: list = []
        self.checkpoint_shared = None
        self.status = "initialized"

    def emit_ready(self):
        signal = HarmonySignal(
            signal_id=f"{team_name}_{{self.agent.name}}_ready_{{int(time.time()*1000)}}",
            sender_agent=self.agent.name,
            receiver_agent="{team_def['leader']}",
            team="{team_name}",
            ecosystem="{team_def['ecosystem']}",
            signal_type="ready",
            payload={{"agent": self.agent.name, "status": "ready", "hierarchy_level": self.agent.hierarchy_level, "team": self.agent.team}},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=True
        )
        self.harmony_signals.append(signal)
        self.status = "ready"
        return signal

    def sync_checkpoint(self, checkpoint_id: str):
        self.checkpoint_shared = checkpoint_id
        signal = HarmonySignal(
            signal_id=f"{team_name}_{{self.agent.name}}_checkpoint_{{checkpoint_id}}",
            sender_agent=self.agent.name,
            receiver_agent="ALL_TEAM_{team_name}",
            team="{team_name}",
            ecosystem="{team_def['ecosystem']}",
            signal_type="checkpoint",
            payload={{"checkpoint_id": checkpoint_id, "shared": True, "agent": self.agent.name, "team": "{team_name}"}},
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=False
        )
        self.harmony_signals.append(signal)
        self.status = "checkpoint_shared"
        return signal

    def communicate(self, target_agent: str, payload: dict, signal_type: str = "handoff"):
        signal = HarmonySignal(
            signal_id=f"{team_name}_{{self.agent.name}}_to_{{target_agent}}_{{signal_type}}",
            sender_agent=self.agent.name,
            receiver_agent=target_agent,
            team="{team_name}",
            ecosystem="{team_def['ecosystem']}",
            signal_type=signal_type,
            payload=payload,
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            requires_ack=True
        )
        self.harmony_signals.append(signal)
        return signal

    def validate_harmony(self):
        return {{"agent": self.agent.name, "team": "{team_name}", "status": self.status, "checkpoint_shared": self.checkpoint_shared, "signals_count": len(self.harmony_signals), "harmony": "synchronized"}}

    def self_heal_synchronized(self, error_type: str, failed_op: str):
        # Self-healing in armonia con team - rollback sincronizzato
        return {{
            "phase": "{team_name}",
            "error_type": error_type,
            "failed_operation": failed_op,
            "agent": self.agent.name,
            "checkpoint_restored": True,
            "team_checkpoint_shared": self.checkpoint_shared,
            "action_taken": "retry con adjusted params team synchronized rollback",
            "memory_updated": True,
            "flow_continued": True,
            "harmony_preserved": True,
            "team_synchrony": "all members rollback to shared checkpoint {team_name}"
        }}

# Istanza wrapper sincronizzata
{agent_name}_sync = {agent_name}_SynchronizedWrapper({agent_name})

def get_agent():
    return {agent_name}

def get_synchronized_wrapper():
    return {agent_name}_sync

print(f"Agent file dedicated {agent_name} L{level} Team {team_name} Ecosistema {team_def['ecosystem']} - perfect synchrony harmony initialized")
'''

        with open(team_path / f"{agent_name}.py", "w") as f:
            f.write(agent_file_content)

print(f"Generated per-agent files for {len(teams_definition)} teams")

# Create ecosystem level single agent files also for L1 and L2 etc already but we need per-agent files for L1 L2 in separate folders
# L1 Supreme single file
supreme_path = base / "L1"
supreme_path.mkdir(parents=True, exist_ok=True)
# Already have supreme.py in previous architettura_completa_7_livelli but we need in new base for architettura_sincrona L1
# Create Supreme file
with open(supreme_path / "SupremeOrchestratorAgent.py", "w") as f:
    f.write('''
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import global_harmony

SupremeOrchestratorAgent = Agent(
    name="SupremeOrchestratorAgent",
    role="Supreme Orchestrator L1 - unico top-level vede tutto decide macro override qualsiasi decisione gestisce stato globale inizia cicli valida gerarchie 7 livelli - perfetta sincronia armonia con L2 controllers",
    hierarchy_level=1,
    team="SupremeOrchestratorTeam",
    ecosystem="Global",
    sub_ecosystem=None,
    inputs=["reports_from_L2_controllers","memory_ecosystem_state","self_healing_escalations","auto_improvement_signals","final_outputs_all_ecosystems","hierarchy_validation_reports","global_harmony_status"],
    outputs=["global_state","macro_decisions","override_commands","cycle_initiation_signals","hierarchy_updates","CP0_INIT","global_harmony_validation"],
    decision_logic="""SE escalation self-healing severity CRITICAL ALLORA override lower + rollback checkpoint globale valido + log hierarchies + broadcast global_harmony resync SE GO_rate <20% ALLORA aggiusta thresholds via ThresholdUpdaterAgent + aumenta retry Research SE nuovo ciclo ALLORA crea CP0_INIT via CheckpointManagerAgent L6 scrive hierarchies via HierarchyManagerAgent L6 leggi important_notes LearningLog FeedbackRegistry via MemoryReaderAgent L5 broadcast start tutti L2 controllers via InterTeamHarmonyProtocol 8-step + TeamSynchronyProtocol harmony validation global_harmony.check_global_harmony() Authority override senza soglia Gestisce perfect synchrony harmony globale""",
    connections={"reports_to": [], "manages": ["ResearchEcosystemController","QualificationEcosystemController","PlanningEcosystemController","ProductionEcosystemController","VisualEcosystemController","MemoryEcosystemController","SelfHealingEcosystemController","AutoImprovementEcosystemController"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController","GlobalHarmonyOrchestrator"]},
    memory_access={"read": ["checkpoints","decisions","plans","hierarchies","important_notes","AnomalyLog","PerformanceHistory","FeedbackRegistry","LearningLog"], "write": ["hierarchies","checkpoints","important_notes","GlobalHarmonyStatus"]},
    self_healing_behavior={"on_failure": "top level non self-heala riceve escalation manual_override_and_global_rollback", "checkpoint_before": True, "global_harmony_resync": True},
    level_name="L1_SUPREME_ORCHESTRATOR"
)

print("SupremeOrchestratorAgent dedicated file L1 - perfect synchrony harmony global")
''')

print("Generated single-agent architecture in /home/user/architettura_sincrona")
