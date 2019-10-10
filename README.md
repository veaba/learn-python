## learn python

## 链接/文档/指引
- Python官方的一些QA https://docs.python.org/zh-cn/3/faq/programming.html#performance

## 疑问

1. python 变量不会提升
```python
# 顺序不能反着
a=99
print(a)
```
2. 二进制符合转十进制
3. 十进制如何转二进制
4. 随机数，报错
> 随机数，`.py`的文件名不能是`random`，否则无法引入module，从而报错
```python
import random

print(random.random())

```
5. 数字1 如何转为字符1
> str(1) => '1'

6. 月份或者秒数，未满10如何快速补零，在转为时间格式的时候

7. 如何读取任意的一行？
8. TODO 如果写入中文汉字？
9. raise关键字
10. 运行python文件，打印了一堆以前的日志
11. 交换变量
```python
a=1
b=2
a,b=b,a
```
12. 判断是否是数字？
13. 如何可选参数？
14. list 转字符

```python

list1=[12,123,56,99]
list2=[str(1) for i in list1]
print(' '.join(list2))

```
15. 默认下，字典，写成json是 单引号的key，如何转为双引号
16. pass 关键字是做什么的
```python
pass
```

17. 文件暴露变量给其他用

a.py

```python
xx=[11,22,33]
```

b.py

```python
from a import *

print(a)
```
18. python 异步编程怎么搞？

19. python for 循环里面的任务过于长，怎么多线程处理？

20. python 如何查看某个module的方法和属性：dir(xx)
--------------------

## 数据类型
- Number数字 ——`不可变数据`
	- int
	- float
	- bool
	- complex 复数
- String 字符串 ——`不可变数据`
- Tuple 元组 `不可变数据`

- List 列表 ——`可变数据`
- Set 集合 ——`可变数据`
- Dictionary 字典 ——`可变数据`

## 列表

### 快速创建列表

```python
alist=range(5)
print(list(alist))

```

## 字典（js中的对象）


### 字典排序等
```python
def dirt_sort():
    obj = {
        "127.0.0.1": 54,
        "115.192.59.226": 33,
        "124.160.26.190": 192,
        "74.82.47.4": 6,
        "140.205.225.204": 100,
        "120.55.13.109": 69,
        "47.52.210.105": 25,
        "93.174.95.106": 1,
        "140.205.225.190": 75,
        "196.52.43.53": 2,
        "47.94.52.138": 56,
        "47.52.210.90": 21,
        "74.82.47.3": 12,
        "121.42.203.142": 37,
        "119.23.138.247": 72}
    print(obj.values())
    print(obj.keys())  
    # list_obj_value = list(obj.values())
    # list_obj_key = list(obj.keys())

    # print(list_obj_value)
    # print(list_obj_key)
    # 默认对obj的键从小到大排序
    # print("排序:", sorted(obj))
    # 默认对obj的键从小到大排序，取得元组的排序
    print("排序:", sorted(obj.items()))

    # 结果
    print("对值排序：", sorted(obj.items(), key=lambda x: x[1]))
   
    print("对值逆序：", sorted(obj.items(), key=lambda x: x[1], reverse=True))
    
    # 需要转回字典
    print("对值逆序：", dict(sorted(obj.items(), key=lambda x: x[1], reverse=True))) 

```
### 字段转字符

```python
dict_keys(['tf.train'])

#

print(''.join(obj.keys()))

```
### list 转为字典

```python

def list_to_dict():
    a_list = ["127.0.0.1", "99,99,9,99"]

    print(dict.fromkeys(a_list))


list_to_dict() # {'127.0.0.1': None, '99,99,9,99': None}

```
### list key、index，用enumerate返回list
```python
for index,key in enumerate(f.readlines()):
    print(index,key)

```

### 元组转为字典

```python
a_tup=[('127.0.0.1', 192)]
print(dict(a_tup)) #{'127.0.0.1': 192}

```

### 字典相减，目的为了移除部分
```python
from collections import Counter
def dict_subtract():
    parent_dict = {"a": 999, "b": 888, "c": 777, "d": 666}
    child_dict = {"d": 666}

    print(dict(Counter(parent_dict)-Counter(child_dict)))


dict_subtract()
```

