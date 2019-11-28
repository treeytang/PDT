from time import sleep
import random
import datetime
import socket
import sys


class GPS_Signal():

    def __init__(self, calling_party, callend_party, recv_ip, rcu, lai):
        self.udp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        recv_ip = recv_ip
        recv_port = 16889
        send_ip = "192.168.1.249"
        send_port = 6004#8006#
        self.Bs_dn = rcu
        self.lai = lai
        self.udp_socket_client.bind((recv_ip, recv_port))
        self.recv_address = (recv_ip, int(recv_port))
        self.send_address = (send_ip, int(send_port))
        self.rcu_north = 30.62097
        self.rcu_east = 104.07126
        self.calling_party = calling_party
        self.callend_party = callend_party


    def utc_time(self):
        t = ("%.3f" % float(datetime.datetime.now().strftime("%H%M%S.%f")))
        return t

    def floatrange(self, start, stop, steps):
        return [start+float(i)*(stop-start)/(float(steps)-1) for i in range(steps)]


    def north(self):
        start = self.rcu_north - 0.1
        stop = self.rcu_north + 0.1
        step = 20000
        north_list = self.floatrange(start, stop, step)
        return north_list

    def east(self):
        start = self.rcu_east - 0.1
        stop = self.rcu_east + 0.1
        step = 20000

        east_list = self.floatrange(start, stop, step)
        return east_list

    def coordinate(self, north_list, east_list):
        north = float(random.choice(north_list))
        east = float(random.choice(east_list))
        a = self.rcu_north-north
        b = self.rcu_east-east
        r = 0.1
        if a**2+b**2>r**2:
            return self.coordinate(north_list, east_list)
        else:
            return [north, east]

    def transition(self,paramters):
        paramter = str(paramters).split('.')
        degree = paramter[0]
        minutes_second = (str(float("0."+paramter[1])*60)).split('.')
        minutes = minutes_second[0]
        if len(minutes)==1:
            minutes = "0"+minutes
        second = str(round((float('0.'+minutes_second[1])*60), 2)).split('.')
        a = 0
        for i in second:
            if len(i)==1:
                second[a]='0'+(i)
            a+=1
        seconds = second[0]+second[1]
        return degree+minutes+'.'+seconds

    #场强
    def upstream_field_strength(self, north, east):
        maximum = max(abs(self.rcu_north - float(north)), abs(self.rcu_east - float(east)))
        if maximum < 0.02:
            return str(random.choice(range(-60, -50)))
        elif 0.02 <= maximum < 0.04:
            return str(random.choice(range(-70, -60)))
        elif 0.04 <= maximum < 0.06:
            return str(random.choice(range(-80, -70)))
        elif 0.06 <= maximum < 0.08:
            return str(random.choice(range(-90, -80)))
        elif 0.08 <= maximum < 0.1:
            return str(random.choice(range(-100, -90)))

    def down_field_strength(self, north, east):
        maximum = max(abs(self.rcu_north-float(north)), abs(self.rcu_east-float(east)))
        if maximum<0.02:
            return '-60~-70'
        elif 0.02<=maximum<0.04:
            return '-70~-80'
        elif 0.04<=maximum<0.06:
            return '-80~-90'
        elif 0.06<=maximum<0.08:
            return '-90~-100'
        elif 0.08<=maximum<0.1:
            return '-100~-110'


    def send_signal(self, user, dic):
        value = dic[user].split(',')
        flag = value[0]
        north = value[1]
        east = value[2]
        count = value[3]
        down_fs = self.down_field_strength(north, east)
        upstream_fs = self.upstream_field_strength(north, east)
        norths = self.transition(north)
        easts = self.transition(east)
        group = "57797321"
        # if str(user) == '44530205':
        #     group = '32820947'
        # if str(user) == '60020201':
        #     group = "60020901"
        # if str(user) == '44530202':
        #     group = '60020909'
        # if str(user) == '44530203':
        #     group = '60020900'
        # if str(user) == '44530204':
        #     group = "60020910"

        send_data = "GPGLL,{},{},N,{},E,A,500,,{},<5%,{},I,15,,{},,,{},{},,,,,,,".format(user,norths,easts,
                                                                                               self.utc_time(),
                                                                                               upstream_fs,
                                                                                               group,
                                                                                               self.Bs_dn,
                                                                                               self.lai)
        if int(count)%2==0:
            send_data = "GPGLL,{},{},N,{},E,A,500,,{},{},{},I,15,,{},,,{},{},,,,,,,".format(user,norths,easts,
                                                                                                  self.utc_time(),
                                                                                                  down_fs, upstream_fs,
                                                                                                  group,
                                                                                                  self.Bs_dn, self.lai)
        a = 0
        for i in send_data:
            a = a ^ (ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas = "$" + send_data + "*" + checksum + " "
        print(send_datas)
        self.udp_socket_client.sendto(send_datas.encode('utf-8'), self.send_address)
        if int(flag) == 1:
            north = (float(north) - float(0.00008))
            # north = (float(north) - float(0.005))
            # east = (float(east) - float(0.))
        counts = int(count) + 1
        dic[user] = "{},{},{},{}".format(flag, north, east, counts)


    def start(self):
        # sleep(500)
        initialize = 1
        # filename = open('./userid.txt', 'r')
        # l = (filename.read()).split('***')
        # filename.close()
        # l.pop()

        #将已经注册了的用户的空口好转换为用户号
        l = [str(((int(x) - 1048577) // 32768 + 328)) + str(((int(x) - 1048577) % 32768) // 700 + 20) + str(
            ((int(x) - 1048577) % 32768) % 700 + 200) for x in range(self.calling_party, self.callend_party)]

        # 获取所有的经纬度可用列表点位
        north_list = self.north()
        east_list = self.east()
        while True:
            print("循环进入第%d次" % initialize)
            dic = {}
            counts = 0
            # 筛选出需要变动的用户
            for user in l:
                # 标记需要变动的用户
                flag = random.choice(range(0, 2))
                # flag = 1
                if flag == 1:
                    counts += 1
                if counts > (len(l) // 4):
                    flag = 0
                n_e = self.coordinate(north_list, east_list)
                north = n_e[0]
                east = n_e[1]
                count = 1
                dic[user] = "{},{},{},{}".format(flag, north, east, count)
            for i in range(10):
                for user in dic:
                    self.send_signal(user, dic)

                sleep(3)
            sleep(2)
            initialize += 1


def main():
    calling_party = 1048777
    callend_party = 1048978
    recv_ip = "192.168.1.45"
    rcu = "r105.pdt.cn"
    lai = '105'
    GPS_Signal(calling_party, callend_party, recv_ip, rcu, lai).start()


if __name__ == "__main__":
    main()
