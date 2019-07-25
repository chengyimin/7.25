# 华氏温度转换为摄氏温度

f = int(input("请输入华氏温度："))
c = (f-32)/1.8
print("当前华氏温度对应的摄氏温度为：",c)

# 输入圆的半径，计算其面积

import math
r = int(input("请输入圆的半径："))
s = r**2*math.pi
print("该圆的面积是：",s)


# 输入年份，判断是否为闰

y = int(input("请输入年份："))
if y % 100 == 0:
    if y % 400 == 0:
        print('%d年是闰年'%y)
    else:
        print('%d年不是闰年'%y)
else:
    if y % 4 == 0:
        print('%d年是闰年'%y)
    else:
        print('%d年不是闰年'%y) 