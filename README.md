# cc-playground

Claude Code plugin playground.

## Plugin Structure

```
.claude-plugin/
├── marketplace.json          # Plugin metadata and configuration
├── README.md                 # Plugin documentation
├── THIRD_PARTY_NOTICES.md    # License information
└── skills/                   # Skill definitions
    └── daily-briefing/
        └── SKILL.md          # Daily briefing skill
```

## Installation

```bash
# Install the plugin from this directory
claude plugin install .
```

## Skills

- **daily-briefing**: Generate daily briefing summaries including weather, news, calendar events, and task priorities

## Development

See `.claude-plugin/README.md` for development details.