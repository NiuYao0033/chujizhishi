ny_num = 0
for i in range(1,100):
    if i%7 == 0 or i%10 == 7:
        ny_num += 1
    else:
        continue
print('从1数到99共拍腿  %d 次。'%ny_num)
