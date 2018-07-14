while True:
    shuru = int(input('请输入1-100之间的数'))
    if shuru <= 99:
        print('命运给予我们的不是失望之酒,而是机会之杯\n'*shuru)
        continue
    elif shuru == 100:
        break
    else: 
        shuru = int(input('请输入1-100之间的数'))
        continue
