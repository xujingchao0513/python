# --coding:utf-8--

#range(1,5)������һϵ�����֣���������Ҳ�����ԭ��
for value in range(1,5):
	print(value)

print('------------------------')
#list.range(x,y)����һ���б�-
numbers = list(range(1,6))
print(numbers)

#range()��������ָ������������ӡ1~10�ڵ�ż��
num = list(range(2,11,2))
print(num)

#��1~10��ƽ���������б�����ʾ
squares = []
for value in range(1,11):
	squate = value**2
	squares.append(squate)
	
print(squares)

#������ ִ�м򵥵�ͳ�Ƽ���
digits = [1,2,3,5,6,7,8,9,11]
num = min(digits)
print(num)
num = max(digits)
print(num)
num = sum(digits)
print(num)
print('--------------------------------')

# �б����
squares = [value**2 for value in range(1,11)]
print(squares)
# ����
num = [int**3 for int in range(1,11)]
print(num)
