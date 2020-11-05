from ship import Ship,Count_Ship
from field import Field
import random
F1 = Field(1,1)
f = F1.CreateF()
print('расчитываем поле')
for c in range(3-1,-1,-1):
    i=0
    z = c+1
    xpaluba = 'Count_Ship.SHIP_VAL'+str(z)


    while i != eval(xpaluba)():
        ship1 = Count_Ship.gen_ship()
        y = ship1[0]-1
        x = ship1[1]-1
        orien = ship1[2]
        if f[x][y]!='1' and f[x-1][y]!='1' and f[x][y-1]!='1' and f[x+1][y]!='1' \
                and f[x][y+1]!='1' and f[x+1][y+1]!='1' \
                and f[x-1][y-1]!='1' and f[x-1][y+1]!='1'and f[x+1][y-1]!='1':
            if z == 2:
                if orien:
                    f[x][y] = '1'
                    f[x+1][y]= '1'
                else:
                    f[x][y] = '1'
                    f[x][y+1] = '1'
                print('2')
            if z == 3:
                if orien:
                    f[x][y] = '1'
                    f[x + 1][y] = '1'
                    f[x + 2][y] = '1'
                else:
                    f[x][y] = '1'
                    f[x][y+1] = '1'
                    f[x][y+2] = '1'
                print('3')
            if z ==1 :
                f[x][y] = '1'
                print('1')
            i=i+1




for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == '1':
            val ='■'
        else:
            val = f[i][j]
        print(val, end=' ')
    print()