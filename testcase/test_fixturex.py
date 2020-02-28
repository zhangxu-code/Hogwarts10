import requests

def test_1(topics):
    assert len(topics["topics"]) ==2

def test_2(topics2):
    assert topics2["topics"][0]["deleted"] == False