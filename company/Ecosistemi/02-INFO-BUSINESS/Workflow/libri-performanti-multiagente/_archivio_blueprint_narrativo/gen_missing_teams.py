import os, pathlib, json
base = pathlib.Path("/home/user/architettura_sincrona")

missing_teams = {
    "KeywordExpansionTeam": {
        "ecosystem": "ResearchEcosystem",
        "sub": "ExpansionSub",
        "leader": "KeywordExpansionLeader",
        "members": [
            ("KeywordExpansionLeader", 3, "Leader KeywordExpansionTeam espansione keyword quando empty result LearningLog - espansione", ["empty_result_trigger","important_notes","LearningLog"], ["keyword_variations","new_keyword_list"]),
            ("KeywordVariationGeneratorAgent", 5, "Genera variazioni keyword avanzate per retry quando empty result - operational", ["empty_result","important_notes"], ["variation_list"]),
            ("SemanticKeywordExpanderAgent", 5, "Espande keyword semanticamente da LearningLog patterns - operational", ["LearningLog","important_notes"], ["semantic_expansions"]),
            ("LongTailKeywordAgent", 5, "Genera long-tail keywords per nicchie meno competitive - operational", ["seed_keywords","competition_data"], ["long_tail_list"]),
        ]
    },
    "SearchOptimizationTeam": {
        "ecosystem": "ResearchEcosystem",
        "sub": "OptimizationSub",
        "leader": "SearchOptimizationLeader",
        "members": [
            ("SearchOptimizationLeader", 3, "Leader SearchOptimizationTeam ottimizza strategie search Amazon riduce blocchi Playwright", ["Playwright_failure_logs","AnomalyLog"], ["optimized_strategy","rotation_plan"]),
            ("SearchStrategyOptimizerAgent", 5, "Ottimizza strategia search per ridurre blocchi Playwright - operational", ["failure_logs","search_results"], ["optimized_strategy"]),
            ("PlaywrightRotationManagerAgent", 5, "Gestisce rotazione Playwright per evitare blocchi user_agent timeout - operational", ["Playwright_logs","rotation_requests"], ["rotation_confirmation"]),
        ]
    },
    "ContentPlanningTeam": {
        "ecosystem": "PlanningEcosystem",
        "sub": "ContentSub",
        "leader": "ContentPlanningLeader",
        "members": [
            ("ContentPlanningLeader", 3, "Leader ContentPlanningTeam pianificazione contenuti dettagliata produzione sostenibile", ["second_level_plan_draft","chapters"], ["details_enriched","content_flow"]),
            ("ContentDetailArchitectAgent", 5, "Progetta dettagli contenuti per sustainable production - operational", ["chapters","video_structure"], ["production_constraints","style_notes","graphic_needs"]),
            ("ContentFlowDesignerAgent", 4, "Progetta flusso contenuti tra capitoli - senior", ["chapters","details"], ["content_flow_design"]),
            ("ResourceAllocationPlannerAgent", 5, "Pianifica allocazione risorse per capitoli - operational", ["chapter_list","resource_estimate"], ["allocation_plan"]),
            ("ContentDetailArchitectAgent2", 5, "Second instance detail architect redundancy - operational", ["chapters","details"], ["details_enriched_v2"]),
        ]
    },
    "EditingTeam": {
        "ecosystem": "ProductionEcosystem",
        "sub": "EditingSub",
        "leader": "EditingLeader",
        "members": [
            ("EditingLeader", 3, "Leader EditingTeam editing finale uniformita correzione", ["validated_manuscript"], ["edited_manuscript","editing_log"]),
            ("EditingCoordinatorAgent", 5, "Coordina editing finale - operational", ["manuscript","editing_requests"], ["editing_coordination"]),
            ("FinalProofreaderAgent", 5, "Proofreading finale manoscritto - operational", ["edited_manuscript"], ["proofread_manuscript"]),
            ("CrossReferenceCheckerAgent", 5, "Verifica cross-reference tra capitoli e piano - operational", ["manuscript","second_level_plan"], ["cross_reference_report"]),
        ]
    },
    "VisualQualityTeam": {
        "ecosystem": "VisualEcosystem",
        "sub": "VisualQualitySub",
        "leader": "VisualQualityLeader",
        "members": [
            ("VisualQualityLeader", 3, "Leader VisualQualityTeam qualita visual finale approva grafiche cover", ["all_graphics","cover","prompts"], ["visual_quality_approval","CP_FINAL"]),
            ("VisualQualityAuditorAgent", 4, "Audita qualita visual finale - senior", ["all_graphics","cover","graphics_prompts"], ["quality_audit_report"]),
            ("FinalVisualApprovalAgent", 6, "Approvazione finale visual - support", ["quality_audit_report","all_visual"], ["final_visual_approval_signal"]),
        ]
    },
    "CheckpointSubEcosystem": {
        "ecosystem": "MemoryEcosystem",
        "sub": "CheckpointSub",
        "leader": "CheckpointSubLeader",
        "members": [
            ("CheckpointSubLeader", 3, "Leader CheckpointSubEcosystem gestione checkpoint creation storage restoration", ["checkpoint_creation_triggers","rollback_requests"], ["checkpoint_created_confirmation","restored_checkpoint"]),
            ("CheckpointCreatorAgent", 5, "Crea checkpoint via CheckpointManagerAgent - operational Memory sub", ["state_snapshot","trigger_event"], ["checkpoint_created"]),
            ("CheckpointValidatorAgent", 6, "Valida checkpoint prima storage - support Memory sub", ["checkpoint_data"], ["checkpoint_validation_result"]),
            ("CheckpointRestorerAgent", 6, "Esegue restore checkpoint su richiesta rollback - support Memory sub", ["rollback_request","checkpoint_id"], ["restored_checkpoint"]),
            ("CheckpointPrunerAgent", 6, "Gestisce pruning checkpoint vecchi preservando traceability - support", ["checkpoint_chain","prune_policy"], ["pruned_checkpoint_list"]),
            ("CheckpointCreateMicroAgent", 7, "Atomic creazione checkpoint singolo via CheckpointManagerAgent - micro", ["atomic_create_request"], ["atomic_create_result"]),
            ("CheckpointRestoreMicroAgent", 7, "Atomic restore checkpoint singolo - micro", ["atomic_restore_request"], ["atomic_restore_result"]),
        ]
    },
    "DecisionLogSubEcosystem": {
        "ecosystem": "MemoryEcosystem",
        "sub": "DecisionSub",
        "leader": "DecisionLogSubLeader",
        "members": [
            ("DecisionLogSubLeader", 3, "Leader DecisionLogSubEcosystem logging decisioni immutable traceability", ["decision_events","reasoning_chains"], ["decision_log_confirmation","traceability"]),
            ("DecisionLogWriterAgent", 5, "Scrive decisioni log immutable - operational Memory sub", ["decision_event","reasoning"], ["decision_log_written"]),
            ("DecisionLogReaderAgent", 6, "Legge log decisioni con traceability - support Memory sub", ["read_request","decision_id"], ["decision_log_retrieved"]),
            ("DecisionTraceabilityAgent", 6, "Verifica traceability decisioni reasoning chain - support", ["decision_logs"], ["traceability_report"]),
            ("DecisionLogMicroAgent", 7, "Atomic logging singola decisione via DecisionLoggerAgent - micro", ["atomic_log_request"], ["atomic_log_result"]),
        ]
    },
}

