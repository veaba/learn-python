## learn python
## 链接/文档/指引
- Python官方的一些QA https://docs.python.org/zh-cn/3/faq/programming.html#performance

## 疑问
- python 变量不会提升
```python
# 顺序不能反着
a=99
print(a)
```
- 二进制符合转十进制
- 十进制如何转二进制
- 随机数，报错
> 随机数，`.py`的文件名不能是`random`，否则无法引入module，从而报错
```python
import random

print(random.random())

```
## 变量
- 大小写英文、数字或者`_`的组合，且不能数字开头
- 没有关键字声明，没有类型
## 关键字
- print
- input
- chr
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
## 数据类型
- Number数字 ——不可变数据
	- int
	- float
	- bool
	- complex 复数
- String 字符串 ——不可变数据
- Tuple 元组 不可变数据
- List 列表 ——可变数据
- Set 集合 ——可变数据
- Dictionary 字典 ——可变数据
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
- strip([chars])
- swapcase()
- title()
- translate(table,deletechars="")
- upper()
- zfill(widht)
- isdecimal()
- 
## 方法 
### ord() 获取字符串的整数表述
### chr()编码转为对应字符
### input()
### encode
### print()
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
