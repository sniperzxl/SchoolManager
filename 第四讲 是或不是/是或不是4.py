import random
num = random.randint(1,10)
val = int(input("请输入大于等于%d的数字: "% num))
if val >= num:
    print("你太棒了!")
else:
    print("错了哦，%d小于%d" % (val,num))
