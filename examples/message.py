"""
Before you implement this in your bot, please note that its just for testing, 
If you have a test bot and are professional with your code, you can experiment 
with different features and report the bugs in an issue
"""


from EpikCord import Client,Intents,Messageable, Embed

intents = Intents().guilds.guild_members.guild_messages.direct_messages

client = Client("your_token", intents)

@client.event
async def message_create(message):
    if message.author.id == client.user.id:
        return
    if message.content == "example test":
        message.channel = Messageable(client, message.channel_id)

        await message.channel.send(content="hello, chat testing")

client.login()