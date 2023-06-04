import pymongo
import asyncio
from connect_db import db_client


async def count_command():
    """
    Counts the number of commands called.
    Imports and update new counts to database.
    """
    client = await db_client()
    db = client["octo"]
    collection = db.milestone

    find_details = {"_id": "command_count"}
    old_count = collection.find_one(find_details)

    if old_count is None:
        return

    new_count = old_count["count"] + 1
    update_query = {"$set": {"count": new_count}}

    collection.update_one(old_count, update_query)
