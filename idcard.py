print('程序员甲说：你知道我的生日吗？')
print('程序员乙说：输入你的身份证号码')
number = str(input('程序员甲说：'))
year = number[6:10]
month = number[10:12]
day = number[12:14]
print('程序员乙说：你是%s年%s月%s日出生的，所以你的生日是%s月%s日'%(year,month,day,month,day))

