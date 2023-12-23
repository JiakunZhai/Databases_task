import pymysql
from prettytable import PrettyTable


class FOODTABLE:
    def __init__(self, tableid, tablenumber, tablestate) -> None:
        self.tableid = tableid
        self.tablenumber = tablenumber
        self.tablestate = tablestate

    # 连接数据库
    @staticmethod
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='200525', port=3306, db='restaurantproject')

    # 增加操作
    def insert_table(self):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO foodtable (tablenumber, tablestate) VALUES (" + str(
                self.tablenumber) + ", '" + self.tablestate + "');"
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

            sql = "DELETE FROM foodtable WHERE tablenumber=" + \
                str(self.tablenumber) + ";"
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
    def select_table(self):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM foodtable WHERE tablenumber = " + \
                str(self.tablenumber) + " AND tablestate = \'N\' " + ";"
            print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                table = PrettyTable()
                table.field_names = ["餐桌编号", "座位数", "使用状态"]

                for row in results:
                    table.add_row(row)

                print(table)
                res = 1
            else:
                print("暂时没有符合您要求的餐桌，请稍等")
                res = 0

        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()
            return res

    # 修改操作

    def update_table(self):
        try:
            db = FOODTABLE.connect_db()
            cursor = db.cursor()

            sql = "UPDATE foodtable SET tablestate='" + self.tablestate + \
                "' WHERE tablenumber=" + str(self.tablenumber) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()
