import json
import os

from pymongo import MongoClient

uri = os.environ['MONGO_URI']
client = MongoClient(uri)


def lambda_handler(event, context):

    try:
        data = json.loads(event['body'])
        database = client.get_database("calicaloml")
        macros = database.get_collection("macros")

        macros.insert_many(data)

    except Exception as e:
        raise Exception("Error uploading data to mongo: ", e)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
        }),
    }
