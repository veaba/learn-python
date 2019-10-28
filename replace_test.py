
import re
the_list= [
    "__version__ = '2.0.0'", 'bfloat16', 'bool', 'complex128', 'complex64', 'double', 
    'float16', 'float32', 'float64', 'half', 'int16', 'int32', 'int64', 'int8', 'qint16', 
    'qint32', 'qint8', 'quint16', 'quint8', 'resource', 'string', 'uint16', 'uint32', 'uint64', 'uint8']
the_text="uint8"
def fn_parse_code(list_str, text):

    print("list_str:",list_str)
    print("text:",text)
    for code in list_str:
        # print('code:',code)
        # text = text.replace(code, '`' + code + '`',1)
        text=re.sub(r''+code+'','\\1',code)
    return text

# x =fn_parse_code(the_list,the_text)

# print("结果：",x) # 期待是 `uint8` 而不是 u`int8`


def demo2():
    str1='ixt8 uint8'

    str2= ['int','uint8']
    str2.reverse()
    for item in str2:
        print("item:",item)
        str1=str1.replace(item,'`'+item+'`')

    print("结果：",str1) # ixt8 `u`int`8` 不对


str1='ixt8 uint8'

str2= ['int','uint8']
str2.reverse()
for item in str2:
    print("item:",item)
    str1=re.sub(r''+item+'','`222'+item+'`',str1)

print("结果：",str1) # ixt8 `u`int`8` 不对