# stack-composable-stack-v1 (Hermes Agent plugin)

Composable Stack v1 dev plugin. Integrates PostgreSQL (direct MCP + PostgREST API), NocoDB, n8n, Trigger.dev, and NocoBase (prod + dev sandbox via nc-mcp) for building data-driven applications with low-code interfaces.

## Install

Recommended (git-clone install, if this bundle is pushed to its own repo):

```bash
hermes plugins install <org>/stack-composable-stack-v1
```

Manual (flattened) install:

```bash
mkdir -p ~/.hermes/plugins/stack-composable-stack-v1
cp .hermes-plugin/plugin.yaml .hermes-plugin/__init__.py ~/.hermes/plugins/stack-composable-stack-v1/
cp -r skills ~/.hermes/plugins/stack-composable-stack-v1/
```

## Skills (7)

- `background-job` — This skill should be used when the user wants to "create a background job", "run async task", "process data in background", "schedule recurring task", "set up a queue", or needs patterns for background processing using Trigger.dev and n8n in the Composable Stack.
- `full-feature` — This skill should be used when the user wants to "build a complete feature", "create end-to-end functionality", "implement a full feature across all layers", "build feature with data model and automation", or needs a step-by-step recipe for building features that span the Data, Logic, and Interface layers of the Composable Stack.
- `init-project` — This skill should be used when the user asks to "set up composable stack", "initialize project", "configure environment", "connect MCP services", or needs to set up all MCP connections and environment variables for the Composable Stack v1.
- `nocobase-to-n8n` — This skill should be used when the user wants to "trigger n8n from NocoBase", "connect NocoBase UI to n8n", "automate NocoBase actions with n8n", "create NocoBase workflow that calls n8n", or needs to integrate NocoBase interface events with n8n workflow automation.
- `nocodb-to-n8n` — This skill should be used when the user wants to "trigger n8n workflow from NocoDB", "connect NocoDB data to n8n", "create webhook from NocoDB to n8n", "automate NocoDB with n8n", or needs to integrate NocoDB data events with n8n workflow automation.
- `nocodb-to-trigger` — This skill should be used when the user wants to "trigger background task from NocoDB", "connect NocoDB to Trigger.dev", "process NocoDB data with Trigger.dev", "run background job on NocoDB change", or needs to integrate NocoDB data events with Trigger.dev background tasks.
- `postgresql-api` — This skill should be used when the user wants to "query PostgreSQL directly", "use PostgREST API", "make REST calls to PostgreSQL", "use postgresql-mcp tools", "run SQL via MCP", "check database status", "inspect database schema", "analyze query performance", or needs to perform direct database operations via PostgreSQL MCP tools or PostgREST REST API in the Composable Stack.

## Not carried over

- 1 agent(s) — no Hermes manifest equivalent
- MCP servers — not generated for Hermes

## Source

Canonical: https://github.com/agents-store/claude-public-plugins/tree/main/plugins/stack-composable-stack-v1
