import multiprocessing

from udp_message.GPS_signal import Gps_Signal
from udp_message.rcu_heartbeat import Heart_Beat
from udp_message.user_register import User_Register

'''
    author:haoyu Tang
    time:2019-2-27
    address:Chengdu
    email:treeytang@163.com
    theme: simulation
'''



if __name__ == "__main__":
    #心跳
    heartbeat = Heart_Beat()
    #用户注册
    user_register = User_Register()
    #用户GPS
    user_GPS = Gps_Signal()
    p1 = multiprocessing.Process(target = heartbeat.heartbeat)
    p2 = multiprocessing.Process(target = user_register.user_register)
    p3 = multiprocessing.Process(target = user_GPS.start)
    p1.start()
    p2.start()
    p3.start()
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
