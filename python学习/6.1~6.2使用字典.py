#	--coding:utf-8--
#	6.1һ���򵥵��ֵ�
#	���������˵���ɫ�ͷ���
alien = {'color': 'green','point': 5}
#alien = {'color': 'green','point': 5,'color':'blue'}	#�����һ���ֵ������ͬ���ļ�ֵ������ʾ���ļ�ֵ
print(alien['color'])
print(alien['point'])

#	6.2�����ֵ��е�ֵ
alien = {'color': 'green','point': 5}
new_point = alien['point']
print(new_point)

#	��Ӽ���ֵ�� 
alien = {'color': 'green','point': 5}
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

#	����һ�����ֵ�
alien = {}
alien['color'] = 'green'
alien['point'] = 5
print(alien)
#	ʹ���ֵ����洢�û��ṩ�����ݻ��ڱ�д���Զ����ɴ�������ֵ�ԵĴ���ʱ��ͨ���ȶ���һ�����ֵ�

#	�޸��ֵ��е�ֵ
alien = {'color':'green'}
print('The alien is ' + alien['color'])
alien['color'] = 'yellow'
print('The alien is now' + alien['color'])

#	ɾ������ֵ��
#	�����ֵ��в�����Ҫ����Ϣ����ʹ��del��佫��Ӧ�ļ���ֵ�Գ���ɾ����ʹ��del���ʱ������ָ���ֵ�����Ҫɾ���ļ�
alien = {'color': 'green','point': 5}
print(alien)
del alien['point']
print(alien)
#	ɾ���ļ�-ֵ�Ի���Զ��ʧ

#	�����ƶ�����ɵ��ֵ�
favorite_languages = {
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'java'
	}
