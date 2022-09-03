import time
from telnetlib import Telnet


def connect_device(host, cmds=None):
    try:
        with Telnet(host, port=23, timeout=1) as tn:
            tn.read_until(b'Login:', timeout=1)
            tn.write(b'root' + b'\n')
            tn.read_until(b'Password:', timeout=1)
            tn.write(b'dyx000710' + b'\n')
            index, obj, output = tn.expect([b'>', b'#'], timeout=1)
            print(index, obj, output)
            # tn.read_until(b'#')
            for cmd in cmds:
                tn.write(cmd.encode() + b'\n')
                time.sleep(2)
                output = tn.read_very_eager().decode()
                print(output)
    except Exception as e:
        print('连接错误{}'.format(e))


if __name__ == '__main__':
    show_cmds = ['ll']
    connect_device("192.168.137.100", show_cmds)
