# 对用户输入次数进行限制，如果3次没有猜中直接结束游戏
guess = input('请输入一个整数：')
guess = int(guess)
count = 0
if guess == 8:
    print("哇草，你是小甲鱼心里的蛔虫吗?")
    print("哼，猜中了也没有奖励")
    print("游戏结束，不玩啦~~~~")
else:
    while guess !=
while guess != 8 and count != 3:
        if guess > 8:
            print("哥，大了大了~~~")
        if guess < 8:
            print("嘿，小了！小了！！")
        guess = input('请重新输入一个整数：')
        guess = int(guess)
        count += 1
else:
    print("哇草，你是小甲鱼心里的蛔虫吗?")
    print("哼，猜中了也没有奖励")
print("游戏结束，不玩啦~~~~")


