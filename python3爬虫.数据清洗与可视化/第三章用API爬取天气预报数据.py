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

print('----------------------------3.2 end--------------------------------------')
#   3.3.1下载并安装MOngoDB
#   1.下载MongoDB
#   官网下载:https://www.mongodb.com/download-center#community
#   2.配置本地MongoDB
#   每次启动时都需要在CMD中配置,找到安装目录下的bin文件夹路径
#   cd C:\Program Files\MongoDB\Server\4.0\bin
#   配置数据库路径,配置前要先新建文件夹
#   实际上再windows安装的时候已经配置过data和log的路径,所以可以省略此步骤
#   mongod --dbpath D:\MongoDB\Server\4.0\data
#   再打开一个CMD,进入MongoDB确认数据库已经启动,进入bin路径
#   cd C:\Program Files\MongoDB\Server\4.0\bin
#   键入mongo连接数据库,显示">"表示MongoDB已经正常启动
#   mongo
#   3.3.2在PyCharm中安装Mongo Plugin
#   在PyCharm中的菜单,依次选择"File"--"setting"--"plugins"--"browse repositories"--输入"mongo",然后选择
#   Mongo Plugin,,安装好后重启PyCharm,就可以在右侧看到Mongo Explorer
#   如果没有这个窗口,可以将鼠标光标停留在左下角的图标上,然后在自动弹出的菜单中选择Mongo Explorer命令
#   接下来在Mongo Explorer窗口中单机设置按钮,创建连接(在PyCharm File菜单的Setting中也可以 设置)
#   在Mongo Servers设置窗口中单机左侧加号按钮(addServer)
#   实际上新版的PyCharm不需要点设置,直接点左上角的"+"就可以了
#   输入连接名,然后单击"Test Connection"(测试连接)按钮,提示信息为"Connection test successful"时表示连接正常,
#   然后单击右下角的"OK"按钮,保存设置即可.

#   3.3.3将数据存入MongoDB
#   下面尝试将获取的数据存入MongoDB中
import requests
import time
#   加载pymongo库
import pymongo
#   建立连接
client= pymongo.MongoClient('localhost',27017)
#   在MongoDb中新建名为weather的数据库
book_weather = client['weather']
#   在weather库中新建名为sheet_weather_3的表
sheet_weather=book_weather['sheet_weather_3']
url = 'https://cdn.heweather.com/china-city-list.txt'
strhtml=requests.get(url)
data = strhtml.text
#   之前的老旧代码不再展示,直接写正确的
data1 = data.split('\n')
print(data1)
for i in  range(6):
    data1.remove(data1[0])
for item in data1:
    print(item[2:13])
    url = 'https://free-api.heweather.com/v5/forecast?city='\
          + item[2:13] + '&key=7d0daf2a85f64736a42261161cd3060b'
    strhtml = requests.get(url)
    strhtml.encoding = 'utf8'
    time.sleep(1)
    dic = strhtml.json()
    #   因为数据太多,所以只取几条数据就可以了,跳出循环
    if (item[2:13]) == "CN101010500":
        break
#   向表中写入一条数据
    sheet_weather.insert_one(dic)

#   运行后双击连接,可以看到名为weather的数据库
#   展开weather数据库,双击sheet_weather_3这张表,会弹出预览窗口,可以从该窗口观察获取到的天气数据,数据以JSON格式
#   存在数据库中
#   可以直接在预览窗口中展开JSON的树形结构

'''
#   ps:需要提前安装PyMongo库,这是一个提供Python和MongoDB链接的库
    1.建立连接
    其中localhost是主机名,27017是端口号
    client=pymonngo.MongoClient('localhost',27017)
    2.新建名 为'weather'的数据库
    book_weather=client['weather']
    3.新建名为'sheet_weather_3'的表
    sheet_weather = book_weather['sheet_weather_3']
    4.写入数据
    dic='数据'
    sheet_weather.insert_one(dic)    
'''
print('----------------------------3.3 end--------------------------------------')
#   3.4MongoDB数据库查询
#   基于3.3的代码,查询北京的天气数据
import pymongo
client = pymongo.MongoClient('localhost',27017)
book_weather=client['weather']
sheet_weather=book_weather['sheet_weather_3']
#   查找键HeWeather5.basic.city值为北京的数据
for item in sheet_weather.find({'HeWeather5.basic.city':'北京'}):
    print(item)

#   查询的语法是sheet_weather.find(),其中sheet_weather代表weather,数据库中的表格sheet_weather_3

#   接下来查询天气最低气温大于5摄氏度的城市名
#   承接上面的代码
for item in sheet_weather.find():
#   因为数据需要3天的天气预报,因此循环3次
    for i in range(3):
        tmp = item['HeWeather5'][0]['daily_forecast'][i]['tmp']['min']
        #使用update方法,将表中最低气温数据修改为数值型
        sheet_weather.update_one({'_id':item['_id']},{'$set':{'HeWeather5.0.daily_forecast.{}.tmp.min'.format(i):int(tmp)}})
#提取冲最低气温高于5摄氏度的城市
for item in sheet_weather.find({'HeWeather5.daily_forecast.tmp.min':{'$gt':5}}):
    print(item['HeWeather5'][0]['basic']['city']+'////')

#   由于这里目标是提取最低温度大于5摄氏度的城市名,因此先将最低温度设置成整形数据,更新数据用sheet_weather,其中update_one,
#   update_one用于指定更新一条数据,代码如下
"""
    sheet_weather.update_one({'_id':item['_id']},{'$set':{'HeWeather5.0.daily_forecast.{}.tmp.min
    .format(i):int(tmp)'}})
"""
#   这里第一个参数是{'_id':item['_id']},表示要更新的查询条件,对应_id字段,第二个参数表示要更新的信息,$set是MongoDB中的
#   一个修改器,用于指定一个键并更新键值 ,若键不存在则创建一个键

"""
#   ps:常用的修改器:
    $inc: 可以对文档的某个值为数字型(只能为满足要求的数字)的键进行增减操作
    $unset:用于删除键
    $push:向文档的某个数组类型的键添加一个数组元素,不过滤重复的数据,添加时,若键存在,要求键值类型必须是数组;
    若键不存在,则创建数组类型的键
#   常用的符号
    $lt:<
    $lte:<=
    $gt:>
    $gte:>=
"""
#   拓展内容
#   可以将3.2节中的url部分:
'''
    url = 'https://free-api.heweather.com/v5/forecast?city='\
          + item[2:13] + '&key=7d0daf2a85f64736a42261161cd3060b'
          
    写成:
     url = 'https://free-api.heweather.com/v5/forecast?city={}
        &key=7d0daf2a85f64736a42261161cd3060b.format(item[2:13])'
        
    解释:
        路径中的{}的数据,由路径后面的.format(i)指定
'''