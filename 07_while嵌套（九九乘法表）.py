i = 0
j = 0
mul = 0

while i < 9:
    i += 1
    while j < i:
        j += 1
        mul = i * j
        print(f"{j}*{i}={mul}", end=" ")
    j = 0
    print("")
print("九九乘法表已完成")
