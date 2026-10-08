# Figma

Agents read files and frames, export screens as images and read and write comments, with your Figma account.

## How it connects

The Figma REST API through the Agents Company app (OAuth with PKCE). Figma's official MCP server only accepts clients from its catalog, and new clients are paused for now, so the tools are ours, on top of the API. Sign-in returns through `https://auth.agentscompany.ai/figma` ([agentscompany/auth](https://github.com/agentscompany/auth)). Tokens stay in your Agents Company daemon; agents never see them.

## What agents can do

- Read a file's pages and frames, and the details of frames and layers (text, styles, colors, sizes, layout)
- Export frames as images to look at the actual screen
- Read comments and versions; list team projects and files
- Post comments (after you approve the text)
