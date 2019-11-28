import tornado.ioloop
import tornado.web
import os
import subprocess
import multiprocessing
import GPS
from tornado.httpserver import HTTPServer

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.get_body_argument("callingParty")
        data1 = self.get_body_argument("callendParty")
        print(data, data1)
        os.system("python userRegister.py {} {}".format(data,data1))
        self.write("发送成功")

class LogoutHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.get_body_argument("callingParty")
        data1 = self.get_body_argument("callendParty")
        print(data, data1)
        os.system("python userLogout.py {} {}".format(data, data1) )
        self.write("发送成功")

class UserGpsHandler(tornado.web.RequestHandler):
    def post(self):
        self.data = self.get_body_argument("callingParty")
        self.data1 = self.get_body_argument("callendParty")
        self.write("发送成功")
        global GPS_pid
        GPS_pid = 123
        print(GPS_pid)
        recv_ip = "192.168.1.45"
        rcu = "r105.pdt.cn"
        lai = '105'
        GPS.GPS_Signal(self.data, self.data1, recv_ip, rcu, lai).start()

        os.system("python GPS.py {} {}".format(self.data, self.data1))


    if __name__=="__main__":
        mp1 = multiprocessing.Process(target=post, args=(100,))


class StopGpsHandler(tornado.web.RequestHandler):
    def post(self):

        cmd = "killall python GPS.py"
        os.system(cmd)
        self.write("GPS已暂停")


application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/register", RegisterHandler),
    (r"/logout", LogoutHandler),
    (r"/gps", UserGpsHandler),
    (r"/stopGps", StopGpsHandler),
    ])

if __name__=="__main__":
    # application.listen(9999)
    # tornado.ioloop.IOLoop.instance().start()
    server = HTTPServer(application)
    server.bind(9999)
    server.start(0)

    tornado.ioloop.IOLoop.current().start()