class Animal():
    def __init__(self,new_color,new_name):
        self.color = new_color
        self.name = new_name
    def call(self):
        print('{}在叫'.format(self.name))
class Fish(Animal):
    def __init__(self,new_color,new_name,new_tail):
        super().__init__(new_color,new_name)
        self.tail = new_tail
    def call(self):
        print('{}不会叫'.format(self.name))
dongwu = Animal('白','白虎')
dongwu.call()
liyu = Fish('红','鲤鱼',True)
liyu.call()
