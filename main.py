import uvicorn
from fastapi import FastAPI

from data.MovieService import MovieService

app = FastAPI()


@app.get("/movie/{search_type}/{keyword}")
async def transform(search_type: str = 'title', keyword: str = None):
    movie_service = MovieService()
    return await movie_service.search(search_type, keyword)


if __name__ == "__main__":
    uvicorn.run(app)
