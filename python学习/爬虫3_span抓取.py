#	--coding:utf-8--
from urllib import request
import chardet


charset = {}
if __name__ == "__main__":
    response = request.urlopen("http://www.finalnoob.com")
    html = response.read()
#�����ͨ���鿴F12�еı���ȥ�鿴��ǰҳ��ı���
#    html = html.decode("utf-8")
#��ȻҲ����ʹ�õ�������ȥ��ȡҳ��ı����ʽ

	
    charset = chardet.detect(html)
    print(charset)
#    ����Ľ��������ֱ�Ӿ��ܹ�ʹ��,������ʽ����:
#   {'encoding': 'utf-8', 'confidence': 0.99, 'language':  ' ' }
#   ���������Ҫʵ���Զ���ȡ�Ļ�,����Ҫ�Է��ؽ�����н�ȡ(�ֵ�)
abd=''
if(charset!=''):
	abd = charset['encoding']
print(abd)
html = html.decode(abd)
print(html)
