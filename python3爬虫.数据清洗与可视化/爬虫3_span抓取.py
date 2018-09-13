#	--coding:utf-8--
from urllib import request
import chardet


charset = {}
if __name__ == "__main__":
    response = request.urlopen("http://www.finalnoob.com")
    html = response.read()
#你可以通过查看F12中的编码去查看当前页面的编码
#    html = html.decode("utf-8")
#当然也可以使用第三发库去获取页面的编码格式

	
    charset = chardet.detect(html)
    print(charset)
#    输出的结果并不是直接就能够使用,样例形式如下:
#   {'encoding': 'utf-8', 'confidence': 0.99, 'language':  ' ' }
#   所以如果想要实现自动获取的话,还需要对返回结果进行截取(字典)
abd=''
if(charset!=''):
	abd = charset['encoding']
print(abd)
html = html.decode(abd)
print(html)
