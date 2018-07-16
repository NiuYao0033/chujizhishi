shuru = input('请输入：')
number = 0
for a in shuru:
    if a.isdigit():
        number += 1
print('数字的个数为：%d'%number)
