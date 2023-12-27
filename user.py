import pymysql


class USER:

    def __init__(self, userid, username, userphone):
        self.userid = userid
        self.username = str(username)
        self.userphone = str(userphone)

    # 连接数据库
    @staticmethod
    def connect_db():
        return pymysql.connect(host='localhost', user='root', passwd='200525', port=3306, db='restaurantproject')

    # 增加操作
    def insert_user(self):
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "INSERT INTO user (username, userphone) VALUES ('" + \
                self.username + "', '" + self.userphone + "');"
            # print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            userid = cursor.lastrowid
            print('注册成功')

        except Exception as e:
            print('注册失败')
            print(e)
        finally:
            db.close()
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM user WHERE userphone=" + \
                str(self.userphone) + ";"
            # print('sql:', sql)

            cursor.execute(sql)
            results = cursor.fetchall()

            if len(results) > 0:
                for row in results:
                    print("用户编号:", row[0])
                    print("用户名:", row[1])
                    print("用户手机号:", row[2])
            return userid
        finally:
            db.close()

    # 查找操作
    def select_user(self):
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM user WHERE userid=" + str(self.userid) + ";"
            # print('sql:', sql)

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

            sql = "UPDATE user SET username='" + self.username + "', userphone='" + \
                self.userphone + "' WHERE userid=" + str(self.userid) + ";"
            # print('sql:', sql)

            cursor.execute(sql)
            db.commit()
            print('数据修改成功!')
        except Exception as e:
            print('操作错误')
            print(e)
        finally:
            db.close()

    # 删除操作
    def delete_user(self):
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "DELETE FROM user WHERE userid=" + str(self.userid) + ";"
            cursor.execute(sql)
            db.commit()
            print('注销成功')
        except Exception as e:
            print('注销失败')
            print(e)
        finally:
            cursor.close()
            db.close()

    def login(self):
        res = 0
        try:
            db = USER.connect_db()
            cursor = db.cursor()

            sql = "SELECT * FROM user WHERE username='" + \
                self.username + "' AND userphone='" + self.userphone + "';"
            cursor.execute(sql)

            result = cursor.fetchone()
            if result is not None:
                userid = result[0]
                username = result[1]
                userphone = result[2]
                res = res+1
                return (USER(userid, username, userphone), res)
            else:
                return None
        except Exception as e:
            print('登录失败')
            print(e)
        finally:
            cursor.close()
            db.close()
