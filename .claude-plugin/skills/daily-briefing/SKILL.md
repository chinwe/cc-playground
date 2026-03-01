---
name: daily-briefing
description: Generate daily briefing summaries including weather, news, calendar events, and task priorities. Use this when users request a daily summary, morning briefing, or daily overview.
license: MIT
---

# Daily Briefing

Generate comprehensive daily briefings to help users start their day organized and informed.

## When to Use

- User requests "daily briefing", "morning summary", or "daily overview"
- User asks "what's on my agenda today?" or "what should I focus on?"
- User wants a summary of news, weather, or upcoming events

## Briefing Components

### 1. Header Section
- Current date and day of week
- Greeting based on time of day

### 2. Weather (if applicable)
- Current conditions
- Temperature
- Forecast for the day

### 3. News Summary
- Top 3-5 headlines
- Brief one-sentence summaries

### 4. Calendar/Agenda
- Upcoming meetings or events
- Time slots and durations

### 5. Priority Tasks
- Top 3 priorities for the day
- Quick action items

## Output Format

Use a clean, structured markdown format with clear section headers and bullet points.

## Example

```markdown
# Good Morning! 🌅
**Thursday, March 1, 2026**

## 🌤️ Weather
Currently 65°F, partly cloudy. High of 72°F expected today.

## 📰 News Highlights
- Tech giant announces new AI capabilities
- Markets show steady growth amid economic indicators
- Climate summit reaches key agreements

## 📅 Today's Agenda
- 9:00 AM - Team standup (30 min)
- 11:00 AM - Design review (1 hour)
- 3:00 PM - Client call (45 min)

## 🎯 Top Priorities
1. Complete project proposal draft
2. Review and respond to urgent emails
3. Prepare for tomorrow's presentation
```
