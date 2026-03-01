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

1. Create a new plugin directory in the project root (e.g., `my-plugin/`)
2. Add skill directories under the plugin folder
3. Update `marketplace.json` to reference the new plugin:

```json
{
  "plugins": [
    {
      "name": "my-plugin",
      "description": "Plugin description",
      "source": "./",
      "strict": false,
      "skills": ["./my-plugin/skill-name"]
    }
  ]
}
```

### Adding Skills to Existing Plugins

1. Create a skill directory under the plugin folder (e.g., `daily-use/my-skill/`)
2. Add a `SKILL.md` file with the skill configuration
3. Update `marketplace.json` to add the skill to the plugin's skills array

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
