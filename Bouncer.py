import discord
from discord.ext import commands

token = "TOKEN HERE"
whitelist = open("whitelist.txt", "r")
data = whitelist.read()
authorized_bots = data.split("\n")
authorized_bots = [int(i) for i in authorized_bots]
whitelist.close()

intents=discord.Intents.all()
client = commands.Bot(command_prefix='!', description="description", intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_member_join(member):
    log_channel = client.get_channel("Log channel ID here")
    if member.bot:
        if member.id not in authorized_bots:
            await member.kick(reason="Bot not authorized")
            msg = (f"**-----------------** \nBot name: {member.name}\nBot ID: {member.id}\n**Check audit log to check who invited the bot**")
            embed=discord.Embed(title="**UNAUTHORIZED BOT KICKED**", description=(f"Place the bot's ID to whitelist this bot"), color=0xff0000)
            embed.add_field(name=(msg), value="**-----------------**", inline=False)
            embed.set_footer(text="Bouncer rev.1")
            await log_channel.send(embed=embed)
            
client.run(token=token)
