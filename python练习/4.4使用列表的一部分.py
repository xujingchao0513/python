#  --coding:utf-8--

#��Ƭ
players = ['aa','bb','cc','dd','ee']
print(players[1:3])
print(players[:3])	#��ָ����һ�����������б�ͷ��ʼ��ȡ
print(players[3:])	#ͬ���ģ���ָ����β����ȡ���б�ĩβ
print(players[-3:])	#ʹ�����ַ�������������Nλ��ֵ

#	������Ƭ
#	����б�ǰ3����ֵ
for player in players[:3]:
	print(player.title())
#	�����б�
text = players[:]
print(text)	

hello = players[1:2]
print(hello)
print('//////////////////////////////////////')
###	�ر�ע��
#	���ʹ�ã�  text = players ����д��ȷʵ���Եõ�ͬ����Ч��
#	��������� text,players�е��κ�һ�����޸ĵĻ����ͻᵼ�£���һ�����в����仯
#	��ָ��ָ��ͬһ��ַ����
#	ʵ����
text = players
text.append('what?')
print(players)


players.append('wrong')
print(text)
print(players)
#ϰ��
for out in players:
	print(out)



