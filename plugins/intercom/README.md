# Intercom

Customer support: agents read conversations and tickets and draft replies.

## How it connects

Intercom's official MCP server (`https://mcp.intercom.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
