#	--coding:utf-8--
#	���庯��
def greet_user():
	print('hello')
greet_user()
#	���ݲ���
def greet_user(name):
	print('hello  ' + name.title())
greet_user('Alex')
#	name���β�,'Alex'��ʵ��
print("-------------------------------------------")

#	���ú���ʱ,���뽫ÿ��ʵ�ζ����������������е�һ���β�,��򵥵Ĺ�����ʽ��ʵ�ε�˳��
#	���ֹ�����ʽ����Ϊ:λ��ʵ��
def describe_pet(animal_type,pet_name):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
	
describe_pet("hamster","harry")
describe_pet("dog","willie")
print("-------------------------------------------")
#	�ؼ���ʵ��
#	�ؼ���ʵ���Ǵ��ݸ�����������-ֵ��
def describe_pet(animal_type,pet_name):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
describe_pet(animal_type="dog",pet_name="willie")
describe_pet(pet_name="harry",animal_type="hamster")
print("-------------------------------------------")
#	Ĭ��ֵ
def describe_pet(animal_type="dog",pet_name="willie"):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
describe_pet(animal_type="pig",pet_name="YAYA")
print("-------------------------------------------")
#	��Ч�ĺ�������
#	��Ĭ��ֵ,����ֵʱʹ��Ĭ��ֵ
def describe_pet(pet_name,animal_type="dog"):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
describe_pet("YAYA")	
#describe_pet(animal_type="pig","YAYA")#����д����
describe_pet("YAYA",animal_type="pig")
#	����
#def describe_pet(animal_type="dog",pet_name):#����д�ᱨ��

