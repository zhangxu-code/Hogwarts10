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

    def is_existed_sqlexec(self, wherestr):
        sql = do_yaml.read("mysql", "select_demo_sql")
        if self.run(sql, args=[wherestr]):
            return True
        else:
            return False


if __name__ == '__main__':
    do_mysql = HandleMysql()
    print(do_mysql.is_existed_sqlexec(1))
    do_mysql.close()