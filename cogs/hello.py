import disnake
from disnake.ext import commands


class Hello(commands.Cog):
    """ Sends hello message """
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Says Hello")
    async def hello(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Hello <3")

    # Useful comments

def setup(bot: commands.Bot):
    bot.add_cog(Hello(bot))
