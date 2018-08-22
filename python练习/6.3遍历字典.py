#	--coding:utf-8--

user_0 = {
'username':'efermi',
'first':'enrico',
'last':'fermi'
	}
#	遍历字典的键-值对items()
for key,value in user_0.items():
	print("\nKey: " +key)
	print("Value: " + value)
#	分割线
print('-----------------------------------')

favorite_languages = {
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'python',
}

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is "
	+ language.title() + ".")
#	分割线
print('-----------------------------------')	
#	遍历字典中所有的键keys()

for name in favorite_languages.keys():
	print(name.title())
#	分割线
print('-----------------------------------')	
#	遍历字典是,会默认遍历所欲的键,所以keys()可以省略,不建议省略,不直观
for name in favorite_languages:
	print(name.title())
#	分割线
print('-----------------------------------')	
#	方法keys()并非只能用于遍历,实际上它返回一个列表.
friends = ['phil','sarah']
for name in favorite_languages.keys():
	
	if name in friends:
		print(name.title() + 'is my friend')
#	分割线		ps:此处不能适用print(),会截断for循环而报错
#print('-----------------------------------')	
#	根据之前的代码,简化下列代码
#	if 'erin' not in favorite_languages.keys():
#	print('Erin, please take our poll')
	if 'erin' not in name:
		print('Erin, please take our poll')
#	分割线
print('-----------------------------------')	
#	遍历字典包含的值.values(),这种情况是可能存在重复数据的
for language in favorite_languages.values():
	print(language.title())
#	分割线
print('-----------------------------------')
#	去掉重复的值,set()
for language in set(favorite_languages.values()):
	print(language.title())	
