# 字符串

a = "abc"
b = '你好 世界！'
print(a,b)

# type函数，查看变量类型
# print(type(a),type(b))

a = 0b11
b = 0xfe
c = 3.1415926
print(a,b,c)
print(type(a),type(b),type(c))


# 进制之间转换 bin()返回字符串类型
c = 15
#c = bin(c)
#c = hex(c)
c = oct(c)
print(c,type(c))

#将 只含数字的字符串转换成对应的十进制的数字 int()
d = "10"
d = int(d)
print(d,type(d))

e = "10"
e = int(e,16) #将十六进制的10转换成十进制赋值给e
print(e,type(e))

#取整
f = 2.71828
f = int(f)
print(f,type(f))

input_data = input("请输入一个数字：")
# input_data = int(input_data)#取整
print(input_data,type(input_data))

# 输入一个二进制数字，然后将其转换成十进制，打印其值和类型
a = input("请输入一个二进制数字：")
a = int(a,2)
print(a,type(a))



#输入一个十进制数字，然后将其转换成二进制加上5，
#再转换成十进制，打印出来它的值和类型
a = input("请输入一个十进制数字：")
a = int(a,10)   #将输入的字符串转换成整型
d = bin(a)      #将整型的十进制转换成二进制
c = a+5         #将整型的十进制+5
print(c,type(c))#打印结果的值和类型


#布尔类型
ABC = True
abc = False
print(ABC,abc,type(ABC),type(abc))
