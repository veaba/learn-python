import re
# li='<ul><li>甲</li><li>乙</li><li>丙</li><ul><li>AA</li><li>BB</li><li>CC</li><ul><li>11</li><li>22</li><li>33</li></ul></ul><ul><li>AA</li><li>BB</li><li>CC</li><ul><li>11</li><li>22</li><li>33</li></ul></ul></ul>'

# # 0 前提是一个完整的ul块
# # 1 查找ul标签
# patten=re.compile(r'<ul')
# patten_end_ul=re.compile(r'</ul')
# ul_list=patten.findall(li)
# end_ul_list=patten_end_ul.findall(li)

# if len(ul_list)!=len(end_ul_list):
#     raise RuntimeError('HTML标签格式错误') 
# # 2 查找ul的长度是，但无法确认是有多少级
# print("找到的<ul 长度：",len(ul_list))

# 3 如何确定ul 最深有多少级？

# 如何将一个html 的ul 组合组成数组格式的！！！
def demo1():
    # li ='<ul><li>甲</li><li>乙</li><li>丙</li><ul><li>AA</li><li>BB</li><li>CC</li><ul><li>11</li><li>22</li><li>33</li></ul></ul><ul><li>AA</li><li>BB</li><li>CC</li><ul><li>11</li><li>22</li><li>33</li></ul></ul></ul>'
    # li ='<ul><li>11111<ul><li>222</li><ul><li>4444</li></ul></ul></li></ul>'
    li='<ul><li>111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li></ol></ul>'
    a=re.sub(r'<ul(.*?)>','[',li)
    print(1,a)
    a=re.sub(r'</ul>',']',a)
    print(2,a)
    #=== 1 首尾ul 变为[ ]
    #a='[<li>甲</li><li>乙</li><li>丙</li><ul><li>AA</li><li>BB</li><li>CC</li><ul><li>11</li><li>22</li><li>33</li></ul></ul><ul><li>AA</li><li>BB</li><li>CC</li><ul><li>11</li><li>22</li><li>33</li></ul></ul>]'

    a=re.sub(r'<li(.*?)>','"',a)
    print(3,a)
    #=== 2 </li><li> ==> ","
    #a='[<li>甲","乙","丙</li><ul><li>AA","BB","CC</li><ul><li>11","22","33</li></ul></ul><ul><li>AA","BB","CC</li><ul><li>11","22","33</li></ul></ul>]'
   
    a=re.sub(r'</li>','"',a)
    print(4,a)
    #=== 3  <li> " 
    #a='["甲","乙","丙</li><ul>"AA","BB","CC</li><ul>"11","22","33</li></ul></ul><ul>"AA","BB","CC</li><ul>"11","22","33</li></ul></ul>]'
    a=re.sub(r'""','","',a)
    print(4.1,a)

    a=re.sub(r'\["','",["',a)
    print(5,a)
    #=== 4 </li><ul> ",[
    #a='["甲","乙","丙",["AA","BB","CC",["11","22","33</li></ul></ul><ul>"AA","BB","CC",["11","22","33</li></ul></ul>]'

    a=re.sub(r'""','"',a)
    print(6,a)
    #=== 5 </li> "
    #a='["甲","乙","丙",["AA","BB","CC",["11","22","33"</ul></ul><ul>"AA","BB","CC",["11","22","33"</ul></ul>]'


    a=re.sub(r',",\["',',[',a)
    print(6.1,a)

    a=re.sub(r'\]",','],',a)
    print(6.3,a)

    a=re.sub(r'\],",\[','],[',a)
    print(6.4,a)

    a=re.sub(r'^",\[','[',a)
    print(7,a)
    #=== 6  </ul><ul>   ],[
    #a='["甲","乙","丙",["AA","BB","CC",["11","22","33"</ul>],["AA","BB","CC",["11","22","33"</ul></ul>]'

    a=re.sub(r'\]"\]',']]',a)
    print(8,a)
    #=== 7 </ul> ]
    #a='["甲","乙","丙",["AA","BB","CC",["11","22","33"]],["AA","BB","CC",["11","22","33"]]]'
   
    # a=re.sub(r'<ul>',',[',a)
    # print(10,a)
    # a=re.sub(r'</ul></ul>',']',a)
    # print(11,a)
    # b={}
    b=eval(a)
    print(b,isinstance(b,list)) # ['甲', '乙', '丙', ['AA', 'BB', 'CC', ['11', '22', '33']], ['AA', 'BB', 'CC', ['11', '22', '33']]] True

    #=== 8 
    # exec('a=["甲","乙","丙",["AA","BB","CC",["11","22","33"]],["AA","BB","CC",["11","22","33"]]]')

    # print(a)


