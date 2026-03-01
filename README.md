# cc-playground

A curated directory of plugins for Claude Code.

> **⚠️ Important:** Make sure you trust a plugin before installing, updating, or using it. The plugin author does not control what MCP servers, files, or other software are included in plugins and cannot verify that they will work as intended or that they won't change. See each plugin's documentation for more information.

## Structure

- **`/plugins`** - Plugins for daily productivity and utility
- **`/external_plugins`** - Third-party plugins from partners and the community (optional)

## Installation

Plugins can be installed directly from this marketplace via Claude Code's plugin system.

To install, run `/plugin install {plugin-name}@cc-playground`

or browse for the plugin in `/plugin > Discover`

## Available Plugins

### daily-use

Collection of daily utility skills for productivity and information gathering.

**Skills:**
- **daily-briefing**: Generate daily briefing summaries including weather, news, calendar events, and task priorities

## Contributing

### Adding Plugins

1. Create a new plugin directory under `plugins/` (e.g., `plugins/my-plugin/`)
2. Add `.claude-plugin/plugin.json` with plugin metadata
3. Add a `README.md` for plugin documentation
4. Create appropriate directories (commands/, agents/, skills/)
5. Update root `.claude-plugin/marketplace.json` to reference the new plugin

### Plugin Structure

Each plugin follows a standard structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata (required)
├── commands/            # Slash commands (optional)
├── agents/              # Agent definitions (optional)
├── skills/              # Skill definitions (optional)
└── README.md            # Documentation
```

## Documentation

For more information on developing Claude Code plugins, see the [official documentation](https://code.claude.com/docs/en/plugins).
