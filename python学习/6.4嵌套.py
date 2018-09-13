#	--coding:utf-8--
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
#	分割线
print('-------------*******---------------')	
#	创建一个用于存储的空列表
aliens= []
#	创建30个绿色外星人
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

#	显示前五的绿色外星人
for alien in aliens[:5]:
	print(alien)
print('....')
#	显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
#	使用for循环将前三个外星人做修改
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'dedium'
		alien['points'] = 10
#	显示前五个外星人
for alien in aliens[0:5]:
	print(alien)
print('...')
#	分割线
print('-------------*******---------------')	
#	字典中将一个键关联多个值的时候,可以使用一个for循环来遍历
#	对程序进行改进,如果一个键只对应一个值,那么可以添加if判断
favorite_languages = {
'jen':['python','ruby'],
'sarah':['c'],
'edward':['ruby','go'],
'phil':['python','haskell'],
}
for name, languages in favorite_languages.items():
	if len(languages)>1:
		print("\n" + name.title() + "'s favorite languages are:")
	else:
		print("\n" + name.title() + "'s favorite language is:")
	
	for language in languages:
		print("\t" + language.title())
#	分割线
print('-------------*******---------------')			
#	在字典中存储字典
users = {
'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
		},
'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},
}
for username ,user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
