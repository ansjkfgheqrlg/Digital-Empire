import assert from 'node:assert/strict';
import test from 'node:test';
import { BridgeSupervisor } from '../src/supervisor.js';

test('supervisor rejects illegal transitions', () => {
  const supervisor = new BridgeSupervisor();
  assert.throws(() => supervisor.transition('READY'), /Illegal bridge transition/);
});

test('failure threshold opens and timeout permits restart', () => {
  const supervisor = new BridgeSupervisor(2, 60_000, 30_000);
  supervisor.transition('STARTING');
  supervisor.recordFailure(1000);
  supervisor.recordFailure(2000);
  assert.equal(supervisor.state, 'OPEN');
  assert.equal(supervisor.canRestart(20_000), false);
  assert.equal(supervisor.canRestart(32_001), true);
});
