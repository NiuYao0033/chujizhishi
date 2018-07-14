age = int(input('请输入年龄：'))
subject = input('请输入专业：')
college = input('是不是重点大学毕业？')
if subject == '电子信息工程专业' and age > 25:
    print('恭喜您，面试合格')
elif subject == '电子信息工程专业' and college == '是':
    print('恭喜您，面试合格')
elif age < 28 and subject == '计算机专业':
    print('恭喜您，面试合格')
else:
    print('抱歉，您未达到面试要求')
