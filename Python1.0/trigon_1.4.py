#本版本提高了精度，考虑了正切余切函数的值，可以任意输入角度
#考虑到泰勒展开式的取值范围，将所有输入转化到0到pi/2区间内计算


import math as m
p = m.pi  #pi值

#定义正弦函数
def fsin(a):
    if a<0:
        a = a+360  #移到正半轴
    if 270 >= a >= 90:
        a = 180 - a
    elif a>270:
        a = a - 360
    x = a * p / 180
    y1 = x - (x ** 3 / 6) + x ** 5 / 120
    y11 = m.sin(x)
    return y1,y11
#定义余弦函数
def fcos(a):
    a == abs(a)
    if 270>=a>=90:
        a = a-180
        x = a * p / 180
        y2 = -(1 - x ** 2 / 2 + x ** 4 / 24 - x ** 6 / 720)
    elif a>270:
        a = a-360
        x = a * p / 180
        y2 = 1 - x ** 2 / 2 + x ** 4 / 24 - x ** 6 / 720
    else:
        x = a * p / 180
        y2 = 1 - x ** 2 / 2 + x ** 4 / 24 - x ** 6 / 720
    y22 = m.cos(x)
    return y2,y22

def ftan(a):
    a1 = a%180
    if a1 == 90 or a1 == -90:
        x = a1 * p / 180
        y3 = 'FALSE'
        y33 = m.tan(x)
    else:
        if a1 > 90:
            a1 = a1 - 180
        elif a1 <- 90:
            a1 = a1 + 180
        x = a1 * p / 180
        y3 = x + x ** 3 / 3 + 2 * x ** 5 / 15 + 17 * x ** 7 / 315 + 62 * x ** 9 / 2835
        y3 = round(y3,6)
        y33 = m.tan(x)
    return y3,y33

def fcot(a):
    a2 = a%180
    if a2 == 0:
        x = a2 * p / 180
        y4 = 'FALSE'
        x = x + 0.000001
        y44 = m.cos(x) / m.sin(x)
    else:
        if a2 > 90:
            a1 = a2 - 180
        elif a2 < -90:
            a1 = a2 + 180
        x = a2 * p / 180
        y4 = 1 / x - x / 3 - x ** 3 / 45 - 2 * x ** 5 / 945
        y4 = round(y4,6)
        y44 = m.cos(x)/m.sin(x)
    return y4,y44

a0 = float(input('请输入角度(角度制)：'))
a = a0%360
(y1,y11),(y2,y22),(y3,y33),(y4,y44) = fsin(a),fcos(a),ftan(a),fcot(a)

print("正弦值和相应函数计算值分别为：%.6f，%.6f"%(y1,y11))
print("余弦值和相应函数计算值分别为：%.6f，%.6f"%(y2,y22))
print("正切值和相应函数计算值分别为：%s，%.6f"%(y3,y33))
print("余切值和相应函数计算值分别为：%s，%.6f"%(y4,y44))
