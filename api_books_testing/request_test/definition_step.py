import json
import unittest
from datetime import datetime

from api_books_testing.request_api_book import api_book as api


class ApirequestBooks(unittest.TestCase):
    now = datetime.now()

    def test_get_all_books(self, endpoint):
        self.response = api.get_all_books(endpoint)
        return self.response

    def test_post_new_book(self, endpoint, id, title, Description, PageCount, Excerpt, PublishDate):
        self.payload = {
            "ID": id,
            "Title": "{}".format(title),
            "Description": "{}".format(Description),
            "PageCount": PageCount,
            "Excerpt": "{}".format(Excerpt),
            "PublishDate": PublishDate
        }
        self.response = api.post_new_book(endpoint, json.dumps(self.payload))
        return self.response

    def validate_number_book(self, number_book):
        response_data = json.loads(self.response.text)
        len_book = len(response_data)
        self.assertEquals(len_book, number_book)

    def validate_code(self, code_expected):
        self.assertEquals(self.response.status_code, code_expected)
    def valide_new_book(self):
        print(self.response.text)
        self.assertEquals(self.response.text,json.dumps(self.payload))


if __name__ == '__main__':
    unittest.main()