def demo2():
    li = '<ul><li>111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li><ol><li>啊啊啊11</li><li>哦哦哦222</li></ol></ol></ul>'
    # 移除 <li> 和 </li>
    origin_li=li
    li_struct=re.sub(r'(<li(.*?)>)|</li>','',li)
    print(1,li_struct) 
    # <ul>111222333<ul>1111222133334444</ul><ul>555566667777<ul>aaaabbbbccccdddd</ul><ul>eeeeffffgggghhhh</ul></ul>444<ol>啊啊啊哦哦哦<ol>啊啊啊11哦哦哦222</ol></ol></ul>
    
    new_str={
        'a':""
    }
    def ah(a):
        new_str['a']+=a.group()+'*' # 特殊字符*
        return a.group()
    # 移除 除了<ul 和非 </ul> <ol> </ol> todo 
    li_struct=re.sub(r'(<ul(.*?)>)|(</ul>)|(<ol(.*?)>)|(</ol>)',ah,li_struct)

    print(2,li_struct)

    print('3',new_str['a'])
    # <ul><ul></ul><ul><ul></ul><ul></ul></ul><ol><ol></ol></ol></ul>

    # 4 转换为[] 【
    ul_ol_string= new_str['a']
    print(4,ul_ol_string)
    ul_ol_array= ul_ol_string[0:-1].split('*') # 过滤最后一个并分割为数组
    print(5,ul_ol_array,len(ul_ol_array))
    # 5 循环替换原字符串
    # todo 此时，是不是可以知道ul 是属于哪一个数组层级？
    xx=origin_li
    for item in ul_ol_array:
        pattrn= re.compile(r''+item+'')
        if item=='<ul>':
            xx=re.sub(pattrn,'[',xx,count=1)
        elif item=='</ul>':
            xx=re.sub(pattrn,']',xx,count=1)
        elif item=='<ol>':
            xx=re.sub(pattrn,'【',xx,count=1)
        elif item=='</ol>':
            xx=re.sub(pattrn,'】',xx,count=1)
    
    print(6,xx)
    ul_ol_struct=ul_ol_string
    ul_ol_struct=re.sub(r'<ul(.*?)>','[',ul_ol_struct)
    ul_ol_struct=re.sub(r'</ul>',']',ul_ol_struct)
    ul_ol_struct=re.sub(r'<ol(.*?)>','[',ul_ol_struct)
    ul_ol_struct=re.sub(r'</ol>',']',ul_ol_struct)

    ul_ol_struct=ul_ol_struct.replace('*','')
    print('7',ul_ol_struct) 
    ul_ol_struct=ul_ol_struct.replace('][','],[')
    print(8,ul_ol_struct)
    ul_ol_struct_array=eval(ul_ol_struct)
    print(9,len(ul_ol_struct_array),isinstance(ul_ol_struct_array,list))
    oo=[]
    def recursion_array(array,i=0):
        for item in enumerate(array):
            k=item[0]
            v=item[1]
            k+=i
            print(item)
            oo.append(k)
            if len(v):
               recursion_array(item[1],k)
        
    recursion_array(ul_ol_struct_array)
    # todo 确认级别

    print(10,oo)
    
    # 此处的概念有点模糊了



# demo2()


# def demo3():
#     array=[1,2,4,5,8,9,10,11,16] #0-8,怎么找这组数据的规律
#     right=[18,3,7,6,12,13,14,15,17]
#     space_string=' '
#     array_string=['' for i in range(len(array))] # 创建长度为len(array)的数组：['', '', '', '', '', '', '', '', '']
#     print(array_string)
#     for i in range(len(array)-1,-1,-1):
#         pass
#     print('结果：',array_string)

# demo3()

def demo4():
    li = '<ul><li>111</li><li>222</li><li>333<ul><li>1111</li><li>2221</li><li>3333</li><li>4444</li></ul></li><li><ul><li>5555</li><li>6666</li><li>7777</li><li><ul><li>aaaa</li><li>bbbb</li><li>cccc</li><li>dddd</li></ul></li><ul><li>eeee</li><li>ffff</li><li>gggg</li><li>hhhh</li></ul></ul>444</li><ol><li>啊啊啊</li><li>哦哦哦</li><ol><li>啊啊啊11</li><li>哦哦哦222</li></ol></ol></ul>'

    ul = re.findall(r'\<ul\>[\w\W]+\<\/ul\>|\b(\w+(?![^<>]*>))\b',li)

    for item in ul:
        print(item)

demo4()