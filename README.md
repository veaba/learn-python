## learn python

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
### 比较运算符 TODO
### 赋值运算符 TODO
### 位运算符 TODO
### 逻辑运算符 TODO
### 成员运算符 TODO
### 身份运算符 TODO
### 运算优先级 TODO

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
- `'''`/`""" ` 多行注释

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
```python
print('''
x
o
''')

```
### 占位符

|占位符|替换内容|
|----|---|
|%d|整数 double|
|%f|浮点 float|
|%s|字符串 string|
|%x|十六进制 hex|

```python
print('Hi, %s, you have $%d.dd %xd %f ' % ('Michael', 1000000,0xab,0.33))
```
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