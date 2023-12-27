from user import *
from menus import *
from worker import *
from oder import *
from foodtable import *
from menuoder import *
import pymysql

# 定义全局变量
menuOrderList = []  # 点菜编号
tablenum = 0        # 餐桌编号
oderid = 0          # 订单id
total_cost = 0      # 订单总价
userid = 0
workerid = 0

# 主要函数封装
class MAIN:

    def signon(userid):
        username = str(input("signon > 用户名："))
        userphone = str(input("signon > 手机号码："))
        newuser = USER(None, username, userphone)
        userid = newuser.insert_user()

    def login():
        username = str(input("login > 用户名："))
        userphone = str(input("login > 手机号码："))
        user = USER(None, username, userphone)
        userdb = user.login()
        if userdb[1] == 1:
            print("登录成功")
            PAGE.homepage(menuOrderList, tablenum, total_cost)

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
    def foodTableSelect(tablenum):
        num = int(input("请输入用餐人数：（数字）"))
        num_table = FOODTABLE(None, num, None)
        res = num_table.select_table()
        if res == 1:
            tablenum = str(input("请输入您选择的餐桌编号："))
            # return tablenum

    def menusSelect(menuOrderList, total_cost):
        MENUS.printMenu()
        try:
            db = MENUS.connect_db()
            cursor = db.cursor()

            while True:
                order_input = input("请输入菜品编号和数量（以空格分隔，输入'q'结束点单）：")
                if order_input == 'q':
                    break

                menu_number, quantity = order_input.split()
                quantity = int(quantity)

                sql = f"SELECT * FROM menus WHERE menuid = '{menu_number}'"
                cursor.execute(sql)
                result = cursor.fetchone()

                if result:
                    dish_name = result[1]
                    dish_price = result[2]
                    total_price = float(dish_price) * float(quantity)
                    menuOrderList.append(
                        [menu_number, dish_name, quantity, dish_price, total_price])
                    total_cost += total_price
                else:
                    print("菜品编号无效，请重新选择菜品")

            if menuOrderList:
                print("")
                print("请确认您的点单情况".center(26, "="))
                table = PrettyTable()
                table.field_names = ["菜品编号", "菜品名称", "数量", "单价", "总价"]

                for dish in menuOrderList:
                    table.add_row(
                        [dish[0], dish[1], dish[2], dish[3], dish[4]])

                table.add_row(["总计", "", "", "", total_cost])
                print(table)
                return menuOrderList
            else:
                print("您还未点任何菜品")

        except Exception as e:
            print('系统错误，请联系服务员')
            print(e)
        finally:
            db.close()

    def oder_inster(oderid, userid, ):
        # 对现在的点餐数量结账
        print("欢迎用餐".center(20, '='))
        select = str(input("是否结账？Y/N"))

        if select == "Y":
            if menuOrderList:
                print("")
                print("请确认您的点单情况".center(26, "="))
                table = PrettyTable()
                table.field_names = ["菜品编号", "菜品名称", "数量", "单价", "总价"]

                for dish in menuOrderList:
                    table.add_row(
                        [dish[0], dish[1], dish[2], dish[3], dish[4]])

                table.add_row(["总计", "", "", "", total_cost])
                print(table)
                res = str(input("请确认订单是是否有误？Y/N"))
                if res == 'Y':
                    table = PrettyTable()
                    table.add_row(["总计", total_cost])
                    print(table)
                    oder = ODER(None, tablenum, userid, None, total_cost)
                    oderid = oder.insert_order()


            else:
                print("您还未点任何菜品")


        else:
            return




# 界面封装


class PAGE:

    def mainPage():
        while True:
            print("欢迎用餐 V0.1".center(20, '='))
            print("signon ---------- 登录")
            print("signup ---------- 注册")
            print("deleteuser ------ 注销")
            print("updateinfo ------ 修改")
            print("exit------------- 退出")
            print("".center(23, '='))
            s = str(input("main>")).strip().lower()
            if s == 'signon':
                MAIN.login()
            elif s == 'signup':
                MAIN.signon(userid)
            elif s == 'deleteuser':
                MAIN.delete()
            elif s == 'updateinfo':
                MAIN.update()
            elif s == 'exit':
                break
            else:
                print('输入错误')

    def homepage(menuOrderList, tablenum, total_cost):
        while True:
            print("欢迎用餐 V0.1".center(20, '='))
            print("menus ---------- 菜单")
            print("selectTable ---- 选择餐桌")
            print("oder ----------- 结账")
            # print("updateinfo ---")
            print("exit------------ 退出")
            print("".center(23, '='))

            s = str(input("点餐界面 > "))
            if s == 'menus':
                MAIN.menusSelect(menuOrderList, total_cost)
            elif s == 'selectTable':
                MAIN.foodTableSelect(tablenum)
            elif s == 'oder':
                # todo 暂时没有写函数
                # 这个地方应该是点菜的函数这个函数应该将点了什么菜输出一遍，
                # 然后再订单菜谱表中插入，但是获取的订单编号应该如何做？
                # 订单编号可以在插入的时候获取到，那么还需要讲

                pass
            elif s == 'exit':
                break


if __name__ == '__main__':
    PAGE.mainPage()
