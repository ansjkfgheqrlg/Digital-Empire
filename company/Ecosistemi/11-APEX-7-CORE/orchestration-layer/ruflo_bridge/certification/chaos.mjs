#!/usr/bin/env node
import { mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { RufloMcpClient } from '../dist/src/mcp_client.js';
import { validateToolSchemas } from '../dist/src/validator.js';

const manifest = JSON.parse(await readFile('manifests/tool-schema-hashes.json', 'utf8'));
const expected = Object.fromEntries(
  ['system_health', 'swarm_init', 'agent_spawn', 'agent_execute']
    .map((name) => [name, manifest.tools[name]])
);
const workspace = await mkdtemp(join(tmpdir(), 'ocp-ruflo-chaos-'));
const report = { rufloVersion: manifest.rufloVersion, sourceCommit: manifest.sourceCommit };
let first;
let second;
try {
  first = new RufloMcpClient(manifest.rufloVersion, workspace, 10_000);
  await first.start();
  validateToolSchemas(await first.listTools(), expected);
  report.initialHandshake = 'PASS';
  report.sigkillSent = first.terminate('SIGKILL');
  await new Promise((resolvePromise) => setTimeout(resolvePromise, 500));
  try {
    await first.listTools();
    report.postKillCall = 'UNEXPECTED_SUCCESS';
  } catch {
    report.postKillCall = 'REJECTED';
  }

  second = new RufloMcpClient(manifest.rufloVersion, workspace, 10_000);
  await second.start();
  validateToolSchemas(await second.listTools(), expected);
  const health = await second.callTool('system_health', { deep: false });
  report.restartHandshake = 'PASS';
  report.healthAfterRestart = health.overall ?? 'unknown';
  report.status = report.sigkillSent && report.postKillCall === 'REJECTED' ? 'PASS' : 'FAIL';
} catch (error) {
  report.status = 'FAIL';
  report.error = String(error);
  process.exitCode = 2;
} finally {
  await first?.close();
  await second?.close();
  await rm(workspace, { recursive: true, force: true });
}
await writeFile(resolve('manifests/chaos-report.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
