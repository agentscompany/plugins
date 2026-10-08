# Mercado Livre

Sales, visits, listing quality and questions through the official API; edit listings and answer buyers with your approval.

## How it connects

The official Mercado Livre API, through the Agents Company app registered in Mercado Livre's DevCenter (OAuth with PKCE). Mercado Livre only accepts a fixed HTTPS redirect, so sign-in lands on `https://auth.agentscompany.ai/mercadolivre` ([agentscompany/auth](https://github.com/agentscompany/auth)), a static page that hands the result to the app on your own computer. Tokens stay in your Agents Company daemon; agents never see them. Mercado Livre's official MCP server only searches the developer docs, so the tools are ours, on top of the API.

## What agents can do

- Read your account and reputation, listings, listing quality, visits, orders and buyer questions
- Answer questions, edit a listing (title, price, stock, status) and its description, always after you approve the exact change

## Permissions

The app asks for read and write on users, pre/post-sale messaging, publishing and sync, advertising, promotions and sales and shipping, plus read on billing and business metrics. Every change on your behalf needs your confirmation first, and you can switch off any tool in the app.
