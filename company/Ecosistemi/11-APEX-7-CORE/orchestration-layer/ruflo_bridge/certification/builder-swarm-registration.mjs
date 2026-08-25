#!/usr/bin/env node
import { mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { RufloMcpClient } from '../dist/src/mcp_client.js';
import { validateToolSchemas } from '../dist/src/validator.js';

const manifest = JSON.parse(await readFile('manifests/tool-schema-hashes.json', 'utf8'));
const expected = Object.fromEntries(
  ['swarm_init', 'swarm_status', 'swarm_shutdown', 'agent_spawn', 'agent_status', 'agent_terminate']
    .map((name) => [name, manifest.tools[name]])
);
const roles = [
  ['BUILD-LEAD', 'coordinator'], ['ARCHITECT', 'architect'],
  ['RUFLO-SCOUT', 'researcher'], ['IMPLEMENTER', 'coder'],
  ['TESTER', 'tester'], ['SECURITY', 'security-architect'],
  ['GATEKEEPER', 'reviewer'], ['RELEASE', 'cicd-engineer'],
];
const workspace = await mkdtemp(join(tmpdir(), 'ocp-builder-registration-'));
const client = new RufloMcpClient(manifest.rufloVersion, workspace, 20_000, false);
const report = {
  rufloVersion: manifest.rufloVersion,
  sourceCommit: manifest.sourceCommit,
  providerCredentialsForwarded: false,
  generativeExecution: false,
};
let swarmId;
try {
  await client.start();
  validateToolSchemas(await client.listTools(), expected);
  const swarm = await client.callTool('swarm_init', {
    topology: 'hierarchical', maxAgents: 8, strategy: 'balanced',
    config: { communicationProtocol: 'message-bus', autoScaling: false },
  });
  swarmId = swarm.swarmId;
  if (typeof swarmId !== 'string') throw new Error('swarm_init did not return swarmId');
  const registered = [];
  for (const [agentId, agentType] of roles) {
    const result = await client.callTool('agent_spawn', {
      agentId: `ocp-builder-${agentId.toLowerCase()}`,
      agentType, swarmId,
      task: 'Registration-only sandbox activation. Do not execute a provider call.',
    });
    if (result.success !== true) throw new Error(`agent_spawn failed for ${agentId}`);
    registered.push({ role: agentId, agentId: result.agentId, agentType, status: result.status });
  }
  const status = await client.callTool('swarm_status', {
    swarmId, includeAgents: true, includeMetrics: true,
  });
  report.registered = registered;
  report.swarmAgentCount = status.agentCount;
  report.maxAgents = status.maxAgents;
  report.autoScaling = status.config?.autoScaling;
  report.registration = registered.length === 8 && status.agentCount === 8 ? 'PASS' : 'FAIL';
  for (const agent of registered) {
    await client.callTool('agent_terminate', { agentId: agent.agentId, force: true });
  }
  const shutdown = await client.callTool('swarm_shutdown', { swarmId, graceful: true });
  report.cleanup = shutdown.success === true ? 'PASS' : 'FAIL';
  report.status = report.registration === 'PASS' && report.cleanup === 'PASS' ? 'PASS' : 'FAIL';
} catch (error) {
  report.status = 'FAIL';
  report.error = String(error);
  process.exitCode = 2;
} finally {
  await client.close();
  await rm(workspace, { recursive: true, force: true });
}
await writeFile(resolve('manifests/builder-swarm-registration.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
