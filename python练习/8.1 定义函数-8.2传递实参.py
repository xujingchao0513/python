#	--coding:utf-8--
#	定义函数
def greet_user():
	print('hello')
greet_user()
#	传递参数
def greet_user(name):
	print('hello  ' + name.title())
greet_user('Alex')
#	name是形参,'Alex'是实参
print("-------------------------------------------")

#	调用函数时,必须将每个实参都关联到函数定义中的一个形参,最简单的关联方式是实参的顺序
#	这种关联方式被称为:位置实参
def describe_pet(animal_type,pet_name):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
	
describe_pet("hamster","harry")
describe_pet("dog","willie")
print("-------------------------------------------")
#	关键字实参
#	关键字实参是传递给函数的名称-值对
def describe_pet(animal_type,pet_name):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
describe_pet(animal_type="dog",pet_name="willie")
describe_pet(pet_name="harry",animal_type="hamster")
print("-------------------------------------------")
#	默认值
def describe_pet(animal_type="dog",pet_name="willie"):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
describe_pet(animal_type="pig",pet_name="YAYA")
print("-------------------------------------------")
#	等效的函数调用
#	有默认值,不赋值时使用默认值
def describe_pet(pet_name,animal_type="dog"):
	'''show the animal's information'''
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()+".")
describe_pet("YAYA")	
#describe_pet(animal_type="pig","YAYA")#这样写不行
describe_pet("YAYA",animal_type="pig")
#	补充
#def describe_pet(animal_type="dog",pet_name):#这样写会报错

