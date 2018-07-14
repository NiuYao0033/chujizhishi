print('为了您和他人的安全，严禁酒后驾车！')
alcohol_content = int(input('请输入每100毫升血液的酒精含量'))
if alcohol_content < 100:
    if alcohol_content > 0 and alcohol_content < 20:
        print('您还构不成饮酒行为，可以开车，但是要注意安全')
    elif alcohol_content >= 20 and alcohol_content < 80:
        print('已经达到酒后驾驶的标准，请千万不要开车')
    else:
        print('已经达到醉酒驾车的标准，请不要开车')

