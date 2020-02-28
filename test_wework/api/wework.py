import requests

from test_wework.api.baseapi import BaseApi


class WeWork(BaseApi):
    #企业ID
    corpid = "wwbbf6d6da2ca6552d"
    #agentID
    agent_id = "1000002"
    #agentsecret
    agent_secret="XlA4d4zgJqI4tYu0ddhkl0yO0cRhZl4-34j7d2cJi60"
    #通讯录secret
    contact_secret = "v8RXo5laFOr3fgfhf1XEcSRa7BRAulZxor6t9hqqnzw"
    #存放tocken的缓存变量
    access_token = None

    @classmethod
    def get_token(cls):
        if cls.access_token == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            params = {'corpid':cls.corpid, 'corpsecret': cls.contact_secret}
            r = requests.get(url, params=params).json()
            print("first get token")
            print(r)
            cls.access_token = r['access_token']
        return cls.access_token