#	--coding:utf-8--
#	if�����forѭ����ͬ���������ͨ���ˣ���ִ��if���������������Ĵ����У����򽫺�������
age = 19
if age >= 18:
	print('You are old enough to vote')
#	if-else ���
age = 17
if age >= 18:
	print("ok")
else:
	print('You are too young')
#	if-elif-else �ṹ
age = 12
if age <4:			
	price = 0
elif age < 18:
	price = 5
elif age >65:			#	��ͬ�� age < 65:						
	price = 6			#	price = 10
else:					#	else:
	price = 10			#	price = 5
print('Your admission cost is $ '+str(price)+'.')	
# ��java�е�if-else if -else һ�������������һ���������㣬�����ж���������

#	ʡ��else����飺
age = 12
if age <4:			
	price = 0
elif age < 18:
	price = 5
elif age < 65:							
	price = 10			
elif age >= 65:					
	price = 6			
#	���棬��ȫ�о����������ĸ������ˡ����Ǿ�����else������ȷ������жϵĽ���

#	���Զ������
#	�������ᵽ��һ��,if-elif-else �������ڵ�һ���������ʱ������ж����������������������д��

request = ['aa','bb','cc']
if 'aa' in request:
	print('good')
if 'bb' in request:
	print('well')
if 'ee' in request:
	print('wrong')
print('end')
