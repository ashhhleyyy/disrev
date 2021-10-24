from typing import Union
import revolt
from config import DISCORD_WEBHOOK, REVOLT_CHANNEL
from dhooks import Webhook


class DisrevController:
    def __init__(self) -> None:
        self.revolt: Union[revolt.Client, None] = None
        self.discord_webhook: Union[Webhook, None] = None

    def configure_revolt(self, revolt_client: revolt.Client):
        self.revolt = revolt_client

    def configure_discord(self):
        self.discord_webhook = Webhook.Async(url=DISCORD_WEBHOOK)

    async def send_to_revolt(self, author: str, message: str):
        if not self.revolt:
            return

        channel: revolt.TextChannel = self.revolt.get_channel(REVOLT_CHANNEL)
        if channel:
            await channel.send(f"[{author}] {message}")

    async def send_to_discord(self, username: str, avatar: str, message: str):
        if not self.discord_webhook:
            return

        await self.discord_webhook.send(content=message, username=username, avatar_url=avatar)
