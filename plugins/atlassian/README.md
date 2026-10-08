# Atlassian

Jira and Confluence: agents see the tickets assigned to you, comment, move status, create tasks and read and write pages.

## How it connects

Atlassian's official MCP server (`https://mcp.atlassian.com/v2/mcp`). At sign-in, the Agents Company app registers itself with Atlassian (dynamic OAuth client registration) and you pick the site to connect. Tokens stay in the user's Agents Company daemon; agents never see them. Only Atlassian Cloud sites (`*.atlassian.net`) are supported.

## Permissions

Jira and Confluence read, write and search through Atlassian's agent interface, Rovo search, and your basic profile (read:me, read:account, email, offline_access).

## What agents can do

- Search issues with JQL, read issues, create and edit issues, transition status, add comments
- Search, read, create and update Confluence pages

## Before you connect a client's or employer's site

Admins of that organization can see the connected app, and the content of tickets and pages goes to the AI models your agents use. Check their policy first.

Anything that changes something on your behalf (commenting, moving status, editing, publishing) needs your confirmation first.
