for number in range(2,100):
    for number1 in range(2,number):
        if number%number1 == 0:
            break
        number1 +=1
    else:
        print(number,end=',')
    number +=1
print('')
