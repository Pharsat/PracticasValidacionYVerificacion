import json
import unittest
from datetime import datetime
from api_books_testing.request_api_author import api_author as api


class ApiRequestAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_authors_by_book_200_response(self, endpoint, book_id):
        self.response = api.get_all_authors_by_book(endpoint, book_id)
        self.assertEqual(self.response.status_code, 200)

    def test_get_all_authors_200_response(self, endpoint):
        self.response = api.get_all_authors(endpoint)
        self.assertEqual(self.response.status_code, 200)

    def test_get_author_200_response(self, endpoint, author_id):
        self.response = api.get_author(endpoint, author_id)
        self.assertEqual(self.response.status_code, 200)

    def test_create_author_200_response(self, endpoint, author_data):
        self.response = api.create_author(endpoint, author_data)
        self.assertEquals(self.response.status_code, 200)

    def test_delete_author_200_response(self, endpoint, author_id):
        self.response = api.delete_author(endpoint, author_id)
        self.assertEquals(self.response.status_code, 200)

    def test_update_author_200_response(self, endpoint, author_id, author_data):
        self.response = api.update_author(endpoint, author_id, author_data)
        self.assertEquals(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()