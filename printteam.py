print('2017~2018赛季NBA西部联盟前8名:')
group = ['火箭','勇士','开拓','爵士','鹈鹕','马刺','雷霆','森林狼']
for i,a in enumerate(group):
    if i%2 == 0:
        print(a,'',end='\t')
    else:
        print(a)
