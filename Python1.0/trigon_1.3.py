#尝试增大计算精度，以及考虑正切余切函数的定义域附近的取值

import math as m
import random
p = m.pi  #pi值

def sanjiao(a):
    #转化为弧度制
    x = a*p/180
    #正弦函数级数展开
    y1 = x - (x**3/6)+x**5/120
    #余弦函数
    y2 = 1-x**2/2+x**4/24-x**6/720
    #正切函数
    y3 = x + x**3/3 + 2*x**5/15+ 17*x**7/315+62*x**9/2835
    #余切函数
    y4 = 1/x - x/3 - x**3/45 - 2*x**5/945
    return x,y1,y2,y3,y4

#输入角度
i = float(input('请输入角度(角度)：'))
#角度为0时，影响部分太乐了展开式的计算
if i == 0:
    i = i + 0.000001
x,y1,y2,y3,y4 = sanjiao(i)
print(x)
n = random.randint(0,20)

#判断输入角度是否无限接近于正切函数的非定义域附近
for j in range(0,n):
    if 0<= ((1.570795+6.28318*j)-x)<=0.01 or -0.01<= ((1.570795+6.28318*j)+x)<=0:
        y3 = float('inf')
    elif 0<= (x - (1.570795+6.28318*j)) <=0.01:
        y3 = float('-inf')
    else:
        pass

##判断输入角度是否无限接近于余切函数的非定义域附近
for j in range(0,n):
    if 0<= (3.14159*j-x)<=0.01:
        y4 = float('-inf')
    elif 0<=(x - 3.14159*j)<=0.01:
        y4 = float('inf')
    else:
        pass

#均保留六位小数
print("正弦值和相应函数计算值分别为：%.6f，%.6f"%(y1,m.sin(x)))
print("余弦值和相应函数计算值分别为：%.6f，%.6f"%(y2,m.cos(x)))
print("正切值和相应函数计算值分别为：%.6f，%.6f"%(y3,m.tan(x)))
print("余切值和相应函数计算值分别为：%.6f，%.6f"%(y4,m.cos(x)/m.sin(x)))

#input()
