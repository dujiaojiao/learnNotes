# 注：python下的变量：不需要预先声明变量的类型，变量的类型和值在赋值的那一刻被初始化(声明和定义的过程一气完成)
#     在python中，每一个变量在内存中创建，我们可以通过变量来查看内存中的值
#                                                  类似于c的指针】
#     示例：x = 5
#          存储过程：系统先是找了一块内存，将5存储进去，紧接着x志向当前的这块内存
#          id(x) -> 地址：104113976，这个地址当前存储为5

# 字面常量：5、1.23、或如'This is a string'这样的文本
# 数字的类型分为：Integers Floats
# 字符串：可以使用 '' 或 “”，用三引号 ''' 或 """ 来指定多行字符串
# 注：内置的type()函数可以用来查询变量所指的对象类型

# 一、format函数
# format()函数：这个方法会把字符串当作一个模板，通过传入的参数进行格式化
#               这个格式化的模板使用大括号{}作为特殊字符，数字是可选项
#                eg: '{0} is {1} years old'.format(name,age)
#                    '{} is {} years old'.format(name,age)
# 1> 字符串的参数使用{NUM}进行表示, 0表示第一个参数, 1表示第二个参数, 以后顺次递加;
# 2> 使用":", 指定代表元素需要的操作, 如":.3"小数点三位, '{0:.3f}',format(1.0/3)   ":8"占8个字符空间等
# 3> 使用(^)定义'___hello___'字符串长度为11, _是用来补充字符的   '{0:_^11}'.format('hello')

# 二、
# print使用注意：
# 1> 使用关键字输出： print('{name} wrote {book}'.format(name='Swaroop',book='A vyty of python'))
# 2> print会换行，可以通过end指定其应以空白结尾(不换行)
#    eg: print('a',end='') print('b',end='')  -> ab
#        print('a',end=' ') print('b',end=' ')  -> a b


# 注：每当需要提供命令行参数时，点击Run->Edit Configurations 并在Script parameters：部分输入相应参数，并点击ok
# 注：在python中认为：同样缩进的代码块是一个模块

# 运算符与表达式
# + - * ** / // % << >>  &  |  ^(按位异或) ~(按位取反)  <  > <= >= == !=  not(布尔非)  nd  or
# ** 乘方 // 整除

# 读取键盘输入 ：raw_input  input

# 三、函数 -> 用def定义
# 1> 定义全局变量 ：global  EG: global x
# 2> 函数的默认参数  EG:   def say(message, time=1):
#                          print(message*times)
#                        若调用：say('hello',3) -> 结果：hellohellohello
# 3> 关键字参数  EG：def func(a, b=5, c=10)
#                       print('a is',a,'and b is',b,'and c is',c)
#                   调用：func(24,c=35) -> c=35：就是关键字参数赋值
# 4> 可变参数：定义的函数里面能够有任意数量的变量，也就是参数数量是可变的
#    示例：
#       def total(a = 5, *numbers,**phonebook):
#       print('a',a)
#       for i in numbers:
#           print('number ',i)
#       for first,second in phonebook.items():
#           print(first,': ',second)
#
#       total(100,1,2,3,John=1234,merry=5678,Tom=6789)
#    解释：
#        *numbers:    称为数组参数
#        **phonebook: 称为字典参数
#        在调用total函数式，total中匹配完定义好的参数，剩余的参数以元素的形式存储在args中，字典参数的值存储在phonebook中
# 5> return语句
#    每个函数都在其末尾隐含了一句 return None

# 注：Python中的pass语句用于指示一个没有内容的语句块
#     EG:  def some_function():
#               pass

# 6> DocStrings 文档字符串 ''' *** '''
#    可以通过函数的 __doc__属性来获取函数的文档字符串属性
#    示例：
#    def Mymax(a,b):
#       ''' Mymax函数用来打印两个数的最大值'''
#        if a>b:
#            return a
#        elif a<b:
#            return b
#
#    print(Mymax(5,10))
#    print(Mymax.__doc__)   -> 输出：Mymax函数用来打印两个数的最大值

