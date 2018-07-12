print('输入年份，测试是平年还是闰年')
number = int(input())
if number%4 == 0 and number%100 != 0:
    print('闰年')
elif number%400 == 0:
    print('闰年')
else:
    print('平年')
