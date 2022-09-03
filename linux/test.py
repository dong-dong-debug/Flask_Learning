import os
import paramiko

ip = "192.168.137.100"
port = "22"
user = "root"
password = "dyx000710"
# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()
# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接远程机器，地址，端口，用户名密码
ssh.connect(ip, port, user, password, timeout=10)

oldpath = os.path.abspath(__file__) + '../../../static/upload/test.zip'
newpath = r'/home/zc/PPU/test.zip'

sftp = ssh.open_sftp()
# 从本地上次文件到linux
sftp.put(oldpath, newpath)

# 关闭连接
ssh.close()
