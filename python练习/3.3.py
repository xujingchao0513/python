#  --coding:utf-8--

#	�б�����	sort()  ���øı��б�Ԫ������

text = ['I','want','to','HangZhou','aa']
text1 = ['i','want','to','hangzhou']
print(text)
text.sort()
text1.sort()
print(text)
print(text1)
# �����ԣ����ִ�д��ĸ������ǰ�棬Ȼ��������Сд��ĸ���������õ�AscII����ֵ��

# ��sort()���������reverse=true������ʵ�ַ�������
text = ['I','want','to','HangZhou']
text.sort(reverse=True)  #Ture ����ĸ��д��д��ture�ᱨ��
print(text)
#	�ָ���
print("--------------------------------")

# ʹ��sorted()�������Խ��б������ʱ����
text = ['I','want','to','HangZhou']
print(sorted(text))
print(text)

List = [('english',9),('math',90)]
print(sorted(List, key=lambda s: s[1], reverse=True))

print(sorted(List,  reverse=True))
