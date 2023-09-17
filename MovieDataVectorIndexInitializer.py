import pymongo
from sentence_transformers import SentenceTransformer

from config.Settings import Settings

if __name__ == '__main__':
    settings = Settings()
    client = pymongo.MongoClient(settings.mongo_url)
    db = client.sample_mflix
    collection = db.movies

    st = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    movies = collection.find({'plot': {"$exists": True}}).limit(50)

    for doc in movies:
        doc['plot_embedding_hf'] = st.encode(doc['plot']).tolist()
        collection.replace_one({'_id': doc['_id']}, doc)

    for doc in movies:
        doc['title_embedding_hf'] = st.encode(doc['title']).tolist()
        collection.replace_one({'_id': doc['_id']}, doc)

    for doc in movies:
        actor_vector = []
        for actor in doc['cast']:
            actor_vector.extend(st.encode(actor).tolist())
        doc['actor_embedding_hf'] = actor_vector
        collection.replace_one({'_id': doc['_id']}, doc)
