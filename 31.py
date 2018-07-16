a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]
for row in a:
    for col in b:
        if col <= row:        
            print('%d*%d=%d'%(col,row,col*row),end='\t ')
    print('')
