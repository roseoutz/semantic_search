import unittest

from transformer.DataTransformer import DataTransformer


class DataTransformerTest(unittest.TestCase):

    def test_semantic_transformer(self):
        transformer = DataTransformer()
        result = transformer.transform("Mongo")
        print(result)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
