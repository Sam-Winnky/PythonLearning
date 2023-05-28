i = 0
while i <5:
    i += 1
    print("媳妇我错了")
else:
    print("Ohhhhhh，老婆原谅我了")

print()

#break
i = 0
while i <5:
    i += 1
    print("媳妇我错了")
    if i == 3:
        print("呜呜呜呜呜呜，老婆不会原谅我了")
        break
else:
    print("Ohhhhhh，老婆原谅我了")#非正常结束时，else不执行

print()

#continue
i = 0
while i <5:
    if i == 3:
        i += 1
        print()
        continue
    i += 1
    print("媳妇我错了")
else:
    print("Ohhhhhh，老婆原谅我了")

print()

#for
str1 = "itheima"
for i in str1 :
    print(i)
else:
    print("跳出！正常结束时出现")

print()

str1 = "itheima"
for i in str1 :
    if i == "e":
        print("遇e结束")
        break
    print(i)
else:
    print("跳出！正常结束时出现")

print()

str1 = "itheima"
for i in str1 :
    if i == "e":
        i += "i"
        print("遇e跳出")
        continue
    print(i)
else:
    print("跳出！正常结束时出现")