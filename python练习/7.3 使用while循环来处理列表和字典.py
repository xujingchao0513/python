#	--coding:utf-8--

#	����һ������֤���û��б�ʹ洢����֤�û��Ŀ��б�
#	���б�֮���춯Ԫ��
unconfirmed_users = ['AAA','BBB','CCC']
confirmed_users=[]

while unconfirmed_users:
	#��δ��֤���б���ȡ���һ�����Ƹ�����֤�б�
	confirmed_user = unconfirmed_users.pop()
	print("Verifyinguser: " + confirmed_user.title())
	confirmed_users.append(confirmed_user)
#	��ʾ������֤�û�
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#	ɾ�������ض�ֵ�������б�Ԫ��
pets =['aaa','bbb','aaa','ccc','aaa','ddd','aa','fff','aa','eee','ggg']
print(pets)

while 'aa' in pets:
	pets.remove('aa')	#��ȷƥ��,ֻȥ��'aa',��'aaa'û��Ӱ��
	
print(pets)

#	ʹ���û�����������ֵ�
responses = {}	#�����ֵ�
polling_active = True

while polling_active:
	name = input("\nWhis your name?")
	response = input("\nWhich mountain would you like to climb someday?")
	responses[name] = response	#���𰸴����ֵ���
	repeat = input("would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
#����
print("\n ---Poll Results ---")
for name,response in responses.items():
	print(name + " would like to climb " + response + ".")
