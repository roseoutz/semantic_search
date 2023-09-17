import pymongo
from sentence_transformers import SentenceTransformer

from config.Settings import Settings

if __name__ == '__main__':
    settings = Settings()
    client = pymongo.MongoClient(settings.mongo_url)
    db = client.sample_mflix
    collection = db.movies

    transformer = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    query = "imaginary characters from outer space at war"

    vector = transformer.encode(query).tolist()
    results = collection.aggregate([
        {
            '$search': {
                "index": "PlotSemanticSearch",
                "knnBeta": {
                    "vector": vector,
                    "k": 4,
                    "path": "plot_embedding_hf"}
            }
        }
    ])

    for document in results:
        print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
