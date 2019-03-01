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
lai = (114,0)
#基站RCU的IP地址  4个字节大小
rcu_ip = (192, 168, 1, 52)
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
            print('收到來自<%s>的信息'% recv_addr[0],
                    recv_data + '\n' + '<<', end='')
        except Exception as e:
            print(e)


def udp_socket_send_client(udp_socket_client, send_address):
    print('连接成功,开始发送信息了:)')
    a = 0
    while True:
        # 0103 0100  ....A.Bh.|X.....  88 140
        #  消息类型
        # 0x0020:  0000 0000 0000 bc04 0000    6900      c0a8 01d5  ..........i.....
	    #            厂家识       序号       基站系统号   基站ip不变
        # 0x0030:  0000 0000 0000 0000     0100      0000    0000    0000  ................
                                         #组网类型          延迟时间
        # 0x0040:  0000 0000    0200 0000     fa22 4c00   3345 724a  ........."L.3ErJ
		# 		    rsvd1         抖动率                     网络丢包率
        # 0x0050:  7057 565a 0000 0000 0000 0000 0000 0000  pWVZ............
        #           健康指数
        # 0x0060:  0000 0000 0000 0000 0000 0000 0000 0000  ................
        # 0x0070:  0000 0000 0000 0000 0000 0000 0000 0000  ................
        # 0x0080:  0000 0000 0000 0000 0000 0000 0000 0000  ................
        # 该基站为109
        # send_datas = '01 03 01 00 00 00 00 00 00 00 f2 ea 00 00 6d 00 '\
        #              'c0 a8 01 38 00 00 00 00 00 00 00 00 01 00 00 00 '\
        #              '02 00 00 00 00 00 00 00 01 00 00 00 6e 19 59 00 '\
        #              '50 3a 73 3e 30 5b 44 5a 00 00 00 00 00 00 00 00 '\
        #              '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '\
        #              '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '\
        #              '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '\
        #              '00 00 00 00'
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
    udp_socket_client.bind(('192.168.1.52', 16888))
    recv_ip = "192.168.1.52"
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
