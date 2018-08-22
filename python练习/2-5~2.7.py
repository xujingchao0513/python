# --coding:utf-8--

text1 = " Albert Einstein once said, " 
text2 = " A person  who never made a mistake never tried anything new.  "
text3 = '"'
print (text1 + text3 +  text2 +text3)

text4 = " AA "
text5 = " \n\tbb "
text6 = " \t\ncc "

print (text4 + text5 + text6)



# \t 	添加制表符，也就是tab键的作用
# \n 	换行符
# \n\t 	换行加制表符
# \t\n 	只有换行起了作用

text7 = "  去空格  "
print (text7.rstrip())
print (text7.lstrip())
print (text7.strip())

# rstrip() 	去掉字符串后面的空格
# lstrip()	去掉字符串前面的空格
# strip() 	去掉字符串前后的空格  相当于java中的.trim();

# python 与 js类似，可以分为"",'',两种形式去定义变量
