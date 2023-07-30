import pandas as pd
import asyncio
from bot.db.client import db
from bot.utils.api import get_summoner_id

df = pd.read_csv("top24.csv")

async def fill_data():
    for summoner in df["summoner"]:
        print(summoner)
        try:
            summoner_id = await get_summoner_id(summoner)
            print(summoner_id)
            db.opencup.insert_one({"summoner": summoner, "summoner_id": summoner_id})
        except Exception as e:
            print(e)

asyncio.run(fill_data())
