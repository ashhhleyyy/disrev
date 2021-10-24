from config import DISCORD_TOKEN, DISCORD_WEBHOOK
from controller import DisrevController
import hikari
import re

WEBHOOK_ID_FROM_URL_REGEX = re.compile(r"^https:\/\/(ptb\.|canary\.)?discord\.com\/api\/webhooks/([0-9]*)/.*$")


def get_webhook_id_from_url(url: str) -> str:
    return WEBHOOK_ID_FROM_URL_REGEX.fullmatch(url).group(2)


async def run_discord(controller: DisrevController):
    client = hikari.GatewayBot(token=DISCORD_TOKEN)

    webhook_id = get_webhook_id_from_url(DISCORD_WEBHOOK)

    @client.listen()
    async def on_ready(event: hikari.StartedEvent):
        print(f'Logged into Discord as {client.get_me().username}')
        controller.configure_discord()

    @client.listen()
    async def on_message(event: hikari.GuildMessageCreateEvent):
        if event.message.author.id == client.get_me().id or event.message.author.is_system:
            return

        if str(event.message.author.id) == webhook_id:
            return

        if not event.message.content:
            return

        display_name = event.message.member.display_name if event.message.member else event.message.author.username
        if event.message.author.discriminator != '0000':
            display_name += f'#{event.message.author.discriminator}'

        print(f'[Discord] [#{event.get_channel().name}] {display_name}: {event.message.content}')

        await controller.send_to_revolt(display_name, event.message.content)

    print('Starting Discord client...')
    await client.start()
