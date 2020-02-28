import json
from unittest import TestCase

import pytest
from ddt import ddt,data,file_data,unpack
import yaml
from src.calc import Calc

@ddt
class TestCalc:
    def setup(self) -> None:
        self.calc = Calc()
    @pytest.mark.parametrize("a,b,c",[
           (1,1,2),
           (1,0,1),
           (1,-1,0),
           (1000000,1,1000001)])
    def test_add(self, a, b, c):

        assert self.calc.add(a, b) == c

    #@file_data("calc.yaml")
    @pytest.mark.parametrize("a,b,c",yaml.load(open("calc2.yaml")))
    def test_div(self, a, b, c):
        print(a,b,c)
        assert self.calc.div(a,b) == c

    @data((3,2,True), #验证a>b的
          (1,-2,True),
          (4,4,False),#验证a=b的
          (0,0,False),
          (1,5,False), #验证a<b的
          (-1,0,False),
          ("a","b",False),#传入非数值型，验证容错
          (3.1,2,True),#浮点型
          (2.2,2.2,False),
          (-1.5,-1.1,False))
    @unpack
    def test_above(self,a,b,c):
        assert self.calc.above(a,b)==c




