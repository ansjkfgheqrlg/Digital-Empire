# repository-adr

Analyze only the repository files explicitly listed in the validated input. Read them through the Tool Gateway, preserve path and SHA-256 evidence, and write one ADR under `adr/` through an immutable artifact grant.

The output must contain Status, Context, Decision, Consequences and Evidence. It must not infer facts about files outside scope, execute repository code, access the network or enable RuFlo.
