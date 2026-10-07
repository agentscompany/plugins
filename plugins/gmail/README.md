# Gmail

Read and search email, prepare drafts and send them, always after you approve the text.

## How it connects

Google's official MCP server (`https://gmailmcp.googleapis.com/mcp/v1`), with an OAuth login to the Agents Company app. Tokens stay in the user's Agents Company daemon; agents never see them.

Fallback: Gmail REST API (same login) while Google's MCP server is in Developer Preview.

## Permissions

gmail.readonly, gmail.compose

## What agents can do

- Search threads, read threads and messages, list labels and drafts
- Create drafts, including replies in a thread
- Send a draft, only after showing you the recipient, subject and text and getting your approval (through the Gmail API: Google's MCP server has no send tool)

## What agents don't do

- Send anything you haven't approved
- Label, archive, trash or mark as spam (needs gmail.modify, which is not requested)

Anything that changes something on your behalf (sending, publishing, editing, approving) needs your confirmation first.
