# -*- coding: utf-8 -*-

#2.1关于爬虫的合法性
'''
    几乎每一个网站都有一个名为robots.txt的文档,也有部分没有,对于没有设定robots.txt的网站可以通过网络爬虫
获取没有口令加密的数据,也就是该网站所有页面数据都可以爬取.如果网站有robots.txt,则要判断是否有禁止访客获取的
数据.
    以淘宝网为例:www.taobao.com/robots.txt,淘宝网允许部分爬虫访问他的部分路径,而对于没有允许的用户,则全部
    禁止爬取,代码如下:
    ----------------------------------------
    User-agent:  Baiduspider
    Allow:  /article
    Allow:  /oshtml
    Allow:  /ershou
    Disallow:  /product/
    Disallow:  /

    User-Agent:  Googlebot
    Allow:  /article
    Allow:  /oshtml
    Allow:  /product
    Allow:  /spu
    Allow:  /dianpu
    Allow:  /oversea
    Allow:  /list
    Allow:  /ershou
    Disallow:  /

    User-agent:  Bingbot
    Allow:  /article
    Allow:  /oshtml
    Allow:  /product
    Allow:  /spu
    Allow:  /dianpu
    Allow:  /oversea
    Allow:  /list
    Allow:  /ershou
    Disallow:  /

    User-Agent:  360Spider
    Allow:  /article
    Allow:  /oshtml
    Allow:  /ershou
    Disallow:  /

    User-Agent:  Yisouspider
    Allow:  /article
    Allow:  /oshtml
    Allow:  /ershou
    Disallow:  /

    User-Agent:  Sogouspider
    Allow:  /article
    Allow:  /oshtml
    Allow:  /product
    Allow:  /ershou
    Disallow:  /

    User-Agent:  Yahoo!  Slurp
    Allow:  /product
    Allow:  /spu
    Allow:  /dianpu
    Allow:  /oversea
    Allow:  /list
    Allow:  /ershou
    Disallow:  /

    User-Agent: *
    disallow: /

    ------------------------------------
    User-Agent: *
    disallow: /
    这一句的意思是除了前面指定的爬虫外,不允许其他爬虫爬取任何数据.
'''

#   2.2 了解网页
#    1.HTML
#    2.CSS
#    3.Jscript
#   略过

#   2.3     使用requests库请求网站
#       2.3.1   安装requests库
#       可以使用PyCharm或者pip install xxx
#       2.3.2   爬虫的基本原理
#       1)网页请求的过程
#       1.Request(请求)
#         没一个展示在用户面前的网页都必须经过这一步,也就是想服务器发送访问请求
#       2.Response(响应)
#         服务器在接收到用户的请求后,会验证请求的有效性,然后向用户(客户端)发送响应的内容,客户端接收服务器响应的内容
#         ,将内容展示出来,就是我们所熟悉的网页请求
#       2)网页请求的方式
#       1.GET:最常见的方式,一般用于获取或者查询资源信息,也是大多数网站使用的方式,响应速度快.
#       2.POST:相比GET方式,多了以表单形式上传参数的功能,因此除查询信息外,还可以修改信息.

#       2.3.3   使用GET方式抓取数据
import requests
url='http://www.cntour.cn/'
strntml = requests.get(url)
print(strntml.text)

#       2.3.4   使用POST方式抓取数据
#       以有道翻译网站为例,通过F12,单击'Network',获取'Headers'中的url
import json
'''
    原网页中方法是translate_o,但是会报错
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
'''
"""
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
Form_data = {
    'i':'我爱',
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1536992178877',
    'sign':'ceae140112028f9b816ea23ae3360968',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult':'false'
}

#请求表单数据
response = requests.post(url,data=Form_data)
#将json格式字符串转字典
content = json.loads(response.text)
#打印翻译后的数据
print(content['translateResult'][0][0]['tgt'])
"""
#   2.4 使用Beautiful Soup 解析网页
#   需要安装bs4,和lxml库,不装lxml库就会使用python默认的解析器.

from bs4 import BeautifulSoup
#   lxml解析网页文档
soup = BeautifulSoup(strntml.text,'lxml')
#   #main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li:nth-child(1) > a
#   因为要获取所有的头条新闻,,所以将li:nth-child(1)中的冒号及后面的部分
#
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(data)

#   2.5清洗和组织数据
#   刚刚只是取得了Html代码,并没有吧数据取出来.
#   用for循环把soup匹配到的多个数据取出来
"""
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')

    }
   print(result)
"""
#   链接在<a>标签的href属性中,提取标签中的href属性用get()方法,在括号中指定要提取的属性数据
#   看到每一个文章链接中都有一个数据id,用正则表达式去这个id
#   在python中调用正则表达式使用re库,不用安装.可以直接调用
import re
#   \d  匹配数字
#   +匹配前一个字符一次或多次
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
        'ID':re.findall('\d+',item.get('href'))
    }
    print(result)
