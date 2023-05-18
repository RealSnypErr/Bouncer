import discord
from discord.ext import commands

token = Token here
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
    log_channel = await client.fetch_channel(LOG CHANNEL ID HERE)
    if member.bot:
        if member.id not in authorized_bots:
            print(f"Bot {member.id} isnt authorized")
            await member.kick(reason="Bot not authorized")
            msg = (f"**-----------------** \nBot name: {member.name}\nBot ID: {member.id}\n**Check audit log to check who invited the bot**")
            embed=discord.Embed(title="**UNAUTHORIZED BOT KICKED**", description=(f"Contact {client.owner} or any available Moderator/Whitelister to whitelist this bot"), color=0xff0000)
            embed.add_field(name=(msg), value="**-----------------**", inline=False)
            embed.set_footer(text="Bouncer rev.1")
            await log_channel.send(embed=embed)

@client.command()
@commands.has_role(WHITELISTER ROLE HERE)
async def add(ctx, id):
    global authorized_bots
    await ctx.send(f"Adding bot {id} (<@{id}>) to the whitelist")
    with open("whitelist.txt", "a") as file:
        file.write(f"\n{id}")

    authorized_bots = []
    with open("whitelist.txt", "r") as file:
        data = file.read().strip()
        authorized_bots = data.split("\n")
        authorized_bots = [int(i) for i in authorized_bots]


            
client.run(token=token)
