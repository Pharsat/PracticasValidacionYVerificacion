import json
import unittest
from datetime import datetime

from api_books_testing.request_api_book import api_book as api

class ApiRequestAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_books(self, endpoint):
        self.response = api.get_all_books(endpoint)
        return self.response

    def validate_number_book(self, number_book):
        response_data = json.loads(self.response.text)
        len_book = len(response_data)
        self.assertEquals(len_book, number_book)

    def validate_code(self, code):
        self.assertEquals(self.response.status_code, code)

if __name__ == '__main__':
    unittest.main()