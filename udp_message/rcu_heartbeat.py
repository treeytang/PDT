from time import sleep
import socket
import random
import struct
import threading


class Heart_Beat():
    #一下为
    def __init__(self):
        # 消息类型(RCU给MSC心跳报文请求) 2个字节大小
        self.msg_type = (1, 3)
        # 厂家识别号  2个字节大小
        self.mfid = (1, 0, 0, 0, 0, 0, 0, 0)
        # 序号  2个字节大
        # 基站系统号  2个字节大小
        self.lai = (108, 0)
        # 基站RCU的IP地址  4个字节大小
        self.rcu_ip = (192, 168, 1, 54)
        # 组网类型  4个字节大小
        self.np = (1, 0, 0, 0)
        # rsvd1 2字节大小
        self.rsvd1 = (0, 0, 0, 0, 0, 0)
        # 网络延迟，单位：ms  4个字节大小
        self.net_dly = (51, 69, 114, 74)
        # 网络丢包率，0-100%  4个字节大小
        self.net_ll = (112, 87, 86, 90)

        self.recv_ip = "192.168.1.54"
        self.recv_port = 16888
        self.send_ip = "192.168.1.249"
        self.send_port = 17000

    # 心跳延迟时间  2个字节大小
    def diff(self):
        s = random.randrange(0, 3)
        return (s, 0)

    # 网络健康指数  4个字节大小
    def net_heaths(self):
        s = random.randrange(1, 256)
        s1 = random.randrange(1, 256)
        return (s, s1)

    # 网络抖动率  4个字节大小
    def net_jit(self):
        s = random.randrange(0, 3)
        return (s, 0, 0, 0)

    # 填充字符
    def fn(self):
        l = []
        for i in range(60):
            l.append(0)
        l = tuple(l)
        return l

    def hb_udp_socket_recv_client(self, udp_socket_client, recv_address):
        while True:
            try:
                recv_data, recv_addr = udp_socket_client.recvfrom(4096)
                print([hex(i) for i in struct.unpack('104B', recv_data)])
            except Exception as e:
                print(e)

    def hb_udp_socket_send_client(self, udp_socket_client, send_address):
        print('连接成功,开始发送信息了:)')
        while True:
            g = 0
            for i in range(2, 256, 2):
                num = 1
                for j in range(2, 256, 2):
                    heath = self.net_heaths()
                    if g % 8 == 0:
                        num += 1
                    net_heath = (heath[0], heath[1], num, 0)
                    cseq = (j, i, 0, 0)
                    s = struct.pack('2B8B4B2B4B8B4B2B6B4B4B4B4B60B', *self.msg_type, *self.mfid, *cseq, *self.lai,
                                    *self.rcu_ip,
                                    *(0, 0, 0, 0, 0, 0, 0, 0), *self.np, *self.diff(), *self.rsvd1, *self.net_jit(),
                                    *net_heath, *self.net_dly,
                                    *self.net_ll, *self.fn())
                    udp_socket_client.sendto(s, send_address)
                    sleep(5)



    def heartbeat(self):
        udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket_client.bind((self.recv_ip, self.recv_port))
        recv_address = (self.recv_ip, self.recv_port)
        send_address = (self.send_ip, self.send_port)
        socket_send_thread = threading.Thread(target=self.hb_udp_socket_send_client,
                                              args=(udp_socket_client, send_address)
                                              )
        socket_recv_thread = threading.Thread(target=self.hb_udp_socket_recv_client,
                                              args=(udp_socket_client, recv_address)
                                              )
        socket_recv_thread.start()
        socket_send_thread.start()

