# Meshy

AI 3D models: agents generate models from text or images, add texture, rigging and animation, and download the files, with your Meshy account.

## How it connects

Meshy's official CLI ([meshy-cli](https://github.com/meshy-dev/meshy-cli)), installed on the workspace computer the first time you connect (with Node.js 22 if it is missing). You sign in with a code: the app shows a link and a code, you open the link in your browser and type the code. The login stays on the workspace computer and is shared by all agents there.

Meshy has no hosted MCP server for other apps (its MCP server runs locally with an API key), so this plugin uses the CLI.

Every generation uses your Meshy credits, so agents say what they will generate and ask first.
