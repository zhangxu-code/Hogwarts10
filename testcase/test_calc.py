from unittest import TestCase
from ddt import ddt,data,file_data,unpack
import yaml
from src.calc import Calc

@ddt
class TestCalc(TestCase):

    @data((1,1,2),
           (1,0,1),
           (1,-1,0),
           (1000000,1,1000001))
    @unpack
    def test_add(self, a, b, c):
        calc = Calc()
        result = calc.add(a, b)
        self.assertEqual(result, c)

    @file_data("calc.yaml")
    def test_div(self, a, b, c):
        calc = Calc()
        result = calc.div(a, b)
        self.assertEqual(result, c)

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
        calc = Calc()

        result = calc.above(a,b)
        self.assertEqual(result,c)




