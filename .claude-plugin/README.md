# cc-playground Plugin

Claude Code plugin for cc-playground.

## Overview

This plugin extends Claude Code with additional skills and capabilities.

## Installation

Add this plugin to your Claude Code configuration:

```bash
claude plugin install <path-to-this-repo>
```

## Skills

- **daily-briefing**: Generate daily briefing summaries including weather, news, calendar events, and task priorities

## Development

### Adding New Skills

1. Create a new directory under `.claude-plugin/skills/`
2. Add a `SKILL.md` file with the skill configuration
3. Update `marketplace.json` to reference the new skill (use `./skills/skill-name`)

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
