#!/usr/bin/env node
import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { mkdtemp, rm, writeFile, mkdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import readline from 'node:readline';

const VERSION = process.env.RUFLO_VERSION || '3.38.19';
const REPORT = resolve(process.argv[2] || 'ruflo_bridge/manifests/smoke-report.json');
const TIMEOUT_MS = 30000;

function hash(value) {
  return createHash('sha256').update(JSON.stringify(value)).digest('hex');
}

function parseToolResult(response) {
  const content = response?.result?.content;
  if (!Array.isArray(content)) return response?.result;
  const text = content.find((item) => item.type === 'text')?.text;
  if (!text) return response.result;
  try { return JSON.parse(text); } catch { return { text }; }
}

async function main() {
  const workspace = await mkdtemp(join(tmpdir(), 'ocp-ruflo-smoke-'));
  const childEnv = { ...process.env, NO_COLOR: '1', CLAUDE_FLOW_TELEMETRY_ENABLED: 'false' };
  delete childEnv.ANTHROPIC_API_KEY;
  delete childEnv.OPENROUTER_API_KEY;
  delete childEnv.OLLAMA_API_KEY;
  const child = spawn('npx', ['--yes', `ruflo@${VERSION}`, 'mcp', 'start'], {
    cwd: workspace,
    stdio: ['pipe', 'pipe', 'pipe'],
    env: childEnv,
  });
  const pending = new Map();
  let nextId = 1;
  let stderr = '';
  child.stderr.setEncoding('utf8');
  child.stderr.on('data', (chunk) => { stderr = (stderr + chunk).slice(-16000); });
  const lines = readline.createInterface({ input: child.stdout });
  lines.on('line', (line) => {
    let message;
    try { message = JSON.parse(line); } catch { return; }
    if (message.id !== undefined && pending.has(message.id)) {
      const { resolve: done, timer } = pending.get(message.id);
      clearTimeout(timer);
      pending.delete(message.id);
      done(message);
    }
  });

  function send(method, params = {}) {
    const id = nextId++;
    return new Promise((done, reject) => {
      const timer = setTimeout(() => {
        pending.delete(id);
        reject(new Error(`MCP timeout: ${method}`));
      }, TIMEOUT_MS);
      pending.set(id, { resolve: done, reject, timer });
      child.stdin.write(JSON.stringify({ jsonrpc: '2.0', id, method, params }) + '\n');
    });
  }

  function notify(method, params = {}) {
    child.stdin.write(JSON.stringify({ jsonrpc: '2.0', method, params }) + '\n');
  }

  const started = Date.now();
  let report;
  try {
    const initialize = await send('initialize', {
      protocolVersion: '2024-11-05',
      capabilities: {},
      clientInfo: { name: 'ocp-ruflo-certifier', version: '1.0.0' },
    });
    if (initialize.error) throw new Error(`initialize error: ${JSON.stringify(initialize.error)}`);
    notify('notifications/initialized');
    const listed = await send('tools/list');
    if (listed.error) throw new Error(`tools/list error: ${JSON.stringify(listed.error)}`);
    const tools = listed.result?.tools || [];
    const byName = new Map(tools.map((tool) => [tool.name, tool]));
    const required = [
      'system_health', 'swarm_init', 'swarm_status', 'swarm_shutdown',
      'agent_spawn', 'agent_status', 'agent_terminate', 'agent_execute',
    ];
    const missing = required.filter((name) => !byName.has(name));

    const calls = {};
    const healthResponse = await send('tools/call', {
      name: 'system_health', arguments: { deep: false },
    });
    calls.system_health = parseToolResult(healthResponse);

    const swarmResponse = await send('tools/call', {
      name: 'swarm_init',
      arguments: {
        topology: 'hierarchical', maxAgents: 4, strategy: 'balanced',
        config: { autoScaling: false, communicationProtocol: 'message-bus' },
      },
    });
    calls.swarm_init = parseToolResult(swarmResponse);
    const swarmId = calls.swarm_init?.swarmId || calls.swarm_init?.data?.swarmId;

    const spawnResponse = await send('tools/call', {
      name: 'agent_spawn',
      arguments: {
        agentType: 'architect', agentId: 'ocp-cert-agent', swarmId,
        model: 'haiku', task: 'Certification registration only; do not execute.',
      },
    });
    calls.agent_spawn = parseToolResult(spawnResponse);

    const negativeExecuteResponse = await send('tools/call', {
      name: 'agent_execute',
      arguments: { agentId: 'ocp-cert-agent', prompt: 'Return the word test.', maxTokens: 8 },
    });
    calls.agent_execute_without_credentials = parseToolResult(negativeExecuteResponse);

    const statusResponse = await send('tools/call', {
      name: 'agent_status', arguments: { agentId: 'ocp-cert-agent' },
    });
    calls.agent_status = parseToolResult(statusResponse);

    const swarmStatusResponse = await send('tools/call', {
      name: 'swarm_status', arguments: { swarmId, includeAgents: true, includeMetrics: true },
    });
    calls.swarm_status = parseToolResult(swarmStatusResponse);

    const terminateResponse = await send('tools/call', {
      name: 'agent_terminate', arguments: { agentId: 'ocp-cert-agent', graceful: true },
    });
    calls.agent_terminate = parseToolResult(terminateResponse);

    const shutdownResponse = await send('tools/call', {
      name: 'swarm_shutdown', arguments: { swarmId, graceful: true },
    });
    calls.swarm_shutdown = parseToolResult(shutdownResponse);

    report = {
      reportVersion: '1.0',
      rufloVersion: VERSION,
      protocolVersionRequested: '2024-11-05',
      protocolVersionReturned: initialize.result?.protocolVersion,
      serverInfo: initialize.result?.serverInfo,
      toolsCount: tools.length,
      requiredTools: Object.fromEntries(required.map((name) => [name, {
        present: byName.has(name),
        schemaSha256: byName.has(name) ? hash(byName.get(name).inputSchema) : null,
      }])),
      missing,
      calls,
      agentExecute: {
        status: calls.agent_execute_without_credentials?.success === false
          ? 'NEGATIVE_PATH_PASS' : 'UNEXPECTED_RESULT',
        reason: 'Provider credentials were explicitly removed; execution must fail closed',
      },
      durationMs: Date.now() - started,
      stderrTail: stderr,
      status: missing.length === 0 && calls.agent_execute_without_credentials?.success === false
        ? 'SMOKE_PASS_EXECUTION_PENDING' : 'FAIL',
    };
  } catch (error) {
    report = {
      reportVersion: '1.0', rufloVersion: VERSION, status: 'FAIL',
      error: String(error), durationMs: Date.now() - started, stderrTail: stderr,
    };
    process.exitCode = 2;
  } finally {
    child.stdin.end();
    await new Promise((done) => {
      const timer = setTimeout(() => { child.kill('SIGKILL'); done(); }, 5000);
      child.once('exit', () => { clearTimeout(timer); done(); });
    });
    await rm(workspace, { recursive: true, force: true });
  }
  await mkdir(resolve(REPORT, '..'), { recursive: true });
  await writeFile(REPORT, JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report, null, 2));
}

main().catch((error) => { console.error(error); process.exit(2); });
