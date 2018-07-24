print('定制自己的手机套餐：')
ny_list1 = {1:'0分',2:'50分',3:'100分',4:'300分',5:'不限量'}
ny_list2 = {1:'0M',2:'500M',3:'1G',4:'5G',5:'不限量'}
ny_list3 = {1:'0条',2:'50条',3:'100条'}
print('定制自己的手机套餐：')
print('A.请设置自己的通话时长:')
for k,v in ny_list1.items():
    print(k,v)
k = int(input('输入通话时间编号：'))
print('B.请设置流量：')
for a,b in ny_list2.items():
    print(a,b)
a = int(input('选择的流量编号：'))
print('C.请设置短信：\n1.0条\n2.50条\n3.100条')
for c,d in ny_list3.items():
    print(c,d)
c = int(input('输入选择的短信条数编号：'))
print('')
print('您的手机套餐定制成功：免费通话时长为%s/月，流量为%s/月，短信条数%s/月'%(ny_list1[k],ny_list2[a],ny_list3[c]))
