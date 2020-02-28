from unittest import mock
from unittest.mock import MagicMock
import pytest
import requests

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    def mock(*args,**kwargs):
        print("mock")
        return "mock"
    monkeypatch.setattr(requests.sessions.Session,"request",mock)

def test_post(no_requests):
    requests.request("get","http://www.baidu.com")
    requests.post("http://www.baidu.com")

def test_mock():
    requests.request=MagicMock(return_value="mock test")
    print(requests.request("get", "http://www.baidu.com"))