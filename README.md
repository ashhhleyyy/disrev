# DisRev

A Discord-Revolt chat bridge.

## Configuration (new, multi-channel mode)

Use a JSON-based config file for multi channel mode:
```json
{
    "discord_to_revolt": {
        "xxx": "xxx"
    },
    "revolt_to_webhook": {
        "xxx": "https://discord.com/api/webhooks/xxx/xxx"
    }
}
```

and the following environment variables (supports `dotenv`):
```
REVOLT_TOKEN
DISCORD_TOKEN
```

You then run in multi-channel mode with
```
poetry run src/main.py <path to config>
```

## Configuration (old, single-channel mode)
DisRev is configured in single-channel mode using `dotenv` and the following environment variables:
```
REVOLT_TOKEN
REVOLT_CHANNEL
DISCORD_TOKEN
DISCORD_CHANNEL
DISCORD_WEBHOOK
```

You then can use
```
poetry run src/main.py
```
to launch.

## Compatibility
DisRev should be compatible with proxying bots such as PluralKit, as it will forward messages from other webhooks and bots.

## TODO list
- [ ] Bridge embeds both ways (waiting for revolt.py to implement embeds)
- [ ] Use webhooks on revolt side for custom username+avatar when they are implemented
- [ ] (Maybe) bridge attachments by uploading to the other platform rather than just sending a link
