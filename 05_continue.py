# continue : 一定要修改计数器，要不然会进入死循环！
i = 0
while i < 5:
    if i == 2 :
        i += 1
        print("吃出个大虫子，这个苹果不吃了")
        continue
    i += 1
    print(f"吃了第{i}个苹果")
