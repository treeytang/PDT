import time,os
import unittest
import HTMLTestRunner


def runner(case):
    suite = unittest.TestSuite()#收集测试用例
    # loader = unittest.TestLoader()#加载测试用例
    # l = [['thy','123123123', '慕学在线网登录'],
    #      ['pmh', '123123', '慕学在线网登录'],
    #      ['thy', '123123', '课程机构列表 - 慕学在线网']
    #      ]
    # for i in l:

    suite.addTest(case)
    now = time.strftime('%Y%m%d%H%M%S')
    filename =  os.path.dirname(os.path.abspath('.'))+'\\report\\test_report'+now+'result.html'
    file = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='MuXue测试报告', description='用例的执行情况')
    runner.run(suite)
