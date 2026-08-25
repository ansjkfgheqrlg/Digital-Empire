import assert from 'node:assert/strict';
import test from 'node:test';
import { schemaHash, validateToolSchemas } from '../src/validator.js';

test('stable schema hash is deterministic', () => {
  const schema = { type: 'object', required: ['x'] };
  assert.equal(schemaHash(schema), schemaHash(schema));
});

test('missing tool fails closed', () => {
  assert.throws(() => validateToolSchemas([], { agent_execute: 'x' }), /CAPABILITY_MISMATCH/);
});
