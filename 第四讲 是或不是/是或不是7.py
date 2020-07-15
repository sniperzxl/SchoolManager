import random
import time

#count代表题的数量
count = int(input("请输入要测试的题数量(10,20,30):"))

input("本次测试共%d道题,准备好了请按<enter>开始" % count )

#right代表答对的题数
right = 0
begin = time.time()
for i in range(count):
    a = random.randint(1,100)
    b = random.randint(1,100)
    answer = int(input("%d + %d = " % (a,b)))
    if answer == a + b :
        right = right + 1
end = time.time()
#打印答题结果
print("您答对了%d题，一共%d题。" % ( right , count ))
print("共用时%.2f秒." % (end-begin))
