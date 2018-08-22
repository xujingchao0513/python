# --coding:utf-8--

#修改，添加，插入，删除元素  
text = ['aa','bb','cc']
print(text)
#插入数据
text[0] = 'hello'
print(text)
text[2] = 'good'
print(text)
#在末尾添加数据
text1 = ['aa','bb','cc']
text1.append('dd')
print(text1)
#向空列表添加数据
text2 = []
text2.append('Hello')
text2.append('Alex')
text2.append('I  Love You')
print(text2)
#在指定位置插入数据
text2 = ['aa','bb','cc']
text2.insert(0,'hello')
print(text2)
#删除指定位置的数据
text5 = ['aa','bb','cc']
del text5[1]		#删除第二个
print(text5)
print('-------------------')
#pop的使用
text=['aa','bb','cc']
print(text)
text_pop = text.pop()
print(text)
print(text_pop)
text=['aa','bb','cc']
text_pop = text.pop(1)
print(text)
print(text_pop)
#pop 与 del 的区别
# 删除元素后不再使用的用del，删除后使用pop
print('-------------------')
# 根据元素删除列表中的值
text=['aa','bb','cc']
text.remove('bb')
print(text)

