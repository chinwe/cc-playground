# cc-playground Marketplace

Claude Code plugin marketplace for daily utility skills.

## Overview

This marketplace contains plugins that extend Claude Code with productivity and information gathering capabilities.

## Installation

```bash
claude plugin install <path-to-this-repo>
```

## Plugins

### daily-use
Collection of daily utility skills for productivity and information gathering.

**Skills:**
- **daily-briefing**: Generate daily briefing summaries including weather, news, calendar events, and task priorities

## Development

### Plugin Structure

Each plugin has the following structure:

```
plugins/my-plugin/
├── .claude-plugin/
│   └── plugin.json       # Plugin metadata (name, description, author)
├── README.md             # Plugin documentation
└── skills/               # Skills directory (for skill-based plugins)
    └── skill-name/
        └── SKILL.md      # Skill definition
```

### Adding New Plugins

1. Create a new plugin directory under `plugins/` (e.g., `plugins/my-plugin/`)
2. Create `.claude-plugin/plugin.json` with plugin metadata:

```json
{
  "name": "my-plugin",
  "description": "Plugin description",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  }
}
```

3. Add a `README.md` for plugin documentation
4. Create `skills/` directory (if it's a skill-based plugin)
5. Update root `marketplace.json` to reference the new plugin

### Adding Skills to Existing Plugins

1. Create a skill directory under the plugin's `skills/` folder
2. Add a `SKILL.md` file with the skill configuration

### Skill File Format

Each skill must have a `SKILL.md` file with the following frontmatter:

```yaml
---
name: skill-name
description: Skill description
license: MIT
---
```

## License

MIT