# 四、模块
# 模块：就是包含代码的文件，不一定是python代码，有四种代码类型的模板：
#       1> 使用python写的程序(.py文件)
#       2> c或c++扩展(已编译为共享库或DLL文件)
#       3> 包 (包含多个模块)
#       4> 内建模块 (使用c编写并已链接到python解释器内)
#
# (1)为什么用模块
#    使用模块可以提高代码的可维护性和重复使用，还可以避免函数名和变量名冲突
# (2)import导入模块
#    模块可以包含可执行的语句和函数的定义，这些语句的目的是初始化模块，它们只在模块名第一次遇到导入import语句时才执行
#    即：python优化手段：第一次导入后就将模块名加载到了内存，后续再import引入该模块，只是对该模块对象增加了一次引用，不会重新执行模块内的语句
# (3)模块名称空间
#    每个模块都有一个独立的名称空间，定义在这个模块中函数，把这个模块的名称空间当做全局名称空间，这样我们在编写自己的模块时，就不担心我们定义在自己模块中的全局变量会在被导入时，与使用者的全局变量冲突
# (4)模块的重命名
#    EG: import my_module as new_module
#    EG: #mysql.py
#        def sqlparse():
#            print('from mysql sqlparse')
#        #oracle.py
#        def sqlprase():
#            print('from oracle sqlprase')
#        #test.py
#        db_type=input('>>:')  # 输入mysql或oracle
#        if db_type == 'mysql'
#           import mysql as db
#        elif db_type == 'oracle'
#           import oracle as db
#        db.sqlprase()
#    注：import os
#        print(os.getcwd())   #用来查看程序目前所处的目录
#    1> form...import语句
#       示例：from math import sqrt   -> 将math.sqrt引入到当前文件   应该避免使用，可能会出现名称冲突
#             print('Square root of 16 is',sqrt(16))
#       示例: from my_module import *  -> 把my_module中所有的不是一下划线(_)开头的名字都导入到当前位置    应该避免使用
#       注：在my_module.py中新增一行
#           __all__=['money','read1'] -> 这样在另外一个文件中用from my_module import * 就只能导入列表中规定的这两个名字
#    2> 模块的 __name__属性
#       可以通过模块的全局变量__name__来查看模块名：
#       a. 当做脚本运行： __name__ == '__main__'
#       b. 当做模块导入： __name__ == 模块名
#       作用：用来控制.py文件在不同的应用场景下执行不同的逻辑
# (5) 编译python文件
#     python解释器会在__pycache__目录中下缓存每个模块编译后的版本，格式为: module.version.pyc
#     通常会包含python的版本号 EG: my_module.py模块会被缓存成__pycache__/my_module.cpython-33.pyc

# dir函数：能够返回由对象多定义的名称列表。
#         若这一对象是一个模块，则该列表会包括函数内所定义函数、类、变量
# dir函数接受参数：若参数是模块名称，函数将会返回这一指定模块的名称列表
# dir无参：函数将返回当前模块的名称列表

# 五、数据结构
# (1) List 列表   -> 可以使用下标访问元素
#     示例：  list1 = ['hello','world','Runnable']
#            list2 = [1,2,3,4]
#            list3 = ['hello','world',1,2]
#       列表更新： list1[2] = 'china'
#       列表删除:  del list1[2]
#       列表截取:  list1[1:]  <-> list1[1,3]:下标取值范围 [1,3)
#       列表拼接:  list2 + [5,6,7]
#    1> 函数： len(list)  max(list)  min(list) list(seq) -> 将元祖转换为列表
#    2> 方法： list.append(obj)  list.count(obj)  list.extend(seq)->在列表末尾一次性追加另一个序列中的多个值
#             list.index(obj)  list.insert(insert,obj)  list.pop(obj)->移除列表中的一个元素，默认是最后一个元素
#             list.remove(obj) list.reverse() list.sort()  list.clear()  list.copy()
# (2) 元组 用小括号()表示
#    注：若元组中只有一个元素，需加上逗号 tmp = (50,)
#        元组中的元素之是不允许修改的，但可以对元组进行连接组合
#        元组中的元素值是不允许删除的，但可以使用del语句来删除整个数组
# (3) 字典
#     表现形式：d = {key1:value1, key2:value2 ... ...}
#     修改字典：dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#              dict['Age'] = 8;               # 更新 Age
#              dict['School'] = "菜鸟教程"  # 添加信息
#     删除字典元素： dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#                  del dict['Name'] # 删除键 'Name'
#                  dict.clear()     # 清空字典
#                  del dict         # 删除字典
#     注：key只能出现一次；key必须不可变(EG: 可以使用数字、字符串、元组，不可以使用列表)
#     1> 内置函数
#        str(dict)  以字符串的形式输出字典
#     2> 内置方法
#        dict.get(key) dict.item()->以列表返回可以遍历的(key-value)元组数据
#         dict.key()   dict.values()  pop(key)->删除字典给定key对应的value...
# (4)集合
#    集合是一个无序不重复元素的集，用{}创建集合
# (5)字符串
#    字符串都是str类下的对象
#    字符串内置函数： ... ...

