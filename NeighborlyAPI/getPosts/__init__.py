import json
import logging

import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://project2cosmosaccount:n98jFOmJncwCO36sgHIFmrwZwVIlGlbEB0V5AizdvrTELNhMhqDJvZOUji6sjfCxN1PvHEGT1wK6ACDbPXp3dQ==@project2cosmosaccount.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmosaccount@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['MongoDB']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)