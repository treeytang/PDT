import socket
import threading
import os, signal
from time import sleep
import random


def udp_socket_recv_client(udp_socket_client, recv_address):
    udp_socket_client.bind(recv_address)
    while True:
        try:
            recv_data, recv_addr = udp_socket_client.recvfrom(1024)
            print('收到來自<%s>的信息'% recv_addr[0],
                    recv_data.decode('utf-8') + '\n' + '<<', end='')
        except Exception as e:
            print(e)


def register_num():
    pass



def udp_socket_send_client(udp_socket_client, send_address):
    print('连接成功,可以发送信息了:)')
    a = 1
    while True:
        print("信息发送第%d遍"%a)
        send_data = '''            
R p:4889443
i:Is-m19d
f:<p:4889443>;g=sCMl
t:-
Q:542 R
v:r105.pdt.cn;b=h_P
m:<s:r105.pdt.cn;m=192.168.1.213:18820>
H:70
ua:46 ACTEC-PDT-RCU-1.5.0.0
c:a/m
l:43

<attachgroup><AG>9961476</AG></attachgroup>
            '''
        sleep(2)
        a +=1

        # 退出程序
        if send_data == 'QUIT':
            udp_socket_client.close()
            print('退出成功')
            os.kill(os.getpid(), signal.SIGKILL)
        else:
            udp_socket_client.sendto(send_data.encode('utf-8'), send_address)

def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_ip = "0.0.0.0"
    recv_port = 18820
    send_ip = "192.168.1.249"
    send_port = 5060
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
