
import pytest
import requests
from utils.apis import APIS


@pytest.fixture(scope="module",autouse=True)
def apis():
    return APIS()


def test_getuser_validation(apis):
    response = apis.get("users")
    print("response.json()")

    assert response.status_code == 200
    assert len(response.json()) > 0

def test_postuser_validation(apis):

    user_data = {

        "name": "Gohar3",
        "username": "qa user",
        "email": "test@gmail.com"
    }
    response = apis.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    # assert len(response.json()) > 0
    # assert response.json()["name"] == "Gohar"
    assert response.json()["name"] == "Gohar3"











