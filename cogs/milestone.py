import pymongo
import asyncio
import disnake
import inspect
from connect_db import db_client
from disnake.ext import commands

class Milestone(commands.Cog):
    """
    Registers milestone commands and counts the number of commands called.
    Count the number of servers the bot is in.
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    # Parent command
    @commands.slash_command()
    async def milestone(self, inter):
        await count_command() # counts child commands of milestone
        pass
    
    # Child command
    @milestone.sub_command(description="Get the total number of commands called")
    async def command(self, inter: disnake.ApplicationCommandInteraction):
        """
        Responds to user the total number of commands called.

        :param inter (disnake.ApplicationCommandInteraction): user object.
        """
        await inter.response.defer()        
        total_count = await get_total_count()
        await inter.followup.send(f"{total_count} calls made in total")
            
    @commands.Cog.listener()
    async def on_ready(self):
        """
        Runs the register_command function when the bot is ready.
        """
        await self.register_new_command()
        
    async def register_new_command(self):
        """
        Registers a new command to the database.
        """
        collection = await connect_milestone()
        db_commands = await find_command_document(collection)
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
            print(f"Milestone: Registered new command [{name}]")

def setup(bot: commands.Bot):
    bot.add_cog(Milestone(bot))

async def count_command():
    """
    Counts the command being called.
    
    IMPORTANT:
    This function should be placed inside the command function that needs counting.
    Does not work on commands in child node, place this function in the parent node instead.
    """
    command_name = inspect.stack()[1][3]
    collection = await connect_milestone()
    db_commands = await find_command_document(collection)
    if db_commands is None:
        return
    
    # Update the command count
    if command_name in db_commands:
        current_count = db_commands[command_name]
        
        update_query = {"$set": {f"{command_name}": current_count + 1}}
        collection.update_one(db_commands, update_query)

async def find_command_document(collection):
    """
    Finds the command_count document in database.
    
    :param collection: the database collection object.
    :return db_commands: the command set.
    """
    
    find_details = {"_id": "command_count"}
    db_commands = collection.find_one(find_details)
    
    if db_commands is None:
        return None
    
    return db_commands

async def get_total_count():
    """
    Gets the total number of commands called from the database.
    
    :return total_count: an integer.
    """
    collection = await connect_milestone()
    db_commands = await find_command_document(collection)
    if db_commands is None:
        return
    
    total_count = 0
    
    for command in db_commands:
        if command == "_id":
            continue
        total_count = total_count + db_commands[command]
    
    return total_count

async def connect_milestone():
    """
    Connects to the milestone database.
    
    :return: The milestone collection.
    """
    client = await db_client()
    db = client["octo"]
    collection = db.milestone
    return collection