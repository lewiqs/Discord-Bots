import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print ("Ready to use")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("f"):
        e = discord.Embed()
        e.set_image(url=('/images/respects.jpg'))
        await client.send_message(message.channel, embed=e)
    elif message.content.startswith("F"):
        e = discord.Embed()
        e.set_image(url=('/images/respects.jpg'))
        await client.send_message(message.channel, embed=e)
        
client.run("YOURBOTTOKEN")
