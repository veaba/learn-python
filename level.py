# 这是一个级别演算算法实验文件
# 这个是从pyhtmd 的解析html list标签中抽象出来去解算ul 级别的核心问题
# 2019年12月17日14:54:14

"""
-----------------------------------------------------
已知左边，求右边的结果4个demo组合
0       3    | 0       7    | 0     5   | 0       5
             | 1       6    |           |
    =>       |    =>        | 1  => 4   | 1   =>  4
             | 2       3    |           |
1       2    | 4       5    | 2     3   | 3       2
-----------------------------------------------------

特点：
1. 左右两边相加等于一个从0开始到N，递增+1的数组，且为偶数个数元素
2. 也就是说，知道左边就可以知道右边的元素，但无法定位它出现的次序
3. 这个从ul表现抽象出来的求左边对应闭包的算法问题
4. 核心问题是需要注意的是当左边的依次序递增+1的突变处理
5. 如果知道左边，右边的结果一定是唯一值
6. 右边永远是元素最大值
7. 最元素个数为2个
8. 左边的组合，并不是乱选出来的
"""

# all_array = []  # 可以根据left_array 算出来
# left_array = [0, 1, 2, 4] √
# left_array = [0, 1, 2, 3, 4] √
# left_array = [0, 1, 2, 5, 7] √
# left_array = [0, 1] √
left_array = [0, 1, 3, 4, 5, 6, 11]


def level(left):
    left_count = len(left)
    all_array = [i for i in range(left_count * 2)]

    print('全部数组：', all_array)

    # 可以得出右边的元素集合，但此时，次序是错乱的.
    right_array_temp = list(set(all_array).difference(set(left)))
    right_array = []
    # 最后一个索引1，使用差值替换
    # 1. 总长度
    all_len = len(all_array)
    # 2. 最大值
    max_value = all_len - 1
    # 3. 左边最大值
    max_left_value = max(left)
    # 4. 左边总长度(和右边总长度是相等的)
    left_len_value = len(left)

    # for item in enumerate(left):
    for i in range(left_len_value - 1, -1, -1):
        print(i, left[i])
        k = i  # 索引值
        v = left[i]  # 当前值
        if k > 1:
            # 算法一
            if max_left_value < left_len_value:
                right_value = max_value - (k * 2 - k)
                right_array.insert(0, right_value)
                print('算法一.A：', '(' + str(v) + '=>' + str(right_value) + ')')
            # 算法二，还不对~
            else:
                right_value = all_len - (max_value - v)
                right_array.insert(0, right_value)
                print('算法二.B：', '(' + str(v) + '=>' + str(right_value) + ')')
        elif k == 1:
            spe_array = list(set(right_array_temp).difference(set(right_array)))
            right_value = min(spe_array)
            right_array.insert(0, right_value)
            print('算法二.A：', '(' + str(v) + '=>' + str(right_value) + ')')
        else:
            print('算法三.A：', '(' + str(v) + '=>' + str(max_value) + ')')


level(left_array)
