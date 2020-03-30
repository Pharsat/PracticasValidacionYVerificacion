import json
import unittest
from datetime import datetime
from api_books_testing.request_api_author import api_author as api


class ApiRequestAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_authors_by_book(self, endpoint, book_id):
        self.response = api.get_all_authors_by_book(endpoint, book_id)

    def test_get_all_authors(self, endpoint):
        self.response = api.get_all_authors(endpoint)

    def test_get_author(self, endpoint, author_id):
        self.response = api.get_author(endpoint, author_id)

    def test_create_author(self, endpoint, author_data):
        self.response = api.create_author(endpoint, author_data)

    def test_delete_author(self, endpoint, author_id):
        self.response = api.delete_author(endpoint, author_id)

    def test_update_author(self, endpoint, author_id, author_data):
        self.response = api.update_author(endpoint, author_id, author_data)

    def test_items_count(self):
        response_data = json.loads(self.response.text)
        self.items_count = len(response_data)

    def test_item_check(self):
        response_data = json.loads(self.response.text)
        self.item = response_data


if __name__ == '__main__':
    unittest.main()

