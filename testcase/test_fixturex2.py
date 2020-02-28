
def test_1(topics):
    assert len(topics["topics"]) ==2

def test_2(topics):
    assert topics["topics"][0]["deleted"] == False