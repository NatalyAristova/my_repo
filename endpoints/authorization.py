import requests
from endpoints.endpoint import Endpoint


class Authorize(Endpoint):

    def get_token(self, name='Natalia'):
        response = requests.post(
            f'{self.url}/authorize',
            json={'name': name}
        )
        return response.json()['token']

    def authorize(self, name):
        self.response = requests.post(f'{self.url}/authorize', json={'name': name})
        return self.response

    def authorize_no_body(self):
        self.response = requests.post(f'{self.url}/authorize')
        return self.response
