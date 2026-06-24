import pytest
from endpoints.authorization import Authorize
from endpoints.get_meme import GetMeme
from endpoints.create_meme import PostMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.update_meme import UpdateMeme
from fixture_helper import check_token_alive
from precondition_meme import precondition_meme


@pytest.fixture(scope='session')
def auth_token():
    auth = Authorize()
    token = auth.get_token()
    return token

@pytest.fixture()
def new_meme_id(create_post_endpoint, delete_meme_endpoint):
    print('before test')
    body = precondition_meme()
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
