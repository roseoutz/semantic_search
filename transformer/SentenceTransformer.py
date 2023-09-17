from sentence_transformers import SentenceTransformer


class SentenceTransformer:

    def __init__(self):
        self._model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    def transform(self, text: str) -> list:
        return self._model.encode(text)


if __name__ == '__main__':
    transformer = SentenceTransformer()
    print(transformer.transform("Mongo is awesome"))
