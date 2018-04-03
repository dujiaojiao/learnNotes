# Flask：是一个python实现的web开发微框架

# 入门示例：
# from flask import Flask
#
# app = Flask(__name__)  # 利用Flask类创建一个Flask实例
#
# # 装饰器   @ -> 调用装饰器函数  使用route()装饰器告诉flask什么样的url能触发我们的函数
# @app.route("/")   # 设置网站的url路由   下面的函数(hello)实现了访问该url时要运行的功能
# def hello():
#     return 'Hello World!'
#
# if __name__ == '__main__':  #确保服务器只会在该脚本被python解释器直接执行的时候才会执行，而不是作为模板导入
#     app.run()    # 拉起网站
#                  # 默认只能在自己的计算机上访问，网络中其他任何的地方都不能访问
#                  # app.run(host='0.0.0.0') 这会让操作系统监听所有公网IP

# (1) 调试模式
#     虽然 run() 方法适用于启动本地的开发服务器，但是你每次修改代码后都要手动重启它。这样并不够优雅，而且 Flask 可以做到更好。如果你启用了调试支持，服务器会在代码修改后自动重新载入，
#     并在发生错误时提供一个相当有用的调试器。
#     1> app.debug = True
#        app.run()
#     2> app.run(debug = True)

# (2) URL
#     - route() 装饰器把一个函数绑定到对应的 URL 上
#     要给 URL 添加变量部分，你可以把这些特殊的字段标记为 <variable_name> , 这个部分将会作为命名参数传递到你的函数。
#     规则可以用: <converter:variable_name> 指定一个可选的转换器
#     示例：
#     @app.route('/user/<username>')
#     def show_user_profile(username):
#           # show the user profile for that user
#           return 'User %s' % username
#
#    @app.route('/post/<int:post_id>')
#    def show_post(post_id):
#           # show the post with the given id, the id is an integer
#           return 'Post %d' % post_id

# (3) HTTP方法
#     HTTP （与 Web 应用会话的协议）有许多不同的访问 URL 方法。默认情况下，路由只回应 GET 请求，但是通过 route() 装饰器传递 methods 参数可以改变这个行为。这里有一些例子:
#
#     @app.route('/login', methods=['GET', 'POST'])
#     def login():
#         if request.method == 'POST':
#            do_the_login()   # EG: username = request.form.get('username')   通过request.form.get('***') 来获取用户提交的数据
#         else:
#            show_the_login_form() # EG: username = request.args.get('username')  通过request.args.get('***')来获取用户url中提交的数据

# (4) 模板渲染
#     你可以使用 render_template() 方法来渲染模板。你需要做的一切就是将模板名和你想作为关键字的参数传入模板的变量。
#     这里有一个展示如何渲染模板的简例:
#     from flask import render_template
#     @app.route('/hello/')
#     @app.route('/hello/<name>')
#     def hello(name=None):
#         return render_template('hello.html', name=name)
#
#     Flask 会在 templates 文件夹里寻找模板。所以，如果你的应用是个模块，这个文件夹应该与模块同级；如果它是一个包，那么这个文件夹作为包的子目录:
#     情况 1: 模块:
#      /application.py
#      /templates
#          /hello.html
#     情况 2: 包:
#     /application
#         /__init__.py
#         /templates
#             /hello.html


# (5) HTTP
# 在客户端，Get方式在通过URL提交数据，数据在URL中可以看到；POST方式，数据放置在HTML HEADER内提交。
# 1> requests
#     r：Response对象，从这个对象中获取所有我们想要的信息
#     发送一个PUT、DELETE、HEAD、OPTIONS  ->  r = requests.XXX('url')
#     发送一个HTTP POST请求 -> 传参 data = {'key':'value'}
#     r = requests.post('http://127.0.0.1:5000/login',data = {'username':'Merry', 'password':'123'})

#     传递URL参数,Requests允许你使用params关键字参数，以一个字符串字典来提供这些参数
#     payload = {'username':'dujiao','password':'dj358799'}
#     r = requests.get('http://127.0.0.1:5000/login',params=payload)

