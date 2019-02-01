import socket
import threading
import os, signal
from time import sleep
import random


def comm(num):
    strs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%^&*/[]:.?"
    l = ''
    for i in range(num):
        l += str(random.choice(strs))
    return l


def call_ID():
    num = random.choice([7, 8])
    l = comm(num)
    return l


def tag():
    num = random.choice([3, 4])
    l = comm(num)
    return l


def via_by():
    num = random.choice([3, 4])
    l = comm(num)
    if l[0] == ';':
        l = l.replace(";", "A")
    if l[0] == ',':
        l = l.replace(",", "A")

    return l


def Qseq():
    return (random.randrange(30, 999))






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
    sleep(5)

    a = 1

    # for userid in range(3407873, 3439024):
    for userid in range(3407873, 3408572):
        print("信息发送第%d遍"%a)
        filename = open("userid.txt", "a")
        filename.write("%d***"%userid)
        filename.close()

        send_data = "R p:{}\r\n" \
                    "i:{}\r\n" \
                    "f:<p:{}>;g={}\r\n" \
                    "t:-\r\n" \
                    "Q:{} R\r\n" \
                    "v:r109.pdt.cn;b={}~\r\n" \
                    "m:<s:r109.pdt.cn;m=192.168.1.56:18820>\r\n" \
                    "H:70\r\n" \
                    "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
                    "c:a/m\r\n" \
                    "l:43\r\n" \
                    "\r\n" \
                    "<attachgroup><AG>1146886</AG></attachgroup>\r\n".format(userid, call_ID(), userid, tag(), Qseq(), via_by())
        a += 1
        # 退出程序
        if userid == 3408571:
            sleep(2048)
            print("线程号为：",os.getpid())
            udp_socket_client.close()
            print('退出成功')
            os.kill(os.getpid(), signal.SIGKILL)
        else:
            print("发送内容为：",send_data)
            udp_socket_client.sendto(send_data.encode('utf-8'), send_address)
        sleep(1)

def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_ip = "192.168.1.56"
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
