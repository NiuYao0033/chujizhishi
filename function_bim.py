def ny_function_bim(name,height,weight):
    BMI = weight/(height*height)
    if BMI < 18.5:
        print('%s的身高：%.2f米\t体重：%.2f千克\n%s的BIM指数为：%.2f\n过轻。'%(name,height,weight,name,BMI))
    elif BMI > 18.5 and BMI < 24.9:
        print('%s的身高：%.2f米\t体重：%.2f千克\n%s的BIM指数为：%.2f\n正常。'%(name,height,weight,name,BMI))
    elif BMI > 24.9 and BMI < 29.9:
        print('%s的身高：%.2f米\t体重：%.2f千克\n%s的BIM指数为：%.2f\n胖子，想啥那，减肥吧。'%(name,height,weight,name,BMI))
    else:
        print('%s的身高：%.2f米\t体重：%.2f千克\n%s的BIM指数为：%.2f\n过重。'%(name,height,weight,name,BMI))
ny_function_bim('路人甲',1.83,60)
ny_function_bim('路人乙',1.60,5)
