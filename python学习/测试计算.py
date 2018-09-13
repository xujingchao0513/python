
#	--coding:utf-8--
message = input("Tell me something, and I will repeat it back to you: ")
#	½ØÈ¡Ìæ»»'+'
text_1=message.split('+')
#print(text_1)
string_text=''
for dosing in text_1:
	string_text+=dosing+'+'
string_text=string_text[:-1]
#print(string_text)
string_text_2=''
text_2=string_text.split('*')
for dosing in text_2:
	string_text_2+=dosing+'*'
string_text_2=string_text_2[:-1]
print(string_text)
