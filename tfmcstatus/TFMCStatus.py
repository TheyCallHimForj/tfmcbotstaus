# tfmcstatus.py
import random
from discord import Activity, ActivityType
from discord.ext import tasks

# CRITICAL: Use Redbot's Cog class
from redbot.core import commands
from redbot.core.bot import Red


class TFMCStatus(commands.Cog):
    """
    Randomly cycles the bot's activity every 5 minutes.
    """

    def __init__(self, bot: Red):
        self.bot = bot

        self.statuses = [
            # Playing
            (ActivityType.playing, "TFMC"),
            (ActivityType.playing, "Arma3"),
            (ActivityType.playing, "Risk with Geoff"),

            # Watching
            (ActivityType.watching, "TPS like a hawk"),
            (ActivityType.watching, "Ghosthieve fumble the bag"),
            (ActivityType.watching, "Console"),

            # Listening
            (ActivityType.listening, "Soppgirobygget"),
            (ActivityType.listening, "Daddy Fran ASMR"),
            (ActivityType.listening, "Eoridcois Theme"),

            # Competing
            (ActivityType.competing, "a CK3 game with Sauce"),
            (ActivityType.competing, "a drinking match with Forj"),
            (ActivityType.competing, "a hunt for John TFMC"),
        ]

        self.change_status.start()

    def cog_unload(self):
        self.change_status.cancel()

    @tasks.loop(minutes=5.0)
    async def change_status(self):
        activity_type, name = random.choice(self.statuses)
        activity = Activity(type=activity_type, name=name)
        try:
            await self.bot.change_presence(activity=activity)
        except Exception as exc:
            self.bot.logger.error("Failed to change presence", exc_info=exc)

    @change_status.before_loop
    async def before_change_status(self):
        await self.bot.wait_until_ready()


async def setup(bot: Red):
    await bot.add_cog(TFMCStatus(bot))
