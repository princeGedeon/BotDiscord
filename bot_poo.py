import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

#Chargement des varibles environnements
load_dotenv()

#Gestion des intents et autorisations

class PrinceBot(commands.Bot):
    """
    Une classe qui hérite de commands.Bot
    """

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="/",intents=intents) #Je précise ceci

    async def on_ready(self):
        """
        Evenements on_ready quand le bot est prêt
        :return:
        """
        print(f"{self.user.display_name} est connecté au serveur.")


#Por lancer on va juste créer une instance de notre bot
prince_bot=PrinceBot()
prince_bot.run(os.getenv("TOKEN"))