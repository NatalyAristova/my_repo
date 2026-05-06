import requests
from test_lesson_24.endpoints.endpoint import Endpoint


class Authorize(Endpoint):

    def get_token(self, name='Natalia'):
        response = requests.post(
            f'{self.url}/authorize',
            json={'name': name}
        )
        return response.json()['token']
