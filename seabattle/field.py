class Field:
    def __init__(self,x,y,val='0'):
        self.x =x
        self.y =y


    def CreateF(self):
        f = []
        for j in range(6):
            f.append([])
            for c in range(6):
                f[j].append('0')
        return f
