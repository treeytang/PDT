#coding=utf-8
import psutil
import sys
import time
try:
#输入需要监测的进程PID
    PID = int(input('ProcessPID: '))
    text = open('D:\\CPUresult.txt', 'w')
    def get_cpu_info():
#将结果记录到本地文本
        i = 0
#博主新手靠这样来现实循环
        while i < 100000000000000:
            i = i + 1
#找出本机CPU的逻辑核个数
            cpucount = psutil.cpu_count(logical=True)


            info = psutil.virtual_memory()
#传入进程PID，实现监测功能
            process = psutil.Process(int(PID))
            cpupercent = process.cpu_percent(interval=2)
#得到进程CPU占用，同资源检测管理器的数据
            cpu = int(cpupercent / cpucount)
            if cpu <= 50:
                print('CPU使用率:%s%%' % cpu , '内存使用：',psutil.Process(PID).memory_info().rss , time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                # print(text, 'CPU使用率:%s%%' % cpu , '内存使用：',psutil.Process(PID).memory_info().rss , time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            else:
                print('CPU使用率:%s%%,占用率过高' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                # print(text, 'CPU使用率:%s%%,占用率过高' % cpu + '         ' + time.strftime('%Y-%m-%d %H:%M:%S',
                #                                                                        time.localtime()))
        text.close()
    print('进程%s的' % PID + 'cpu监控已经运行，结果将在D:\\result.txt生成')
    time.sleep(1)
    print("-------------------------------------------------")
    print(get_cpu_info())
finally:
    print('进程%s已经结束'%PID)
    text.close()