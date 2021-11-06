# 正则溢出
# 官方开发者给出的demo
# 地址：https://bugs.python.org/issue38582%3E


def offical_re_demo():
    import re

    NUM = 100

    # items = [ '(001)', '(002)', '(003)', ..., '(NUM)']
    items = [r'(%03d)' % i for i in range(1, 1+NUM)]

    print(items)
    pattern = '|'.join(items)

    print(pattern)  # (001)|(002)|(003)|(004)

    # repl = '\1\2\3...\NUM'
    temp = ('\\' + str(i) for i in range(1, 1+NUM))

    print(temp)
    repl = ''.join(temp)  # \\1
    print(repl)

    text = re.sub(pattern, repl, '(001)')
    print(text)

    # if NUM == 99
    # output: (001)
    # if NUM == 100
    # output: (001@)
    # if NUM == 101
    # output: (001@A)


def actual_re_demo():
    import re
    # 这个是一个不定长的字符串...
    text = "tf.where(condition, x=None, y=None, name=None) tf.batch_gather ..."

    # 准备编译为re,将那些需要匹配的字段转为正则表达式，也是一个不定长
    pattern_str = re.compile('(tf\\.batch_gather)|(None)|(a1)')

    # 因为不知道有多少个，所以这里超出了\\100 \\n
    x = re.sub(pattern_str, '`'+'\\1\\2'+'`', text)

    print(x)

    # hope 假如tf.前缀需要匹配，所以希望返回的结果是:`tf.xx`，

    # 但实际上，这里并不仅仅是tf. 作为前缀，它是一个随机性的字符,也可能为后缀，也可能为其他字符。

    # 有什么办法能够解决这个demo 提出的问题呢？

    #  如果超过100,结果为=>：989¡¢£¤¥¦§89¨©ª«¬­®¯89°±²³´µ¶·89¸¹º»¼½¾¿890123`, name=`None@ABCDEFG89HIJKLMNO89PQRSTUVW89XYZ[\]^_89`abcdefg89hijklmno89pqrstuvw89xyz{|}~8901234567890123456789

    # 我注意到评论区里面提到的，是一个进制混淆的问题引发的，这事情似乎变得尴尬。


# actual_re_demo()


def no_need_re():
    text = "tf.where(condition, x=None, y=None, name=None) tf.batch_gather ..."
    pattern_list = ['tf.batch_gather', 'None']
    for item in pattern_list:
        text=text.replace(item, '`'+item+'`')

    print(text)

no_need_re()