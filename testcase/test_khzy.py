import logging
import pytest

logging.basicConfig(level=logging.DEBUG)
def setup_module():
    logging.info("login")
@pytest.mark.run(order=1)
class TestA:
    #test_1
    def test_1(self):
        logging.info("test_1")
    #test_2
    def test_2(self):
        logging.info("test_2")

    #test_3
    def test_3(self):
        logging.info("test_3")

    #testA环境清理
    def teardown_class(self):
        logging.info("TestA teardown")
@pytest.mark.run(order=2)
class TestB:
    def setup_method(self):
        logging.info("TestB setup method")
    # test_4
    def test_4(self):
        logging.info("test_4")

    # test_5
    def test_5(self):
        logging.info("test_5")

    @pytest.mark.parametrize("a,b,c",[(2,3,5),(1,2,3),(5,5,10)])
    # test_6,验证传过来的3个参数 a+b是否等于c
    def test_6(self,a,b,c):
        assert a+b==c

class TestC:
    # test_7
    @pytest.mark.run(order=5)
    def test_7(self):
        logging.info("test_7")

    # test_8
    @pytest.mark.run(order=3)
    def test_8(self):
        logging.info("test_8")

    # test_9
    @pytest.mark.run(order=4)
    def test_9(self):
        logging.info("test_9")