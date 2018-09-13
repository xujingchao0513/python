#  --coding:utf-8--

#	列表排序	sort()  永久改变列表元素排序

text = ['I','want','to','HangZhou','aa']
text1 = ['i','want','to','hangzhou']
print(text)
text.sort()
text1.sort()
print(text)
print(text1)
# 经测试，发现大写字母总是在前面，然后在排序小写字母，（怀疑用的AscII编码值）

# 对sort()方法，添加reverse=true，可以实现反序排列
text = ['I','want','to','HangZhou']
text.sort(reverse=True)  #Ture 首字母大写，写成ture会报错
print(text)
#	分割线
print("--------------------------------")

# 使用sorted()方法可以将列表进行临时排序
text = ['I','want','to','HangZhou']
print(sorted(text))
print(text)

List = [('english',9),('math',90)]
print(sorted(List, key=lambda s: s[1], reverse=True))

print(sorted(List,  reverse=True))
