# -*- coding: utf-8 -*-
#   3.1注册免费API爬取和阅读技术文档
#   注册地址:http://console.heweather.com
#   文档地址:https://www.heweather.com/documents/api/v5/url
#   建议第一次阅读说明文档时,最好按次序阅读.

#   3.2获取API数据
import requests
import time
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
    print(item[2:13])
#   数据是以JSON的格式返回的,没一个城市/地区都是
#   这段代码调用了time库,为了使用sleep函数,也就是延时函数,因为API提供了3181个城市/地区,为了避免访问服务器过于频繁,
#   保证爬虫的稳定性,这里让程序等待1秒钟.在写爬虫的时候.不管需要访问的次数是多还是少,最好养成写延时的习惯

#   这里的url可以重新定义,也可以用新的值覆盖掉原有的值
#   这里要注意缩进,item取的for循环中的值
    url = 'https://free-api.heweather.com/v5/forecast?city=' + item[2:13] + '&key=7d0daf2a85f64736a42261161cd3060b'

#   item[1:11] 最开始改的时候是这个样子的,但是后来发现,不仅仅少截取了两位,而且在 CN1010100前面有一个空格,在拼到url
#   的时候,会被转译成%20
    print(url)
    strhtml = requests.get(url)
    strhtml.encoding='utf8'
    time.sleep(1)
    print(strhtml.text)
#   如果要将JSON数据解析出来,可以使用for循环语句
#   注意缩进,代码还是接上面
    dic = strhtml.json()
#   因为数据太多,所以只取几条数据就可以了,跳出循环
    if(item[2:13])=="CN101010500":
        break
for item in dic["HeWeather5"][0]["daily_forecast"]:
#   得到最高温度,具体见下面的描述
    print(item["tmp"]["max"])
#   接下来使用JSON在线结构化的工具观察数据结构,网址如下:
#   http://www.json.org.cn/tools/JSONEditorOnline/index.htm
#   将其中一个城市的返回数据复制,粘贴到左侧的文本框中,然后点击中间的向右箭头.
#   如果JSON工具报错,则需要检查复制的内容是否存在多了的空格或者少了符号之类的问题.

#   3.3存储数据到MongoDB
#   MongoDB是一个基于分布式存储的数据库,由C++语言编写,旨在为Web应用提供可扩展的高性能数据存储解决方案
#   MongoDB是一个介于关系数据库和非关系数据库之间的产品,它在非关系数据库中功能最丰富.最像关系数据库

#   3.3.1下载并安装MOngoDB
#   1.下载MongoDB
#   官网下载:https://www.mongodb.com/download-center#community
#   2.配置本地MongoDB
#   每次启动时都需要在CMD中配置,找到安装目录下的bin文件夹路径
#
#   配置数据库路径,配置前要先新建文件夹
#   mongod --dbpath E:\data\db
#   再打开一个CMD,进入MongoDB确认数据库已经启动,进入bin路径
#   cd E:
#   键入mongo连接数据库,显示">"表示MongoDB已经正常启动

#   3.3.2在PyCharm中安装Mongo Plugin
#   在PyCharm中的菜单,依次选择"File"--"setting"--"plugins"--"browse repositories"--输入"mongo",然后选择
#   Mongo Plugin,,安装好后重启PyCharm,就可以在右侧看到Mongo Explorer
#   如果没有这个窗口,可以将鼠标光标停留在左下角的图标上,然后在自动弹出的菜单中选择Mongo Explorer命令
#   接下来在Mongo Explorer窗口中单机设置按钮,创建连接(在PyCharm File菜单的Setting中也可以 设置)
#   在Mongo Servers设置窗口中单机左侧加号按钮(addServer)
#   输入连接名,然后单击"Test Connection"(测试连接)按钮,提示信息为"Connection test successful"时表示连接正常,
#   然后单击右下角的"OK"按钮,保存设置即可.

#   3.3.3将数据存入MongoDB
#   下面尝试将获取的数据存入MongoDB中
import requests
