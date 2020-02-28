import json

import requests

from test_wework.utils.utils import Utils
import pprint


class BaseApi:
    printer = pprint.PrettyPrinter(indent=2)
    json_data = None



    @classmethod
    #格式化json格式
    def verbose(cls,json_object):
        print(Utils.format(json_object))
        #self.printer.pprint(json_object)

    @classmethod
    def jsonpath(cls,expr):
        return Utils.jsonpath(cls.jsonpath,expr)

