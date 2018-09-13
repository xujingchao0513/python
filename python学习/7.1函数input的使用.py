#	--coding:utf-8--
#	函数input()可以让程序暂定运行,等待用户输入一些文本,获取用户输入后,
#	python将其存储在一个变量中
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#	可以输入汉字
#	Sublime Text 是一个编辑器

prompt = 'If you tell us who you are ,we can personalize the  messages see.'
prompt += '\n what is your first name ?'
name = input(prompt)
print("\n Hello, "+name+"!")

#	使用int()来获取数值的输入
age = input("How old are you?")
age = int(age)
print(age >= 18)
'''
#	求模运算符
print(4%3)
print(5%3)

#	Python 2.7 应该使用函数raw_input()来提示用户输入
