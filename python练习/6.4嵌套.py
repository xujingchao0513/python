#	--coding:utf-8--
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
#	�ָ���
print('-------------*******---------------')	
#	����һ�����ڴ洢�Ŀ��б�
aliens= []
#	����30����ɫ������
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

#	��ʾǰ�����ɫ������
for alien in aliens[:5]:
	print(alien)
print('....')
#	��ʾ�����˶��ٸ�������
print("Total number of aliens: " + str(len(aliens)))
#	ʹ��forѭ����ǰ�������������޸�
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'dedium'
		alien['points'] = 10
#	��ʾǰ���������
for alien in aliens[0:5]:
	print(alien)
print('...')
#	�ָ���
print('-------------*******---------------')	
#	�ֵ��н�һ�����������ֵ��ʱ��,����ʹ��һ��forѭ��������
#	�Գ�����иĽ�,���һ����ֻ��Ӧһ��ֵ,��ô�������if�ж�
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
#	�ָ���
print('-------------*******---------------')			
#	���ֵ��д洢�ֵ�
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
