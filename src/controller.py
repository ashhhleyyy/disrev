from typing import Dict, Optional, Union
import revolt
from config import DisrevConfig
from dhooks import Webhook


class DisrevController:
    def __init__(self, config: DisrevConfig) -> None:
        self.config = config
        self.revolt: Optional[revolt.Client] = None
        self.discord_webhooks: Optional[Dict[str, Webhook]] = None

    def configure_revolt(self, revolt_client: revolt.Client):
        self.revolt = revolt_client

    def configure_discord(self):
        self.discord_webhooks = { }
        for revolt_channel, webhook in self.config.revolt_to_webhook.items():
            self.discord_webhooks[revolt_channel] = Webhook.Async(url=webhook)

    async def send_to_revolt(self, discord_channel: str, author: str, message: str):
        if not self.revolt:
            return

        channel_id = self.config.discord_to_revolt.get(discord_channel)
        
        if not channel_id:
            return

        channel: revolt.TextChannel = self.revolt.get_channel(channel_id)
        if channel:
            await channel.send(f"[{author}] {message}")

    async def send_to_discord(self, revolt_channel: str, username: str, avatar: str, message: str):
        webhook = self.discord_webhooks.get(revolt_channel)
        if webhook:
            await webhook.send(content=message, username=username, avatar_url=avatar)
