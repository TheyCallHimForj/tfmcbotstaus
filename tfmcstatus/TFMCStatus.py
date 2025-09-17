import discord
from discord.ext import commands, tasks
import random

class TFMCStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.statuses = [
            # Playing
            (discord.ActivityType.playing, "TFMC"),
            (discord.ActivityType.playing, "Arma3"),
            (discord.ActivityType.playing, "Risk with Geoff"),

            # Watching
            (discord.ActivityType.watching, "TPS like a hawk"),
            (discord.ActivityType.watching, "Ghosthieve fumble the bag"),
            (discord.ActivityType.watching, "Console"),

            # Listening
            (discord.ActivityType.listening, "Soppgirobygget"),
            (discord.ActivityType.listening, "Daddy Fran ASMR"),
            (discord.ActivityType.listening, "Eoridcois Theme"),

            # Competing
            (discord.ActivityType.competing, "a CK3 game with Sauce"),
            (discord.ActivityType.competing, "a drinking match with Forj"),
            (discord.ActivityType.competing, "a hunt for John TFMC")
        ]
        self.change_status.start()

    def cog_unload(self):
        self.change_status.cancel()

    @tasks.loop(minutes=5.0)
    async def change_status(self):
        activity_type, text = random.choice(self.statuses)
        activity = discord.Activity(type=activity_type, name=text)
        await self.bot.change_presence(activity=activity)

    @change_status.before_loop
    async def before_change_status(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(TFMCStatus(bot))

