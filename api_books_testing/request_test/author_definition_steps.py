import json
import unittest
from datetime import datetime
from api_books_testing.request_api_author import api_author as api


class ApiRequestAuthors(unittest.TestCase):
    now = datetime.now()

    def test_get_all_authors_by_book(self, endpoint, book_id):
        self.response = api.get_all_authors_by_book(endpoint, book_id)
        self.assertEqual(self.response.status_code, 200)

    def test_get_all_authors(self, number_book):
        response_data = json.loads(self.response.text)
        len_book = len(response_data)
        self.assertEquals(len_book, number_book)

    def test_get_author(self, code):
        self.assertEquals(self.response.status_code, code)

    def test_create_author(self, code):
        self.assertEquals(self.response.status_code, code)

    def test_delete_author(endpoint, author_id):
        return requests.delete((url + endpoint).format(author_id))

    def test_update_author(endpoint, author_id, author_data):
        return requests.put((url + endpoint).format(author_id), author_data)


if __name__ == '__main__':
    unittest.main()