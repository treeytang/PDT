import os
import smtplib
import sys
import time
import unittest
from email.mime.text import MIMEText
from HTMLTestRunner import HTMLTestRunner

# # =========================邮件接收者============================
mailto_list = ["870686645@qq.com"]
# #============= 设置服务器，用户名、口令以及邮箱的后缀===============
mail_host = "smtp.163.com"
mail_user = "treeytang@163.com"
mail_pass = "thy940311"
# #===========================发送邮件============================
def send_mail(to_list, file_new):
        """
        to_list: 发给谁
        sub: 主题
        content:内容
        send_mail("*******@**.com","测试报告"，"主要功能测试")
        """
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        me = mail_user
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = '自动化测试报告'
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
            s = smtplib.SMTP()
            s.connect(mail_host, 25)
            s.login(mail_user, mail_pass)
            s.sendmail(me, to_list, msg.as_string())
            s.close()
            return True
        except Exception as e:
            print(str(e))
            return False


# # ==============查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
        lists = os.listdir(testreport)
        lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" + fn))
        file_new = os.path.join(testreport, lists[-1])
        print (file_new)
        return file_new







if __name__ == '__main__':
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = os.path.dirname(os.path.abspath('.'))+'\\report\\test_report\\'+now+'result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='nmp网管自动化测试报告',
                        description='测试环境：windows7 浏览器：Chrome Python版本：3.6')
        discover = unittest.defaultTestLoader.discover('..',
                                               pattern='*_sta.py')
        runner.run(discover)
        fp.close()
        file_path =os.path.dirname(os.path.abspath('.'))+'\\report\\test_report'
        file_name = new_report(file_path)
        if send_mail(mailto_list, file_name):
            print("发送成功")
        else:
            print("发送失败")





