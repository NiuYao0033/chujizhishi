ny_s = input()
ny_dict = {}
for i in ny_s.lower():
    if i in ny_dict.keys():
        ny_dict[i] += 1
    else:
        ny_dict[i] = 1
print(ny_dict)
