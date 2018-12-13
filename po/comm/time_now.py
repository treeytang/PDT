import time

def time_now():
    now_time = time.strftime("%Y-%m-%d/%H_%M_%S")
    print(now_time)
    return now_time
