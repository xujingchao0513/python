# --coding:utf-8--

#�޸ģ���ӣ����룬ɾ��Ԫ��  
text = ['aa','bb','cc']
print(text)
#��������
text[0] = 'hello'
print(text)
text[2] = 'good'
print(text)
#��ĩβ�������
text1 = ['aa','bb','cc']
text1.append('dd')
print(text1)
#����б��������
text2 = []
text2.append('Hello')
text2.append('Alex')
text2.append('I  Love You')
print(text2)
#��ָ��λ�ò�������
text2 = ['aa','bb','cc']
text2.insert(0,'hello')
print(text2)
#ɾ��ָ��λ�õ�����
text5 = ['aa','bb','cc']
del text5[1]		#ɾ���ڶ���
print(text5)
print('-------------------')
#pop��ʹ��
text=['aa','bb','cc']
print(text)
text_pop = text.pop()
print(text)
print(text_pop)
text=['aa','bb','cc']
text_pop = text.pop(1)
print(text)
print(text_pop)
#pop �� del ������
# ɾ��Ԫ�غ���ʹ�õ���del��ɾ����ʹ��pop
print('-------------------')
# ����Ԫ��ɾ���б��е�ֵ
text=['aa','bb','cc']
text.remove('bb')
print(text)

