# --coding:utf-8--
# 运算符
# 加减乘除  （+）（-）（*）（/）
print(10-2)
print(2+6)
print(2*4)
print(8/1)
# 乘方 （**）
print(2**10)		
# str()   将内容转换成 string
age = 23		#错误，无法识别23是int还是"2"+"3"
# message = "Happpy "  + age + "rd Birthday"
# print (message)
message1 = "Happpy "  + str(age) + "rd Birthday"
print (message1)

#  在python 2中  3/2 会取整数值与python 3不同
print(3/2)
# python 2 中的写法
print(3.0/2)
print(3/2.0)
print(3.00000/2)

# 浮点数使用时，结果包含的小数位可能不是固定的
print(3*0.1)
