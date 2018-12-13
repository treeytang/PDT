import os
import smtplib
import sys
import time
from email.mime.text import MIMEText

mailto_list = ["870686645@qq.com"]

mail_host = "smtp.163.com"
mail_user = "treeytang@163.com"
mail_pass = "thy940311"


def send_mail(to_list, file_new):
    """
    to_list: 发给谁
    sub: 主题
    content:内容
    send_mail("*******@126.com","测试报告"，"测试")
    """
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    me = mail_user
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = u'自动化测试报告'
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


if __name__ == '__main__':

    file_path = ('./result.html')

    if send_mail(mailto_list, file_path):
        print("发送成功")
    else:
        print("发送失败")