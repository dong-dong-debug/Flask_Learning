# 导入os模块
import os


# 创建一个txt文件
def text_create(name, msg):
    # 自动获取桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop/")
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)


for i in range(10):
    text_create('my_txt' + str(i+1), 'hello world')
