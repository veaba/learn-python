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
9. 步调可短可长，无法确定
10. 左边对应的值，可比它大，也可以比它小

# ***********排列组合问题***********
11. 验证到最后，可以通过一个排列组合的问题来计算出来，但这个不够！
12. 左边奇数，右边必定为偶数，反之亦然
13. 左边+右边，必定为奇数,而值有重复的
14. 最小奇数、最大奇数都是确定的

# ***********标记算法***********
15. [[][[]][]]
16. [[][[]][[]]]
"""

# all_array = []  # 可以根据left_array 算出来
# left_array = [0, 1, 2, 4] √
# left_array = [0, 1, 2, 3, 4] √
# left_array = [0, 1, 2, 5, 7] √
# left_array = [0, 1] √
# left_array = [0, 1, 3, 4, 5, 6, 11] √
left_array = [0, 1, 3, 5, 7, 8, 9, 11]  # =>[15,2,4,6,14,13,10,12]


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
        # 最后一个
        print('==>', k, left_len_value)
        if k == left_len_value - 1:
            right_array.insert(0, v + 1)
        # 第一个
        elif k == 0:
            right_array.insert(0, max_value)

        # # 第二个
        # elif k == 1:
        #     spe_array = list(set(right_array_temp).difference(set(right_array)))
        #     right_value = min(spe_array)
        #     right_array.insert(0, right_value)
        # else:
        #     pre_left_value = left[k + 1]  # 上一个索引值
        #     step = pre_left_value - v  # 上个值减去当前的值
        #     pre_right_value = right_array[0]  # 上个值对应左边的值
        #     if pre_right_value + step in right_array or pre_right_value + step in left_array:
        #         print('哈哈', k, pre_right_value - step)
        #         right_array.insert(0, pre_right_value - step)
        #     else:
        #         print('哦哦', k, pre_right_value - step)
        #         right_array.insert(0, pre_right_value + step)

            # right_array.insert(0, '擦')
    print('left:', left)
    print('right:', right_array)


level(left_array)
