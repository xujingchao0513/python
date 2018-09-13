
from requests_html import HTMLSession

session = HTMLSession()
url = 'http://exitscam.me/api/time'
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

print('------------------------------------------------------------')
print(r.html.text)
print('------------------------------------------------------------')
print(r.html.links)
print('------------------------------------------------------------')
print(r.html.absolute_links)
print('------------------------------------------------------------')

sel = 'body > module-template > div > div.container > p.h4 '
my_carousel = r.html.find(sel)
print(my_carousel)
print('------------------------------------------------------------')
#my_carousel = r.html.find('#main-wrapper', first=True)
#print(my_carousel.find('p:nth-child(2)', first=True))



