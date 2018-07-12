name = '小明'
height = 1.75
weight = 80.5
BMI = int(weight/(height**2))
if BMI <= 18.5:
    print(name,height,weight,BMI)
    print('测试结果：过轻。')
elif BMI > 18.5 and BMI <= 25:
    print(name,height,weight,BMI)
    print('测试结果：正常。')
elif BMI > 25 and BMI <= 28:
    print(name,height,weight,BMI)
    print('测试结果：过重。')
elif BMI > 28 and BMI < 32:
    print(name,height,weight,BMI)
    print('测试结果：肥胖。')
elif BMI > 32:
    print(name,height,weight,BMI)
    print('测试结果：严重肥胖。')
else:
    print('输入有误，请重新输入。')

