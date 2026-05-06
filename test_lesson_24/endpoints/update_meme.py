from test_lesson_24.endpoints.endpoint import Endpoint
import requests
import allure


class UpdateMeme(Endpoint):

    @allure.step('Update meme')
    def make_changes_in_meme(self, new_meme_id, body):
        self.response = requests.put(f'{self.url}/meme/{new_meme_id}', json=body, headers=self.get_headers())
        return self.response
