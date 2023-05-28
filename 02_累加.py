i = 0
s = 0

while i <= 100:
    s += i
    i += 1
    print(s)

print("计算结果完成，计算次数为%d，最终结果为：%d" % (i-1,s))