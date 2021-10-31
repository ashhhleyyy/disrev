from config import DISCORD_TOKEN
from controller import DisrevController
import hikari


async def run_discord(controller: DisrevController):
    client = hikari.GatewayBot(token=DISCORD_TOKEN)

    webhook_ids = controller.config.discord_webhook_ids

    @client.listen()
    async def on_ready(event: hikari.StartedEvent):
        print(f'Logged into Discord as {client.get_me().username}')
        controller.configure_discord()

    @client.listen()
    async def on_message(event: hikari.GuildMessageCreateEvent):
        if event.message.author.id == client.get_me().id or event.message.author.is_system:
            return

        if str(event.message.author.id) in webhook_ids:
            return

        if not event.message.content:
            return

        display_name = event.message.member.display_name if event.message.member else event.message.author.username
        if event.message.author.discriminator != '0000':
            display_name += f'#{event.message.author.discriminator}'

        print(f'[Discord] [#{event.get_channel().name}] {display_name}: {event.message.content}')

        await controller.send_to_revolt(str(event.channel_id), display_name, event.message.content)
        for attachment in event.message.attachments:
            await controller.send_to_revolt(str(event.channel_id), display_name, attachment.url)

    print('Starting Discord client...')
    await client.start()
