#	--coding:utf-8--
#	�������Ԫ��

text = ['mushrooms','green peppers','extra cheese']	#extra cheese:���ң�֥ʿ��
for dosing in text:
	if dosing == 'green peppers':
		print('Sorry,we are out of green peppers right now.')
	else:
		print('Addind  '+ dosing)

print('end')

#	ȷ���б��ǿ�
text = []
if text:
	for dosing in text:
		print('Adding '+ dosing)
	print('end')
else:
	print("It's null")

print('-------------------------------------------')	
#	ʹ�ö���б�		#pepperoni:������㳦
text = ['mushrooms','olives','pepperoni','green peppers','pineapple','extra cheese']	#�ṩ���б�
check = ['mushrooms','french fries','extra cheese']										#��Ҫ���б�
#	ѭ������Ҫ�б��е�ÿһ�ȥ�ж��ṩ�б����Ƿ��ṩ
for dosing in check:
	if dosing in text:
		print("Adding " + dosing)
	else:
		print("Sorry, we don't have " + dosing)
print('end')

#	5.5 ����if����ʽ
#	PEP 8 �ṩ��Ψһ�����ǣ�������==,>=��<=�ȱȽ���������߸����һ���ո�
#	���磺 if age >= 18
