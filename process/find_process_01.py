from linux.linux_commands import Python_Linux

plinux = Python_Linux()
result = plinux.process_find_python()
print(result)
if result[0].__contains__('grep'):
    print("程序未启动")
    plinux.open_python_process()
    print("程序已启动")
else:
    print("程序已启动")
    res = result[0].split()
    port = res[1]
    plinux.kill_python_process(port)
    print("程序已结束")
