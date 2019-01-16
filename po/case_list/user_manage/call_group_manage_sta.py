from time import sleep
import unittest, random, sys,time
from comm import myunit, picture
from test_cases.user_manage.call_group_manage_page import Call_Group
import HTMLTestRunner


class Ticket_Query(myunit.MyTest):

    def user_login(self, username="", password=""):
        Call_Group(self.driver).user_login(username, password)

    def test_show_page_num(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 验证页面显示数量'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).verify_show_num()
        self.assertEqual(msg.strip(), '662')

    def test_show_page_num_1(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 验证每页显示输入框与定量显示'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).verify_show_num_1()
        self.assertEqual(msg.strip(), '1')

    def test_add_group_1(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个正确的组 只填写号码范围 800-40-900/40-910 而后通过操作栏删除'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_1()
        self.assertEqual(msg.strip(), '11')

    def test_add_group_1_1(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个正确的组 只填写号码范围 800-40-900/40-910 而后通过复选框全选删除'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_1_1()
        self.assertEqual(msg.strip(), '11')

    def test_add_group_1_2(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个正确号码 只填写号码范围 800-40-900 命名用户名称为：成都测试 而后通过复选框选择删除'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_1_2()
        self.assertEqual(msg.strip(), '1')

    def test_add_group_1_3(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个正确号码 只填写号码范围 800-40-900 不填写用户名称 点击确定 验证:是否留在该页面'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_1_3()
        self.assertEqual(msg, True)

    def test_add_group_1_4(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个正确号码 只填写号码范围 800-40-900 用户名称大于7个字符 验证：系统是否自动删除了第七位后的字符'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_1_4()
        self.assertEqual(msg.strip(), '1')

    #def test_add_group_1_5(self):
     #   '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个正确号码 号码范围:800-40-900 填写租户呼出范围'''
     #   self.user_login(username="thy", password="admin")
     #   msg = Call_Group(self.driver).add_group_1_5()
     #   self.assertEqual(msg.strip(), '1')

    def test_add_group_2(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个以存在的组 号码范围 328 20 901/910 验证:是否出现替换提示弹窗'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_2()
        self.assertEqual(msg, True)


    def test_add_group_3(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个以存在的组 号码范围 328 20 901/910 验证:点击取消是否关闭弹窗留在添加页面'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_3()
        self.assertEqual(msg, True)

    def test_add_group_4(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个以存在的组 号码范围 328 20 901/910 验证:点击多选择框和“是” 是否返回通话组列表页面'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_4()
        self.assertEqual(msg, True)

    def test_add_group_5(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个以存在的组 号码范围 328 20 901/910 验证:点击多选择框和“否” 是否返回通话组列表页面'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_5()
        self.assertEqual(msg, True)

    def test_add_group_6(self):
        '''检查进入通话组管理界面(默认进入通话组列表) 点击添加 添加一个以存在的组 号码范围 328 20 992 验证:点击多选择框和“是” 是否返回通话组列表页面'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).add_group_6()
        self.assertEqual(msg, True)


    def test_roma_group_list(self):
        '''检查进入漫游 验证页面显示数量与应显示数量'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list()
        self.assertEqual(msg.strip(), '117')

    def test_roma_group_list_1(self):
        '''检查进入漫游 验证页面显示数量与应显示数量'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_1()
        self.assertEqual(msg.strip(), '1')

    def test_roma_group_list_2(self):
        '''检查进入漫游 添加一个漫游组：800-40-990/40-999 添加成功后查看并删除'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_2()
        self.assertEqual(msg.strip(), '10')

    def test_roma_group_list_3(self):
        '''检查进入漫游 添加一个已经存在的漫游组：328-20-931/20-935 验证是否出现替换提示窗'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_3()
        self.assertEqual(msg, True)

    def test_roma_group_list_4(self):
        '''检查进入漫游 添加一个已经存在的漫游用户：328-20-931 用户名称为：bbb 验证是否出现替换提示窗'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_4()
        self.assertEqual(msg, True)

    def test_roma_group_list_5(self):
        '''检查进入漫游 添加一个已经存在的漫游用户：328-20-931 用户名称为空 验证是否留在该页面(无法添加)'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_5()
        self.assertEqual(msg, True)

    def test_roma_group_list_6(self):
        '''检查进入漫游 添加一个漫游组：800-40-900/910  优先等级为：优先 通话限时为：300  通话配置：全选第二项（默认不选的情况全为第一项） 验证是否添加成功'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_6()
        self.assertEqual(msg, True)


    def test_roma_group_list_7(self):
        '''检查进入漫游 添加一个漫游组：800-40-900/910  其余基本信息默认  通话配置：全选第二项（默认不选的情况全为第一项） 验证是否添加成功'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_7()
        self.assertEqual(msg, True)

    def test_roma_group_list_8(self):
        '''检查进入漫游 添加一个漫游组：800-40-900/910  其余基本信息默认  通话配置：默认全为第一项  验证是否添加成功'''
        self.user_login(username="thy", password="admin")
        msg = Call_Group(self.driver).roma_group_list_8()
        self.assertEqual(msg, True)


    def test_grade_group(self):
        '''检查进入分级组管理页面 验证显示数量是否正确'''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).grade_group()
        self.assertEqual(msg.strip(), '6')

    def test_grade_group_1(self):
        '''检查进入分级组管理页面 点击添加 添加一个正确的组号 验证是否添加成功 而后删除该号码 使用操作栏图标删除 '''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).grade_group_1()
        self.assertEqual(msg, True)

    def test_grade_group_1_1(self):
        '''检查进入分级组管理页面 点击添加 添加一个正确的组号 验证是否添加成功 而后删除该号码 使用页面下方图标删除 '''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).grade_group_1_1()
        self.assertEqual(msg, True)

    def test_grade_group_2(self):
        '''检查进入分级组管理页面 点击添加 添加一个不启用的组号 添加成功后通过点击修改启用 验证是否修改后返回分级组管理列表页面 '''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).grade_group_2()
        self.assertEqual(msg, True)


    def test_grade_group_3(self):
        '''检查进入分级组管理页面  验证上一步操作是否修改成功 '''
        #点击添加 添加一个不启用的组号 添加成功后通过点击修改启用
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).grade_group_3()
        self.assertEqual(msg, True)


    def test_grade_group_4(self):
        '''检查进入分级组管理页面  点击添加 添加一个已存在的组号 出现替换提示弹窗 点击确定跳转到分级组管理列表页面 '''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).grade_group_4()
        self.assertEqual(msg, True)




    def test_temp_group(self):
        '''进入临时应急组页面 验证组用户数量'''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).temp_group_list()
        self.assertEqual(msg.strip(), '52')

    def test_temp_group_1(self):
        '''进入临时应急组页面 验证分页按钮数量是否正确'''
        self.user_login(username='thy', password='admin')
        msg = Call_Group(self.driver).temp_group_list_1()
        self.assertEqual(msg.strip(), '1')




