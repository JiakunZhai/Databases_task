import pymysql


def connect_db():
    return pymysql.connect(host='localhost', user='root', passwd='200525', port=3306, db='restaurantproject')


# 增加操作
def insert_menuoder(oderid, menuid, menunum):
    try:
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO menuoder (oderid, menuid, menunum) VALUES ('" + \
            str(oderid) + "', '" + str(menuid) + "', '" + str(menunum) + "');"
        # print('sql:', sql)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('操作错误')
        print(e)
    finally:
        db.close()
