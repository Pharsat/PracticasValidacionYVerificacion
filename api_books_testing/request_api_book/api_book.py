import requests

url ="https://fakerestapi.azurewebsites.net"

def get_all_books(endpoint):
    return requests.get(url+endpoint)





