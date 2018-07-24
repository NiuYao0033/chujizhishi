shuru = input('请输入任意数字:')
ny_list = list(shuru)
ny_list1 = list(shuru)
for i in range(len(ny_list)):
    for j in range(i):
        if ny_list[j] > ny_list[i]:
            ny_list[j],ny_list[i] = ny_list[i],ny_list[j]
print(ny_list)
print('----------------------------------------------------')
for i in range(len(ny_list1)):
    for j in range(i):
        if ny_list1[j] < ny_list1[i]:
            ny_list1[j],ny_list1[i] = ny_list1[i],ny_list1[j]
print(ny_list1)
