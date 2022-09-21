from linux.linux_commands import Python_Linux
import threading

# plinux = Python_Linux()
# result = plinux.process_find_python()
# print(result)
# if result[0].__contains__('grep'):
#     print("程序未启动")
#     plinux.open_python_process()
#     print("程序已启动")
# else:
#     print("程序已启动")
#     res = result[0].split()
#     port = res[1]
#     plinux.kill_python_process(port)
#     print("程序已结束")

plinux = Python_Linux()
# result = plinux.find_process_livetime(6674)
# print(result[1])
# print(type(result[1]))

# thread1 = threading.Timer(5, plinux.process_find_python_status)
# thread1.start()
# print(thread1)

# a = "10:26"
# b = a.split(':')[0]
# print(int(b)<1)

# plinux.process_find_python_status()

# result = plinux.find_file_nummber("/home/zc/PPU/bak")
# print(result[0])

# result = plinux.find_filename("/home/zc/PPU/test")
# print(len(result))

result = plinux.form_source_to_dest("/home/zc/PPU/test", "/home/zc/PPU/testcopy")
print(result)
