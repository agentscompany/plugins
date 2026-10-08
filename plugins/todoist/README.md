# Todoist

Tasks and projects: agents add, organize and close your to-dos.

## How it connects

Todoist's official MCP server (`https://ai.todoist.net/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
