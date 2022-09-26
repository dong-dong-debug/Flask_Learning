from flask import Blueprint, request, render_template, flash, redirect, url_for
from common.decorators import login_required
from linux.linux_commands import Python_Linux
import os

index = Blueprint("index", __name__)


# 文件上传解压移动修改
# @login_required
# @index.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'GET':
#         return render_template('index.html')
#     else:
#         file = request.files['zipfile']
#         destpath = request.form.get("destpath")
#         file_name = file.filename
#         print("获取上传文件的名称为:", file_name)
#         local_file = os.path.abspath(__file__) + '../../../static/upload/' + file_name
#         # remoute_file = "/home/zc/PPU/" + file_name
#         remoute_file = destpath + file_name
#         print(remoute_file)
#         file.save(local_file)  # 保存文件
#         Python_Linux().upload_file(local_file, remoute_file)
#         Python_Linux().unzip_file()
#         Python_Linux().update_file()
#         flash("上传成功")
#         return redirect(url_for("index.upload_file"))


@index.route('/', methods=['GET', 'POST'])
@login_required
def idx():
    if request.method == 'GET':
        return render_template('index.html')


# 文件上传解到指定目录
@index.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['zipfile']
        destpath = request.form.get("destpath")
        file_name = file.filename
        print("获取上传文件的名称为:", file_name)
        local_file = os.path.abspath(__file__) + '../../../static/upload/' + file_name
        # remoute_file = "/home/zc/PPU/" + file_name
        remoute_file = destpath + file_name
        print(remoute_file)
        file.save(local_file)  # 保存文件
        Python_Linux().upload_file(local_file, remoute_file)
        flash("上传成功")
        return redirect(url_for("index.upload_file"))


# 监控进程
# @index.route('/findprocess', methods=['GET', 'POST'])
# def find_process():
#     plinux = Python_Linux()
#     result = plinux.process_find_python()
#     print(result)
#     if result[0].__contains__('grep'):
#         print("程序未启动")
#         plinux.open_python_process()
#         print("程序已启动")
#         return 'TestProcess is restarted'
#     else:
#         print("程序已启动")
#         return 'TestProcess is running'

# 监控进程
# @login_required
# @index.route('/findprocess', methods=['GET', 'POST'])
# def find_process():
#     if request.method == 'GET':
#         return render_template("findprocess-jinjia2.html")
#     else:
#         plinux = Python_Linux()
#         status, times = plinux.process_find_python_status()
#         if status == 0:
#             flash("进程未开启")
#         elif status == 1:
#             flash(f"进程正在运行,进程已经持续：{times[1]}")
#         else:
#             flash(f"进程已经重启,进程已经持续：{times[1]}")
#         return redirect(url_for("index.find_process"))


# 监控进程
@index.route('/findprocess', methods=['GET', 'POST'])
@login_required
def find_process():
    if request.method == 'GET':
        return render_template("findprocess.html")
    else:
        plinux = Python_Linux()
        status, times = plinux.process_find_python_status()
        status = str(status)
        if times != 0:
            times = str(times[1].strip())
        dict = {"status": status, "times": times}
        return dict


# 话单搬运
# @login_required
# @index.route('/billcarry', methods=['GET', 'POST'])
# def bill_carry():
#     if request.method == "GET":
#         return render_template('billcarry-jinjia2.html')
#     else:
#         source = request.form.get("source")
#         dest = request.form.get("dest")
#         print(source)
#         print(dest)
#         plinux = Python_Linux()
#         result = plinux.find_file_nummber(source)
#         print(result)
#         if int(result) < 10:
#             flash("文件数量正常")
#             return render_template('billcarry-jinjia2.html')
#         else:
#             plinux.form_source_to_dest(source, dest)
#             flash("文件数量超标,已经移动到指定位置")
#             return render_template('billcarry-jinjia2.html')

# 话单搬运
@login_required
@index.route('/billcarry', methods=['GET', 'POST'])
def bill_carry():
    if request.method == "GET":
        return render_template('billcarry.html')
    else:
        source = request.form.get("source")
        dest = request.form.get("dest")
        print(source)
        print(dest)
        plinux = Python_Linux()
        result = plinux.find_file_nummber(source)
        # print(result)
        if int(result) < 10:
            status = "normal"
            num = result.strip()
            print(num)
            dict = {"status": status, "num": num}
            return dict
        else:
            plinux.form_source_to_dest(source, dest)
            status = "un-normal"
            num = result
            dict = {"status": status, "num:": num}
            return dict
