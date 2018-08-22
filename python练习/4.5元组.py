#  	coding:utf-8--
#	元组：Python将不能修改的值称为不可变的，而不可变的列表被称为元组
#	dimensions n.规模，大小； 【网络】：尺寸； 
dimensions = (200,50)
print(dimensions[0])
# dimendsions[0]=120	#会报错，不能给元组的元素赋值

#	遍历元组的值
for aaa in dimensions:
	print(aaa)
	
#	修改元组变量
dimensions = (100,200,300)
print(dimensions)
for ddd in dimensions:
	print(ddd)

#	这算哪门子修改嘛，明明就是重新赋值
