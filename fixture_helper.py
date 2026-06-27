import requests
from endpoints.endpoint import Endpoint


def check_token_alive(token):
    url = f"{Endpoint.url}/authorize/{token}"
    response = requests.get(url)
    return response.status_code == 200
