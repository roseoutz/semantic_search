from config.Settings import Settings
from mongo.MongoConnector import MongoConnector


class MovieService:

    def __init__(self):
        settings = Settings()
        self._mongo_client = MongoConnector(settings.mongo_url)

    async def search(self, keyword: str):
        movies = await self._mongo_client.searchByPlot(keyword)

        result = []

        for movie in movies:
            movie.pop("_id")
            movie.pop("plot_embedding_hf")
            result.append(movie)
        return result
