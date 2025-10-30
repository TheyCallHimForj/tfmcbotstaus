# tfmcstatus.py
import random
from discord import Activity, ActivityType
from discord.ext import commands, tasks

from redbot.core.bot import Red
from redbot.core import commands as redcommands


class TFMCStatus(redcommands.Cog):
    """
    Randomly cycles the bot's activity every 5 minutes.
    """

    def __init__(self, bot: Red):
        self.bot = bot

        # ------------------------------------------------------------------
        #  Your status list – keep it exactly as you wrote it
        # ------------------------------------------------------------------
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

        # Start the loop automatically when the cog loads
        self.change_status.start()

    # ----------------------------------------------------------------------
    #  Clean shutdown
    # ----------------------------------------------------------------------
    def cog_unload(self):
        self.change_status.cancel()

    # ----------------------------------------------------------------------
    #  The actual loop
    # ----------------------------------------------------------------------
    @tasks.loop(minutes=5.0)
    async def change_status(self):
        activity_type, name = random.choice(self.statuses)
        activity = Activity(type=activity_type, name=name)
        try:
            await self.bot.change_presence(activity=activity)
        except Exception as exc:                     # never crash the loop
            self.bot.logger.exception("Failed to change presence:", exc_info=exc)

    # ----------------------------------------------------------------------
    #  Wait for the bot to be fully ready before the first change
    # ----------------------------------------------------------------------
    @change_status.before_loop
    async def before_change_status(self):
        await self.bot.wait_until_ready()


# ----------------------------------------------------------------------
#  Red-Bot setup hook
# ----------------------------------------------------------------------
async def setup(bot: Red):
    await bot.add_cog(TFMCStatus(bot))
