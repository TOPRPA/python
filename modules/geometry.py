#在geometry模組中定義幾何運算功能
#計算兩點距離
def distance(x1,y1,x2,y2): 
    return((x2-x1)**2+(y2-y1)**2)**0.5 #用return直接帶回兩點距離公式
#計算兩點斜率
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)