import multiprocessing

from rcu_heartbeat import Heart_Beat
from user_register import User_Register
from GPS_signal import GPS_Signal

'''
    author:haoyu Tang
    time:2019-2-27
    address:Chengdu
    email:treeytang@163.com
    theme: simulation
'''



if __name__ == "__main__":
    print('start')

    #用户注册
    calling_party = 4882434
    callend_party = 4882439
    recv_ip = "192.168.1.56"
    rcu = "r108.pdt.cn"
    lai = '108'
    user_register = User_Register(recv_ip, rcu, calling_party, callend_party)
    #用户GPS
    user_GPS = GPS_Signal(calling_party, callend_party, recv_ip, rcu, lai)
    # 心跳
    heartbeat = Heart_Beat(recv_ip, lai)
    p1 = multiprocessing.Process(target = heartbeat.heartbeat)
    p2 = multiprocessing.Process(target = user_register.user_register)
    p3 = multiprocessing.Process(target = user_GPS.start)
    p1.start()
    p2.start()
    p3.start()
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
