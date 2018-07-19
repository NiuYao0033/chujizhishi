def ny_fun_checkout(ny_list):
    count = 0
    for count1 in ny_list:
        count += count1
    if count >= 500 and count < 1000:
        print('合计金额：%.f\t实际金额：%.2f'%(count,count*0.9))
    elif count >= 1000 and count < 2000:
        print('合计金额：%.f\t实际金额：%.2f'%(count,count*0.8))
    elif count >= 2000 and count < 3000:
        print('合计金额：%.f\t实际金额：%.2f'%(count,count*0.7))
    elif count >= 3000:
        print('合计金额：%.f\t实际金额：%.2f'%(count,count*0.6))
    else:
        print('合计金额：%.f\t实际金额：%.2f'%(count,count))
ny_list = []
while True:
    money = float(input('输入商品金额(输入0表示输入完毕):'))
    ny_list.append(money)
    if money == 0:
        ny_fun_checkout(ny_list)
        break 
