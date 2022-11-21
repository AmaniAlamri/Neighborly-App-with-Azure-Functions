import json

import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://project2cosmosaccount:n98jFOmJncwCO36sgHIFmrwZwVIlGlbEB0V5AizdvrTELNhMhqDJvZOUji6sjfCxN1PvHEGT1wK6ACDbPXp3dQ==@project2cosmosaccount.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmosaccount@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['MongoDB']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

