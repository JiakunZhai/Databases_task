import pymysql


class WORKER:

    def __init__(self, workerid, workername) -> None:
        self.workerid = workerid
        self.workername = workername

    # 连接数据库
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='12345678', port=3306, db='restaurantproject')

    # 增加操作
    def insert_worker(self):
        try:
            db = WORKER.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO WorkerInfo (workername) VALUES ('" + \
                self.workername + "');"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据插入成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 删除操作
    def delete_worker(self):
        try:
            db = WORKER.connect_db()
            cursor = db.cursor()

            sql = "DELETE FROM WorkerInfo WHERE workerid=" + \
                str(self.workerid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据删除成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 查找操作
    def select_worker(self):
        try:
            db = WORKER.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM WorkerInfo WHERE workerid=" + \
                str(self.workerid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                for row in results:
                    print("员工编号:", row[0])
                    print("员工姓名:", row[1])
            else:
                print("未找到记录")

        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 修改操作
    def update_worker(self):
        try:
            db = WORKER.connect_db()
            cursor = db.cursor()

            sql = "UPDATE WorkerInfo SET workername='" + \
                self.workername + "' WHERE workerid=" + str(self.workerid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()
