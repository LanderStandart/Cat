import random
class Ship:
    def __init__(self,x,y,val,orient):
        #определям координаты и палубность корабля и его ориентацию (горизонт, вертикаль)
        self.x = x
        self.y = y
        self.val =val
        self.orient = orient

    def get_ship(self):
        return [self.x,self.y,self.val,self.orient]


class Count_Ship:
    @staticmethod
    def SHIP_VAL1():
        return 4

    @staticmethod
    def SHIP_VAL2():
        return 2

    @staticmethod
    def SHIP_VAL3():
        return 1

    @staticmethod
    def gen_ship():
        a=[]
        a = [random.randrange(1, 6, 1), random.randrange(1, 6, 1), random.randrange(0, 2, 1)]
        return a




