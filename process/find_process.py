import os
import threading
import psutil


def process_find():
    # 查看当前进程pid
    pid = os.getpid()
    print(pid)
    # 获取进程信息
    pro = psutil.Process(pid)
    print(pro.name())
    # 进程路径
    print(pro.exe())
    t1 = threading.Timer(1, process_find)  # 每1秒钟启动一次run函数.不是下面的t启动的
    t1.start()


if __name__ == '__main__':
    t = threading.Timer(1, process_find)  # 1秒，target换成了function
    t.start()
