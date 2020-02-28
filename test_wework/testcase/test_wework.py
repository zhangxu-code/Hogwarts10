from test_wework.api.wework import WeWork


class TestWework:
    def test_get_token(self):
        wework = WeWork()
        token = wework.get_token()
        assert  token != None

        token = wework.get_token()
        assert token != None

        token = wework.get_token()
        assert token != None