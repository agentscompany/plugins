# Granola

Meeting notes and transcripts: agents turn decisions into tasks and answer what was agreed.

## How it connects

Granola's official MCP server (`https://mcp.granola.ai/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
