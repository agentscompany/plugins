# PostHog

Product analytics, feature flags and experiments: agents answer how users use your product.

## How it connects

PostHog's official MCP server (`https://mcp.posthog.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
