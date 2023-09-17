import pymongo
from pymongo.server_api import ServerApi


class MongoConnector:

    def __init__(self, mongo_url: str):
        self.client = pymongo.MongoClient(host=[mongo_url], server_api=ServerApi('1'))
