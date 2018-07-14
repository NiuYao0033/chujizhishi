print('求1-100之间能被7整除，但是同时不能被5整除的所有整数')
i = 1
while i <= 100:
    if i % 7 == 0 and i % 5 != 0:
        print('%d'%i)
    i +=1
