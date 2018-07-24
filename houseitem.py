class HouseItem:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return '{}的占地面积：{}平方米'.format(self.name,self.area)
bed = HouseItem('席梦思',4)
print(bed)
chest = HouseItem('衣柜',2)
print(chest)
table = HouseItem('餐桌',1.5)
print(table)
class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def add_item(self,item):
        print('要添加{}'.format(item))
        if item.area > house.free_area:
            print('{}的面积太大，不能添加到房子里'.format(item))
            return
        self.item_list.append(item.name)
        self.free_area -= item.area
    def __str__(self):
        return '户型：{}\n总面积：{}平方米\n剩余：{}平方米\n家具:{}'.format(self.house_type,self.area,self.free_area,self.item_list)
house = House('两室一厅',60)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
