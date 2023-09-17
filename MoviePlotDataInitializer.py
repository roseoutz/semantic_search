import pymongo

from config.Settings import Settings
from transformer.DataTransformer import DataTransformer

if __name__ == '__main__':
    settings = Settings()
    client = pymongo.MongoClient(settings.mongo_url)
    db = client.sample_mflix
    collection = db.movies

    transformer = DataTransformer()

    for doc in collection.find({'plot': {"$exists": True}}).limit(50):
        doc['plot_embedding_hf'] = transformer.transform(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)
