# Supabase

Postgres projects: agents run SQL, manage tables and migrations, read logs and deploy edge functions.

## How it connects

Supabase's official MCP server (`https://mcp.supabase.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE; the server issues a client secret, which stays in your daemon). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (deploying, running write SQL, changing settings) needs your confirmation first.
