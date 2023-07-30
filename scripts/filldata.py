import asyncio
from bot.db.client import db
from bot.utils.api import get_summoner_data_by_id

async def update_data():
    # Consigue una referencia a tu colección
    opencup_collection = db['opencup']

    # Obtén todos los documentos en la colección
    for document in opencup_collection.find():
        summoner_id = document['summoner_id']

        # Obten los datos del invocador con la función get_summoner_data
        summoner_data = await get_summoner_data_by_id(summoner_id)
        summoner_data = summoner_data[0]
        print("SUMMONER DATA", summoner_data)

        if not summoner_data:
            continue

        if summoner_data["queueType"] == "RANKED_TFT":

            # Calcula el número total de juegos
            games = summoner_data["wins"] + summoner_data["losses"]
            win_ratio = round((summoner_data["wins"] / games) * 100, 2)  # Win ratio as a percentage.

            # Actualiza el documento con los nuevos datos
            opencup_collection.update_one(
                {'_id': document['_id']},  # Query para encontrar el documento a actualizar
                {'$set': {
                    'tier': summoner_data["tier"] if summoner_data["tier"] else "UNRANKED",
                    'rank': summoner_data["rank"] if summoner_data["rank"] else "UNRANKED",
                    'leaguePoints': summoner_data["leaguePoints"] if summoner_data["leaguePoints"] else 0,
                    'wins': summoner_data["wins"],
                    'losses': summoner_data["losses"],
                    'games': games,
                    'top4_rate': win_ratio
                }}
            )

# Luego ejecuta la función con el bucle de eventos de asyncio
asyncio.run(update_data())
