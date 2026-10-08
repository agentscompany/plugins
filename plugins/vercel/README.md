# Vercel

Projects and deployments: agents check deploys, read build and runtime logs and search the Vercel docs.

## How it connects

Vercel's official MCP server (`https://mcp.vercel.com`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (deploying, running write SQL, changing settings) needs your confirmation first.
