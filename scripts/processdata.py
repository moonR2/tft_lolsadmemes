import pandas as pd
from bot.db.client import db

def create_table_by_games():
    opencup_collection = db['opencup']
    
    # Obten todos los documentos en la colección excluyendo el campo "_id"
    documents = opencup_collection.find({}, {"_id": 0})

    # Convertir los documentos en una lista para poder manipularlos con pandas
    documents_list = list(documents)

    # Crear un DataFrame con los documentos
    df = pd.DataFrame(documents_list)

    # Ordena el DataFrame por el número de juegos
    df_sorted = df.sort_values('games')

    # Guarda el DataFrame ordenado en un archivo .csv
    df_sorted.to_csv('results.csv', index=False)

create_table_by_games()
