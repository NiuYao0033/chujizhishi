a = int(input())
while True:   #死循环
    if a%3 == 2 and a%5 == 3 and a%7 == 2:
        print('数字%d符合要求'%a)
        break
    else:
        a = int(input('输入错误，请重新输入'))
