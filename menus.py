import pymysql
from prettytable import PrettyTable


class MENUS:

    def __init__(self, menuid, menuname, mprice):
        self.menuid = menuid
        self.menuname = str(menuname)
        self.mprice = str(mprice)

    # 连接数据库
    @staticmethod
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='200525', port=3306, db='restaurantproject')

    # 增加操作
    def insert_menu(self):
        try:
            db = MENUS.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO MenuInfo (menuname, mprice) VALUES ('" + \
                self.menuname + "', '" + self.mprice + "');"
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
    def delete_menu(self):
        try:
            db = MENUS.connect_db()
            cursor = db.cursor()

            sql = "DELETE FROM MenuInfo WHERE menuid=" + str(self.menuid) + ";"
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
    def select_menu(self):
        try:
            db = MENUS.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM menu WHERE menuid=" + str(self.menuid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                table = PrettyTable()
                table.field_names = ["菜品编号:", "菜品名称:", "菜品价格:"]
                for row in results:
                    table.add_row(row)
            else:
                print("请联系服务员线下点单")

        except Exception as e:
            print('系统错误，请联系服务员')
            print(e)
        finally:
            db.close()

    @staticmethod
    def printMenu():
        try:
            db = MENUS.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM menus"
            # print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                table = PrettyTable()
                table.field_names = ["菜品编号:", "菜品名称:", "菜品价格:"]
                for row in results:
                    table.add_row(row)
                print(table)
                return results
            else:
                print("请联系服务员线下点单")

        except Exception as e:
            print('系统错误，请联系服务员')
            print(e)
        finally:
            db.close()

    # 修改操作
    def update_menu(self):
        try:
            db = MENUS.connect_db()
            cursor = db.cursor()

            sql = "UPDATE MenuInfo SET menuname='" + self.menuname + \
                "', mprice='" + self.mprice + \
                "' WHERE menuid=" + str(self.menuid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()
