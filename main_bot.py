import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True


bot=commands.Bot(command_prefix="/",intents=intents)

#Savoir si le bot est prêt
@bot.event
async def on_ready():
    print("Le bot est prêt")

@bot.command(name='del') # On précise le nom de la commande soit (/del)
async def delte(ctx,number_of_message:int):  #Plusieurs parametres on met ctx le context
    #messages=await ctx.channel.history(limit=number_of_message+1).flatten()
    messages=[msg async for msg in ctx.channel.history(limit=number_of_message+1)]

    for m in messages:
        await m.delete()

@bot.command(name='hello') # On précise le nom de la commande soit (/del)
async def salut(ctx,name:str):  #Plusieurs parametres on met ctx le context
    await ctx.channel.send(f"Hello {name}")



bot.run(os.getenv("TOKEN")) #Le token du bot
