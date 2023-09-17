from motor.motor_asyncio import AsyncIOMotorClient

from transformer.DataTransformer import DataTransformer


class MongoConnector:

    def __init__(self, mongo_url: str):
        self.client = AsyncIOMotorClient(host=[mongo_url])
        self._data_transformer = DataTransformer()

    async def searchByPlot(self, keyword: str):
        vector_query = await self._data_transformer.transform(keyword)
        collection = self.client.sample_mflix.movies

        query_result = collection.aggregate([
            {
                '$search': {
                    "index": "PlotSemanticSearch",
                    "knnBeta": {
                        "vector": vector_query,
                        "k": 4,
                        "path": "plot_embedding_hf"}
                }
            }
        ])

        result = [i async for i in query_result]
        return result
