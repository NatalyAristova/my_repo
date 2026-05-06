from test_lesson_24.endpoints.endpoint import Endpoint
import requests
import allure


class DeleteMeme(Endpoint):

    @allure.step('Delete meme')
    def delete_meme(self, new_meme_id):
        self.response = requests.delete(f'{self.url}/meme/{new_meme_id}', headers=self.get_headers())
        if self.response.headers.get("Content-Type") == "application/json":
            self.json = self.response.json()
        else:
            self.text = self.response.text
        return self.response
