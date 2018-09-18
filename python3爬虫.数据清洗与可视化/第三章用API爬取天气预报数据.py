# -*- coding: utf-8 -*-
#   3.1注册免费API爬取和阅读技术文档
#   注册地址:http://console.heweather.com
#   文档地址:https://www.heweather.com/documents/api/v5/url
#   建议第一次阅读说明文档时,最好按次序阅读.

#   3.2获取API数据
import requests
url = 'https://cdn.heweather.com/china-city-list.txt '
strhtml = requests.get(url)
strhtml.encoding='utf8'
data = strhtml.text
'''
#   原代码可能因为网站信息变动,导致报错,使用的为改正后的代码
data1 = data.split('\r')
print(data1)
for i in  range(3):
    data1.remove(data1[0])
for item in data1:
    print(item[0:11])
'''
#print(data)
data1 = data.split('\n')
print(data1)
for i in  range(6):
    data1.remove(data1[0])
for item in data1:
    print(item[1:11])

