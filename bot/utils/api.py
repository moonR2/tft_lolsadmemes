import os
from riotwatcher import TftWatcher, ApiError 
from dotenv import load_dotenv

load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")
REGION = "la1"

print(RIOT_API_KEY)

if not RIOT_API_KEY:
    raise Exception("Missing RIOT_API_KEY")


watcher = TftWatcher(RIOT_API_KEY)

async def get_summoner_id(name: str) -> str:
    try:
        response = watcher.summoner.by_name(REGION, name)
        return response["id"]

    except ApiError as err:
        raise Exception("Summoner not found or API error", err)

async def get_summoner_data(name: str):
    try:
        account_id = await get_summoner_id(name)
        response = watcher.league.by_summoner(REGION, account_id)

        for key in response:
            print(key)

        print(response)
        return response

    except ApiError as err:
        raise Exception("Summoner not found or API error", err)

async def get_summoner_data_by_id(id: str):
    try:
        response = watcher.league.by_summoner(REGION, id)
        return response

    except ApiError as err:
        raise Exception("Summoner not found or API error", err)
