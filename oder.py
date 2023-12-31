import pymysql


class ODER:

    def __init__(self, oderid, tableid, userid, odertime, oderprice, workerid):
        self.oderid = oderid
        self.tableid = tableid
        self.workerid = workerid
        self.userid = userid
        self.odertime = odertime
        self.oderprice = oderprice

    # 连接数据库
    @staticmethod
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='200525', port=3306, db='restaurantproject')

    # 增加操作
    def insert_order(self):
        try:
            db = ODER.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO oder (tableid, userid, workerid, odertime, oderprice) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, %s)"
            values = (str(self.tableid), str(self.userid),
                      str(self.workerid), str(self.oderprice))
            print('sql:', sql)

            cursor.execute(sql, values)
            db.commit()
            oderid = cursor.lastrowid
            print('数据插入成功!')
            return oderid
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 查找操作
    def select_order(self):
        try:
            db = ODER.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM OrderInfo WHERE oderid=" + \
                str(self.oderid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                for row in results:
                    print("订单编号:", row[0])
                    print("餐桌编号:", row[1])
                    print("用户编号:", row[2])
                    print("员工编号:", row[3])
                    print("订单时间:", row[4])
                    print("订单金额:", row[5])
            else:
                print("未找到记录")

        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 修改操作
    def update_order(self):
        try:
            db = ODER.connect_db()
            cursor = db.cursor()

            sql = "UPDATE oder SET tableid=" + str(self.tableid) + ", userid=" + str(self.userid) + ", workerid=" + str(
                self.workerid) + ", odertime='" + "now()" + "', oderprice=" + str(self.oderprice) + " WHERE oderid=" + str(self.oderid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()
