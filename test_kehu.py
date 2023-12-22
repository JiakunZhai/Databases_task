import pymysql as mysql

class USER:

    def __init__(self, username="", userphone=""):
        self.username = str(username)
        self.userphone = str(userphone)

    def userlogon(self):
        self.name = input("请输入用户名：")
        self.phoneNum = input("请输入联系电话：")

        # 连接数据库
        try:
            db = mysql.connect(host="localhost", user="root", password="200525", port=3306, db="restaurantproject")
            print("连接数据库成功\n")
            cursor = db.cursor()
            sql = "INSERT INTO user (username, userphone) VALUES (%s, %s)"
            values = (self.name, self.phoneNum)
            cursor.execute(sql, values)
            db.commit()
            print("插入数据成功")
        except Exception as e:
            print("发生错误")
            print(e)
            db.rollback()  # 回滚数据库操作
        finally:
            db.close()
    def updata_user_name(self):

        updatename = input("请输入用户名：")
        phoneNum = input("请输入联系电话：")
        # 判断用户是否存在
        
        print("请输入您想修改的内容")
        # 连接数据库
        try:
            db = mysql.connect(host="localhost", user="root", password="200525", port=3306, db="restaurantproject")
            print("连接数据库成功\n")
            cursor = db.cursor()
            sql = "INSERT INTO user (username, userphone) VALUES (%s, %s)"
            values = (self.name, self.phoneNum)
            cursor.execute(sql, values)
            db.commit()
            print("插入数据成功")
        except Exception as e:
            print("发生错误")
            print(e)
            db.rollback()  # 回滚数据库操作
        finally:
            db.close()


