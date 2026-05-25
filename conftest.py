import pytest
from endpoints.authorization import Authorize
from endpoints.get_meme import GetMeme
from endpoints.create_meme import PostMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.endpoint import Endpoint
from endpoints.update_meme import UpdateMeme
import requests
from fixture_helper import check_token_alive


@pytest.fixture(scope='session')
def auth_token():
    auth = Authorize()
    token = auth.get_token()
    while not check_token_alive(token):
        token = auth.get_token()
    return token

@pytest.fixture()
def new_meme_id(create_post_endpoint, delete_meme_endpoint):
    print('before test')
    body = {
    "info": {
        "text1": "meme1",
        "text2": "meme2"
    },
    "tags": [
        "cat",
        "hat"
    ],
    "text": "Cat in a hat",
    "url": "https://www.google.com/imgres?q=%D0%BC%D0%B5%D0%BC&imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F6f%2Fb7%2F26%2F6fb726d46f5894ed0c67399b8b42f4c0.jpg&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Felkablog1%2F%25D0%25BC%25D0%25B5%25D0%25BC%25D1%258B%2F&docid=6ZjWUWjqHZ9LvM&tbnid=9_2seZmg0xwQOM&vet=12ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oECHQQAA..i&w=978&h=978&hcb=2&ved=2ahUKEwi97MWA_pmOAxUzdaQEHV3DIcIQM3oECHQQAA"
}
    response = create_post_endpoint.create_new_meme(body=body)
    meme_id = response.json()['id']
    yield meme_id
    print('after test')
    delete_meme_endpoint.delete_meme(meme_id)

@pytest.fixture()
def get_meme_endpoint(auth_token):
    meme = GetMeme()
    meme.token = auth_token
    return meme

@pytest.fixture()
def get_meme_wrong_auth_token():
    meme = GetMeme()
    meme.token = '1SoyKw8tQXgs8pP'
    return meme

@pytest.fixture()
def get_meme_empty_auth_token():
    meme = GetMeme()
    meme.token = None
    return meme

@pytest.fixture()
def create_post_endpoint(auth_token):
    meme = PostMeme()
    meme.token = auth_token
    return meme

@pytest.fixture()
def update_meme_endpoint(auth_token):
    meme = UpdateMeme()
    meme.token = auth_token
    return meme

@pytest.fixture()
def delete_meme_endpoint(auth_token):
    meme = DeleteMeme()
    meme.token = auth_token
    return meme

@pytest.fixture()
def authorization():
    return Authorize()
