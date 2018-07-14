print('------跳一跳，输入 ‘退出’即可游戏------')
print('欢迎回来，请开始游戏')
print('请输入\（中心、音乐模块、微信支付模块）')
while True:
    shuru = input('请输入：')
    if shuru == '退出':
        print('已退出')
        break
    elif shuru == '中心':
        print('您的分数为：32')
        continue
    elif shuru == '音乐模块':
        print('您的分数为：30')
        continue
    elif shuru == '微信支付模块':
        print('您的分数为：42')
        continue
    else:
        print('输入有误，请重新输入')
        continue    
