print('欢迎登录10086自助查询功能：')
print('输入1.显示您当前的余额')
print('输入2，显示您当前剩余的流量')
print('输入3，显示您当前的剩余通话')
print('请输入')
number = int(input())
if number == 1:
    print('您当前余额为%d元'%(number*100))
elif number == 2:
    print('您当前流量剩余%dG'%(number*10))
elif number == 3:
    print('您当月剩余的免费通话分钟数为：%d分'%(number*100))
else:
    print('输入错误，请重新输')

