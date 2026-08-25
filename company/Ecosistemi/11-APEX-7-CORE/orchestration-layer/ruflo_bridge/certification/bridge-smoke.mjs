#!/usr/bin/env node
import { mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { RufloBridge, RufloMcpClient } from '../dist/src/index.js';

const started = Date.now();
const workspace = await mkdtemp(join(tmpdir(), 'ocp-ruflo-bridge-'));
const manifest = JSON.parse(await readFile('manifests/tool-schema-hashes.json', 'utf8'));
const requiredForBridge = Object.fromEntries(
  ['swarm_init', 'swarm_shutdown', 'agent_spawn', 'agent_execute', 'agent_terminate']
    .map((name) => [name, manifest.tools[name]])
);
const client = new RufloMcpClient(manifest.rufloVersion, workspace, 30_000);
const bridge = new RufloBridge(client, requiredForBridge);
let report;
try {
  await bridge.start();
  const swarmId = await bridge.initializeSwarm();
  report = {
    status: 'PASS', rufloVersion: manifest.rufloVersion,
    sourceCommit: manifest.sourceCommit, supervisorState: bridge.supervisor.state,
    swarmIdObserved: typeof swarmId === 'string',
    agentExecution: 'NOT_EXECUTED_NO_PROVIDER_CREDENTIAL',
    durationMs: Date.now() - started,
  };
} catch (error) {
  report = { status: 'FAIL', error: String(error), durationMs: Date.now() - started };
  process.exitCode = 2;
} finally {
  await bridge.close();
  await rm(workspace, { recursive: true, force: true });
}
const target = resolve('manifests/bridge-smoke-report.json');
await writeFile(target, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
