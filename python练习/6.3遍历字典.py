#	--coding:utf-8--

user_0 = {
'username':'efermi',
'first':'enrico',
'last':'fermi'
	}
#	�����ֵ�ļ�-ֵ��items()
for key,value in user_0.items():
	print("\nKey: " +key)
	print("Value: " + value)
#	�ָ���
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
#	�ָ���
print('-----------------------------------')	
#	�����ֵ������еļ�keys()

for name in favorite_languages.keys():
	print(name.title())
#	�ָ���
print('-----------------------------------')	
#	�����ֵ���,��Ĭ�ϱ��������ļ�,����keys()����ʡ��,������ʡ��,��ֱ��
for name in favorite_languages:
	print(name.title())
#	�ָ���
print('-----------------------------------')	
#	����keys()����ֻ�����ڱ���,ʵ����������һ���б�.
friends = ['phil','sarah']
for name in favorite_languages.keys():
	
	if name in friends:
		print(name.title() + 'is my friend')
#	�ָ���		ps:�˴���������print(),��ض�forѭ��������
#print('-----------------------------------')	
#	����֮ǰ�Ĵ���,�����д���
#	if 'erin' not in favorite_languages.keys():
#	print('Erin, please take our poll')
	if 'erin' not in name:
		print('Erin, please take our poll')
#	�ָ���
print('-----------------------------------')	
#	�����ֵ������ֵ.values(),��������ǿ��ܴ����ظ����ݵ�
for language in favorite_languages.values():
	print(language.title())
#	�ָ���
print('-----------------------------------')
#	ȥ���ظ���ֵ,set()
for language in set(favorite_languages.values()):
	print(language.title())	
