#	--coding:utf-8--
#	检查特殊元素

text = ['mushrooms','green peppers','extra cheese']	#extra cheese:奶酪？芝士？
for dosing in text:
	if dosing == 'green peppers':
		print('Sorry,we are out of green peppers right now.')
	else:
		print('Addind  '+ dosing)

print('end')

#	确定列表不是空
text = []
if text:
	for dosing in text:
		print('Adding '+ dosing)
	print('end')
else:
	print("It's null")

print('-------------------------------------------')	
#	使用多个列表		#pepperoni:意大利香肠
text = ['mushrooms','olives','pepperoni','green peppers','pineapple','extra cheese']	#提供的列表
check = ['mushrooms','french fries','extra cheese']										#需要的列表
#	循环出需要列表中的每一项，去判断提供列表中是否提供
for dosing in check:
	if dosing in text:
		print("Adding " + dosing)
	else:
		print("Sorry, we don't have " + dosing)
print('end')

#	5.5 设置if语句格式
#	PEP 8 提供的唯一建议是，在诸如==,>=和<=等比较运算符两边各添加一个空格，
#	例如： if age >= 18
