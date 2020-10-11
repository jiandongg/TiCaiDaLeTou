from random import sample
CHANCE = 6  # 5次购彩机会

top = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
       31, 32, 33, 34, 35]
bottom = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for num in range(1, CHANCE):
    top_5 = sample(top, 5)  # 随机抽取5个元素
    top_5.sort()
    bottom_2 = sample(bottom, 2)  # 随机抽取2个元素
    bottom_2.sort()
    print("第 %d 个中奖号码" % num)
    print(top_5)
    print(bottom_2)
print("***祝君好运***")
