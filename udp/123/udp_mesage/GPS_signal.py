from time import sleep
import random
import datetime
import socket




pattern_list = [
    [
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],
        [0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0],[0.02,0]
    ],
    [
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
        [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
    ]
]


class Gps_Signal():
    def __init__(self):
        self.udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        recv_ip = "192.168.1.67"
        recv_port = 16888
        send_ip = "192.168.1.249"
        send_port = 6004
        self.udp_socket_client.bind((recv_ip, recv_port))
        self.recv_address = (recv_ip, int(recv_port))
        self.send_address = (send_ip, int(send_port))
        # 北纬

    def northern(self):
        north = str(30) + str(random.choice(range(25, 55))) + '.' + str(
            random.choice(range(100, 999)))
        return north

        # 东经

    def easts(self):
        east = str(random.choice(range(10345, 10385))) + "." + str(
            random.choice(range(100, 999)))
        return east

        # 高度

    def altitude(self):
        h = random.choice(range(1, 1000))
        return h

        # 时间

    def utc_time(self):
        t = ("%.3f" % float(datetime.datetime.now().strftime("%H%M%S.%f")))
        return t

        # 对移动用户的经纬度进行标记

    def move_user_dic(self, lst):
        dic = {}
        for user in lst:
            north = self.northern()
            east = self.easts()
            dic[user] = "{},{}".format(north, east)
        return dic

    def change_northern_1(self, user, dic):
        value = dic[user].split(",")
        flag = value[0]
        north = value[1]
        east = value[2]
        count = value[3]
        print(flag, north, east, count)

        send_data = "GPGLL,{},{},N,{},E,A,500,,{},<5%,-55,I,15,,62224901,,,r124.pdt.cn,124,,,,,22785,,".format(user,north,east,self.utc_time())
        a = 0
        for i in send_data:
            a = a ^ (ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas = "$" + send_data + "*" + checksum + " "
        # print(send_datas)
        self.udp_socket_client.sendto(send_datas.encode('utf-8'), self.send_address)
        if int(flag) == 1:
            north = ("%.3f" % (float(north) - float(pattern_list[0][int(count)][0])))
            east = ("%.3f" % (float(east) - float(pattern_list[0][int(count)][1])))
            count = int(count) + 1
        dic[user] = "{},{},{},{}".format(flag, north, east, count)


    def start(self):
        # sleep(100)
        initialize = 1
        filename = open('./userid.txt', 'r')
        l = (filename.read()).split('***')

        filename.close()
        l.pop()
        l = [str(((int(x) - 1048577) // 32768 + 328)) + str(((int(x) - 1048577) % 32768) // 700 + 20) + str(((int(x) - 1048577) % 32768) % 700 + 200) for x in l]
        print(l)
        while True:
            print("循环进入第%d次" % initialize)
            # l = ['40020200', '40020201', '40020202', '40020203', '40020204', '40020205', '40020206', '40020207',
            #      '40020208', '40020209']
            # print(len(l))


            dic = {}
            counts = 0
            # 筛选出需要变动的用户
            for user in l:
                flag = random.choice(range(0, 2))
                if flag == 1:
                    counts += 1
                    # print(count)
                if counts > (len(l) // 4):
                    flag = 0
                    print(counts, flag)

                north = self.northern()
                east = self.easts()
                count = 0
                dic[user] = "{},{},{},{}".format(flag, north, east, count)
            # print(dic)

            for i in range(160):
                for user in dic:
                    self.change_northern_1(user, dic)
                sleep(1)
                print(dic)
            initialize += 1

#
# s = Gps_Signal()
# s.main()
