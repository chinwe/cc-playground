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

### Adding New Plugins

1. Create a new plugin directory under `plugins/` (e.g., `plugins/my-plugin/`)
2. Add skill directories under the plugin folder
3. Update `marketplace.json` to reference the new plugin:

```json
{
  "plugins": [
    {
      "name": "my-plugin",
      "description": "Plugin description",
      "version": "0.1.0",
      "author": {
        "name": "Your Name",
        "email": "your.email@example.com"
      },
      "source": "./plugins/my-plugin",
      "category": "productivity",
      "strict": false
    }
  ]
}
```

### Adding Skills to Existing Plugins

1. Create a skill directory under the plugin folder (e.g., `plugins/daily-use/my-skill/`)
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
