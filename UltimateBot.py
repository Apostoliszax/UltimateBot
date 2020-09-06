import discord
import random


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()



token = read_token()

client = discord.Client()


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):

    channels = ["commands"]

    id = client.get_guild(750780023266476043)

    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
        "The way to get started is to quit talking and begin doing. -Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
        "Life is what happens when you're busy making other plans. -John Lennon",
        "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa",
        "When you reach the end of your rope, tie a knot in it and hang on. -Franklin D. Roosevelt",
        "The purpose of our lives is to be happy. -Dalai Lama"]

    dadJokes = [
        "Today, my son asked ~Can I have a book mark?~ and I burst into tears. 11 years old and he still doesn't know my name is Brian.",
        "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right.",
        "How do you make holy water? You boil the hell out of it.",
        "I bought some shoes from a drug dealer. I don't know what he laced them with, but I was tripping all day!",
        "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.",
        "If a child refuses to sleep during nap time, are they guilty of resisting a rest?",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "What do you call someone with no body and no nose? Nobody knows.",
        "I ordered a chicken and an egg from Amazon. I’ll let you know",
        "What is the least spoken language in the world? Sign language",
        "A slice of apple pie is $2.50 in Jamaica and $3.00 in the Bahamas. These are the pie rates of the Caribbean.",
        "Justice is a dish best served cold, if it were served warm it would be justwater."]

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send(f"Hello {message.author.name}")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
        elif message.content.find("!quote") != -1:
            await  message.channel.send(random.choice(quotes))
        elif message.content.find("!dadjoke") != -1:
            await  message.channel.send(random.choice(dadJokes))

    if message.content == "!help":
        embed = discord.Embed(title="Hello . Let me help", description="Here are all the commands you'll need")
        embed.add_field(name="!hello", value="Say hello to your little friends")
        embed.add_field(name="!users", value="You'll get to know just how many we are in here")
        embed.add_field(name="!quote", value="Shows you some inspirational quotes to get out of your misery")
        embed.add_field(name="!dadjoke", value="Tells a joke your dad would say to you. If he hadn't left you")
        await message.channel.send(content=None, embed=embed)


client.run(token)
