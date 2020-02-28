import requests
import yaml
from yaml import load,dump
import pytest

def test_yaml():
    env = {
        "docker.testing-studio.com":{
            "dev":"1.1.1.1",
            "test":"1.1.1.2"
        },
        "default":"dev"
    }
    print(env)
    print(dump(env))

    yaml_str = """
    default: dev
    docker.testing-studio.com:
        dev: 1.1.1.1
        test: 1.1.1.2
    """

    print(load(yaml_str))

    f = open("demo.yaml","w")
    print(dump(env, f))

def test_read_yaml_file():
    with open("demo.yaml","r") as f2:
        print(load(f2))

# @pytest.mark.parametrize("num",load(open("demo.yaml","r"))["array"])
# def test_param_from_yaml(num):
#     assert  num >1

class HttpApi(yaml.YAMLObject):
    yaml_tag="!HttpApi"
    def __init__(self,method,url,query):
        self.method = method
        self.url= url
        self.query = query
    def send(self):
        return requests.request(self.method,self.url,params = self.query).json()

    def send(self, url, method="post", data=None, is_json=True, **kwargs):  # 默认的post json去传 (因为讲的项目就是这样的）
        # datas = '["name": "Victor", "gender": true]'    #json格式的字符串
        # datas = "['name': 'Victor', 'gender': True]"    #字典类型的字符串
        if isinstance(data, str):
            try:
                data = json.loads(data)  # 如果传的就是jason类型的就不会报错
            except Exception as e:
                print("使用日志器来记录日志")
                data = eval(data)

        method = method.lower()   # 把请求方法全都转换能小写
        if method == "get":
            # res = self.one_session.get(url, params=datas, **kwargs)  # get 没有请求体 不能传data

            res = self.one_session.request(method, url, params=data, **kwargs)
        elif method in ("post", "put", "delete","patch"):  # 可以www-form表单的形式，也可以传json
            if is_json:     # 如果is_json 为True, 那么以json格式的形式来传参
                # res = self.one_session.post(url, json=datas, **kwargs)
                res = self.one_session.request(method, url, json=data, **kwargs)
            else:  # 如果is_json为False, 那么以WWW-form的形式来传参
                # res = self.one_session.post(url, datas-datas, **kwargs)
                res = self.one_session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print("不支持【{method}】请求方法")
        return res  # 如果传的是字典

def test_write_httpapi():
    h = HttpApi("get","https://testerhome.com/api/v3/topics.json",{"limit":2})
    print(dump(h,open("/tmp/1","w")))

def test_read_httpapi():
    req = load(open("/tmp/1","r"))
    print(req)


def test_get_login():

    req:HttpApi = load(open("httpapi.yaml","r"))
    print(req)
    print(req.send())


    # req = HttpApi("get","https://testerhome.com/api/v3/topics.json",{"limit":2})
    # print(dump(req))
    # print(req.send())
    # assert req.send()['topics'][-1]['user']['login'] == "simple"
    #
    # req = HttpApi("get", "https://testerhome.com/api/v3/topics.json", {"limit": 3})
    # print(req.send())
    #
    # # url = "https://testerhome.com/api/v3/topics.json"
    # # r = requests.get(url, params={'limit': '2'})
    # # print(r.json())
    # assert req.send()['topics'][-1]['user']['login'] == "Jimmy_sunny"
