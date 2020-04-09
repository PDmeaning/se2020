def sanjiao(a):
    #转化为弧度制
    x = a*3.14/180
    #正弦函数级数展开
    y1 = x - (x**3/6)
    #余弦函数
    y2 = 1-x*x/2
    #正切函数
    y3 = x + x**3/6 + 2**5/15
    #余切函数
    y4 = 1/x - x/3 - x**3/45
    return y1,y2,y3,y4

#输入角度
i = float(input('请输入角度(角度)：'))
y1,y2,y3,y4 = sanjiao(i)
#均保留三位小数
print("正弦值为：",'%.3f'%y1)
print("余弦值为：",'%.3f'%y2)
print("正切值为：",'%.3f'%y3)
print("余切值为：",'%.3f'%y4)

input()