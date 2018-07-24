class Circle():
    def __init__(self,Center_position,radii,color):
        self.Center_position = Center_position
        self.radii = radii
        self.color = color
    def perimeter(self):
        C = 2*3.14*self.radii
        print('圆的周长为：{}米'.format(C))
    def the_measure_of_area(self):
        S = 3.14*self.radii**2
        print('圆的面积为：{}平方米'.format(S))
yuan = Circle('O',6,'红色')
yuan.perimeter()
yuan.the_measure_of_area()
