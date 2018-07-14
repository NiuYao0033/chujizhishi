a = 1
while a <= 9:
    b = 0
    while b<= 9:
        c = 0
        while c <= 9:
            if str(a)+str(b)+str(c) == str(a**3+b**3+c**3):
                print(str(a)+str(b)+str(c))
                c +=1
            else:
                c +=1
        b +=1 
    a +=1
