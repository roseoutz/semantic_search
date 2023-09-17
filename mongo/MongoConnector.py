from motor.motor_asyncio import AsyncIOMotorClient

from transformer.DataTransformer import DataTransformer


class MongoConnector:

    def __init__(self, mongo_url: str):
        self.client = AsyncIOMotorClient(host=[mongo_url])
        self._data_transformer = DataTransformer()

    async def searchByPlot(self, search_type: str, keyword: str):
        vector_query = await self._data_transformer.transform(keyword)
        collection = self.client.sample_mflix.movies

        query_param = [
            {
                '$search': {
                    "index": f"{search_type.capitalize()}SemanticSearch",
                    "knnBeta": {
                        "vector": vector_query,
                        "k": 4,
                        "path": f"{search_type}_embedding_hf"}
                }
            }
        ]

        query_result = collection.aggregate(query_param)

        result = [i async for i in query_result]
        return result
