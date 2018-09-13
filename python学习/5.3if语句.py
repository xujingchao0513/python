#	--coding:utf-8--
#	if语句与for循环相同，如果测试通过了，将执行if语句后面所有缩进的代码行，否则将忽略他们
age = 19
if age >= 18:
	print('You are old enough to vote')
#	if-else 语句
age = 17
if age >= 18:
	print("ok")
else:
	print('You are too young')
#	if-elif-else 结构
age = 12
if age <4:			
	price = 0
elif age < 18:
	price = 5
elif age >65:			#	等同于 age < 65:						
	price = 6			#	price = 10
else:					#	else:
	price = 10			#	price = 5
print('Your admission cost is $ '+str(price)+'.')	
# 与java中的if-else if -else 一样，如果有其中一个条件满足，则不再判断其他条件

#	省略else代码块：
age = 12
if age <4:			
	price = 0
elif age < 18:
	price = 5
elif age < 65:							
	price = 10			
elif age >= 65:					
	price = 6			
#	讲真，完全感觉不出哪里变的更清晰了。倒是觉得有else更容易确定这个判断的结束

#	测试多个条件
#	跟上面提到的一样,if-elif-else 仅适用于单一条件满足的时候，如果有多个条件满足则不能适用这种写法

request = ['aa','bb','cc']
if 'aa' in request:
	print('good')
if 'bb' in request:
	print('well')
if 'ee' in request:
	print('wrong')
print('end')
