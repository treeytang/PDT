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

def udp_socket_send_client(udp_socket_client, send_address):

    pass

def main():
    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_ip = "192.168.1.56"
    recv_port = 18820
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
