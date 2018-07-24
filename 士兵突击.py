class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self):
        count = int(input('装入多少颗子弹：'))
        self.bullet_count += count
    def shoot(self):
        if self.bullet_count <=0:
            print('没有子弹')
        else:
            self.bullet_count -=1
            print('士兵发射了子弹')
AK47 = Gun('AK47')
AK47.add_bullet()
AK47.shoot()
class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = int(input('是否为士兵配备一把{}：0.否1.是'.format(AK47.model) ))
    def fire(self):
        if self.gun == 0:
            print('{}还没有枪'.format(self.name))
            return
        else:
            print('{}有把{}'.format(self.name,AK47.model))
            print('{}开火'.format(self.name))
xusanduo = Soldier('许三多')
xusanduo.fire()