### 字典相加，目的，为了融合
```python
from collections import Counter
def dict_subtract():
    parent_dict = {"a": 999, "b": 888, "c": 777, "d": 666}
    child_dict = {"d": 666}

    print(dict(Counter(parent_dict)+Counter(child_dict)))


dict_subtract()
```

## 元组

### 快速创建元组
```python
atup=range(5)
print(tuple(atup))
```

### 元组生成字典

```python
tup1 = (1, 3, 5)
obj4 = dict.fromkeys(tup1) 
obj5 = dict.fromkeys(tup1, "hello")
print(obj4)
print(obj5)

```

### 元组取值 和list 取值一样

tup1[1]

### 列表统计次数转为字段

```python

# list
def go_list():
    a_list = [1, 1, 1, 1, 2, 3, 4, 6, 6, 9]

    obj = {}
    for item in a_list:
        obj[item] = str(a_list.count(item))+'次'
    print(obj)  # {1: '4次', 2: '1次', 3: '1次', 4: '1次', 6: '2次', 9: '1次'}


go_list()


```

## 变量

- 大小写英文、数字或者`_`的组合，且不能数字开头
- 没有关键字声明，没有类型


## 关键字

- end，结果输出到同一行，在末尾添加字符
- print
- input
- chr
- raise
- ord
- `b'ABC'`
- `r''` 表示 `''`内部字符串默认不转译
- `del x `删除某个变量

## 运算符

- `=` 赋值
- `/` 除法
- `//`地板除,取整

### 算数运算符 TODO

|算术运算符|描述|例子|
|---------|---|----|
|+|加法||
|-|减法||
|/|除法||
|*|乘法||
|%|取模，返回除法的余数||
|**|幂，返回x的y次幂||
|//|取整除，向下取接近除数的整数||
||||

### 比较运算符 TODO

|比较运算符|描述|例子|
|---------|---|----|
|>|大于比较符||
|<|小于比较符||
|>=|大于等于比较符||
|<=|小于等于比较符||
|==|等于比较符||
|!=|不等于比较符||

### 赋值运算符 TODO

|赋值运算符|描述|例子|
|---------|---|----|
|=|简单的赋值运算符|c=a+b结果给c|
|+=|加法赋值运算符||
|-=|减法赋值运算符||
|*=|乘法赋值运算符||
|/=|除法赋值运算符||
|%=|取模赋值运算符||
|**=|幂赋值运算符||
|//=|取整除赋值运算符||
||||
### 位运算符 TODO
|位运算符|描述|例子|
|---------|---|----|
|&|与运算||
|▏|或运算||
|^||异或运算|
|~|位取反运算||
|<<|||
|>>|||
||||
### 逻辑运算符 TODO
|逻辑运算符|逻辑表达式|描述|例子|
|---------|---|---|----|
|and|x and y| 布尔与|(a and b)|
|or |x or y|布尔或|(a or b)|
|not|not x|布尔非|not(a and b)|
|||||
### 成员运算符 TODO
|成员运算符|描述|例子|
|---------|---|----|
|in| 指定序列找到某值||
|not int|执行序列没有找到某值||
||||
### 身份运算符 TODO
|身份运算符|描述|例子|
|---------|---|----|
|is|判断是不是引用自一个对象||
|is not|判断是不是引用自不同对象||
### 运算优先级 TODO
|优先级运算符|描述|
|---------|---|
|`**`|指数||
|`~`、`+`、`-`|安位翻转，一元加号、一元减号|
|`*`、`/`、`%`、`//`||
|`+`、`-`||
|`>>`、`<<`|位操作|
|`&`||
|`^`、` ▏`||
|`<=`、`<`、`>`、`>=`||
|`<`、`>`、`==`、`!=`||
|`=`、`%=`、`/=`、`//=`、`-=`、`+=`、`%*=`、`**=`、|赋值运算符|
|`is`、`is not`||
|`in`、`not in`||
|`and`、`and or not`||
|||

## 语法

- 注释 
print('xx')

## python 异步编程怎么搞？

> 循环下异步的任务回来。

## 注释
- `#` 单行
- `'''` 单引号多行注释
- `""" ` 双引号多行注释，推荐,编辑器推荐

## 数据结构
###
### 布尔值
> 大写开头
```python
print(True and True)
# 类似 JavaScript 1&&2

```
- True
- False 
## 语句
### 逻辑语句
- and
```python
print(True and True)
print(True and False)
```
- not
	- 类似JavaScript 中的 ! 操作符
	- not 以下都是True `0 ` 、` False`、`None `、`''`
