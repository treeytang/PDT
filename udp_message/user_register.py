from time import sleep
import random
import socket
import threading
import time
import os




class User_Register():
    def __init__(self):
        self.recv_ip = "192.168.1.54"
        self.recv_port = 18820
        self.send_ip = "192.168.1.249"
        self.send_port = 5060


    def comm(self, num):
        strs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%^&*/[]:.?"
        l = ''
        for i in range(num):
            l += str(random.choice(strs))
        return l


    def call_ID(self):
        num = random.choice([7, 8])
        l = self.comm(num)
        return l


    def tags(self):
        num = random.choice([3, 4])
        l = self.comm(num)
        return l


    def via_by(self):
        num = random.choice([3, 4])
        l = self.comm(num)
        if l[0] == ';':
            l = l.replace(";", "A")
        if l[0] == ',':
            l = l.replace(",", "A")
        return l


    def Qseq(self):
        return (random.randrange(30, 999))


    def ur_udp_socket_recv_client(self, udp_socket_client):
        while True:
            try:
                recv_data, recv_addr = udp_socket_client.recvfrom(1024)
                print('用户注册 收到來自<%s>的信息' % recv_addr[0],
                      recv_data.decode('utf-8') + '\n' + '<<', end='')
            except Exception as e:
                print(e)


    def ur_udp_socket_send_client(self, udp_socket_client, send_address):
        print('连接成功,开始发送信息了:')
        sleep(5)
        a = 1
        for userid in range(4882433, 4882450):

            print("用户注册 信息发送第%d遍" % a)
            filename = open("userid.txt", "a")
            filename.write("%d***" % userid)
            filename.close()
            send_data = "R p:{}\r\n" \
                        "i:{}\r\n" \
                        "f:<p:{}>;g={}\r\n" \
                        "t:-\r\n" \
                        "Q:{} R\r\n" \
                        "v:r108.pdt.cn;b={}~\r\n" \
                        "m:<s:r108.pdt.cn;m=192.168.1.54:18820>\r\n" \
                        "H:70\r\n" \
                        "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
                        "c:a/m\r\n" \
                        "l:43\r\n" \
                        "\r\n" \
                        "<attachgroup><AG>16515073</AG></attachgroup>\r\n".format(userid, self.call_ID(), userid,
                                                                                 self.tags(), self.Qseq(), self.via_by())
            a += 1
            # # 退出程序
            # if userid == 3439023:
            #     sleep(2)
            #     print("线程号为：",os.getpid())
            #     udp_socket_client.close()
            #     print('退出成功')
            #     # os.kill(os.getpid(), signal.SIGKILL)
            # else:
            #     print("发送内容为：",send_data)
            udp_socket_client.sendto(send_data.encode('utf-8'), send_address)
            sleep(0.05)

        pid = os.getpid()
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        os.system(cmd)


    def user_register(self):
        print(os.getpid())
        # sleep(5)
        udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket_client.bind((self.recv_ip, self.recv_port))
        recv_address = (self.recv_ip, self.recv_port)
        send_address = (self.send_ip, self.send_port)
        socket_send_thread = threading.Thread(target=self.ur_udp_socket_send_client,
                                              args=(udp_socket_client, send_address)
                                              )
        socket_recv_thread = threading.Thread(target=self.ur_udp_socket_recv_client,
                                              args=(udp_socket_client,)
                                              )
        socket_recv_thread.start()
        socket_send_thread.start()
        print(1)

User_Register().user_register()