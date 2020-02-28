from test_wework.api.departmentf import Department
from test_wework.scripts.handle_mysql import HandleMysql
from test_wework.utils.utils import Utils


class TestDepartment:
    department = Department()
    do_mysql = HandleMysql()
    def setup_class(self):
        pass
    #部门列表
    def test_list(self):
        #list json assert
        r = self.department.list("")
        assert r["errcode"] == 0
        assert r["department"][0]["name"] == "红色公司"

        #取数据库里的值，做相关断言 因
        result = self.do_mysql.run("SELECT * FROM jmeter_class.user",is_more=True)
        print(result)
        print(result[0]["username"])
        assert result.__len__() >0


    def test_create(self):
        r = self.department.create("第十期7","dsq7",1,1000)
        assert r["errcode"] == 0
        assert r["errmsg"] == "created"
        exist = False


        for depart in self.department.list("")["department"]:
            if depart["id"] == r["id"]:
                exist = True

        assert exist == True

    def test_delete(self):
        delete_id = "32823"
        r = self.department.delete(delete_id)
        print(r)
        assert r["errcode"] == 0
        assert r["errmsg"] == "deleted"

        for depart in self.department.list("")["department"]:
            if depart["id"] != delete_id:
                exist = True

        assert exist == True
