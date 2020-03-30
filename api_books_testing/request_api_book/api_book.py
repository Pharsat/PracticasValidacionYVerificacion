import requests

url = "https://fakerestapi.azurewebsites.net"


def get_all_books(endpoint):
    return requests.get(url + endpoint)


def post_new_book(endpoint, body):
    headers = {"Content-Type": "application/json"}
    return requests.post(url + endpoint, data=body, headers=headers)
