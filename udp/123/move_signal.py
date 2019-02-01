import  random
from time import sleep
import socket
import datetime


class GPS():
    def __init__(self,udp_socket_client,send_address):
        self.udp_socket_client = udp_socket_client
        self.send_address = send_address


    #北纬
    def northern(self):
        north = str(random.choice(range(30, 32))) + str(random.choice(range(50, 55))) + '.' + str(random.choice(range(100, 1000)))
        return north

    #东经
    def easts(self):
        east = str(random.choice(range(103, 105))) + str(random.choice(range(50, 55)))+"."+str(random.choice(range(100, 1000)))
        return east

    #高度
    def altitude(self):
        h = random.choice(range(1,1000))
        return h

    #对移动用户的经纬度进行标记
    def move_user_dic(self, lst):
        dic = {}
        for user in lst:
            north = self.northern()
            east = self.easts()
            dic[user] = "{},{}".format(north, east)
        return dic


    #位置固定不变的用户发送GPS
    def fixedly_user_dic(self, user, east_north):
        EN = east_north.split(",")
        north = EN[0]
        east = EN[1]
        send_data = "GPGLL,{},{},N,{},E,A,500,,101118.517,<5%,-55,I,15,,62224901,,,r106.pdt.cn,106,,,,,22785,,".format(user, north, east)
        a = 0
        for i in send_data:
            a = a ^ (ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas = "$" + send_data + "*" + checksum + " "
        print(send_datas)
        self.udp_socket_client.sendto(send_datas.encode('utf-8'), send_address)


    #先发送GPS信号，然后使北纬变化，东经保持不变，变化纬度每次增加0.01
    def change_northern(self,user, east_north,dic):
        # print(dic[user])
        EN = east_north.split(",")
        north = EN[0]
        east = EN[1]
        send_count = 0

        # selected_partern = random.choice(pattern_list)
        # north = north - selected_partern[send_count % 40][0]
        # send_count += 1
        # if (send_count >= len(selected_partern)):
        #     print("rechoice new pattern")
        #     selected_partern = random.choice(pattern_list)
        #     send_count = 0
        #
        # # print()
        send_data = "GPGLL,{},{},N,{},E,A,500,,101118.517,<5%,-55,I,15,,62224901,,,r106.pdt.cn,106,,,,,22785,,".format(user, north, east)
        a = 0
        for i in send_data:
            a = a^(ord(i))
        checksum = (((hex(a)).upper())[2:4])
        send_datas = "$" + send_data + "*" + checksum + " "
        print(send_datas)
        self.udp_socket_client.sendto(send_datas.encode('utf-8'), send_address)


        north = ("%.3f"%(float(north)+0.01))
        dic[user] = "{},{}".format(north, EN[1])










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
        lst = []
        #筛选出需要变动的用户，并加入到列表中
        for i in range(5):
            element = random.choice(l)
            lst.append(element)
            l.remove(element)

        dic = GPS.move_user_dic(lst)
        dic_1 = GPS.move_user_dic(l)


        # for user in lst:
        #     north = GPS.northern()
        #     east = GPS.easts()
        #     dic[user] = "{},{}".format(north, east)
            # send_data = "GPGLL,{},{},N,{},E,A,{},,101118.517,<5%,-55,I,15,,1146886,,,r106.pdt.cn,106,,,,,22785,,".format(user, northern(), easts(), altitude())
            # a = 0
            # for i in send_data:
            #     a = a^(ord(i))
            #     checksum = (((hex(a)).upper())[2:4])
            #     send_datas = "$" + send_data + "*" + checksum + " "
        print(dic)
        print(dic_1)

        count = 1
        while count:
            for user in dic:
                # print(dic[user])
                GPS.change_northern(user,dic[user], dic)
            for user in dic_1:
                GPS.fixedly_user_dic(user,dic_1[user])

            if count==10:
                break
            print("循环发送消息变幻的纬度字典：",dic)
            print("位置固定的用户字典", dic_1)
            sleep(1.5)




        #循环条件控制，当循环完第10次，跳出循环，结束程序
        # if initialize==10:
        #     break
        # initialize += 1
        # sleep(5)
