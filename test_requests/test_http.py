import json

import requests
from requests import Response
from jsonpath import jsonpath
from jsonschema import validate


class TestHttp:
    def test_get(self):
        proxies = {'http':'http://127.0.0.1:8998/'}
        #r=requests.get('https://testerhome.com/hogwarts',proxies = proxies)
        r = requests.get('http://www.baidu.com', proxies=proxies)

        print(r)

    def test_get_query(self):
        url = "https://httpbin.org/#/HTTP_Methods/get_get"
        payload = {'key1':'value1','key2':['value2','value3']}
        r=requests.get(url,params=payload)
        self.inspect_response(r)

    def test_get_query_header(self):
        url = "https://httpbin.org/get"
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {'a':'2','bcd':'header demo','accept': 'application/json'}
        r = requests.get(url, params=payload, headers = headers)
        self.inspect_response(r)

    def test_post(self):
        url = "https://httpbin.org/post"#https://httpbin.org/post
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {'a':'2','bcd':'header demo','accept': 'application/json'}
        proxies = {'http': 'http://127.0.0.1:8998/'}
        r = requests.post(url, json=payload, headers = headers,proxies = proxies)
        self.inspect_response(r)


    def test_testerhome(self):
        url = "https://testerhome.com/api/v3/topics.json"
        r = requests.get(url, params={'limit':'2'})
        print(r.json())
        print(r.json()['topics'][0]['id'])
        assert r.json()['topics'][0]['id'] == 22058

    #test_get_login() 发起get请求https://testerhome.com/api/v3/topics.json?limit=2 断言最后一条结果中的帖子的用户名是liangqiangWang
    def test_get_login(self):
        url = "https://testerhome.com/api/v3/topics.json"
        r = requests.get(url, params={'limit':'2'})
        print(r.json())
        assert r.json()['topics'][-1]['user']['login'] == "zhuzhu112233"

    def test_get_login_jsonpath(self):
        url = "https://testerhome.com/api/v3/topics.json"
        r = requests.get(url, params={'limit': '2'})
        print(r.json())
        #jsonpath.jsonpath(r.json(),"$..[?(@login == 'mzmb')]")
        assert jsonpath(r.json(),"$.topics[?(@.user.login == 'mzmb')].user.id")[0] == 19896

    def test_get_login_jsonschema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topics_schema.json"))
        validate(data,schema=schema)

    #使用requests发送get请求，从企业微信的响应中获取access_token
    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {'corpid':'ww16ecb3d02ad26cb1','corpsecret':'4HeWY_ekQkrObcTKHi_gOP2ZI7-HKHDRZlEciCEv8Tk'}#4HeWY_ekQkrObcTKHi_gOP2ZI7-HKHDRZlEciCEv8Tk
        r = requests.get(url,params=params)
        print(r.json())
        print(r.json()['access_token'])


    #test_xueqiu_search 在雪球上发起股票搜索，搜索sogo股票，断言结果中有名字为“搜狗”的股票
    def test_xueqiu_search(self):
        url = "https://xueqiu.com/stock/search.json"
        params = {'code':'sogo','size':'3','page':'1'}
        headers = {
            'Accept':'application/json',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
        }
        cookies = {
            "xq_a_token": "e50af02165b86c42cf428646aec7411e6404439f"
        }
        r = requests.get(url,params=params,headers = headers,cookies = cookies)
        print(r.json())
        assert  r.json()['stocks'][0]['name'] == '搜狗'


    def inspect_response(self,r:Response):
        print(r.headers)
        print(r.cookies)
        print(r.status_code)
        print(r.encoding)
        print(r.url)
        print(r.content)
        print(r.text)
        print(r.raw)
        print(r.json())