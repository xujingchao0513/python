# --coding:utf-8--

#range(1,5)能生成一系列数字，秉承左包右不包的原则
for value in range(1,5):
	print(value)

print('------------------------')
#list.range(x,y)生成一个列表-
numbers = list(range(1,6))
print(numbers)

#range()函数可以指定步长，例打印1~10内的偶数
num = list(range(2,11,2))
print(num)

#求1~10的平方，放入列表中显示
squares = []
for value in range(1,11):
	squate = value**2
	squares.append(squate)
	
print(squares)

#对数列 执行简单的统计计算
digits = [1,2,3,5,6,7,8,9,11]
num = min(digits)
print(num)
num = max(digits)
print(num)
num = sum(digits)
print(num)
print('--------------------------------')

# 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)
# 立方
num = [int**3 for int in range(1,11)]
print(num)