```python
print(not True)
print(not False)
```
### if
- 需要在语句结束后，加冒号
- 且需要前置tab 换行，否则出错
- 可以是4个，但建议是8个空格
```python
name = 100
if name >= 0:
    print(name)
else:
    print(-name)

```

### and
```python
print (True and True)
```
## 字符串
- 字符串，单引号或者双引号创建，这一点和JavaScript一样
- 字符串链接也和JS一样,使用 `+`加号来实现
```python
print('''
x
o
''')

```

### Python 转义符

|转义字符|描述|
|-------|----|
|`\`（在行尾时）|续行符|
|`\\`|反斜杠符号|
|`\'`|单引号|
|`\"`|双引号|
|`\a`|响铃|
|`\b`|退格(backspace)|
|`\000`|空|
|`\n`|换行符|
|`\v`|纵向字符表|
|`\t`|横向字符表|
|`\r`|回车|
|`\f`|换页|
|`\oyy`|八进制，yy代表字符，\o12代表换行|
|`\xyy`|十六进制，yy代表字符，\x0a代表换行|
|`\other`|其他字符以普通格式输出|
|||

### 占位符/字符串格式化

|占位符|替换内容|
|----|---|
|`%c`||
|`%d`|整数 double|
|`%f`|浮点 float|
|`%s`|字符串 string|
|`%x`|格式化十六进制 hex|
|`%X`|格式化十六进制（大写） hex|
|`%u`|格式化无符号整形，什么叫无符号整形|
|`%o`|格式化无符号八进制|
|`%e`|科学计数法格式化浮点数|
|`%E`|同%e|
|`%g`|%f 和 %e的简写|
|`%G`|%f 和 %E简写|
|`%p`|用十六进制格式化变量的地址|
|||
```python
print('Hi, %s, you have $%d.dd %xd %f ' % ('Michael', 1000000,0xab,0.33))
```
### Python字符串运算符
|操作符|描述|
|-----|----|
|`+`||
|`*`||
|`[]`||
|`[:]`||
|`in`||
|`not in`||
|`r/R`||
|`%`|格式化字符|
|||

### 三引号
> 可以使用特殊字符和引号，比如html代码等

### Unicode字符串/Python字符串内建函数
- capitalize()第一个字符串转大写
> 
- center(width,fillChar) 指定宽度填充字符
> 
- count(str,beg=0,end=len(string)) 返回str在string里面出现的次数，
- bytes.decode(encoding="utf-8",error="strict")
> 
- encode(encoding="UTF-8",errors="strict")
- endswith(suffix,beg=0,end=len(string))
- expandtabs(tabsize=0)
- expandtabs(tabsize=0)
- find(str,beg=0,end=len(string))
- index(str,beg=0,end=len(string))
- isalnum()
- isalpha()
- isdigit() 判断是否是数字组成的
- islower()
- isnumeric()
- isspace()
- istitle()
- isupper()
- join(seq)
- len(string)
- ljust(width[.fillchar])
- lower()
- maketrans()
- max(str)
- min(str)
- replace(old,new[,max])
- rfind(str,beg=0,end=len(string))
- rindex(str,beg=0,end=len(string))
- rjust(width,[,fillchar])
- rstrip()
- split(str="",num=string.count(str))
- splitline([keepends])
- startswith(substr,beg=0,end=len(string))
- strip([chars]) 雷同js中的trim()，移除首位空格
- swapcase()
- title()
- translate(table,deletechars="")
- upper()
- zfill(widht)
- isdecimal()
- 

## 异步编程：asyncio
> python 由于GIL（全局锁：啥玩意？？），无法发挥多核优势

[_asyncio](_asyncio.py)

- 同步：先完成这个，等待，阻塞
- 异步：完成一系列任务，取最长的时间的那个任务为总任务时间，任务之间，通过状态、通知、回调来处理调用处理结果


### 每秒输出一行字符

```python
import time


def hello():
    time.sleep(1)

def run():
    for i in range(10):
        hello()
        print("哇哈哈：%s" % time.time())

run()



```


## 方法/函数
- 区别：
	- 函数手动self，方法不要传
	- 函数，需要类名去调用，方法，用对象去调用
- 如何可选参数?

### 函数参数
    - 必须参数
    - 关键字参数
    - 默认参数
    - 不定长参数
