str1 = "itheima"
for i in str1 :
    print(i)

print()

for i in str1 :
    if i == "e":
        print("遇e跳出")
        break
    print(i)

print()

for i in str1:
    if i == "e":
        print("遇e不打印")
        continue
    print(i)