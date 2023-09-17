import uvicorn
from fastapi import FastAPI

from data.MovieService import MovieService

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/plot/{keyword}")
async def transform(keyword: str):
    movie_service = MovieService()
    return await movie_service.search(keyword)


if __name__ == "__main__":
    uvicorn.run(app)