# 2> Cookie : 总是保存在客户端
#    - 用途：
#       因为HTTP协议是无状态的，即服务器不知道用户上一次做了什么，这严重阻碍了交互式Web应用程序的实现。在典型的网上购物场景中，用户浏览了几个页面，买了一盒饼干和两瓶饮料。最后结帐时，
#       由于HTTP的无状态性，不通过额外的手段，服务器并不知道用户到底买了什么，所以Cookie就是用来绕开HTTP的无状态性的“额外手段”之一。服务器可以设置或读取Cookies中包含信息，借此维护
#       用户跟服务器会话中的状态。
#       在刚才的购物场景中，当用户选购了第一项商品，服务器在向用户发送网页的同时，还发送了一段Cookie，记录着那项商品的信息。当用户访问另一个页面，浏览器会把Cookie发送给服务器，于是
#       服务器知道他之前选购了什么。用户继续选购饮料，服务器就在原来那段Cookie里追加新的商品信息。结帐时，服务器读取发送来的Cookie就行了。
#       Cookie另一个典型的应用是当登录一个网站时，网站往往会请求用户输入用户名和密码，并且用户可以勾选“下次自动登录”。如果勾选了，那么下次访问同一网站时，用户会发现没输入用户名和密码
#       就已经登录了。这正是因为前一次登录时，服务器发送了包含登录凭据（用户名加密码的某种加密形式）的Cookie到用户的硬盘上。第二次登录时，如果该Cookie尚未到期，浏览器会发送该Cookie，
#       服务器验证凭据，于是不必输入用户名和密码就让用户登录了。
#    - 缺陷：
#       1> Cookie会被附加在每个HTTP请求中，所以无形中增加了流量。
#       2> 由于在HTTP请求中的Cookie是明文传递的，所以安全性成问题，除非用HTTPS。
#       3> Cookie的大小限制在4KB左右，对于复杂的存储需求来说是不够用的。
#
#   使用：
#    r = requests.get('url')
#    r.cookies['example_cookie_name']
#
#   注：在使用postman时，post方法要提交的数据是追加在 Body -> form-data中

# (6) SQLite
#     - SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说没有独立的维护进程，所有的维护都来自于程序本身
#     - 连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建数据库文件，而是直接打开该数据库文件。
#       连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库执行完任何操作后，都不需要提交事务的(commit)
#       示例：
#        创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
#        创建在内存上面： conn = sqlite3.connect('"memory:')

#     下面我们一硬盘上面创建数据库文件为例来具体说明：
#     conn = sqlite3.connect('c:\\test\\hongten.db')
#     其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：
#
#         commit()            --事务提交
#         rollback()          --事务回滚
#         close()             --关闭一个数据库链接
#         cursor()            --创建一个游标
#
#     cu = conn.cursor()
#     这样我们就创建了一个游标对象：cu
#     在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
#     对于游标对象cu，具有以下具体操作：
#
#         execute()           --执行一条sql语句
#         executemany()       --执行多条sql语句
#         close()             --游标关闭
#         fetchone()          --从结果中取出一条记录
#         fetchmany()         --从结果中取出多条记录
#         fetchall()          --从结果中取出所有记录
#         scroll()            --游标滚动

#    注：execute()方法是可以带参数查询的
#       1> cu.execute("select * from table where name=?", (uname, ))   ->这个(uname, )参数类型, 必须是元组!
#       2> params = (name, int(age), id)
#          cur.execute("insert into message values(?,?,?)", params)

# (7) 爬虫入门
#   1> get请求：通过url链接的方式传输相关的参数和数据  一般打开网址是get方式请求
#      urllib是基于http的高层库，它有以下三个主要功能：
#      - request处理客户端的请求
#      - response处理服务端的响应
#      - parse会解析url
#
#   python 3.x中urllib库和urilib2库合并成了urllib库
#   其中urllib2.urlopen()变成了urllib.request.urlopen()
#   urllib2.Request()变成了urllib.request.Request()
#
#   函数：
#   urllib.request：用来发送request和获取request结果
#   - urllib.request.urlopen(url,data,timeout)
#        - data：post请求索要
#   - urllib.parse.urlencode(values)   -> 在Python中，我们通常使用urllib中的urlencode方法将字典编码  将字典组成 x1=a&x2==b的形式
#   - urllib.request.Request(url,data,headers,method)
#
#   2> POST请求：通常是Form表单提交数据常用的请求方式
#               通常出现在登陆、提交表单、向API接口发送JSON数据这几种情况
#   3> html解析
#      示例：
#      soup = BeautifulSoup(html, 'html.parser')   # html解析器：lxml html.parser
#
#      #直接获取body标签下的全部子标签的文本内容
#      #print(''.join(soup.body.stripped_strings))
#
#      items = soup.select('a')
#      for item in items:
#          print(item.string, end=' ')
#          print(item.get('href'))
#
#          # 要获取当前item下的子标签 ->  t = item.select('.t a')
#          # 要获取t下的子标签，因为t是list列表  -> img = t[0].select('XXX')




