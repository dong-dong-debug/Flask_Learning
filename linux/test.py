import threading
from linux_commands import Python_Linux
t = threading.Timer(3, Python_Linux().process_find)  # 1秒，target换成了function
t.start()
