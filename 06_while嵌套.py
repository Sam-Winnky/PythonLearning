i = 0
j = 0

while i < 100:
    i += 1
    j = 0
    while j < i:
        j += 1
        print("*", end="")
    print("")
    print(f"第{i}行")
print("执行完毕")