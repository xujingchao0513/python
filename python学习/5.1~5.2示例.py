#	--coding:utf-8--
	
#5.1	示例	
cars = ['audi','bmw','subaru','toyuta']
for car  in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())	

#5.2	条件测试
#	每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为：条件测试
car = 'bmw'
car == 'bmw'
aa=(car == 'bmw')	#猜测可以将布尔值赋值给变量aa
print(aa)			#经验证，猜想正确

#	在Python中，检查是否相等时，区分大小写
aa = 'abc'
aa == 'Abc'
bb = (aa == 'Abc')
print(bb)	#结果为False

#	如果大小写不做区分且大小写有必要可是使用lower()方法
car = 'ABC'
other_car = 'Abc'
aa=car.lower() == other_car.lower()		#经测试不加括号也不影响aa的值，感觉加括号易读性更好
print(aa)
#	lower()方法不会修改存储在car中的值
print(car)

#	检查是否不相等
if(car != aa):
	print('Hold the anchovies')		#anchovies n.小银鱼；不清楚为什么输出这个

#	比较数字
age = 18
if(age == 18):
	print('true')
if(age != 19):
	print('false')
if(age < 20):
	print('true')

#	检查多个条件

#	java/python   &&：and   ||：or
age = 18
age_1 = 20
if(age == 18 and age_1 ==20):
	print("&&")

if(age == 20 or age_1 ==20):
	print("||")

print('----------------------------------')
#	检查特定值是否包含在列表中
text = ['aa','bb','cc']
aa = 'aa' in text
bb = 'ee' in text
print(aa)
print(bb)

#	检查特定值是否不含在列表中
text = ['aa','bb','cc']
aa = 'ee' not in text
bb = 'aa' not in text
print(aa)
print(bb)

#	布尔表达式
aa = True
bb = False		#注意,定义布尔值首字母要大写
