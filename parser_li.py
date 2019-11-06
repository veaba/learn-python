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
    li ='<ul><li>11111<ul><li>222</li><ul><li>4444</li></ul></ul></li></ul>'
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

    a=re.sub(r'\]",','],',a)
    print(6.1,a)

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

demo1()