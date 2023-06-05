import pymongo
import asyncio
import disnake
from connect_db import db_client
from disnake.ext import commands

class Milestone(commands.Cog):
    """
    Registers milestone commands and counts the number of commands called.
    Count the number of servers the bot is in.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def connect_milestone(self):
        """
        Connects to the milestone database.
        
        Returns: The milestone collection.
        """
        client = await db_client()
        db = client["octo"]
        collection = db.milestone
        return collection

    async def count_command(self):
        """
        Counts the number of commands called.
        
        This function should be placed below the command it is counting.
        """

    async def register_new_command(self):
        """
        Registers a new command to the database.
        """
        collection = await self.connect_milestone()
        
        find_details = {"_id": "command_count"}
        db_commands = collection.find_one(find_details)
        
        if db_commands is None:
            return
        
        # Get current available commands and compare with database
        bot_commands = self.bot.slash_commands
        for command in bot_commands:
            name = command.name
            if name in db_commands:
                continue
            
            update_query = {"$set": {f"{name}": 0}}
            collection.update_one(db_commands, update_query)
            print(f"Registered new command for milestone: {name}")
            
    @commands.Cog.listener()
    async def on_ready(self):
        """
        Runs the register_command function when the bot is ready.
        """
        await self.register_new_command()

def setup(bot: commands.Bot):
    bot.add_cog(Milestone(bot))
