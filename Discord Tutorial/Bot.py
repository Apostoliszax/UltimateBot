import asyncio
import datetime
import discord



def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()



messages = joined = 0


token = read_token()

client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {datetime.datetime.utcnow()}, Messages: {messages}, Members Joined: {joined} \n")

            messages = 0
            joined = 0

            await  asyncio.sleep(5)
        except Exception as e:
            print(e)

@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("tim") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="No stop that!")




@client.event
async def on_member_join(member):

    global joined
    joined += 1

    for channel in member.server.channels:
        print(f'{member} has joined a server.')
        await member.send('To blepeis?')

@client.event
async def on_message(message):

    global messages
    messages += 1

    id = client.get_guild(749320287916523550)
    channels = ["commands"]
    valid_users = ["Not me#0578", "Not me Bot#5328","Влади́мир Пу́тин#8294" ,"Teo#2291"]
    bad_words = ["bad", "stop", "45"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)


    if message.content == "!help":
        embed = discord.Embed(title="Help for commands", description="some useful commands:")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints the number of users")
        await message.channel.send(content=None, embed=embed)


    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await  message.channel.send("Hi")
        elif message.content == "!users":
            await  message.channel.send(f"""There are {id.member_count} users in this server.""")
    else:
        print((f"""User:{message.author} tried to do command {message.content}, in channel {message.channel}"""))



    







client.loop.create_task(update_stats())
client.run(token)

