import pymysql


class USER:

    def __init__(self, userid, username, userphone):
        self.userid = userid
        self.username = str(username)
        self.userphone = str(userphone)

    # 连接数据库
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='200525', port=3306, db='restaurantproject')

    # 增加操作
    def insert_user(self):
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO UserInfo (username, userphone) VALUES ('" + self.username + "', '" + self.userphone + "');"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据插入成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 查找操作
    def select_user(self):
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM UserInfo WHERE userid=" + str(self.userid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                for row in results:
                    print("用户编号:", row[0])
                    print("用户名:", row[1])
                    print("用户手机号:", row[2])
            else:
                print("未找到记录")

        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 修改操作
    def update_user(self):
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "UPDATE UserInfo SET username='" +self.username + "', userphone='" + self.userphone + "' WHERE userid=" + str(self.userid) + ";"
            print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

