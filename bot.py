import discord
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('present ma\'am'):
        await message.channel.send('no attendance for u!')
client.run('OTM5MzU1OTQ2NTEyMTc5MjQw.Yf3pZg.pI2P_GK92BAIj8ec3e8NE_Mfnpg')