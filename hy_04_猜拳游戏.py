qq_num = int(input("输入你的qq号："))
qq_pas = int(input("输入你的qq密码："))
qq_1 = 123
qq_2 = 123
b = 0
c = 0
d = 0
if qq_num == qq_1 and qq_pas == qq_2:
    print("登录成功！")
    i = 0
    while True:
        while i < 3:
            import random
            com = random.randint(1, 3)
            if com == 1:
                a = "石头"
            elif com == 2:
                a = "布"
            elif com == 3:
                a = "剪刀"
            hum = input("输入你要出的拳头： ")
            print("您输入的拳头为 %s,电脑输入的拳头是 %s" % (hum, a))

            if hum == "石头":
                hum = 1
            elif hum == "布":
                hum = 2
            elif hum == "剪刀":
                hum = 3

            if ((hum == 1 and com == 2)
                    or (hum == 2 and com == 3)
                    or (hum == 3 and com == 1)):
                b = b + 1
                print("电脑赢了！")
                if b >= 2:
                    i = i + 1

            elif hum == com :
                i = i - 1
                d = 1 + d
                print("双方平局！")

            elif ((hum == 1 and com == 3)
                    or (hum == 2 and com == 1)
                    or (hum == 3 and com == 2)):
                c = c + 1
                print("你赢了！")
                if c >= 2:
                    i = i + 1
            i = i + 1
        e = d + i - 1
        if c > 0:
            z = c / e
        elif c == 0:
            z = 0
        print("一共进行了%02d局,电脑赢了%02d局,你赢了%02d局,平局次数为%02d局" % (e,b, c,d))
        print("你获胜的概率为%.02f%%"%(z * 100))
        if b >= 2:
            print("最后你输了！")
        elif c >= 2:
            print("最后你赢了！")
        choice = input("退出程序请按【1】，继续请按【2】: ")
        if choice == "1":
            print("欢迎再次使用！")
            break
        elif choice == "2":
            i = 0
            e = 0
            b = 0
            c = 0
            d = 0
else:
    print("登录失败！")
    print("请输入正确的账号或密码！")
