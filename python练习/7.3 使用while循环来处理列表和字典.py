#	--coding:utf-8--

#	创建一个待验证的用户列表和存储已验证用户的空列表
#	在列表之间异动元素
unconfirmed_users = ['AAA','BBB','CCC']
confirmed_users=[]

while unconfirmed_users:
	#从未验证的列表中取最后一个复制给已验证列表
	confirmed_user = unconfirmed_users.pop()
	print("Verifyinguser: " + confirmed_user.title())
	confirmed_users.append(confirmed_user)
#	显示所有验证用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#	删除包含特定值的所有列表元素
pets =['aaa','bbb','aaa','ccc','aaa','ddd','aa','fff','aa','eee','ggg']
print(pets)

while 'aa' in pets:
	pets.remove('aa')	#精确匹配,只去掉'aa',对'aaa'没有影响
	
print(pets)

#	使用用户输入来填充字典
responses = {}	#定义字典
polling_active = True

while polling_active:
	name = input("\nWhis your name?")
	response = input("\nWhich mountain would you like to climb someday?")
	responses[name] = response	#将答案存在字典中
	repeat = input("would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False
#结束
print("\n ---Poll Results ---")
for name,response in responses.items():
	print(name + " would like to climb " + response + ".")