### ord() 获取字符串的整数表述
### chr()编码转为对应字符
### input()  读键盘输入
### encode()
### decode()
### range函数
### print() 打印函数
### enumerate()函数,遍历得到索引值和值
### type 查看数据类型

```python
a=111
print(type(a))


print(type(obj) == dict)# dict
print(type(obj)==str) #string

```
### isinstance
```python
a=652
isinstance(a,int)
```
### items()方法
### zip函数
### reversed函数，逆序
### sorted函数排序 
### dir()函数,导入模块定义的其他名称
### str()函数：用户易读，数字转为字符串
### repr()函数：产生一个解释器易读的表达式形式
### format() 字符串填充的方法，
> print('{}xx:,{}oo'.format("hello","world"))
> print("{0:.3f}",format(math.pi)) # Pi保留小数点后三位

> 表格格式化
```python
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3};
for name,number in table.items():
	print("{0:10} ==> {1:10d}".format(name,number))

```

### open(filename,mode) 

## 循环迭代

### for

```python
test = [541564, 5, 654, 656, 5]
array = ["维", "护", "世", "界", "和", "平"]
for x in test + array:
    print(x)

```
### while

- 只有一行时候可以写成为一行
### while else语句

### break可以跳出for的循环体

### range函数，遍历数字序列
## 判断
- python 没有switch-case语句
- 0 为false
### if
### elif
### else

## 外部脚本
```python
# 键盘输入
age=int(input("请输入xxx:"))

# 回车执行
input("click enter out")

```


## 作用域
- 只有module、class、函数(def、lambda)才会引入新的作用域
- if/elif/esle、try/except、for/while 定义的变量，外部可以访问
### 本地作用域
### 闭包函数外函数作用域
### 全局作用域
### 内置作用域
```python
#import builtins
#import __builtin__
#import __builtin__
# dir(builtins)
#print(dir(builtins))

```
- ArithmeticError
- AssertionError
- AttributeError
- BaseException
- BlockingIOError
- BrokenPipeError
- BufferError
- BytesWarning
- ChildProcessError
- ConnectionAbortedError
- ConnectionError
- ConnectionRefusedError
- ConnectionResetError
- DeprecationWarning
- EOFError
- Ellipsis
- EnvironmentError
- Exception
- False
- FileExistsError
- FileNotFoundError
- FloatingPointError
- FutureWarning
- GeneratorExit
- IOError
- ImportError
- ImportWarning
- IndentationError
- IndexError
- InterruptedError
- IsADirectoryError
- KeyError
- KeyboardInterrupt
- LookupError
- MemoryError
- ModuleNotFoundError
- NameError
- None
- NotADirectoryError
- NotImplemented
- NotImplementedError
- OSError
- OverflowError
- PendingDeprecationWarning
- PermissionError
- ProcessLookupError
- RecursionError
- ReferenceError
- ResourceWarning
- RuntimeError
- RuntimeWarning
- StopAsyncIteration
- StopIteration
- SyntaxError
- SyntaxWarning
- SystemError
- SystemExit
- TabError
- TimeoutError
- True
- TypeError
- UnboundLocalError
- UnicodeDecodeError
- UnicodeEncodeError
- UnicodeError
- UnicodeTranslateError
- UnicodeWarning
- UserWarning
- ValueError
- Warning
- WindowsError
- ZeroDivisionError
- __build_class__
- __debug__
- __doc__
- __import__
- __loader__
- __name__
- __package__
- __spec__
- abs
- all
- any
- ascii
- bin
- bool
- breakpoint
- bytearray
- bytes
- callable
- chr
- classmethod
- compile
- complex
- copyright
- credits
- delattr
- dict
- dir
- divmod
- enumerate
- eval
- exec
- exit
- filter
- float
- format
- frozenset
- getattr
- globals
- hasattr
- hash
- help
- hex
- id
- input
- int
- isinstance
- issubclass
- iter
- len
- license
- list
- locals
- map
- max
- memoryview
- min
- next
- object
- oct
- open
- ord
- pow
- print
- property
- quit
- range
- repr
- reversed
- round
- set
- setattr
- slice
- sorted
- staticmethod
- str
- sum
- super
- tuple
- type
- vars
- zip
### global 和monlocal关键字


## module

