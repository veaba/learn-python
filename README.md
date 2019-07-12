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
> # print('xx')
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
- find(str,beg=0,end=len(string))
- index(str,beg=0,end=len(string))
- isalnum()
- isalpha()
- isdigit()
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

## 方法/函数
- 区别：
	- 函数手动self，方法不要传
	- 函数，需要类名去调用，方法，用对象去调用
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
    print(x, end=" ")

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
import builtins

# dir(builtins)

print(dir(builtins))

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
### os.getcwd()
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
```python
while True:
	try:
		x= int (input("输入个数字"))
		break
	except ValueError:
		print("不对，请重输入")

```

### 预定义的清理行为
确保文件f总总是被关闭的
```python
with open("xx.txt") as f:
	for line in f:
		print(line,end=" ")

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


### 多继承
### 方法重写
### 类的私有属性
### 类的方法
### 私有方法
### 实例
### 类的专用方法
### 运算符重载
