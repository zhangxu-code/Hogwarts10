import json

import requests


class HandleRequests:
    """处理请求"""

    def __init__(self):
        self.one_session = requests.Session()

    def add_headers(self, headers):

        """添加公共请求头"""
        self.one_session.headers.update(headers)

    def send(self, url, method="post", data=None, is_json=True, **kwargs):  # 默认的post json去传 (因为讲的项目就是这样的）
        # datas = '["name": "Victor", "gender": true]'    #json格式的字符串
        # datas = "['name': 'Victor', 'gender': True]"    #字典类型的字符串
        if isinstance(data, str):
            try:
                data = json.loads(data)  # 如果传的就是jason类型的就不会报错
            except Exception as e:
                print("使用日志器来记录日志")
                data = eval(data)

        method = method.lower()  # 把请求方法全都转换能小写
        if method == "get":
            res = self.one_session.request(method, url, **kwargs)
        elif method in ("post", "put", "delete", "patch"):  # 可以www-form表单的形式，也可以传json
            if is_json:  # 如果is_json 为True, 那么以json格式的形式来传参
                res = self.one_session.request(method, url, json=data, **kwargs)
            else:  # 如果is_json为False, 那么以WWW-form的形式来传参
                res = self.one_session.request(method, url, data=data, **kwargs)
        else:
            res = None
            print("不支持【{method}】请求方法")
        return res

    def close(self):
        # 调用会话对象的close方法，是释放资源,还是可以发起请求
        self.one_session.close()