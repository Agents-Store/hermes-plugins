# n8n (Hermes Agent plugin)

n8n workflow automation plugin. Manage workflows, execute automations, configure nodes, handle credentials, monitor executions, expression syntax, node configuration patterns, and code node best practices via MCP tools.

## Install

Recommended (git-clone install, if this bundle is pushed to its own repo):

```bash
hermes plugins install <org>/n8n
```

Manual (flattened) install:

```bash
mkdir -p ~/.hermes/plugins/n8n
cp .hermes-plugin/plugin.yaml .hermes-plugin/__init__.py ~/.hermes/plugins/n8n/
cp -r skills ~/.hermes/plugins/n8n/
```

## Skills (8)

- `code-patterns` — Code node patterns — JavaScript and Python data transformation, API processing, date handling, binary data. This skill should be used when the user asks to write code in Code nodes, transform data with JavaScript or Python, or process binary data.
- `credential-tag-management` — Credentials and tags management. This skill should be used when the user asks to create or manage credentials, list service connections, organize workflows with tags, or configure authentication.
- `examples` — Tool call patterns, end-to-end workflow examples, and scenario references. This skill should be used when the user needs reference implementations, complete examples, or tool call patterns.
- `execution-monitoring` — Workflow execution, monitoring, and debugging. This skill should be used when the user asks to run a workflow, check execution status, view execution history, or debug workflow errors.
- `expression-syntax` — Expression syntax — variables, methods, JMESPath, data references. This skill should be used when the user asks to write expressions, reference data between nodes, use JMESPath, or debug expression errors.
- `node-configuration` — Node configuration — HTTP Request, Code, IF, Switch, Merge, Split In Batches, error handling. This skill should be used when the user asks to configure a specific node type, set up authentication, write conditions, or add error handling.
- `workflow-creation` — Workflow creation — node definitions, connections, triggers, workflow structure. This skill should be used when the user asks to create a new workflow, build an automation, set up triggers, or scaffold a workflow structure.
- `workflow-editing` — Workflow editing — adding/removing nodes, updating connections, modifying node parameters. This skill should be used when the user asks to edit, modify, or update an existing workflow, add or remove nodes, or change node settings.

## Not carried over

- 2 agent(s) — no Hermes manifest equivalent
- 9 command(s) — no Hermes manifest equivalent
- MCP servers — not generated for Hermes

## Source

Canonical: https://github.com/agents-store/claude-public-plugins/tree/main/plugins/n8n
