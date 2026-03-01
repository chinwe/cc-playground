# cc-playground

Claude Code plugin playground.

## Marketplace Structure

```
.claude-plugin/
├── marketplace.json          # Marketplace metadata and configuration
├── README.md                 # Marketplace documentation
└── THIRD_PARTY_NOTICES.md    # License information

plugins/                      # Plugin directory
└── daily-use/                # Daily utility plugin
    └── daily-briefing/
        └── SKILL.md          # Daily briefing skill
```

## Plugins

### daily-use
Collection of daily utility skills for productivity and information gathering.

**Skills:**
- **daily-briefing**: Generate daily briefing summaries including weather, news, calendar events, and task priorities

## Installation

```bash
# Install the plugin from this directory
claude plugin install .
```


## Development

See `.claude-plugin/README.md` for development details.