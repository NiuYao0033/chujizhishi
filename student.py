class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.scores = {'语文':98,'数学':99,'英语':100}
    def get_name(self):
        print('学生姓名：{}'.format(self.name))
    def get_age(self):
        print('年龄：{}'.format(self.age))
    def get_course(self,scores_list):
        for k,v in self.scores.items():
            scores_list.append(v)
        print('最高成绩：{}'.format(max(scores_list)))
scores_list = []
xiaoming = Student('小明',23)
xiaoming.get_name()
xiaoming.get_age()
xiaoming.get_course(scores_list)
