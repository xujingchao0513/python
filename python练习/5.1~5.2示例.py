#	--coding:utf-8--
	
#5.1	ʾ��	
cars = ['audi','bmw','subaru','toyuta']
for car  in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())	

#5.2	��������
#	ÿ��if���ĺ��Ķ���һ��ֵΪTrue��False�ı��ʽ�����ֱ��ʽ����Ϊ����������
car = 'bmw'
car == 'bmw'
aa=(car == 'bmw')	#�²���Խ�����ֵ��ֵ������aa
print(aa)			#����֤��������ȷ

#	��Python�У�����Ƿ����ʱ�����ִ�Сд
aa = 'abc'
aa == 'Abc'
bb = (aa == 'Abc')
print(bb)	#���ΪFalse

#	�����Сд���������Ҵ�Сд�б�Ҫ����ʹ��lower()����
car = 'ABC'
other_car = 'Abc'
aa=car.lower() == other_car.lower()		#�����Բ�������Ҳ��Ӱ��aa��ֵ���о��������׶��Ը���
print(aa)
#	lower()���������޸Ĵ洢��car�е�ֵ
print(car)

#	����Ƿ����
if(car != aa):
	print('Hold the anchovies')		#anchovies n.С���㣻�����Ϊʲô������

#	�Ƚ�����
age = 18
if(age == 18):
	print('true')
if(age != 19):
	print('false')
if(age < 20):
	print('true')

#	���������

#	java/python   &&��and   ||��or
age = 18
age_1 = 20
if(age == 18 and age_1 ==20):
	print("&&")

if(age == 20 or age_1 ==20):
	print("||")

print('----------------------------------')
#	����ض�ֵ�Ƿ�������б���
text = ['aa','bb','cc']
aa = 'aa' in text
bb = 'ee' in text
print(aa)
print(bb)

#	����ض�ֵ�Ƿ񲻺����б���
text = ['aa','bb','cc']
aa = 'ee' not in text
bb = 'aa' not in text
print(aa)
print(bb)

#	�������ʽ
aa = True
bb = False		#ע��,���岼��ֵ����ĸҪ��д
