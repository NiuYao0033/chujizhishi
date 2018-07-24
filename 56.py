ny_s = input()
ny_list = list(ny_s)
a = ny_list[-1]
ny_list.reverse()
ny_list.append(a)
ny_list.reverse()
ny_list.pop(-1)
ny_string = ''.join(ny_list)
print('----------------------')
ny_s1 = ny_s[-1] 
ny_s2 = ny_s[0:-1]
print(ny_s1+ny_s2)
