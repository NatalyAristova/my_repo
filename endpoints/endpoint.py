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

    @allure.step('Check that status code is 401')
    def check_response_status_code_is_401(self):
        assert self.response.status_code == 401, 'Status code is incorrect'

    @allure.step('Check that status code is 403')
    def check_response_status_code_is_403(self):
        assert self.response.status_code == 403, 'Status code is incorrect'

    @allure.step('Check that status code is 404')
    def check_response_status_code_is_correct_404(self):
        print(self.response.status_code)
        assert self.response.status_code == 404, 'Status code is incorrect'

    @allure.step('Check that status code is 400')
    def check_response_status_code_is_correct_400(self):
        print(self.response.status_code)
        assert self.response.status_code == 400, 'Status code is incorrect'

    @allure.step('Check that status code is 500')
    def check_response_status_code_is_500(self):
        print(self.response.status_code)
        assert self.response.status_code == 500, 'Status code is incorrect'

    @allure.step('Check that name is the same name as sent')
    def check_response_name_is_correct(self, name):
        assert self.response.json()['name'] == name, 'Name is incorrect'

    @allure.step('Check that user is the same user as sent')
    def check_response_user_is_correct(self, name):
        assert self.response.json()['user'] == name, 'Name is incorrect'

    @allure.step('Check that id is correct')
    def check_response_id_is_correct(self, id):
        assert self.response.json()['id'] == id, 'ID is incorrect'

    @allure.step('Check that list is not empty')
    def check_meme_list_is_not_empty(self):
        assert len(self.response.json()['data']) > 0, 'Meme list is empty'

    @allure.step('Check that each meme has required fields')
    def check_meme_has_required_fields(self, meme):
            assert 'id' in meme
            assert 'text' in meme
            assert 'url' in meme
            assert 'tags' in meme
            assert 'info' in meme
            assert 'updated_by' in meme

    @allure.step('Check that each meme has required fields')
    def check_all_memes_have_required_fields(self):
        for meme in self.response.json()['data']:
            self.check_meme_has_required_fields(meme)

    @allure.step('Check that id exist in POST response')
    def get_id_from_response(self):
        assert 'id' in self.response.json(), 'No id in response'
        return self.response.json()['id']

    @allure.step('Check that value is correct')
    def check_response_value_is_correct(self, key, expected_value):
        assert self.response.json()[key] == expected_value
