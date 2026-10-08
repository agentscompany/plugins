# Linear

Issues, projects and cycles: agents read and create issues, comment, update status and plan with your Linear account.

## How it connects

Linear's official MCP server (`https://mcp.linear.app/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, public client with PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

## What agents can do

- Search and read issues, projects, cycles and comments
- Create and update issues, comment and change status (after you confirm)
