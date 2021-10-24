from typing import Union
import aiohttp
import revolt
from revolt.enums import RelationshipType

from config import REVOLT_TOKEN
from controller import DisrevController


class RevoltClient(revolt.Client):
    def __init__(self, session: aiohttp.ClientSession, token: str, controller: DisrevController):
        super().__init__(session, token)
        self.controller = controller
        self.self_user: Union[revolt.User, None]
    
    async def on_ready(self):
        self.self_user = self.get_self()
        print(f'Logged into Revolt as {self.self_user.name}!')
        self.controller.configure_revolt(self)
    
    def get_self(self) -> Union[revolt.User, None]:
        for _, user in self.state.users.items():
            if user.relationship == RelationshipType.user:
                return user
        return None

    async def on_message(self, message: revolt.Message):
        if message.author.id == self.self_user.id:
            return
        
        if not isinstance(message.content, str):
            return
        
        display_name = message.author.nickname if message.author.nickname else message.author.name
        channel: revolt.TextChannel = message.channel

        print(f'[Revolt]  [#{channel.name}] {display_name}: {message.content}')

        await self.controller.send_to_discord(display_name, message.author.avatar.url, message.content)

async def run_revolt(controller: DisrevController):
    async with aiohttp.ClientSession() as session:
        client = RevoltClient(session, REVOLT_TOKEN, controller)

        print('Starting Revolt client...')
        await client.start()
