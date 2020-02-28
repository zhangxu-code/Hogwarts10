
import requests

from test_wework.api.baseapi import BaseApi
from test_wework.api.wework import WeWork
from test_wework.scripts.handle_requests import HandleRequests


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def __init__(self):
        self.do_request = HandleRequests()
    #部门列表
    def list(self,id):
        params = {'access_token': WeWork.get_token(), 'id': id}
        self.json_data = self.do_request.send(self.list_url, method="get", params=params).json()
        self.verbose(self.json_data)
        return self.json_data

    #创建部门
    def create(self, name, name_en, parentid, order):
        data = {"name": name, "name_en": name_en, "parentid": parentid, "order": order,"access_token": WeWork.get_token()}
        params = {"access_token": WeWork.get_token()}
        # 上传中有中文，需要设置UTF-8编码
        headers = {'content-type': 'application/json; charset=utf-8'}
        self.do_request.add_headers(headers)
        self.json_data = self.do_request.send(self.create_url, method="post", data=data, params=params).json()
        self.verbose(self.json_data)
        return self.json_data


    #删除部门
    def delete(self,id):
        params = {"access_token": WeWork.get_token(), "id": id}
        self.json_data = self.do_request.send(self.delete_url, method="get", params=params).json()
        return self.json_data

    #更新部门
    def update(self):
        pass