import discord
from discord.ext import commands
import sqlite3 as db
import os, random

bot = commands.Bot(command_prefix='-')
print("Starting...")

# @bot.event
# async def on_typing(channel, user, when):
#     print("typing")

@bot.command()
async def test(ctx):
    print(ctx.message.author)



@bot.command()
@commands.has_role("KlenBarel - Official Members")
async def create_invite(ctx):
    print("recieved")
    url = await ctx.channel.create_invite(max_age=3600, max_uses=1)
    await ctx.send("Invite link generated (1 use): \n" + str(url))

@bot.command()
async def mgamble(ctx, value: int):
    if value==random.randint(0,1):
        await ctx.send("You have won!")
    else:
        await ctx.send("Better luck next time!")

@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        print("test")
        await ctx.send('Invalid command!')


token_data = open(os.path.join("data", "token"))
bot.run(token_data.readline())
token_data.close()

def create_db_connection():
    try:
        data = os.path.join("data", "barelbotdat.db")
        conn = db.connect(data)
        cur = conn.cursor()
        cur.execute("SELECT * FROM members")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except db.Error as e:
        print(e)
