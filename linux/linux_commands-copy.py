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

    # 监控python进程
    def process_find_python(self):
        self.connect()
        stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep TestProcess.py")
        result = stdout.readlines()
        self.close()
        return result

    # 启动python程序
    def open_python_process(self):
        self.connect()
        self.ssh.exec_command("python /home/zc/PPU/bak/TestProcess.py")
        self.close()

    # 杀死进程
    def kill_python_process(self, port):
        self.connect()
        with self.ssh.invoke_shell() as execute:
            execute.send(f"kill -9 {port}" + "\n")
            time.sleep(3)
        self.close()

    # 监控进程状态
    def process_find_python_status(self):
        # status 0:未启动  1：正在启动  2：已重启
        result = self.process_find_python()
        if result[0].__contains__('grep'):
            print("程序未启动")
            status = 0
            times = 0
        else:
            port = result[0].split()[1]  # 获取端口号码
            times = self.find_process_livetime(port)
            print(f"进程已经持续{times[1]}")
            data = times[1].split(':')
            if len(data) < 3:
                status = 1
                islive = int(data[0]) < 1
                if islive:
                    status = 2
        return status, times

    # 查看进程存活时间
    def find_process_livetime(self, port):
        self.connect()
        stdin, stdout, stderr = self.ssh.exec_command(f"ps -p {port} -o etime")
        result = stdout.readlines()
        self.close()
        return result

    # 查询文件夹文件个数
    def find_file_nummber(self, filepath):
        self.connect()
        stdin, stdout, stderr = self.ssh.exec_command(f'ls {filepath} -l |grep "^-"|wc -l')
        result = stdout.readlines()
        self.close()
        return result[0]

    # 移动文件到指定位置
    def form_source_to_dest_2(self, sourcepath, destpath):
        result = self.find_filename(sourcepath)
        print(result[2].strip())
        print(len(result))
        print(result)
        self.connect()
        for i in range(len(result)):
            sourcefile = sourcepath + "/" + result[i].strip()
            print(sourcefile)
            destfile = destpath + "/" + result[i].strip()
            print(destfile)
            command = "mv " + sourcefile + " " + destfile
            print(command)
            self.ssh.exec_command(command)
        self.close()
        return result

    # 查看指定文件夹下所有文件名称
    def find_filename(self, filepath):
        self.connect()
        stdin, stdout, stderr = self.ssh.exec_command(f"ls {filepath}")
        result = stdout.readlines()
        self.close()
        return result

    # 移动文件到指定位置 方法二
    def form_source_to_dest(self, sourcepath, destpath):
        self.connect()
        command = "mv " + sourcepath + "/* " + destpath + "/"
        print(command)
        self.ssh.exec_command(command)
        self.close()


if __name__ == '__main__':
    Python_Linux().unzip_file()
    Python_Linux().update_file()
