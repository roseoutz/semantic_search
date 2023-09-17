import unittest

from config.Settings import Settings
from mongo.MongoConnector import MongoConnector


class MongoConnectorTest(unittest.TestCase):

    def test_mongo_connector_constructor(self):
        connector = MongoConnector(Settings().mongo_url)
        db = connector.client["sample_mflix"]
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
