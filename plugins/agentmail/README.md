# AgentMail

Email inboxes for your agents: create addresses, receive, read, reply and send email, with your AgentMail account.

## How it connects

AgentMail's official MCP server (`https://mcp.agentmail.to`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, public client with PKCE). Tokens stay in your Agents Company daemon; agents never see them.

## What agents can do

- List, create and update inboxes; search and read threads and messages; attachments
- Draft, reply, forward and send email (sending needs your approval of the exact message)

Anything that changes something on your behalf needs your confirmation first.
