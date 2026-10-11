# Tripo

AI 3D models: agents turn text or images into 3D assets and download them, with your Tripo account.

## How it connects

Tripo's official MCP server (`https://developers.tripo3d.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Each generation uses your Tripo credits, so agents ask before generating.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
