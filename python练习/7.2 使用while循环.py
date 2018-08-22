#	--coding:utf-8--
#	使用while循环
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number +=1

#	使用while循环让程序在用户愿意时不断运行,定义一个退出值
'''
prompt = "\n Tell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)
	
	if message != 'quit':
		print(message)

#	使用标志,用以在多个方法中有一个变量控制程序是否继续执行
prompt = "\n Tell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program."
active = True
message = ""
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)
#	使用break退出循环
active = True
message = ""
while active:
	message = input(prompt)
	
	if message == 'quit':
		break
	else:
		print(message)
'''
#	在循环中使用continue,可以返回循环开头,病根据条件测试结果决定循环是否继续
print("------------------------分割线-----------------------------")
current_num = 0
while current_num <  10:
	current_num += 1
	if current_num %2 ==0:
		continue
	print(current_num)
#	避免无线循环--注意对while条件的控制
