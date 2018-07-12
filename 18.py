number = 859580735
password = 123456
money = 100000000
print('请输入账号')
number1 = int(input())
print('请输入密码')
password1 = int(input())
if int(number1) == int(number) and password1 == password:
    print('请输入取款金额')
    money1 = int(input())
    if money1 <= money:
        c = money-money1
        print('取了%d元'%money1)
        print('剩余%d元'%c)
    else:
        print('没钱你取个毛线！！！')
else:
    print('非法账号')

