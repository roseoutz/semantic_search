from sentence_transformers import SentenceTransformer


class DataTransformer:

    def __init__(self):
        self._model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def transform(self, text: str) -> list:
        return self._model.encode(text)
