#   4.1观察页面特征和解析数据
#   JSON格式的数据比较容易处理,所以在获取数据时最好选择JSON格式的数据
#   通过对比PC端和无线端,这里决定数据采集自无线端,原因是无线端返回的数据是JSON格式,这里以
#   touch.qunar.com的自由行为例
#   在浏览器访问touch.qunar.com
#   接下里按F12进入开发者模式,单击"自由行"选项进入自由行频道,在自由行频道中单击搜索框
#   随后进入搜索页面,这个页面有各个地区的热门旅游城市列表,以"JS"格式读取右侧的数据,在"Preview"可以
#   观察到树状的结构
#   切换到Headers页面,在General信息中,有一下两条重要信息
#   (1)Request URL(请求链接):将通过这个链接访问服务器获取数据
#   (2)Request Method(请求方法):决定使用的函数方法和上传参数.常见的请求方法有GET方法和POST方法,其中GET方法权限单一,
#   只有查询数据的权限,只要访问URL就可以返回数据;POST方法需要权限验证和请求内容,服务器通过权限放行,通过请求内容
#   返回客户端请求的数据