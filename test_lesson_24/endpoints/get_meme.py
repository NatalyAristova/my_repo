from test_lesson_24.endpoints.endpoint import Endpoint
import requests
import allure


class GetMeme(Endpoint):

    @allure.step('Get all memes')
    def get_all_memes(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.get_headers())
        self.json = self.response.json()
        return self.response

    @allure.step('Get one meme')
    def get_one_meme(self, new_meme_id):
        self.response = requests.get(f'{self.url}/meme/{new_meme_id}', headers=self.get_headers())
        return self.response
