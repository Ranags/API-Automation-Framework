
import pytest
import requests
from utils.apis import APIS


@pytest.fixture(scope="module")
def apis():
    return APIS()


def test_getuser_validation(apis):
    response = apis.get("users")
    print("response.json()")

    assert response.status_code == 200
    assert len(response.json()) > 0



