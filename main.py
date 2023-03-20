#On importe la bliblotheque
from dotenv import load_dotenv
import os #Recupérer les données environnement os.getenv("TOKEN")
load_dotenv()#Par défaut ça reconnait automatiquement .env et loader les infos dans les varaibles d'environnements
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members=True

#On va créer un client
client=discord.Client(intents=intents)

@client.event  #Pour dire que la fonction est spéciam
async def on_ready(): #La fonction a le nom de l'evnement
    print("Le bot est prêt") # Execute quand tout est prêt

"""@client.event
async def on_message(message:discord.Message):
    if message.content.startswith("!del"):
        number=int(message.content.split()[1])
        number=int(message.content.split()[1])
        #Récupérer les numbers derniers messages
        messages=message.channel.history(limit=number+1)


        #Maintenant supprimer
        for m in messages:
            await m.delete()
"""
@client.event
async def on_member_join(member:discord.Member):
    #On va récupérer le salon principal afin de lui souhaiter bonne arrivé
    general_channel: discord.TextChannel =client.get_channel() # On va mettre id qu'on va trouver dans notre serveur
    await general_channel.send(content=f"Bienvenue sur le erveur {member.display_name} ! ")


#Pour lancer ce client
client.run(token=os.getenv("TOKEN"))#On prend le token du bot