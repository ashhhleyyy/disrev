# DisRev

A Discord-Revolt chat bridge.

## Configuration
DisRev is configured using `dotenv` and the following environment variables:
```
REVOLT_TOKEN
REVOLT_CHANNEL
DISCORD_TOKEN
DISCORD_CHANNEL
DISCORD_WEBHOOK
```

## Compatibility
DisRev should be compatible with proxying bots such as PluralKit, as it will forward messages from other webhooks and bots.

## TODO list
- [ ] Bridge embeds both ways (waiting for revolt.py to implement embeds)
- [ ] Use webhooks on revolt side for custom username+avatar when they are implemented
