s = 'I,love,python'
print(s[2:6])
print('-----------------')
s1 = 'aabbccddee'
a = s1.replace('dd','ff',1)
print(a)
print('-----------------')
s3 = 'ab2b3n5nn2n67mm4n2'
b = s3.count('n')
print(b)
print('------------------')
word_dict = {}
for i in s3:
    if i in word_dict.keys():
        word_dict[i] +=1
    else:
        word_dict[i]= 1
print(word_dict)
