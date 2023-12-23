from user import *
from menus import *
import worker
import oder
from foodtable import *
import pymysql


class MAIN:

    def signon():
        username = str(input("用户名："))
        userphone = str(input("手机号码："))
        newuser = USER(None, username, userphone)
        newuser.insert_user()

    def login():
        username = str(input("用户名："))
        userphone = str(input("手机号码："))
        user = USER(None, username, userphone)
        user.login()

    def delete():
        userid = str(input("用户编号："))
        username = str(input("用户名："))
        userphone = str(input("手机号码："))
        user = USER(userid, username, userphone)
        user.delete_user()

    def update():
        userid = str(input("用户编号："))
        username = str(input("用户名："))
        userphone = str(input("手机号码："))
        user = USER(userid, username, userphone)
        user.update_user()

        # 选择餐桌
    def foodTableSelect():
        num = int(input("请输入用餐人数：（数字）"))
        num_table = FOODTABLE(None, num, None)
        res = num_table.select_table()
        if res == 1:
            tablenum = str(input("请输入您选择的餐桌编号："))
            return tablenum

    def menusSelect():

        MENUS.printMenu()
        while True:
            pass


class PAGE:

    def mainPage():
        while True:
            print("欢迎用餐 V0.1".center(20, '='))
            print("signup ---------- 登录")
            print("signon ---------- 注册")
            print("deleteuser ------ 注销")
            print("updateinfo ---------- 修改")
            print("exit------------- 退出")
            print("".center(23, '='))
            s = str(input("main>")).strip().lower()
            if s == 'signon':
                MAIN.signon()
            elif s == 'signup':
                MAIN.login()
            elif s == 'deleteuser':
                MAIN.delete()
            elif s == 'updateinfo':
                MAIN.update()
            elif s == 'exit':
                break
            else:
                print('输入错误')

    def signupPage():
        print("欢迎登录")


# PAGE.mainPage()
# MAIN.foodTableSelect()
MENUS.printMenu()
