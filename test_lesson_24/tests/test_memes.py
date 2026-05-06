import pytest
import allure
from test_lesson_24.conftest import get_meme_endpoint


TEST_DATA = [{
    "info": {
        "text1": "meme1",
        "text2": "meme2"
    },
    "tags": [
        "cat",
        "hat"
    ],
    "text": "Cat in a hat",
    "url": "https://www.google.com/imgres?q=%D0%BC%D0%B5%D0%BC&imgurl=https%3A%2F%2Fi.pinimg."
           "com%2Foriginals%2F6f%2Fb7%2F26%2F6fb726d46f5894ed0c67399b8b42f4c0.jpg&imgrefurl="
           "https%3A%2F%2Fwww.pinterest.com%2Felkablog1%2F%25D0%25BC%25D0%25B5%25D0%25BC%25D1%258B%"
           "2F&docid=6ZjWUWjqHZ9LvM&tbnid=9_2seZmg0xwQOM&vet=12ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oE"
           "CHQQAA..i&w=978&h=978&hcb=2&ved=2ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oECHQQAA"
}]

NEGATIVE_TEST_DATA = [{

},{
    "tags": [
        "cat",
        "hat"
    ],
    "text": "Cat in a hat",
    "url": "https://www.google.com/imgres?q=%D0%BC%D0%B5%D0%BC&imgurl=htt"
           "ps%3A%2F%2Fi.pinimg.com%2Foriginals%2F6f%2Fb7%2F26%2F6fb726d46"
           "f5894ed0c67399b8b42f4c0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest."
           "com%2Felkablog1%2F%25D0%25BC%25D0%25B5%25D0%25BC%25D1%258B%2F&docid=6"
           "ZjWUWjqHZ9LvM&tbnid=9_2seZmg0xwQOM&vet=12ahUKEwi97MWA_pmOAxUzdaQEHV3DIcI"
           "QM3oECHQQAA..i&w=978&h=978&hcb=2&ved=2ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oECHQQAA"
}, {
    "info": {
        "text1": "meme1",
        "text2": "meme2"
    },
    "text": "Cat in a hat",
    "url": "https://www.google.com/imgres?q=%D0%BC%D0%B5%D0%BC&imgurl=https%3A%2F"
           "%2Fi.pinimg.com%2Foriginals%2F6f%2Fb7%2F26%2F6fb726d46f5894ed0c6739"
           "9b8b42f4c0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Felkablog1%2"
           "F%25D0%25BC%25D0%25B5%25D0%25BC%25D1%258B%2F&docid=6ZjWUWjqHZ9LvM&tbnid=9_2"
           "seZmg0xwQOM&vet=12ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oECHQQAA..i&w=978&h=978&"
           "hcb=2&ved=2ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oECHQQAA"
}]

@allure.feature('Viewing memes')
@allure.story('Get request')
@allure.title('Getting all memes')
def test_all_memes(get_meme_endpoint):
    get_meme_endpoint.get_all_memes()
    get_meme_endpoint.check_response_status_code_is_correct()
    get_meme_endpoint.check_meme_list_is_not_empty()
    get_meme_endpoint.check_all_memes_have_required_fields()


@allure.feature('Viewing memes')
@allure.story('Get request')
@allure.title('Getting one meme')
def test_one_meme(get_meme_endpoint, new_meme_id):
    get_meme_endpoint.get_one_meme(new_meme_id)
    get_meme_endpoint.check_response_status_code_is_correct()
    get_meme_endpoint.check_response_id_is_correct(new_meme_id)
    get_meme_endpoint.check_one_meme_has_required_fields()


@allure.feature('Memes managing')
@allure.story('Post request')
@allure.title('Adding new meme')
@pytest.mark.parametrize('body', TEST_DATA)
def test_post_an_object(create_post_endpoint, body):
    create_post_endpoint.create_new_meme(body=body)
    create_post_endpoint.check_response_status_code_is_correct()
    id = create_post_endpoint.get_id_from_response()
    create_post_endpoint.check_response_id_is_correct(id)
    create_post_endpoint.check_response_text_is_correct(body['text'])
    create_post_endpoint.check_response_tags_are_correct(body['tags'])
    create_post_endpoint.check_response_info_is_correct(body['info'])
    create_post_endpoint.check_response_url_is_correct(body['url'])


@allure.feature('Memes managing')
@allure.story('Post request')
@allure.title('Adding new meme: negative cases')
@pytest.mark.parametrize('body', NEGATIVE_TEST_DATA)
def test_post_an_object_without_data(create_post_endpoint, body):
    create_post_endpoint.create_new_meme(body=body)
    create_post_endpoint.check_response_status_code_is_correct_400_404()


@allure.feature('Memes managing')
@allure.story('PUT request')
@allure.title('Changing meme')
def test_put_meme(update_meme_endpoint, new_meme_id):
    body = {
    "id": new_meme_id,
    "info": {
        "text1": "meme1_updated",
        "text2": "meme2_updated"
    },
    "tags": [
        "updated",
        "updated"
    ],
    "text": "Updated",
    "url": "updated"
}
    update_meme_endpoint.make_changes_in_meme(new_meme_id, body)
    update_meme_endpoint.check_response_status_code_is_correct()
    update_meme_endpoint.check_response_text_is_correct(body['text'])
    update_meme_endpoint.check_response_tags_are_correct(body['tags'])
    update_meme_endpoint.check_response_info_is_correct(body['info'])
    update_meme_endpoint.check_response_url_is_correct(body['url'])


@allure.feature('Memes managing')
@allure.story('PUT request')
@allure.title('Changing meme without reguired data')
def test_put_meme_negative(update_meme_endpoint, new_meme_id):
    body = {
    "id": new_meme_id,
    "info": {
        "text1": "meme1_updated",
        "text2": "meme2_updated"
    },
    "text": "Updated",
    "url": "updated"
}
    update_meme_endpoint.make_changes_in_meme(new_meme_id, body)
    update_meme_endpoint.check_response_status_code_is_correct_400_404()


@allure.feature('Memes managing')
@allure.story('DELETE meme')
@allure.title('Deleting meme')
def test_delete_meme(delete_meme_endpoint, get_meme_endpoint,  new_meme_id):
    delete_meme_endpoint.delete_meme(new_meme_id)
    delete_meme_endpoint.check_response_status_code_is_correct()
    get_meme_endpoint.get_one_meme(new_meme_id)
    get_meme_endpoint.check_response_status_code_is_correct_400_404()
