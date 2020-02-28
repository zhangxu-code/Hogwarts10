import random

import pymysql

from test_interface.scripts.handle_yaml import do_yaml


class HandleMysql(object):

    def __init__(self):
        self.conn = pymysql.connect(host=do_yaml.read("mysql", "host"),
                                    user=do_yaml.read("mysql", "user"),
                                    password=do_yaml.read("mysql", "password"),
                                    db=do_yaml.read("mysql", "db"),
                                    port=do_yaml.read("mysql", "port"),
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.cursor = self.conn.cursor()

    def run(self,sql,args=None, is_more=False):
        self.cursor.execute(sql,args)
        self.conn.commit()
        if is_more:
            #返回值是单个的元组, 也就是一行记录, 如果没有结果, 那就会返回null
            return self.cursor.fetchall()
        else:
            # 返回值是单个的元组,也就是一行记录,如果没有结果,那就会返回null
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def create_mobile():
        return "152"+"".join(random.sample("0123456789",8))

    def is_existed_mobile(self, mobile):
        sql = do_yaml.read("mysql", "select_user_sql")
        if self.run(sql,args=[mobile]):
            return True
        else:
            return False

    def create_not_existed_mobile(self):
        while True:
            one_mobile = self.create_mobile()
            if not self.is_existed_mobile(one_mobile):
                break
        return one_mobile

    def is_existed_sqlexec(self, wherestr):
        sql = do_yaml.read("mysql", "select_demo_sql")
        if self.run(sql, args=[wherestr]):
            return True
        else:
            return False


if __name__ == '__main__':
    do_mysql = HandleMysql()
    # print(do_mysql.create_mobile())
    print(do_mysql.create_not_existed_mobile())
    do_mysql.close()