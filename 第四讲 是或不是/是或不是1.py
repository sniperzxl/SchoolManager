import random
num = random.randint(0,9)
valString = input("请输入你猜的数字:")
varNum = int(valString)
if varNum == num:
    print("恭喜你，你获得了奖励。")
if varNum != num:
    print("抱歉，你不能获得我的奖励了。正确的数字是：%d" % num)
