# Context7

Up-to-date library documentation for coding, so agents don't rely on outdated APIs.

## How it connects

Context7's official MCP server (`https://mcp.context7.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
