ny_list = [{'name':'绮梦','height':1.7,'weight':65},{'name':'零语','height':1.78,'weight':50},{'name':'黛兰','height':1.72,'weight':66},{'name':'紫轩','height':1.8,'weight':75},{'name':'冷伊一','height':1.75,'weight':70}]
def ny_function_bmi_upgrade(list_dict):
    list_dict['name']
    list_dict['height']
    list_dict['weight']
    BMI = list_dict['weight']/(list_dict['height']*list_dict['height'])
    if BMI < 18.5:
        print('============%s============\n身高:%.f\t体重：%d千克\nBMI指数为：%.2f，体重过轻'%(list_dict['name'],list_dict['height'],list_dict['weight'],BMI))
    elif BMI > 18.5 and BMI < 24.9:
        print('============%s============\n身高:%.f\t体重：%d千克\nBMI指数为：%.2f，正常'%(list_dict['name'],list_dict['height'],list_dict['weight'],BMI))
    elif BMI > 24.9 and BMI < 29.9:
        print('============%s============\n身高:%.f\t体重：%d千克\nBMI指数为：%.2f，过重。'%(list_dict['name'],list_dict['height'],list_dict['weight'],BMI))
    else:
        print('============%s============\n身高:%.f\t体重：%d千克\nBMI指数为：%.2f，肥胖。'%(list_dict['name'],list_dict['height'],list_dict['weight'],BMI))
for list_dict in ny_list:
    ny_function_bmi_upgrade(list_dict)
