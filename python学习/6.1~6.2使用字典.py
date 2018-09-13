#	--coding:utf-8--
#	6.1一个简单的字典
#	设置外星人的颜色和分数
alien = {'color': 'green','point': 5}
#alien = {'color': 'green','point': 5,'color':'blue'}	#如果在一个字典里添加同样的键值，会显示最后的键值
print(alien['color'])
print(alien['point'])

#	6.2访问字典中的值
alien = {'color': 'green','point': 5}
new_point = alien['point']
print(new_point)

#	添加键—值对 
alien = {'color': 'green','point': 5}
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

#	创建一个空字典
alien = {}
alien['color'] = 'green'
alien['point'] = 5
print(alien)
#	使用字典来存储用户提供的数据或在编写能自动生成大量键—值对的代码时，通常先定义一个空字典

#	修改字典中的值
alien = {'color':'green'}
print('The alien is ' + alien['color'])
alien['color'] = 'yellow'
print('The alien is now' + alien['color'])

#	删除键—值对
#	对于字典中不再需要的信息，可使用del语句将相应的键—值对彻底删除，使用del语句时，必须指定字典名和要删除的键
alien = {'color': 'green','point': 5}
print(alien)
del alien['point']
print(alien)
#	删除的键-值对会永远消失

#	由类似对象组成的字典
favorite_languages = {
'jen':'python',
'sarah':'c',
'edward':'ruby',
'phil':'java'
	}
