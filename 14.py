import random
print('请您输入数字1-10')
player = int(input())
computer = random.randint(1,10)
if player == computer:
    print('胜利！！！')
else:
    print('失败，你是一个loser')