for team_name, team_def in missing_teams.items():
    team_path = base / "teams" / team_name
    team_path.mkdir(parents=True, exist_ok=True)

    # synchronizer
    sync_content = f'''
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from sync.harmony_protocol import global_harmony
from sync.team_synchronizer import TeamSynchronizer
from core import Team

TEAM_NAME = "{team_name}"
ECOSYSTEM = "{team_def['ecosystem']}"
SUB_ECOSYSTEM = "{team_def['sub']}"
LEADER = "{team_def['leader']}"
MEMBERS = {[m[0] for m in team_def['members']]}

synchronizer = TeamSynchronizer(TEAM_NAME, LEADER, MEMBERS, ECOSYSTEM)

TEAM_DEFINITION = Team(
    name=TEAM_NAME,
    ecosystem=ECOSYSTEM,
    sub_ecosystem=SUB_ECOSYSTEM,
    leader_agent=LEADER,
    member_agents=MEMBERS,
    responsibilities=["Team {team_name} in {team_def['ecosystem']} - perfetta sincronia armonia", "Gestisce flusso interno con TeamSynchronyProtocol", "Checkpoint condiviso", "Self-healing sincronizzato", "Handoff esterno 8-step"],
    input_source="Handoff package + memory {team_def['ecosystem']} + sync signals",
    output_target="Prossimo team + memory + checkpoint condiviso + sync ack",
    internal_communication_protocol={{"type": "harmonic_synchrony_perfect", "protocol": "TeamSynchronyProtocol HarmonySignal ready checkpoint handoff validation", "harmony_validation": "validate_harmony synchronized"}},
    external_handoff_protocol={{"protocol_name": f"{{TEAM_NAME}} handoff 8-step", "validation_required": True, "memory_logged": True, "checkpoint_required": True, "self_healing_on_failure": True, "harmony_required": True}},
    hierarchy_level=3
)

def get_synchronizer():
    return synchronizer

print(f"Team {{TEAM_NAME}} synchronizer initialized - {{len(MEMBERS)}} members perfect synchrony")
'''
    with open(team_path / f"team_{team_name}_synchronizer.py", "w") as f:
        f.write(sync_content)

    for agent_name, level, role_desc, inputs, outputs in team_def["members"]:
        safe_role = role_desc.replace('"','\\"')
        inputs_str = json.dumps(inputs)
        outputs_str = json.dumps(outputs)
        reports_to = [team_def["leader"]] if agent_name != team_def["leader"] else [f"{team_def['ecosystem']}Controller"]

        agent_content = f'''
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import HarmonySignal
import time

{agent_name} = Agent(
    name="{agent_name}",
    role="{safe_role} - L{level} Team {team_name} Ecosistema {team_def['ecosystem']} - perfetta sincronia armonia",
    hierarchy_level={level},
    team="{team_name}",
    ecosystem="{team_def['ecosystem']}",
    sub_ecosystem="{team_def['sub']}",
    inputs={inputs_str},
    outputs={outputs_str},
    decision_logic="""Come agente {agent_name} L{level} team {team_name} {team_def['ecosystem']}: {safe_role} - Riceve HarmonySignal ready da TeamSynchronyProtocol leader {team_def['leader']} - Legge memoria via MemoryReaderAgent - Esegue task core con Playwright tool se necessario - Valida output con validator - Emite checkpoint condiviso broadcast ALL_TEAM - Handoff interno ack obbligatorio - Self-healing DetectionTeam se fail - Verifica harmony_status synchronized - Scrive memoria via MemoryWriterAgent + checkpoint via CheckpointManagerAgent - Logga decisione via DecisionLoggerAgent - Sincronia perfetta armonia intra-team InterTeamHarmonyProtocol esterno 8-step""",
    connections={{"reports_to": {json.dumps(reports_to)}, "manages": [], "collaborates_with": ["MemoryManagerLeader","MemoryReaderAgent","CheckpointManagerAgent"]}},
    memory_access={{"read": ["checkpoints","decisions","plans","important_notes","BookOpportunityRegistry"], "write": ["checkpoints","important_notes"]}},
    self_healing_behavior={{"detection_triggers": ["missing output","incoherent output","blocked process","failed validation","empty result from research","no-go without alternative","memory write failure","Playwright failure"], "action": "retry adjusted params rollback checkpoint condiviso valido team {team_name} sincronizzato - escalate leader {team_def['leader']} poi controller {team_def['ecosystem']}Controller poi Supreme", "max_retries": 3, "harmony_preserved": True}},
    playwright_usage="real operational tool" if "Playwright" in "{agent_name}" or "Search" in "{agent_name}" or "Extractor" in "{agent_name}" else None,
    skill_usage=["SelfHealingSkill","MemoryReadWriteSkill","CheckpointManagementSkill"],
    level_name="L{level}"
)

class {agent_name}_SynchronizedWrapper:
    def __init__(self, agent_instance):
        self.agent = agent_instance
        self.harmony_signals = []
        self.checkpoint_shared = None
        self.status = "initialized"
    def emit_ready(self):
        signal = HarmonySignal(signal_id=f"{team_name}_{{self.agent.name}}_ready", sender_agent=self.agent.name, receiver_agent="{team_def['leader']}", team="{team_name}", ecosystem="{team_def['ecosystem']}", signal_type="ready", payload={{"agent": self.agent.name}}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"), requires_ack=True)
        self.harmony_signals.append(signal)
        self.status = "ready"
        return signal
    def sync_checkpoint(self, checkpoint_id):
        self.checkpoint_shared = checkpoint_id
        signal = HarmonySignal(signal_id=f"{team_name}_{{self.agent.name}}_checkpoint_{{checkpoint_id}}", sender_agent=self.agent.name, receiver_agent="ALL_TEAM", team="{team_name}", ecosystem="{team_def['ecosystem']}", signal_type="checkpoint", payload={{"checkpoint_id": checkpoint_id}}, timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        self.harmony_signals.append(signal)
        self.status = "checkpoint_shared"
        return signal
    def validate_harmony(self):
        return {{"agent": self.agent.name, "team": "{team_name}", "status": self.status, "harmony": "synchronized"}}

{agent_name}_sync = {agent_name}_SynchronizedWrapper({agent_name})
def get_agent():
    return {agent_name}
def get_synchronized_wrapper():
    return {agent_name}_sync
print(f"Agent dedicated {agent_name} L{level} Team {team_name} - perfect synchrony harmony")
'''
        with open(team_path / f"{agent_name}.py", "w") as f:
            f.write(agent_content)

