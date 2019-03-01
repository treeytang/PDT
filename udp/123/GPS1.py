import  random
from time import sleep
import socket
import datetime


max_patern_point_number = 40

pattern_list = [
    [
        [0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],
        [0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],
        [0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],
        [0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0],[0.05,0]
    ],
    [
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
    ]
]



class GPS():
    def __init__(self,udp_socket_client,send_address):
        self.udp_socket_client = udp_socket_client
        self.send_address = send_address

    #北纬
    def northern(self):
        north = str(random.choice(range(30, 32))) + str(random.choice(range(35, 40))) + '.' + str(random.choice(range(100, 1000)))
        return north

    #东经
    def easts(self):
        east = str(random.choice(range(103, 105))) + str(random.choice(range(40, 55)))+"."+str(random.choice(range(100, 1000)))
        return east

    #高度
    def altitude(self):
        h = random.choice(range(1,1000))
        return h

    #时间
    def utc_time(self):
        t = ("%.3f"%float(datetime.datetime.now().strftime("%H%M%S.%f")))
        return t

    #对移动用户的经纬度进行标记
    def move_user_dic(self, lst):
        dic = {}
        for user in lst:
            north = self.northern()
            east = self.easts()
            dic[user] = "{},{}".format(north, east)
        return dic



    def change_northern_1(self,user, dic):
        value = dic[user].split(",")
        flag = value[0]
        north = value[1]
        east = value[2]
        count = value[3]
        print(flag,north,east,count)

        send_data = "GPGLL,{},{},N,{},E,A,500,,{},<5%,-55,I,15,,62224901,,,r106.pdt.cn,106,,,,,22785,,".format(user, north, east, self.utc_time())
        a = 0
        for i in send_data:
            a = a ^ (ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas = "$" + send_data + "*" + checksum + " "
        # print(send_datas)
        self.udp_socket_client.sendto(send_datas.encode('utf-8'), send_address)
        if int(flag) == 1:
            north = ("%.3f"%(float(north)-float(pattern_list[0][int(count)][0])))
            east = ("%.3f"%(float(east)-float(pattern_list[0][int(count)][1])))
            count=int(count)+1
        dic[user] = "{},{},{},{}".format(flag, north, east, count)


if __name__=="__main__":

    udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_ip = "192.168.1.56"
    recv_port = 16888
    send_ip = "192.168.1.249"
    send_port = 6004
    recv_address = (recv_ip, int(recv_port))
    send_address = (send_ip, int(send_port))
    GPS = GPS(udp_socket_client,send_address)

    initialize = 1
    while True:
        print("循环进入第%d次" % initialize)
        l = ['40020200', '40020201', '40020202', '40020203', '40020204', '40020205', '40020206', '40020207', '40020208', '40020209']
        # print(len(l))
        dic = {}
        counts = 0
        #筛选出需要变动的用户
        for user in l:
            flag = random.choice(range(0,2))
            if flag == 1:
                counts+=1
                # print(count)
            if counts>(len(l)//4):
                flag = 0
                print(counts,flag)

            north = GPS.northern()
            east = GPS.easts()
            count = 0
            dic[user] = "{},{},{},{}".format(flag,north,east,count)

        print(dic)





        for i in range(40):
            for user in dic:
                GPS.change_northern_1(user,dic)

            sleep(1)
            print(dic)
        # sleep(1)

        initialize+=1
