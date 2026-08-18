# mem0 (Hermes Agent plugin)

Mem0 memory management plugin. Store, search, update, and organize memories with semantic search, batch operations, file attachments, and change history tracking via MCP tools.

## Install

Recommended (git-clone install, if this bundle is pushed to its own repo):

```bash
hermes plugins install <org>/mem0
```

Manual (flattened) install:

```bash
mkdir -p ~/.hermes/plugins/mem0
cp .hermes-plugin/plugin.yaml .hermes-plugin/__init__.py ~/.hermes/plugins/mem0/
cp -r skills ~/.hermes/plugins/mem0/
```

## Skills (5)

- `examples` — Tool call patterns, end-to-end workflow examples, and scenario references. This skill should be used when the user needs reference implementations, complete examples, or tool call patterns.
- `file-management` — File management — attach files to memories and search file content via vector search. This skill should be used when the user asks to upload documents, attach files, or search within attached files.
- `history-tracking` — Memory history and change tracking — view evolution of memories over time, audit modifications, and track knowledge changes. This skill should be used when the user asks to see memory changes, audit modifications, or track how information evolved.
- `memory-crud` — Memory CRUD operations — add, get, update, delete memories, and batch operations. This skill should be used when the user asks to create, read, update, or delete memories, or perform bulk memory management.
- `search-retrieval` — Search and retrieval — semantic search, listing, filtering, and relevance tuning. This skill should be used when the user asks to find memories, search knowledge, list stored information, or tune search results.

## Not carried over

- 2 agent(s) — no Hermes manifest equivalent
- 11 command(s) — no Hermes manifest equivalent
- MCP servers — not generated for Hermes

## Source

Canonical: https://github.com/agents-store/claude-public-plugins/tree/main/plugins/mem0
