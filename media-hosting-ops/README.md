# media-hosting-ops (Hermes Agent plugin)

Media hosting operations plugin. Upload images by public URL to MinIO-based media hosting via the uploadImageToMinio MCP tool.

## Install

Recommended (git-clone install, if this bundle is pushed to its own repo):

```bash
hermes plugins install <org>/media-hosting-ops
```

Manual (flattened) install:

```bash
mkdir -p ~/.hermes/plugins/media-hosting-ops
cp .hermes-plugin/plugin.yaml .hermes-plugin/__init__.py ~/.hermes/plugins/media-hosting-ops/
cp -r skills ~/.hermes/plugins/media-hosting-ops/
```

## Skills (2)

- `examples` — Scenario walkthroughs for media hosting operations. Use when learning how to upload images or seeing practical usage patterns.
- `upload-image` — Use when the user asks to "upload image", "host image", "upload to minio", "image url to hosting", "store image", "upload picture", "get hosted url for image", "save image to hosting", "re-host image", "get a permanent url for image", "I need a stable link for this picture", "minio upload", or needs to upload an image from a public URL to media hosting. Also trigger when the user wants to store an image somewhere reliable, get a permanent/stable URL for a picture, or move an image to their own hosting — even if they don't explicitly say "upload".

## Not carried over

- 1 agent(s) — no Hermes manifest equivalent

## Source

Canonical: https://github.com/agents-store/claude-public-plugins/tree/main/plugins/media-hosting-ops
