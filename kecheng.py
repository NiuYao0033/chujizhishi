class  Courses():
    def __init__(self,number,subject,teacher,place):
        self.number = number
        self.subject = subject
        self.teacher = teacher
        self.__place = place
    def classroom_information(self):
        print('课程编号：{}\n课程名称：{}\n任课老师：{}\n上课地点：{}'.format(self.number,self.subject,self.teacher,self.__place))
python = Courses(2,'python','翁闻宇',202)
python.classroom_information()
