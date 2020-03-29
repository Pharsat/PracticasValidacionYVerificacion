import requests

url = "https://fakerestapi.azurewebsites.net"


def get_all_authors_by_book(endpoint, book_id):
    return requests.get((url + endpoint).format(book_id))


def get_all_authors(endpoint):
    return requests.get(url + endpoint)


def get_author(endpoint, author_id):
    return requests.put((url + endpoint).format(author_id))


def create_author(endpoint, author_data):
    return requests.post(url + endpoint, author_data)


def delete_author(endpoint, author_id):
    return requests.delete((url + endpoint).format(author_id))


def update_author(endpoint, author_id, author_data):
    return requests.put((url + endpoint).format(author_id), author_data)
