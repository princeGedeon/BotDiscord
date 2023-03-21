import datetime
import os
import random

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

from utils.api_chat import generate_prompt
from utils.api_dalle import create_image_by_prompt, create_variation_image
from utils.util import save_image_by_url

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True


bot=commands.Bot(command_prefix="/",intents=intents)

#Savoir si le bot est prêt
@bot.event
async def on_ready():
    print("Le bot est prêt")

@bot.command(name='del') # On précise le nom de la commande soit (/del)
async def delete(ctx,number_of_message:int):  #Plusieurs parametres on met ctx le context
    #messages=await ctx.channel.history(limit=number_of_message+1).flatten()
    messages=[msg async for msg in ctx.channel.history(limit=number_of_message+1)]

    for m in messages:
        await m.delete()

@bot.command(name='hello') # On précise le nom de la commande soit (/del)
async def salut(ctx,name:str):  #Plusieurs parametres on met ctx le context
    await ctx.channel.send(f"Hello {name}")


@bot.command(name="talk")
async def speak_with_bot(ctx,prompt:str):
    await ctx.channel.send(generate_prompt(prompt))
    print("PrinceBot a parlé")

@bot.command(name="imagine")
async def imagine_bot(ctx,prompt:str):
    url=create_image_by_prompt(prompt)
    name=f'img/image{random.randint(1,999)}.jpg'
    save_image_by_url(url,path=name)

    await ctx.channel.send(url)

@bot.command(name="propose")
async def edit_image(ctx):

    try:
        url=ctx.message.attachments[0].url
    except IndexError:
        print("Error : Aucun fichier")
        await ctx.send("Aucun fichier détecter")
    else:
        url2=create_variation_image(url)
        await ctx.channel.send(url2)

        print("PrinceBot a imaginé")
bot.run(os.getenv("TOKEN")) #Le token du bot
