import socket
import threading
import os, signal
from time import sleep

import random


def northern():
    north = str(random.choice(range(10,100)))+str(random.choice(range(10,60)))+'.'+str(random.choice(range(100,1000)))
    print("北纬：",north)
    return north

def easts():
    east = str(random.choice(range(100, 181))) + str(random.choice(range(10, 60)))+"."+str(random.choice(range(100, 1000)))
    print("东经：", east)
    return east

def altitude():
    #高度
    h = random.choice(range(1,1000))
    return h





def udp_socket_recv_client(udp_socket_client, recv_address):
    udp_socket_client.bind(recv_address)
    while True:

        try:
            recv_data, recv_addr = udp_socket_client.recvfrom(1024)
            print('收到來自<%s>的信息'% recv_addr[0],
                    recv_data.decode('utf-8') + '\n' + '<<', end='')
        except Exception as e:
            print(e)






def udp_socket_send_client(udp_socket_client, send_address):
    print('连接成功,开始发送信息了:)')
    a = 1
    for userid in range(40020200,40020329):
        send_data = "GPGLL,{},{},N,{},E,A,{},,101118.517,<5%,-55,I,15,,1146886,,,r106.pdt.cn,106,,,,,22785,,".format(userid, northern(), easts(), altitude())
        a = 0
        for i in send_data:
            a = a ^ (ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas="$"+send_data+"*"+checksum+" "

        print("发送内容为：",send_datas)

        a += 1
        # 退出程序
        if userid == 40020400:

            print("线程号为：",os.getpid())
            sleep(2048)
            udp_socket_client.close()
            print('退出成功')
            os.kill(os.getpid(), signal.SIGKILL)
            os.kill(os.getpid(), signal.SIGKILL)
        else:
            udp_socket_client.sendto(send_datas.encode('utf-8'), send_address)
        sleep(1)


def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_ip = "192.168.1.56"
    recv_port = 16888
    send_ip = "192.168.1.249"
    send_port = 6004
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