# 注：引用
#     eg: list1 = [1,2,3]
#         s1 = list1     #s1和list1指向同一对象
#     eg：s2 = list1[:]  #通过生成一份完整的切片制作一份list1的副本
#         del s2[0]      #这个操作只会对s2产生影响

# 六、迭代器和生成器
#  (1)迭代器的两个基本方法： iter() 和 next()
#     示例：list=[1,2,3,4]
#          it=iter(list)
#          for x in it
#              print(x,end=' ')
#     示例：it1=iter(list)
#           print(next(it))   #输出迭代器的下一个元素
#  (2)生成器
#     在python中，使用了yield的函数被称为生成器
#     在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，并在下一次执行next()方法时从当前位置继续执行  ?

# 七、面向对象编程
#     1> 方法
#        类成员方法：必须多加一个参数(self)在参数列表开头,在调用该类方法时不需要给该参数赋值
#                   Python中的self <--> C++中的this指针
#        类方法(静态方法) ：用 @classmethod 声明
#     2> __init__方法
#        会在类对象被实例化时立即执行 (相当于C++中的构造方法)
#     3> 类变量与对象变量
#        类变量：可以被属于该类的所有实例访问。该类变量只有一个副本，当任何一个对象对类变量做出改变时，发生的变动将在其它所有实例中都得到体现  以"类名."调用
#        对象变量：有类对象所拥有。一般在 __init__()方法中声明  以"self."开头
#     4> 继承
#        要想使用继承，需要在派生类后面跟一个包含基类名称的元组  EG：class Tearch(People): ...
#        注：若在派生类中定义了 __init__方法，需要自己显示的调用基类的__init__方法  -> 此时调用基类的__init__方法需要在参数列表中写入 self
#           若在派生类中没有定义__init__方法，python会自动调用基类的构造函数
#        多重继承：继承元组中有超过一个类
#     注：所有类成员都是公开的
#         但若数据成员(变量、方法)使用双下划线作为前缀(eg: __privatervar)，Python会使用名称调整来使其有效的成为一个私有变量 或 私有方法  类外不能访问
#         可以使用 对象._classname__**  :  调用类(classname)的私有成员**  该私有成员可以是 类变量 对象变量 私有方法

# 八、文件IO
# (1) open函数
#     -打开一个文件，创建一个file对象
#     file object = open(file_name [,access_mode] [,buffering])
#     - access_mode: 决定打开文件的模式
#       - r: 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#       - rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
#       - r+: 打开一个文件用于读写。文件指针将会放在文件的开头
#       - rb+: 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
#       - w: 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#       - wb: 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
#       - w+: 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#       - wb+: 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
#       - a: 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#       - ab: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#       - a+: 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
#       - ab+: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
#
# (2) python读取文件函数 read() readline() readlines()   -> 取决于文件指针的位置
#     1> read() 一次性读取文本全部的内容，以字符串的形式返回结果
#     2> readline() 只读取文本第一行的内容，以字符串的形式返回结果
#     3> readlines() 读取文本所有内容，并且以数列的格式返回结果，一般配合for in 使用
#     示例：读取文件"file1.txt"
#           - 使用readline()
#           while True:
#                 str = file.readline()
#                 if(0 == len(str)):
#                      break
#                 print(str, end='')
#           - 使用readlines()
#           for str in file.readlined():
#               print(str,end = '')
# (3) close()方法
#     -刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
#     注：file.flush()：刷新文件内部缓冲，直接把缓冲区的数据立刻写入文件，而不是被动的等待输出缓冲区写入
# (4) write()方法
#     - 方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
#     - 注：write()方法不会在字符串的结尾添加换行符('\n')，若需要换行，需要自己在字符串中添加 \n
#     - 语法：fileObject.write(string)
#     注：在write内容之后，直接read文件输出会为空，是因为指针已经在内容末尾了
#         为了保证无论是否出错都能正确的关闭文件，我们可以使用try...finally来实现
# (5) 文件定位
#     tell()方法：告诉文件内的当前位置
#     seek(offset [,from])：改变当前文件的位置
#     - offset：表示要移动的字节数
#     - from：指定开始移动字节的参考位置
#             - 0 : 意味着将文件的开头作为移动字节的参考位置
#             - 1 : 使用当前位置作为参考位置
#             - 2 : 将文件的末尾作为参考位置
# (6) 重命名和删除文件
#     - 需导入python的os模块
#     os.rename(current_file_name,new_file_name)
#     os.remove(file_name)
# (7) 目录操作
#     os.mkdir("newdir"): 使用os模块的mkdir()方法在当前目录下创建新的目录
#     os.chdir("newdir"): 改变当前目录路劲
#     os.getcwd():显示当前的工作目录
#     os.rmdir("dir")：删除目录，在删除这个目录之前，它的所有内容都应该先被清除
#     os.chmod(path, mode)：更改权限
#     os.fstat(fd)：返回文件描述符fd的状态，像stat()。
#     os.fstatvfs(fd)：返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
#     os.removedirs(path)：递归删除目录。
#     os.pipe()：创建一个管道. 返回一对文件描述符(r, w) 分别为读和写