### import sys 
```text
>>> import sys
>>> sys.ps1='爱>'
爱>
```
### import your_module
### form xxx import oo
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中

### from...import * 
- 把一个模块的所有内容全都导入到当前的命名空间也是可行的
- 那些下划线_ 开头的名字无法导入,而是作为私有的属性

### __name__属性，如果是__main__自己的本身运行，否则是别人在引用


### 包package，点模块名称

### 从一个包中导入*
- 包定义文件 `__init__.py` 中包含一个叫`__all__`的列表变量 

## 文件

### f.write 写一个文件内容，并返回写入的长度

### f.close()
### f.flush()
### f.fileno()
### f.isatty()
### f.read()
### f.readline([size])
### f.readline([sizeint]) 
若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
### f.seek(offset[whence])
### f.tell()
### f.truncate([size]) 从size开始阶段，无size则从当前位置。阶段后面被删除
### f.write(str)
### f.writelines(squence) 写入一个序列字符串列表


## os(62个)
### os.access(path,mode)
### os.chdir(path)
### os.chflags(path,flogs)
### os.chmod(path,mode)
### os.chown(path,uid,gid)
### os.chroot(path)
### os.close(fd)
### os.closerange(fd_low,fd_high)
### os.dup(fd)
### os.dup2(fd,fd2)
### os.fchdir(fd)
### os.fchmod(fd,mode)
### os.fchown(fd,uid,gid)
### os.fdatasync(fd)
### os.fdopen(fd[,mode[,bufzie]])
### os.fpathconf(fd,name)
### os.fstat(fd)
### os.fstatvfs(fd)
### os.fsync(fd)
### os.ftruncate(fd,length)
### os.getcwd() 获取当前目录
### os.getcwdu()
### os.istty(fd)
### os.lchflags(path,flags)
### os.lchmod(path,mode)
### os.lchown(path,uid,gid)
### os.link(src,dst) 
### os.listdir(path)
### os.lseek(fd,pos,how)
### os.lstat(path)
### os.major(device)
### os.makedev(major,minor)
### os.makedirs(path[,mode])
### os.minor(device)
### os.mkdir(path,[,mode])
### os.mkfifo(path,[,mode])
### os.mknod(filename[,mode=0600,device])
### os.open(file,flags[,mode])
### os.openpty()
### os.pathconf(path,name)
### os.pip()
### os.popen(command[,mode[,bufsize]])
### os.read(fd,n)
### os.readlink(path)
### os.remove(path)
### os.removedirs(path)
### os.rename(src,dst)
### os.renames(old,new)
### os.rmdir(path)
### os.stat(path)
### os.stat_float_times([newvalue])
### os.statvfs(path)
### os.symlink(src,dst)
### os.tcgetpgrp(fd)
### os.tcsetpgrp(fd,pg)
### os.ttyname(fd)
### os.unlink()
### os.utime(path,time)
### os.walk(top[.topdown=True,onerror=None[,followlinks=False]])
### os.write(fd,str)
### os.path模块


## 错误和异常

### 语法错误

### 异常

### 异常处理
- `except OSError as err:`
- `except ValueError:`
- `except IOError:`
- `except ZeroDivisionError as err:`
- `except FileNotFoundError as err:`
- `except UnicodeDecodeError as err:`

```python
while True:
	try:
		x= int (input("输入个数字"))
		break
	except ValueError:
		print("不对，请重输入")

```
### 抛出异常
-
### 预定义的清理行为

确保文件f总总是被关闭的
```python
with open("xx.txt") as f:
	for line in f:
		print(line)

```


## 面向对象

### class 类。

属性和方法的集合。每个对象共用的方法和属性，对象是类的实例

### method 方法。

类中定义的函数

### 类变量。

整个实例化对象中是共用的，类变量定义在类中且在函数体之外，类变量通常不作为实例变量使用

### 数据成员。

类变量或者实例变量用于处理类 及其实例对象的相关数据

### 方法重写。

从父类继承的方法不能满足子类的需求，需要对齐进行改写，这个方法叫覆盖(override)，也叫方法的重写

### 局部变量。

方法中的变量，只作用于当前实例的类

### 实例变量。

在类中的声明中，属性是用变量来表示的，这种变量叫实例变量，类声明的内部，但在类的其他成员的方法之外。属于单独的类型的属性变量
### 继承。

