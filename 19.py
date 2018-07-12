print('请输入身高')
height = int(input())
print('请输入身价')
social_status = int(input())
print('请输入颜值分')
Face_score = int(input())
if height > 180 and social_status > 1000000 and Face_score > 99:
    print('高富帅')
elif height < 180 and social_status > 1000000 and Face_score > 99:
    print('富帅')
elif height < 180 and social_status < 1000000 and Face_score > 99:
    print('帅')
elif height < 160 and social_status < 100 and Face_score < 60:
    print('矮穷矬')
