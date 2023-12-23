import pymysql

class FOODTABLE:
    def __init__(self, tableid, tablenumber, tablestate) -> None:
        self.tableid = tableid
        self.tablenumber = tablenumber
        self.tablestate = tablestate

    # 连接数据库
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='12345678', port=3306, db='restaurantproject')

    # 增加操作
    def insert_table(self):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO TableInfo (tablenumber, tablestate) VALUES (" + str(self.tablenumber) + ", '" + self.tablestate + "');"
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
    def delete_table(self):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "DELETE FROM TableInfo WHERE tablenumber=" + str(self.tablenumber) + ";"
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
    def select_table(tablenumber):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM TableInfo WHERE tablenumber=" + str(tablenumber) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                for row in results:
                    print("餐桌编号:", row[0])
                    print("座位数:", row[1])
                    print("使用状态:", row[2])
            else:
                print("未找到记录")

        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 修改操作
    def update_table(self):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "UPDATE TableInfo SET tablestate='" + self.tablestate + "' WHERE tablenumber=" + str(self.tablenumber) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()