派生类derived class 继承基类base class的字段(属性)和方法，
继承允许把一个派生类的对象作为基类对象对待。
派生类会覆盖基类的任何方法
方法中可以调用基类的同名方法

### 实例化。

创建一个类型的实例，类的具体对象，一个过程.

### 对象

通过类定义的数据结构实例，对象包括两个数据成员（类变量、实例变量）的方法


### 构造方法 __init__ 调用类的时候会自动去调用

### self代表类的实例，而非类


### class 的方法

### 多继承,尚未掌握

### 方法重写

### 类的私有属性,__ 两个下划线开头

### 类的方法

### 私有方法
- `__init__`      构造函数，在生成对象时候调用
- `__del__`       析构函数，释放对象时使用
- `__repr__`      打印，转换
- `__setitem__`   按照索引赋值
- `__getitem__`   按照索引获取值
- `__cmp__`       获取长度
- `__call__`      比较运算
- `__add__`       加运算
- `__sub__`       减运算
- `__mul__`       乘运算
- `__truediv__`   除运算
- `__mod__`       求余、取模预算
- `__pow__`       乘方

### 实例

### 类的专用方法

### 运算符重载

```python
# 运算符重载

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # TODO?
    def __str__(self):
        # print("__str__:", self)
        return "Vector (%d, %d)" % (self.a, self.b)

    # 此处的other
    def __add__(self, other):
        # print("self:", self)
        # print("other:", other)
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(6, 9)
v2 = Vector(8, 12)
print(v1, v2)
print(v1 + v2)

```

## 标准库

### 操作系统 os模块
### 文件通配符 glob模块
- glob.glob("*.py") 返回当前目录的文件名，数组的形式返回
### 命令行参数 sys模块
- sys.argv
### 标准输入输出错误 sys模块
- sys.stdin
- sys.stdout
- sys.stderr
### 错误输出重定向和程序终止 sys模块
- sys.exit()
### 字符串正则匹配 re模块
- re模块

### url接受数据的urllib.request
### 发送电子邮件的smtplib

### 性能度量

### 测试模块

## 正则

### 处理marddown 用到的一段代码

```python
import re
def list_to_str(str_list,code=""):
    if isinstance(str_list, list):
        return code.join(str_list)
    else:
        return EOFError
a_list=['aa','bb']
st= 'while_loop(...): Repeat body while the condition cond is true.aa,擦擦,oooaAddsa.ssbb'

a_str=list_to_str(a_list,"|")
pa= re.compile(r'('+a_str+')')

xx =re.sub(pa,"`"+"\\1"+"`",st)

print(xx)
# 问题。把 aa和 bb换成 `aa` `bb`
```
## socket编程

### socket对象-服务器端套接字
- `s.bind()` (host,port)
- `s.listen()` TCP监听，backlog指定在拒绝连接之前，至少1，一般设置为5即可
- `s.accept()` 被动接受TCP客户端连接
### socket对象-客户端套接字
- `s.connect()`
- `s.connect_ex()`
### socket对象-公共用用途的套接字函数
- `s.recv()`
- `s.send()`
- `s.sendall()`
- `s.recvfrom()`
- `sendto()`
- `s.close()`
- `s.getpeername()`
- `s.getsockname()`
- `s.setsockopt(level,optname,value)` 设置socket超时，浮点单位s，
- `s.getsocketopt(leve,optname[,buflen])`
- `s.settimeout(timeout)`
- `s.gettimetout()`
- `s.fileno()`
- `s.setblocking(flag)`
- `s.makefile()`

## Python 如何实现HTTP服务- 网页服务
- httplib
- urllib
- xmlrpclib
## Python 如何实现NNTP服务- 帖子
- nntplib
## Python 如何实现FTP服务- 文件传输
- ftplib
- urllib
## Python 如何实现SMTP服务- 发送邮件
- smtplib
## Python 如何实现POP3服务- 接收邮件
- poplib
## Python 如何实现IMAP4服务- 获取邮件
- imaplib
## Python 如何实现Telnet服务-命令行
- telnetlib
## Python 如何实现Gopher服务-信息查找
- gopherlib
- urllib

## 多线程 (TODO后续再学习)

【优点】：
- 可以把占据长时间中的任务放到后台去处理
- 程序的运行速度可能加快
- 对于用户输入、读写、网络收发，可以释放内存占用等资源

【特点】：
- 线程可以被抢占（中断）
- 在其他线程运行时，线程可以暂时被搁置（睡眠）——线程的退让

