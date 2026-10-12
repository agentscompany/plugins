# Replicate

Thousands of AI models: agents search models and run them to generate images, video, audio and more, billed to your Replicate account.

## How it connects

Replicate's official MCP server (`https://mcp.replicate.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Every prediction is billed to your Replicate account, so agents say which model they will run and ask first.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
