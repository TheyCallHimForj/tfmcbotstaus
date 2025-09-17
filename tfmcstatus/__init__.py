from .TFMCStatus import TFMCStatus

async def setup(bot):
    await bot.add_cog(TFMCStatus(bot))