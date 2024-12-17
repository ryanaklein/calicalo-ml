import pprint
import os

from pymongo import MongoClient


uri = os.environ["MONGO_URI"]
client = MongoClient(uri)

pp = pprint.PrettyPrinter(indent=4)

try:
    database = client.get_database("calicaloml")
    macros = database.get_collection("macros")

    query = {}
    results = macros.find(query)

    for result in results:
        pp.pprint(result)
        print('\n\n') 

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
