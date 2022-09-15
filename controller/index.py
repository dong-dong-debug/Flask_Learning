from flask import Blueprint, request, render_template
from common.decorators import login_required
from linux.linux_commands import Python_Linux
import os

index = Blueprint("index", __name__)


@index.route('/', methods=['GET', 'POST'])
@login_required
def idx():
    return render_template('index.html')


@index.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['zipfile']
    file_name = file.filename
    print("获取上传文件的名称为:", file_name)
    local_file = os.path.abspath(__file__) + '../../../static/upload/' + file_name
    remoute_file = "/home/zc/PPU/" + file_name
    file.save(local_file)  # 保存文件
    Python_Linux().upload_file(local_file, remoute_file)
    Python_Linux().unzip_file()
    Python_Linux().update_file()
    return '上传成功'


# 监控进程
@index.route('/findprocess', methods=['GET', 'POST'])
def find_process():
    plinux = Python_Linux()
    result = plinux.process_find_python()
    print(result)
    if result[0].__contains__('grep'):
        print("程序未启动")
        plinux.open_python_process()
        print("程序已启动")
        return 'TestProcess is restarted'
    else:
        print("程序已启动")
        return 'TestProcess is running'
