import socket
import threading
import struct,random
from time import sleep


#消息类型(RCU给MSC心跳报文请求) 2个字节大小
msg_type = (1, 3)
#厂家识别号  2个字节大小
mfid = (1,0,0,0,0,0,0,0)
#序号  2个字节大
#基站系统号  2个字节大小
lai = (119,0)
#基站RCU的IP地址  4个字节大小
rcu_ip = (192, 168, 1, 63)
#组网类型  4个字节大小
np = (1,0,0,0)
#心跳延迟时间  2个字节大小
def diff():
    s = random.randrange(0,3)
    return (s, 0)
# rsvd1 2字节大小
rsvd1 = (0,0,0,0,0,0)
#网络健康指数  4个字节大小
def net_heaths():
    s = random.randrange(1,256)
    s1 = random.randrange(1,256)
    return (s,s1)
#网络延迟，单位：ms  4个字节大小
net_dly = (51,69,114,74)
#网络丢包率，0-100%  4个字节大小
net_ll = (112,87,86,90)
#网络抖动率  4个字节大小
def net_jit():
    s = random.randrange(0,3)
    return (s,0,0,0)
#填充字符
def fn():
    l = []
    for i in range(60):
        l.append(0)
    l = tuple(l)
    return l


def udp_socket_recv_client(udp_socket_client, recv_address):
    while True:
        try:
            recv_data, recv_addr = udp_socket_client.recvfrom(4096)
            print(recv_addr)
        except Exception as e:
            print(e)


def udp_socket_send_client(udp_socket_client, send_address):
    print('连接成功,开始发送信息了:)')
    a = 0
    while True:

        g = 0
        for i in range(2, 256, 2):
            num = 1
            for j in range(2, 256, 2):
                heath = net_heaths()
                if g % 8 == 0:
                    num += 1
                net_heath = (heath[0], heath[1], num, 0)
                cseq = (j, i, 0, 0)
                s = struct.pack('2B8B4B2B4B8B4B2B6B4B4B4B4B60B', *msg_type, *mfid, *cseq, *lai, *rcu_ip,
                                *(0, 0, 0, 0, 0, 0, 0, 0), *np, *diff(), *rsvd1, *net_jit(), *net_heath, *net_dly,
                                *net_ll, *fn())
                # print(s)
                # print(len(s))
                # print(struct.unpack('2B8B4B2B4B8B4B2B6B4B4B4B4B60B', s))
                sleep(5)
                udp_socket_client.sendto(s, send_address)

def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket_client.bind(('192.168.1.63', 16888))
    recv_ip = "192.168.1.63"
    recv_port = 16888
    send_ip = "192.168.1.249"
    send_port = 17000
    recv_address = (recv_ip, int(recv_port))
    send_address = (send_ip, int(send_port))
    socket_send_thread = threading.Thread(target=udp_socket_send_client,
            args=(udp_socket_client, send_address)
            )
    socket_recv_thread = threading.Thread(target=udp_socket_recv_client,
            args=(udp_socket_client, recv_address)
            )
    socket_recv_thread.start()
    socket_send_thread.start()
if __name__ == '__main__':
    main()
