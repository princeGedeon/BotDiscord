#On importe la bliblotheque
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members=True

#On va créer un client
client=discord.Client(intents=intents)

@client.event  #Pour dire que la fonction est spéciam
async def on_ready(): #La fonction a le nom de l'evnement
    print("Le bot est prêt") # Execute quand tout est prêt

@client.event
async def on_message(message):
    if message.content.lower()=='ping':
    # On va faire parler le bot on doit savoir dans quel salon on se trouve
        await message.channel.send("pong")

@client.event
async def on_member_join(member:discord.Member):
    #On va récupérer le salon principal afin de lui souhaiter bonne arrivé
    general_channel: discord.TextChannel =client.get_channel() # On va mettre id qu'on va trouver dans notre serveur
    await general_channel.send(content=f"Bienvenue sur le erveur {member.display_name} ! ")


#Pour lancer ce client
client.run(token="MTA4Njk4NjQ1NzQ1OTIwNDE3Ng.GVDdIO.0JSVkOq3qAJdUry8K3ifw1OQOLmGpxfCtT-olY")#On prend le token du bot