from pymongo import MongoClient
from decouple import config


client = MongoClient(f"mongodb+srv://{config("DB_USER")}:"
                     f"{config("DB_PASSWORD")}@{config("DB_HOST")}/"
                     f"jan?retryWrites=true&w=majority")

db = client.adamecko
 
collection_name = db.odpovede

