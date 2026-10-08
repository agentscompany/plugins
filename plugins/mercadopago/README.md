# Mercado Pago

Payments, sales and reconciliation: what came in, fees, what is still to be released and disputes.

## How it connects

Mercado Pago's official MCP server (`https://mcp.mercadopago.com/mcp`). At sign-in the Agents Company app registers itself (dynamic OAuth client registration, PKCE). Tokens stay in your Agents Company daemon; agents never see them. This plugin needs no app release: the app picks it up from `catalog.json`.

Reading is free; anything that changes something on your behalf (sending, publishing, editing, paying, deleting) needs your confirmation first.