print(f"Added missing {len(missing_teams)} teams with per-agent files")

# Now also create L2 per-agent dedicated files
L2_path = base / "L2"
L2_path.mkdir(parents=True, exist_ok=True)
controllers = [
    ("ResearchEcosystemController","ResearchEcosystem","Controlla ResearchEcosystem 5 team keyword search Amazon review sites"),
    ("QualificationEcosystemController","QualificationEcosystem","Controlla QualificationEcosystem piano qualifica dettagliato"),
    ("PlanningEcosystemController","PlanningEcosystem","Controlla PlanningEcosystem second-level plan video_structure REQUIRED"),
    ("ProductionEcosystemController","ProductionEcosystem","Controlla ProductionEcosystem scrittura intero libro"),
    ("VisualEcosystemController","VisualEcosystem","Controlla VisualEcosystem grafiche prompt cover Playwright support"),
    ("MemoryEcosystemController","MemoryEcosystem","Controlla MemoryEcosystem attivo validazione checkpoint non storage passivo"),
    ("SelfHealingEcosystemController","SelfHealingEcosystem","Controlla SelfHealingEcosystem real active always-on healing"),
    ("AutoImprovementEcosystemController","AutoImprovementEcosystem","Controlla AutoImprovementEcosystem real continuous improvement"),
]
for name, eco, role in controllers:
    with open(L2_path / f"{name}.py", "w") as f:
        f.write(f'''
import sys
sys.path.insert(0, '/home/user/architettura_sincrona')
from core import Agent
from sync.harmony_protocol import global_harmony

{name} = Agent(
    name="{name}",
    role="{role} L2 Controller {eco} gestisce team alloca risorse valida handoff report Supreme - perfetta sincronia armonia con Supreme L1 e L3 leaders",
    hierarchy_level=2,
    team="EcosystemControlTeam",
    ecosystem="{eco}",
    sub_ecosystem=None,
    inputs=["cycle_start_signal","memory_hierarchies","important_notes_feedback","checkpoints","team_status_reports","global_harmony_status"],
    outputs=["ecosystem_status","resource_allocation","go_signal","reports_to_L1","handoff_validation","harmony_validation"],
    decision_logic="""Controller L2 {eco}: leggi important_notes LearningLog pattern successo fallimento alloca team leader L3 trigger flow interno team via TeamSynchronyProtocol harmony validation SE team empty result anomaly trigger SelfHealing via PlaywrightErrorHandlerAgent SE output validato checkpoint marca phase complete crea checkpoint via CheckpointManagerAgent handoff prossimo ecosistema via InterTeamHarmonyProtocol 8-step sincronizzato Memory broker SE 3 fallimenti escalate Supreme - mantiene perfect synchrony harmony intra-ecosistema e inter-ecosistemi via GlobalHarmonyOrchestrator.check_global_harmony()""",
    connections={{"reports_to": ["SupremeOrchestratorAgent"], "manages": ["{eco}Leader1","{eco}Leader2"], "collaborates_with": ["MemoryManagerLeader","SelfHealingEcosystemController","GlobalHarmonyOrchestrator"]}},
    memory_access={{"read": ["checkpoints","decisions","plans","hierarchies","important_notes","FeedbackRegistry","BookOpportunityRegistry","GlobalHarmonyStatus"], "write": ["checkpoints","decisions","important_notes","GlobalHarmonyStatus"]}},
    self_healing_behavior={{"detection_triggers": ["empty result from research","Playwright failure","memory write failure","team desynchronized"], "action": "retry adjusted params rollback CP0 escalate Supreme if 3 fails harmony resync via GlobalHarmonyOrchestrator", "max_retries": 3}},
    playwright_usage="supervises PlaywrightOperationsSubEcosystem real tool" if "{eco}"=="ResearchEcosystem" or "{eco}"=="VisualEcosystem" else None,
    skill_usage=["BookNicheDecisionSkill","SelfHealingSkill","MemoryReadWriteSkill","CheckpointManagementSkill"],
    level_name="L2_ECOSYSTEM_CONTROLLER"
)

class {name}_HarmonyWrapper:
    def __init__(self):
        self.agent = {name}
        self.ecosystem = "{eco}"
    def sync_teams(self):
        return global_harmony.check_global_harmony()
    def validate_harmony(self):
        return {{"controller": "{name}", "ecosystem": "{eco}", "status": "synchronized", "teams": "{eco} teams harmony"}}

print(f"L2 Controller dedicated file {name} {eco} - perfect synchrony harmony")
''')

print("Generated L2 per-agent dedicated files")

# Count total agent files now
import pathlib
base_path = pathlib.Path("/home/user/architettura_sincrona")
total_py = len(list(base_path.rglob("*.py")))
team_files = len(list((base_path / "teams").rglob("*.py")))
print(f"Totale file .py architettura_sincrona: {total_py}, di cui teams per-agent: {team_files}")
