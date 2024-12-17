import os

from pymongo import MongoClient

uri = os.environ["MONGO_URI"]
client = MongoClient(uri)

try:
    database = client.get_database("calicaloml")
    macros = database.get_collection("macros")

    macros.delete_many({})

    client.close()

except Exception as e:
    raise Exception("Unable to clear collection: ", e)