# 九、异常处理
#    异常是一个Python对象，表示一个错误
#    捕获异常：
#    语法：try...except...else
#    1> 可以通过raise语句来引发一次异常
#       '''自定义异常：测试异常处理'''
#       class ShortLengthException(Exception):
#            def __init__(self,len,minlen):
#                self.len = len
#                self.minlen = minlen
#       # 异常测试
#       minlen = 3
#       str = input('please input >> ')
#       try:
#           if len(str) < minlen:
#               raise ShortLengthException(len(str), minlen)
#       except IOError:
#           print("input error")
#       except ShortLengthException as ex:
#           print("ShortLengthException :The input len was {},excepted at least {}".format(ex.len,ex.minlen))
#       else:
#           print("succeed!")
#    2> try...finally
#       示例：
#       import time
#       ''' 文件异常处理 '''
#       file = None
#       try:
#           file = open("./test.txt","r+")
#           str = file.readline()
#           print(str,end="")
#           print("press Ctrl+C",end='')
#           time.sleep(5)
#       except IOError:
#           print("Can not find file")
#       except KeyboardInterrupt:  #用户终端执行
#           print("raised KeyboardInterrupt")
#       else:
#           if file:
#               file.close()
# 十、 网络编程
# 1> python使用socket()函数来创建套接字
#    s = socket.socket(family,type,proto)
#    - family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）
#    - type：套接字类型，可以是 SOCKET_STREAM（流式套接字，主要用于 TCP 协议）或者SOCKET_DGRAM（数据报套接字，主要用于 UDP 协议）
#    - protocol: 一般不填默认为0
# 2> socket对象内建方法
#    -- 服务器套接字
#       s.bind(address) 绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
#       s.listen(backlog) 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
#       s.accept() 接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
#    -- 客户端套接字
#       s.connect() 主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
# 3> 公共用途的套接字函数
#    s.recv() 接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
#    s.send() 发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
#    s.sendall() 完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
#    s.recvfrom() 接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
#    s.sendto() 发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
#    s.close()  关闭套接字
#    s.fileno() 返回套接字的文件描述符。
#    s.setblocking(flag) 如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。

#    注：send、recv发送的是bytes，用户可以看清的是str
#        encode(): 将str编码为指定的bytes
#        decode(): 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes  -> bytes变为str
#        示例：
#            n = s.send(send_data.encode())
#            recv_data = s.recv(1024).decode()

#   https://www.cnblogs.com/nulige/p/6235531.html?utm_source=itdadao&utm_medium=referral  使用到的模块解析

