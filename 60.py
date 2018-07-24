print('车次\t出发站-到达站\t出发时间\t到达时间\t历时\nT40\t长春-北京\t00:12\t\t12:20\t\t12:08\nT298\t长春-北京\t00:06\t\t10:50\t\t10:44\nZ158\t长春-北京\t12:48\t\t21:06\t\t08:18\nZ62\t长春-北京\t21:58\t\t06:08\t\t8:20')
ny_num = input('请输入要购买的车次：')
ny_name = input('请输入乘车人（用逗号分隔）:')
if ny_num == 'T40':
    print('您已购%s次列车  长春-北京  00:12开，请%s尽快换取纸质车票。【铁路客服】'%(ny_num,ny_name))
elif ny_num == 'T298':
    print('您已购%s次列车  长春-北京  00:06开，请%s尽快换取纸质车票。【铁路客服】'%(ny_num,ny_name))
elif ny_num == 'Z158':
    print('您已购%s次列车  长春-北京  12:48开，请%s尽快换取纸质车票。【铁路客服】'%(ny_num,ny_name))
elif ny_num == 'Z62':
    print('您已购%s次列车  长春-北京  21:58开，请%s尽快换取纸质车票。【铁路客服】'%(ny_num,ny_name))
else:
    print('输入错误，请重新输入')
