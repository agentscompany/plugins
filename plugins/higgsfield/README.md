# Higgsfield

AI video and images: agents generate clips and pictures with 30+ models (Veo, Sora, Kling, Seedance, Higgsfield Soul), using your Higgsfield credits.

## How it connects

Higgsfield's official MCP server (`https://mcp.higgsfield.ai/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Needs a paid Higgsfield plan; every generation uses your credits, so agents ask before generating.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
