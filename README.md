# Agents Company plugins

The catalog of apps that [Agents Company](https://agentscompany.ai) agents can use on your behalf: Gmail, Google Calendar, GitHub, Jira and more. Each plugin says what it does, how it connects and which permissions it asks for, so you can check exactly what an agent can reach before you connect it.

This repository is **data only**: manifests, logos and docs. It never contains scripts or code that runs on your machine.

## Layout

```
plugins/<id>/
  plugin.json   name, description, category (and categories), developer, website, connection
  logo.svg      (and logo-dark.svg when the logo needs a dark-mode variant)
  README.md     what agents can and can't do, and the permissions requested
```

`catalog.json` is the index the app reads (every 6 hours, with an offline copy). It is rebuilt from the plugin folders by `scripts/build-catalog.py`, which CI also runs on every push. A new plugin of type `mcp-oauth` whose server supports dynamic client registration works in the app without a new release; other types still need app support.

## Connection types

| Type | How it works |
|---|---|
| `mcp-oauth` | The service's official remote MCP server. You sign in with OAuth to the Agents Company app; tokens stay in your Agents Company daemon and agents never see them. |
| `api-key` | You paste an API key once in the app. It stays in the daemon; agents never see it. |
| `cli-tool` | The service's official CLI, installed on the workspace computer, with its own login. |
| `agent-cli` | An agent CLI (Claude Code, Codex, Cursor, Grok, opencode) used as an agent's brain, signed in to your account; Cursor and Codex also take work from other agents. |
| `browser` | The agent's own browser profile. You sign in yourself by taking over the screen; agents never type passwords. |

In every case, anything that changes something on your behalf (sending, publishing, editing, approving) needs your confirmation first.

## Contributing

Suggest a plugin or a fix with a pull request. A new plugin needs a `plugin.json` following the existing ones, a square SVG logo and a README that lists what agents can and can't do. Plugins are reviewed before they appear in the app.

## License

MIT for the manifests and docs. Logos are trademarks of their respective owners and are used only to identify their services.
