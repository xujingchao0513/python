#  --coding:utf-8--

#切片
players = ['aa','bb','cc','dd','ee']
print(players[1:3])
print(players[:3])	#不指定第一个索引，从列表开头开始提取
print(players[3:])	#同样的，不指定结尾则提取到列表末尾
print(players[-3:])	#使用这种方法可以输出最后N位的值

#	遍历切片
#	输出列表前3个数值
for player in players[:3]:
	print(player.title())
#	复制列表
text = players[:]
print(text)	

hello = players[1:2]
print(hello)
print('//////////////////////////////////////')
###	特别注意
#	如果使用：  text = players 这种写法确实可以得到同样的效果
#	但是如果对 text,players中的任何一个做修改的话，就会导致，另一个数列产生变化
#	与指针指向同一地址类似
#	实例：
text = players
text.append('what?')
print(players)


players.append('wrong')
print(text)
print(players)
#习题
for out in players:
	print(out)



