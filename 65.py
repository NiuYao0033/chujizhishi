ny_mon = int(input('请输入月份(例如：5)：'))
ny_day = int(input('请输入日期(例如：17)：'))
if ny_mon == 1 and ny_day in range(20,31) or ny_mon ==2 and ny_day in range(1,19):
    print('%d月%d日的星座为：水瓶座'%(ny_mon,ny_day))
elif ny_mon == 2 and ny_day in range(19,31) or ny_mon ==3 and ny_day in range(1,21):
    print('%d月%d日的星座为：双鱼座'%(ny_mon,ny_day))
elif ny_mon == 3 and ny_day in range(21,31) or ny_mon ==4 and ny_day in range(1,20):
    print('%d月%d日的星座为：白羊座'%(ny_mon,ny_day))
elif ny_mon == 4 and ny_day in range(20,31) or ny_mon ==5 and ny_day in range(1,21):
    print('%d月%d日的星座为：金牛座'%(ny_mon,ny_day))
elif ny_mon == 5 and ny_day in range(21,31) or ny_mon ==6 and ny_day in range(1,22):
    print('%d月%d日的星座为：双子座'%(ny_mon,ny_day))
elif ny_mon == 6 and ny_day in range(22,31) or ny_mon ==7 and ny_day in range(1,23):
    print('%d月%d日的星座为：巨蟹座'%(ny_mon,ny_day))
elif ny_mon == 7 and ny_day in range(23,31) or ny_mon ==8 and ny_day in range(1,23):
    print('%d月%d日的星座为：狮子座'%(ny_mon,ny_day))
elif ny_mon == 8 and ny_day in range(23,31) or ny_mon ==9 and ny_day in range(1,23):
    print('%d月%d日的星座为：处女座'%(ny_mon,ny_day))
elif ny_mon == 9 and ny_day in range(23,31) or ny_mon ==10 and ny_day in range(1,24):
    print('%d月%d日的星座为：天秤座'%(ny_mon,ny_day))
elif ny_mon == 10 and ny_day in range(24,31) or ny_mon ==11 and ny_day in range(1,23):
    print('%d月%d日的星座为：天蝎座'%(ny_mon,ny_day))
elif ny_mon == 11 and ny_day in range(23,31) or ny_mon ==12 and ny_day in range(1,22):
    print('%d月%d日的星座为：射手座'%(ny_mon,ny_day))
elif ny_mon == 12 and ny_day in range(22,31) or ny_mon ==1 and ny_day in range(1,20):
    print('%d月%d日的星座为：摩羯座'%(ny_mon,ny_day))
