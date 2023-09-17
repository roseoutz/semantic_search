from config.Settings import Settings
from mongo.MongoConnector import MongoConnector


class MovieService:

    def __init__(self):
        settings = Settings()
        self._mongo_client = MongoConnector(settings.mongo_url)

    async def search(self, search_type: str, keyword: str):

        if search_type not in ['title', 'plot']:
            raise Exception("not contain")

        movies = await self._mongo_client.searchByPlot(search_type, keyword)

        result = []

        for movie in movies:
            movie.pop("_id")
            movie.pop("plot_embedding_hf")
            movie.pop("title_embedding_hf")
            movie.pop("actor_embedding_hf")
            result.append(movie)
        return result