【线程分类】：
- 内核线程：又操作系统内核创建和撤销
- 用户线程：不需要内核支持而在用户程序中实现的线程

【Python线程模块】：
- _thread
- threading(推荐)

### 线程模块 
### threading 模块创建线程
### 线程同步
### 线程优先级队列（Queue）

## XML解析
## JSON
### json.dumps()编码
|Python|JSON|
|---   |----|
|dict|object|
|list,tuple|array|
|str|string|
|int,float,int-& float-derived enums|number|
|True|true|
|False|false|
|None|null|
|||
### json.loads()解码
|JSON|Python|
|----|------|
|object|dict|
|array|list|
|string|str|
|number(int)|int|
|number(real)|float|
|true|True|
|false|False|
|null|None|
|||
## Mongodb
- https://pypi.org/project/pymongo/


## 时间
```python
from datetime import  datetime
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # 2019-07-14 20:09:45
```
- %a 本地简化星期名称 比如sun
- %A 本地完成星期名称 Sunday
- %b 本地简化月份的名称 Jul
- %B 本地完成月份名称 July
- %c 本地响应的日期表示和时间表示 'Sun Jul 14 20:24:02 2019'
- %j 年内的一天(001-366) 195
- %w 星期(0-6)，星期天为一个星期的开始
- %W 一年中的星期数（00-53）星期一位星期的开始 27
- %Y 年份 四位年份表示(0000-9999)
- %m 月份 (0-12)
- %d 天 (0-31)
- %H 时 24小时制(0-23)
- %l 12小时制(0-12)
- %M 分(00-59)
- %p 本地A.M 和P.M PM
- %S 秒(00-59)
- %U 一年中的星期数(00-53)，第几个星期，星期天位星期的开始
- %y 两位数的年份表示(00-99)
- %x 本地相应的日期表示 07/14/19
- %X 本地相应的时间表示 20:30:16
- %Z 当前时区的名称，空字符：''
- %% %号本身

## 内置函数
- abs()
- all()
- any()
- dict()
- dir()
- help()
- hex()
- min()
- next()

- slice()
- divmod()
- id()
- object()
- sorted()
- ascii()
- enumerate()
- input()
- oct()
- staticmethod()
- bin()
- eval()
- int()
- open()
- str()
- bool()
- exec()
- isinstance()
- ord()
- sum()
- bytearray()
- filter()
- issubclass()
- pow()
- super()
- bytes()
- float()
- iter()
- print()
- tuple()
- callable()
- format()
- len()
- property()
- type()
- chr()
- frozenset()
- list()
- range()
- vars()
- classmethod()
- getattr()
- delattr()
- setattr()
- locals()
- repr()
- zip()
- compile()
- globals()
- map()
- reversed()
- __import__()
- complex()
- hasattr()
- max()
- round()
- hash()
- memoryview()
- set()

## redis
-  https://pypi.org/project/redis/

### pip安装
> pip install redis

### python 使用redis
```python
def redis_get_keys():
    import redis
    host = "xxxx"
    port = 6379
    r = redis.Redis(host, port, db=1, password="password")
    keys = r.keys('*')
    return keys


redis_get_keys()

```

## python 设置和获取windows的环境变量

### 永久改变
- https://blog.csdn.net/doots/article/details/86705182

### 添加到系统变量
    os.system("setx BAIDU_REDIS_PASSWORD xxx")
    os.system("setx ALIYUN_HOST ooo")
### 只是临时改变
```python
import os
print(os.environ)
# 设置
os.environ["xx"]="xxx"
print(os.environ["xx"])

```

### setx 永久方式，但需要重启机器
```cmd
// 设置到用户变量里面
setx xx ooo

// 设置到环境变量里面
setx /M oo xx

// 在新的cmd下，会出来
echo %xx%

// 但在idea下没办法出来，需要重启机器吧
print(os.environ["BAIDU_HOST"])
print(os.environ["BAIDU_REDIS_PASSWORD"])
print(os.environ["ALIYUN_HOST"])

// 或者 os.system，需要重启   
print(os.system("echo %xx%"))    
print(os.system("echo %BAIDU_HOST%"))    
print(os.system("echo %BAIDU_REDIS_PASSWORD%"))    
print(os.system("echo %ALIYUN_HOST%"))    
```
