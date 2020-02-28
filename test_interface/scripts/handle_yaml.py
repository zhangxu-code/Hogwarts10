import yaml

from test_interface.scripts.handle_path import CONFIG_FILE_PATH


class HandleYaml(object):

    def __init__(self, filename):
        with open(filename, encoding="utf8") as one_file:
            self.datas = yaml.full_load(one_file)

    def read(self, section, option):
        """
        读取yaml文件的数据
        :param section: yaml文件区域名
        :param option:  yaml文件选项名
        :return:
        """
        return self.datas[section][option]

    @staticmethod
    def write(datas, filename):
        """
        写入数据
        :param self:
        :param datas: 嵌套字典的字典
        :param filename: yaml文件路径
        :return:
        """
        with open(filename, mode="w", encoding="utf8") as one_file:
            yaml.dump(datas, one_file, allow_unicode=True)


do_yaml = HandleYaml(CONFIG_FILE_PATH)

if __name__ == '__main__':
    do_yaml = HandleYaml(CONFIG_FILE_PATH)
    print(do_yaml.read("msg", "success_result"))
    pass