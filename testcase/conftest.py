import requests
import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
@pytest.fixture(scope="session")
def topics():
    url="http://0.0.0.0:8889/topics.html"
    #url="https://testerhome.com/api/v3/topics.json?limit=2"
    yield requests.get(url).json()
    logging.info("teardown")

@pytest.fixture(params=[
    "http://0.0.0.0:8889/topics.html",
    "https://testerhome.com/api/v3/topics.json?limit=2"])
def topics2(request):
    url = request.param
    # url="https://testerhome.com/api/v3/topics.json?limit=2"
    def fin():
        logging.info("after yield teardown")
    request.addfinalizer(fin)
    return requests.get(url).json()


