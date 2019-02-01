import socket
import threading
import os, signal
from time import sleep


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
    print('连接成功,可以发送信息了:)')
    a = 1
    while True:
        print("信息发送第%d遍"%a)
        # send_data ="R s:sxu.pdt.cn\r\n" \
        #            "i:T?DZyNk\r\n" \
        #            "f:<s:r108.pdt.cn>;g=C3%e\r\n" \
        #            "t:+\r\n" \
        #            "Q:83 R\r\n" \
        #            "v:r108.pdt.cn;b=axLk\r\n" \
        #            "m:<s:r108.pdt.cn;m=192.168.1.55:15062>\r\n" \
        #            "H:70\r\n" \
        #            "Z:application/config+xml\r\n" \
        #            "N:pdt b=69;c=f2.1-1+0;s=43000\r\n" \
        #            "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
        #            "l:0\r\n"

        userid= 1048577
        send_data = "R p:%d\r\n" \
                    "i:~Py!UK/\r\n" \
                    "f:<p:%d>;g=a+o\r\n" \
                    "t:-\r\n" \
                    "Q:257 R\r\n" \
                    "v:r108.pdt.cn;b=AIq~\r\n" \
                    "m:<s:r108.pdt.cn;m=192.168.1.55:15062>\r\n" \
                    "H:70\r\n" \
                    "ua:46 ACTEC-PDT-RCU-1.5.0.0\r\n" \
                    "c:a/m\r\n" \
                    "l:43\r\n" \
                    "\r\n" \
                    "<attachgroup><AG>1146886</AG></attachgroup>\r\n"%(userid,userid)
        userid+=1
        a += 1
        # 退出程序
        if send_data == 'QUIT':
            udp_socket_client.close()
            print('退出成功')
            os.kill(os.getpid(), signal.SIGKILL)
        else:
            udp_socket_client.sendto(send_data.encode('utf-8'), send_address)
        sleep(3)

def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_ip = "0.0.0.0"
    recv_port = 15062
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