# 注：socketserver详解
#   SocketServer框架式一个基本的socket服务器框架，使用了threading来处理多个客户端的连接，使用seletor模块来处理高并发访问
#   SocketServer内部使用IO多路复用以及"多进程"和"多线程"，从而实现并发处理客户端请求
#   SocketServer提供5个基本服务类：
#   -请求处理类
#       - BaseServer 基类，不直接对外服务
#           - TCPServer：派生类，针对TCP套接字流
#               - UnixStreamServer针对UNIX域套接字，不常用
#           - UDPServer：派生类，针对UDP数据报套接字
#               - UnixDatagramServer针对UNIX域套接字，不常用
#    请求处理类有三种方法：
#    - setup() 也就是在handle()之前被调用，主要的作用就是执行处理请求之前的初始化相关的各种工作。默认不会做任何事
#    - handle() 做那些所有与处理请求相关的工作。默认也不会做任何事。他有数个实例参数：self.request    self.client_address   self.server
#    - finish() 在handle()方法之后会被调用，他的作用就是执行当处理完请求后的清理工作，默认不会做任何事
#
#    用socketserver创建一个服务的步骤：
#    1、创建一个request handler class（请求处理类），合理选择StreamRequestHandler和DatagramRequestHandler之中的一个作为父类（当然，使用BaseRequestHandler作为父类也可），并重写它的handle()方法。
#    2、实例化一个server class对象，并将服务的地址和之前创建的request handler class传递给它。
#    3、调用server class对象的handle_request() 或 serve_forever()方法来开始处理请求。
#
# 十一、多线程
# Python使用线程有两种方式：函数 或者 用类来包装线程对象
# (1) thread模块的start_new_thread()函数
#     语法：start_new_thread(function,args[,kwargs])
#          - function: 线程函数
#          - args: 传递给线程函数的参数，必须是tuple类型(元组类型)
#          - kwargs: 可选参数
# (2)threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
#    threading.currentThread(): 返回当前的线程变量。
#    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
#    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
#
#    除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
#    run(): 用以表示线程活动的方法。
#    start():启动线程活动。
#    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
#    isAlive(): 返回线程是否活动的。
#    getName(): 返回线程名。
#    setName(): 设置线程名。

# 十二、Gevent
# Gevent是一个基于greenlet的Python的并发框架，以微线程greenlet为核心，使用了epoll事件监听机制以及诸多其他优化而变得高效。
# gevent每次遇到io操作，需要耗时等待时，会自动跳到下一个协程继续执行
# gevent是第三方库，通过greenlet实现协程的基本思想是：
# - 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等待IO操作完成，再在适当的时候切换回来继续执行。
# - 由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO
# - 在gevent里面，上下文切换是通过yielding(退位)来完成 -> 通过调用gevent.sleep(***),让它们yield向对方

# (1) 协程，又称微线程，纤程
#     - 协程的特点在于是一个线程执行
#     - 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#     - 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#     - 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能

# (2) Greenlets
#     在gevent中用到的主要模式是Greenlet，它是以C扩展模块形式接入Python的轻量级协程
#     - 创建Greenlets
#    import gevent
#    from gevent import Greenlet
#
#    def foo(message, n):
#       """
#       Each thread will be passed the message, and n arguments
#       in its initialization.
#       """
#       gevent.sleep(n)
#       print(message)
#
#
#   thread1 = Greenlet.spawn(foo, "Hello", 1)
#   thread2 = gevent.spawn(foo, "I live!", 2)
#   thread3 = gevent.spawn(lambda x: (x+1), 2)
#
#   threads = [thread1, thread2, thread3]
#
#   # Block until all threads complete.
#   gevent.joinall(threads)


# 十三、python调用shell命令
# (1) os模块的system方法
#     system方法：会创建子进程执行外部程序
#     示例： os.system("ls")
# (2) os模块popen方法
#     popen方法：可以的搭配shell命令的返回值  os.popen(cmd)后，需要在调用read()或者readlines()这两个命令，输出结果
#     示例：os.popen("ls").read()
# (3) commands模块
#     使用commands模块的getoutput方法，这样的方法同popend的差别在于popen返回的是一个文件句柄，而本方法将外部程序的输出结果当作字符串返回。非常多情况下用起来要更方便些。
#     主要方法:
#     commands.getstatusoutput(cmd)         返回(status, output)
#     commands.getoutput(cmd)                   仅仅返回输出结果
#     commands.getstatus(file)                     返回ls -ld file的运行结果字符串，调用了getoutput。不建议使用此方法
#
# (4) subprocess模块
#     使用subprocess模块能够创建新的进程。能够与新建进程的输入/输出/错误管道连通。并能够获得新建进程运行的返回状态。使用subprocess模块的目的是替代os.system()、os.popen*()、commands.*等旧的函数或模块。
#     subprocess.call(["some_command","some_argument","another_argument_or_path"])
#     subprocess.call(command,shell=True)
#     subprocess.Popen(command,shell=True)
#           假设command不是一个可运行文件。shell=True不可省。
#     示例：
#     from subprocess import call
#     call(['ls','-l'])
#     或
#     from subprocess import Popen
#     Popen(['ls','-l'])


























