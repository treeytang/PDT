import socket
import threading
import os, signal
import time
from time import sleep
import random
import sys

calling = int(sys.argv[1])
callend = int(sys.argv[2])

class Logout:
    def __init__(self, recv_ip, rcu, calling_party, callend_party):
        self.recv_ip = recv_ip
        self.recv_port = 15062
        self.send_ip = "192.168.1.249"
        self.send_port = 5060
        self.rcu = rcu
        self.calling_party = calling_party
        self.callend_party = callend_party

    def comm(self, num):
        strs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*/[]:.?"
        l = ''
        for i in range(num):
            l += str(random.choice(strs))
        return l

    def call_ID(self):
        num = random.choice([7, 8])
        l = self.comm(num)
        return l

    def tag(self):
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

    def udp_socket_recv_client(self, udp_socket_client, recv_address):
        udp_socket_client.bind(recv_address)
        while True:
            try:
                recv_data, recv_addr = udp_socket_client.recvfrom(1024)
                pass
                # print('收到來自<%s>的信息'% recv_addr[0],
                #         recv_data.decode('utf-8') + '\n' + '<<', end='')
            except Exception as e:
                print(e)

    def udp_socket_send_client(self, udp_socket_client, send_address):
        # print('连接成功,开始发送信息了:)')
        a = 1

        # for userid in range(3407883, 3408259):
        for user in range(self.calling_party, self.callend_party):
            userid = str(user)
            # print("信息发送第%d遍" % a)

            send_data = "R p:{}\r\n" \
                        "i:{}\r\n" \
                        "f:<p:{}>;g={}\r\n" \
                        "t:-\r\n" \
                        "Q:{} R\r\n" \
                        "v:r108.pdt.cn;b={}~\r\n" \
                        "m:<s:r105.pdt.cn;m=192.168.1.37:15062>;e=0\r\n" \
                        "H:70\r\n" \
                        "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
                        "l:0\r\n" \
                        "\r\n".format(userid, self.call_ID(), userid, self.tag(), self.Qseq(), self.via_by())
            a += 1
            # print(send_data)
            # 退出程序
            udp_socket_client.sendto(send_data.encode('utf-8'), send_address)
            sleep(0.02)
        # udp_socket_client.close()
        pid = os.getpid()
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        os.system(cmd)



    def start(self):
        print(os.getpid())
        udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        recv_ip = self.recv_ip
        recv_port = self.recv_port
        send_ip = self.send_ip
        send_port = self.send_port
        recv_address = (recv_ip, int(recv_port))
        send_address = (send_ip, int(send_port))

        socket_send_thread = threading.Thread(target=self.udp_socket_send_client,
                                              args=(udp_socket_client, send_address)
                                              )
        socket_recv_thread = threading.Thread(target=self.udp_socket_recv_client,
                                              args=(udp_socket_client, recv_address)
                                              )
        socket_recv_thread.start()
        socket_send_thread.start()


def main():
    calling_party = int(sys.argv[1])
    callend_party = int(sys.argv[2])
    Logout("192.168.1.45", "r105.pdt.cn", calling_party, callend_party).start()


if __name__ == '__main__':
    main()
