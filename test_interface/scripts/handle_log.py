import logging
import os

from test_interface.scripts.handle_path import LOGS_DIR
from test_interface.scripts.handle_yaml import do_yaml


class MyLogger(object):

    @classmethod
    def create_logger(cls):
        my_log = logging.getLogger(do_yaml.read("log","log_name"))
        my_log.setLevel(do_yaml.read("log","logger_level"))
        formater = logging.Formatter(do_yaml.read("log","formatter"))
        sh = logging.StreamHandler()
        sh.setLevel(do_yaml.read("log","logger_level"))
        sh.setFormatter(formater)
        my_log.addHandler(sh)

        fh = logging.FileHandler(filename=os.path.join(LOGS_DIR, do_yaml.read("log", "logfile_name")),
                                 encoding='utf8')
        fh.setLevel(do_yaml.read("log", "logfile_level"))
        fh.setFormatter(formater)
        my_log.addHandler(fh)
        return my_log


do_log = MyLogger.create_logger()


if __name__ == '__main__':
    do_log = MyLogger.create_logger()
    do_log.debug("debug")
    pass