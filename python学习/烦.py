#	--coding:utf-8--
from requests_html import HTMLSession
import time
import urllib2   
import re  
session = HTMLSession()
url = 'http://www.finalnoob.com'
#url = 'http://exitscam.me/play'
#url = 'http://www.win4000.com/zt/xinggan.html'
'''
def get_real_url(url,try_count = 1):
	if try_count > 3:
		return url
	try:
		rs = requests.get(url,headers=http_headers,timeout=10)
		if rs.status_code > 400:
			return get_real_url(url,try_count+1)
		return rs.url
	except:
		return get_real_url(url, try_count + 1)
url= get_real_url(url)
'''

r = session.get(url)
print(url)
print('------------------------------------------------------------')
print(r.html.text)
print('------------------------------------------------------------')
print(r.html.links)
print('------------------------------------------------------------')
print(r.html.absolute_links)
print('------------------------------------------------------------')

#sel = 'body > module-template > div > div.container > p.h4 '
#my_carousel = r.html.find(sel)
#print(my_carousel)
print('--------------------result----------------------------------------')
hour_1 = r.html.find('.hours', first=True)
hour = hour_1.find('span',class_='hours').get_text()
minutes = r.html.find('.minutes', first=True)
seconds = r.html.find('.tile tile-seconds', first=True)

#print(my_carousel.find('p:nth-child(2)', first=True))
print(hour)
print('------------------------------------------------------------')
print(minutes)
print('------------------------------------------------------------')
print(seconds)
print('------------------------------------------------------------')

#	将抓取Result output到txt文本中
'''
filename = 'output.txt'
with open(filename,'w') as file_object:
	file_object.write(r.html.text)

'''
