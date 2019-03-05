from time import sleep
import random
import datetime
import socket




pattern_list = [
    [
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],
        [0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0],[0.01,0]
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

    def floatrange(self, start, stop, steps):
        return [start+float(i)*(stop-start)/(float(steps)-1) for i in range(steps)]


    # 北纬
    def northern(self):
        #按照基站r108定位的纬度进行变化 30.62097 加减0.1度
        start = 30.62097-0.1
        stop = 30.62097+0.1
        step = 20000
        north_list = self.floatrange(start, stop, step)
        north = random.choice(north_list)
        return round(north,5)


    # 东经
    def easts(self):
        #按照基站r108定位的经度进行变化 104.07126 加减0.1度
        start = 104.07126 - 0.1
        stop = 104.07126 + 0.1
        step = 20000
        east_list = self.floatrange(start, stop, step)
        east = random.choice(east_list)
        return round(east, 5)

    def longitude_latitude(self):
        north = self.northern()
        east =  self.easts()
        a = (30.62097-north)
        b = (104.07126-east)
        r = 0.1

        if (a**2)+(b**2)>(r**2):
            return self.longitude_latitude()
        else:
            return [north, east]

    def north_transition(self, north):

        north = str(north).split('.')
        degree = north[0]
        ms = (str(float("0." + north[1]) * 60)).split('.')
        minutes = ms[0]
        if len(ms[0]) == 1:
            minutes = "0" + ms[0]
        second = str(round((float("0." + ms[1]) * 60), 2)).split('.')
        seconds = second[0] + second[1]
        if len(second[0]) == 1:
            seconds = "0" + second[0] + second[1]
        norths = degree + minutes + '.' + seconds
        return norths

    def east_transition(self, east):
        east = str(east).split('.')
        degree = east[0]
        ms = (str(float("0."+east[1])*60)).split('.')
        minutes = ms[0]
        if len(ms[0])==1:
            minutes = "0"+ms[0]
        second = str(round((float("0."+ms[1])*60), 2)).split('.')
        seconds = second[0] + second[1]
        if len(second[0])==1:
            seconds = "0"+second[0]+second[1]
        easts = degree+minutes+'.'+seconds
        return easts


    def transition(self):
        n_e = self.longitude_latitude()
        # print(type(n_e))
        north = n_e[0]
        east = n_e[1]
        east = self.east_transition(east)
        north = self.north_transition(north)
        return [north, east]




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

    def change_northern_1(self, user, dic, carousel):
        value = dic[user].split(",")
        flag = value[0]
        north = value[1]
        east = value[2]
        count = value[3]
        send_data = "GPGLL,{},{},N,{},E,A,500,,{},<5%,-55,I,15,,62224901,,,r108.pdt.cn,108,,,,,,,".format(user,north,east,self.utc_time())
        if (carousel+1)%2==0:
            send_data = "GPGLL,{},{},N,{},E,A,500,,{},-60~-70,-55,I,15,,62224901,,,r124.pdt.cn,124,,,,,,,".format(user,north,east,self.utc_time())
        a = 0
        for i in send_data:
            a = a ^ (ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas = "$" + send_data + "*" + checksum + " "
        print(send_datas)
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
        while True:
            print("循环进入第%d次" % initialize)


            dic = {}
            counts = 0
            radius = ''
            # 筛选出需要变动的用户
            for user in l:
                flag = random.choice(range(0, 2))
                if flag == 1:
                    counts += 1
                    # print(count)
                if counts > (len(l) // 4):
                    flag = 0

                n_e= self.transition()
                north = round(float(n_e[0]),3)
                east = round(float(n_e[1]), 3)
                print(north, east)
                count = 0
                dic[user] = "{},{},{},{}".format(flag, north, east, count)
                sleep(0.001)
            carousel = 0
            sleep(10)
            for i in range(160):
                for user in dic:
                    carousel+=1
                    self.change_northern_1(user, dic, carousel)
                sleep(1)
            initialize += 1


s = Gps_Signal()
s.start()
