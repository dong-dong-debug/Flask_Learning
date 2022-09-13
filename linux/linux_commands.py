import paramiko
import time
import threading


class Python_Linux:
    def __init__(self):
        self.ip = "192.168.137.100"
        self.port = "22"
        self.user = "root"
        self.password = "dyx000710"

    # 建立连接
    def connect(self):
        try:
            # 创建SSHClient 实例对象
            self.ssh = paramiko.SSHClient()
            # 调用方法，表示没有存储远程机器的公钥，允许访问
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接远程机器，地址，端口，用户名密码
            self.ssh.connect(self.ip, self.port, self.user, self.password, timeout=10)
        except Exception as e:
            print("连接错误{}".format(e))

    # 关闭连接
    def close(self):
        self.ssh.close()

    # 上传文件
    def upload_file(self, local_file, remoute_file):
        self.connect()
        try:
            sftp = self.ssh.open_sftp()
            # 从本地上次文件到linux
            sftp.put(local_file, remoute_file)
        except Exception as e:
            print("连接错误{}".format(e))
        finally:
            sftp.close()
            self.close()

    # 下载文件
    def download_file(self, local_file, remoute_file):
        self.connect()
        try:
            sftp = self.ssh.open_sftp()
            # 从本地上次文件到linux
            sftp.get(local_file, remoute_file)
        except Exception as e:
            print("连接错误{}".format(e))
        finally:
            sftp.close()
            self.close()

    # 解压文件
    def unzip_file(self):
        self.connect()
        with self.ssh.invoke_shell() as execute:
            execute.send("cp /home/zc/PPU/test.zip /home/zc/PPU/bak/" + "\n")
            time.sleep(2)
            execute.send("unzip /home/zc/PPU/bak/test.zip -d /home/zc/PPU/bak/" + "\n")
            time.sleep(2)
        self.close()

    # 修改文件
    def update_file(self):
        self.connect()
        with self.ssh.invoke_shell() as execute:
            execute.send('sed -i "s/NO/YES/g" /home/zc/PPU/bak/PPU_config.txt\n')
            time.sleep(2)
            execute.send('sed -i "s/2/100/g" /home/zc/PPU/bak/PPU_config.txt\n')
            time.sleep(2)
        self.close()

    # 监控进程
    def process_find(self):
        self.connect()
        with self.ssh.invoke_shell() as execute:
            execute.send("top" + "\n")
            # execute.send("top | grep xxx" + "\n")
            # execute.send("kill -9 pid" + "\n")
            time.sleep(3)
            resp = execute.recv(65535)
            print(resp.decode())

        t1 = threading.Timer(3, self.process_find)  # 每1秒钟启动一次run函数.不是下面的t启动的
        t1.start()
        # 关闭连接
        self.close()


if __name__ == '__main__':
    Python_Linux().unzip_file()
    Python_Linux().update_file()
