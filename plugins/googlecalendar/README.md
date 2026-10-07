# Google Calendar

See your schedule, find free time and create, edit or answer events.

## How it connects

Google's official MCP server (`https://calendarmcp.googleapis.com/mcp/v1`), with an OAuth login to the Agents Company app. Tokens stay in the user's Agents Company daemon; agents never see them.

Fallback: Google Calendar REST API (same login) while Google's MCP server is in Developer Preview.

## Permissions

calendar.readonly, calendar.events

## What agents can do

- List calendars and events, search events
- Suggest free time
- Create, update, delete and answer events (after you confirm)

## What agents don't do

- Invite people by email unless you ask (notifications are off by default)

Anything that changes something on your behalf (sending, publishing, editing, approving) needs your confirmation first.
