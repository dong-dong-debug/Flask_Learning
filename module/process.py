from sqlalchemy import Table
from common.database import dbconnect

dbsession, md, Dbase = dbconnect()


class Process(Dbase):
    __table__ = Table('process', md, autoload=True)

    # 插入一条进程任务状态
    def insert_process(self, status, time):
        process = Process(status=status, time=time)
        dbsession.add(process)
        dbsession.commit()

    # 查询最新一条任务状态
    def find_last_status(self):
        result = dbsession.query(Process.status, Process.time).order_by(Process.id.desc()).limit(1).first()
        return result

