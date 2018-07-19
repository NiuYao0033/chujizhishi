import datetime
ny_list = ['今天是星期一：\n坚持下去不是我很坚强，而是我别无选择。','今天是星期二：\n含泪播种的人一定能笑着收获','今天是星期三：\n作对的事情比把事情做对更重要。','今天是星期四;\n命运给我们的不是失望之酒，二十希望之杯。','今天是星期五：\n不要等到明天，明天太遥远，今天就行动。','今天星期六：\n求之若饥，虚心若愚',"今天是星期日：\n成功降属于那些从不说'不可能'的人。"]
def function_tips(ny_list):
    day = datetime.datetime.now().weekday()
    print(ny_list[day])
function_tips(ny_list)
