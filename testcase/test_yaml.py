import os

import yaml


def test_yaml():
    print(yaml.load(open("calc.yaml")))
    print(os.path.realpath(__file__))
    print(os.getcwd())
