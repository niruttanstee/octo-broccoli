# Import necessary modules from the Disnake library
# disnake: The main Disnake module
# commands: Submodule for defining commands and cogs
import disnake
from disnake.ext import commands
import cogs.milestone as milestone


# Define a class called "Hello" that extends commands.Cog
class Hello(commands.Cog):
    """ Sends hello message """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Define a slash command named "hello" using the @commands.slash_command decorator
    # This command takes an "inter" parameter of type disnake.ApplicationCommandInteraction
    # and sends the message "Hello <3" as a response
    @commands.slash_command(description="Says Hello")
    async def hello(self, inter: disnake.ApplicationCommandInteraction):
        await milestone.count_command()  # Counts the number command calls for milestone
        await inter.response.send_message("Hello <3")

    # Useful comments


# Define a setup function that adds an instance of the Hello cog to the bot
# This function takes a "bot" parameter of type commands.Bot
def setup(bot: commands.Bot):
    bot.add_cog(Hello(bot))
