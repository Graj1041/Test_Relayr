import requests
import json
from Utilities.customLogger import LogGen
from Utilities.assertions import assert_valid_schema
import random
# import validators


class Test_API:

    # Additional headers
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    url = 'https://dog.ceo/api/breeds/'
    logger = LogGen.log_gen()

    def test_validate_single_random_img_dogs_collection(self):
        self.logger.info("test_validate_single_random_img_dogs_collection started")
        # Arrange
        url = self.url + 'image/random'
        # Act
        resp = requests.get(url, headers=self.headers)
        json_data = (json.loads(resp.text))
        # Assert
        assert resp.status_code == 200
        assert_valid_schema(json_data, 'singleDog.json')
        assert 'https:' in json_data['message']
        self.logger.info("test_validate_single_random_img_dogs_collection completed")

    def test_validate_multiple_random_img_dogs_collection(self):
        self.logger.info("test_validate_multiple_random_img_dogs_collection started")
        # Arrange
        n = random.randint(1, 100)
        url2 = self.url + 'image/random/' + str(n)
        # Act
        resp = requests.get(url2, headers=self.headers)
        json_data = (json.loads(resp.text))
        # Assert
        assert resp.status_code == 200
        assert_valid_schema(json_data, 'multipleDogs.json')
        assert len(json_data['message']) <= 50
        self.logger.info("test_validate_multiple_random_img_dogs_collection completed")
