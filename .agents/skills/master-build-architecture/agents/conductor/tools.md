# Conductor Tools (L3 + External)

**Core L3 Python Tools:**
- scripts/memory_manager.py (init, create_checkpoint, record_decision, append_to_index, validate)
- scripts/kg_builder.py (build traceability graph from multi-source)
- scripts/plan_versioner.py (generate and manage PLAN-vN.md)
- scripts/swarm_topology_generator.py (Ruflo-compatible topology maps)
- scripts/validator.py (coverage_check, schema_validator, no_summary_lint)
- scripts/ruflo_bridge.py (emit ready-to-run npx ruflo commands)
- scripts/package_skill.py (official packaging)

**External / Ruflo MCP (when available):**
- swarm_init, agent_spawn, memory_store, memory_search, federation_send, etc.

**Handoff to L3:** Always via explicit instruction in the L2 agent's prompt ("Call python scripts/xxx.py --target ...").

**When to use L3 vs L2:** Deterministic/mechanical work → L3. Judgment, generation, coordination → L2.