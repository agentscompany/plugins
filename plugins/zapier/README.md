# Zapier

Thousands of apps without their own connector, and automations agents can set up for you.

## How it connects

Zapier's official MCP server (`https://mcp.zapier.com/api/mcp/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
