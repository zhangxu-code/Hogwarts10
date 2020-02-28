# -*- conding: utf-8 -*-
# @Time:2019/11/17 16:51
# @Author:lyc
# @File: handle_excel.py
# @Software: PyCharm


import os
import openpyxl as openpyxl
from test_interface.scripts.handle_path import DATAS_DIR
from test_interface.scripts.handle_yaml import do_yaml


class CaseData(object):
    pass


class HandleExcel(object):

    def __init__(self, sheetname, filename=None):
        if filename is None:
            self.filename = os.path.join(DATAS_DIR, do_yaml.read("excel", "cases_path"))
        else:
            self.filename = filename
        self.sheetname = sheetname

    def open(self):
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    def read_data(self):
        self.open()
        rows = list(self.sh.rows)
        cases = []
        title = [c.value for c in rows[0]]
        for r in rows[1:]:
            data = [c.value for c in r]
            case_data = dict(zip(title, data))   #实现数据键值格式
            cases.append(case_data)
        self.wb.close()
        return cases

    def read_data_obj(self):
        self.open()
        rows = list(self.sh.rows)
        cases = []
        title = [c.value for c in rows[0]]
        for r in rows[1:]:
            data = [c.value for c in r]
            case = CaseData()
            for i in zip(title, data):
                setattr(case, i[0], i[1])
            cases.append(case)
        self.wb.close()
        return cases

    def write_data(self, row, column, value):
        self.open()
        self.sh.cell(row=row, column=column, value=value)
        self.wb.save(self.filename)
        self.wb.close()


if __name__ == '__main__':
    read = HandleExcel('register')
    read.read_data_obj()
    pass
