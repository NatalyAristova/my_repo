from test_lesson_24.endpoints.endpoint import Endpoint
import requests
import allure


class PostMeme(Endpoint):

    @allure.step('Create new meme')
    def create_new_meme(self, body):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=self.get_headers())
        return self.response
