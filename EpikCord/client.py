from typing import (
    List
)
from .exceptions import InvalidArgumentType
from .section import Section
from .ws import WebsocketClient
from .application import Application, ApplicationCommand
from .route import Route
from aiohttp import ClientSession

class HTTPClient:
    def __init__(self, *args, **kwargs):
        self.session = ClientSession(*args, **kwargs)
        self.base_uri: str = "https://discord.com/api/v9"

    async def get(self, url, *args, **kwargs):
        return await self.session.get(f"{self.base_uri}{url}", *args, **kwargs)

    async def post(self, url, *args, **kwargs):
        return await self.session.post(f"{self.base_uri}{url}", *args, **kwargs)

    async def patch(self, url, *args, **kwargs):
        return await self.session.patch(f"{self.base_uri}{url}", *args, **kwargs)

    async def delete(self, url, *args, **kwargs):
        return await self.session.delete(f"{self.base_uri}{url}", *args, **kwargs)

    async def put(self, url, *args, **kwargs):
        return await self.session.put(f"{self.base_uri}{url}", *args, **kwargs)

    async def head(self, url, *args, **kwargs):
        return await self.session.head(f"{self.base_uri}{url}", *args, **kwargs)


class Client(WebsocketClient):

    def __init__(self, token: str, intents: int = 0, **options):
        super().__init__(token, intents)
        
        self.commands: List[ApplicationCommand] = []
        
        self.options: dict = options

        self.http = HTTPClient(
            headers = {"Authorization": f"Bot {token}"}
            )
        self.api = Route
        # self.application: Application = Application(self, self.user) # Processes whatever it can        

    def add_section(self, section: Section):
        if not isinstance(section, Section):
            raise InvalidArgumentType("You must pass in a class that inherits from the Section class.")
        for name, command_object in section.commands:
            self.commands[name] = command_object

        for event_name, event_func in section.events:
            self.events[event_name.lower().replace("on_")] = event_func
        
        # Successfully extracted all the valuable stuff from the section        

# class ClientUser(User):
    
#     def __init__(self, client: Client, data: dict):
#         super().__init__(data)
    
#     async def fetch(self):
#         response = await self.client.http.get("users/@me")
#         data = await response.json()
#         super().__init__(data) # Reinitialse the class with the new data.
    
# class ClientGuildMember(Member):
#     def __init__(self, client: Client,data: dict):
#         super().__init__(data)