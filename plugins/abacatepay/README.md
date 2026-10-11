# AbacatePay

Brazilian payments: agents manage customers, create charges and Pix QR codes, payment links and coupons, with your AbacatePay account.

## How it connects

AbacatePay's official MCP server (`https://mcp.abacatepay.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Creating charges or coupons changes your account, so agents show the exact amount and customer and ask first.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
