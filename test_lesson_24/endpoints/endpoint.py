import allure
import requests


class Endpoint:

    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    token = None
    headers = {'Content-Type': 'application/json'}

    def get_headers(self):
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['Authorization'] = self.token
        print("HEADERS:", headers)
        return headers

    def request(self, method, url, **kwargs):
        headers = self.get_headers()
        return requests.request(method, url, headers=headers, **kwargs)


    @allure.step('Check that status code is 200')
    def check_response_status_code_is_correct(self):
        print(self.response.status_code)
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('Check that status code is 400')
    def check_response_status_code_is_correct_400_404(self):
        print(self.response.status_code)
        assert self.response.status_code in [404, 400], 'Status code is incorrect'

    @allure.step('Check that name is the same name as sent')
    def check_response_name_is_correct(self, name):
        assert self.response.json()['name'] == name, 'Name is incorrect'

    @allure.step('Check that id is correct')
    def check_response_id_is_correct(self, id):
        assert self.response.json()['id'] == id, 'ID is incorrect'

    @allure.step('Check that list is not empty')
    def check_meme_list_is_not_empty(self):
        assert len(self.response.json()['data']) > 0, 'Meme list is empty'

    @allure.step('Check that each meme has required fields')
    def check_all_memes_have_required_fields(self):
        for meme in self.response.json()['data']:
            assert 'id' in meme
            assert 'text' in meme
            assert 'url' in meme
            assert 'tags' in meme
            assert 'info' in meme
            assert 'updated_by' in meme

    @allure.step('Check that each meme has required fields')
    def check_one_meme_has_required_fields(self):
            assert 'id' in self.response.json()
            assert 'text' in self.response.json()
            assert 'url' in self.response.json()
            assert 'tags' in self.response.json()
            assert 'info' in self.response.json()
            assert 'updated_by' in self.response.json()

    @allure.step('Check that id exist in POST response')
    def get_id_from_response(self):
        assert 'id' in self.response.json(), 'No id in response'
        return self.response.json()['id']

    @allure.step('Check that text is correct')
    def check_response_text_is_correct(self, text):
        assert self.response.json()['text'] == text

    @allure.step('Check that tags are correct')
    def check_response_tags_are_correct(self, tags):
        assert self.response.json()['tags'] == tags

    @allure.step('Check that info is correct')
    def check_response_info_is_correct(self, info):
        assert self.response.json()['info'] == info

    @allure.step('Check that url is correct')
    def check_response_url_is_correct(self, url):
        assert self.response.json()['url'] == url

    @allure.step('Check that id is correct')
    def check_response_id_is_correct(self, id):
        assert self.response.json()['id'] == id
