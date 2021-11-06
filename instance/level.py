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
# left_array = [0, 1, 2, 4] # [7, 6, 3, 5]
# left_array = [0, 1, 2, 3, 4]  # [9,8,7,6,5]
# left_array = [0, 1, 2, 5, 7]  # [9, 4, 3, 6, 8]
# left_array = [0, 1] # [3,2]
# left_array = [0, 1, 3, 4, 5, 6, 11]  # [13, 2, 10, 9, 8, 7, 12]
# left_array = [0, 1, 2, 4, 7]  # => [9, 6, 3, 5, 8]
left_array = [0, 1, 3, 5, 7, 8, 9, 11]  # =>[15,2,4,6,14,13,10,12]


# 是偶数则返回True，否则返回False
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# 解析算法
def level(left):
    left_count = len(left)
    all_array = [i for i in range(left_count * 2)]
    # 可以得出右边的元素集合，但此时，次序是错乱的.
    right_array_temp = list(set(all_array).difference(set(left)))
    right_array = []
    # 最后一个索引1，使用差值替换
    # 1. 总长度
    all_len = len(all_array)
    # 2. 最大值
    max_value = all_len - 1
    # 3. 左边总长度(和右边总长度是相等的)
    left_len_value = len(left)

    # for item in enumerate(left):
    for i in range(left_len_value - 1, -1, -1):
        k = i  # 索引值
        v = left[i]  # 当前值
        # 最后一个
        if k == left_len_value - 1:
            right_array.insert(0, v + 1)
        # 第一个
        elif k == 0:
            right_array.insert(0, max_value)
        else:
            # 比v大，且与v奇偶互斥。且不存在left 且不存在right里面
            right_stay_array = list(set(right_array_temp).difference(set(right_array)))  # 去临时数组和right_array的交集
            big_then_array = [big for big in right_stay_array if big > v]  # 取出比v还大的数组
            # 取出奇偶互斥的数组
            if is_even(v):
                mutex_array = [mutex for mutex in big_then_array if not is_even(mutex)]  # 当v为偶数时候，取出奇数
            else:
                mutex_array = [mutex for mutex in big_then_array if is_even(mutex)]  # 当v为奇数时候，取出偶数
            min_value = min(mutex_array)
            right_array.insert(0, min_value)

    print('left :', left)
    print('      ', ' ↓ ' * left_len_value)
    print('right:', right_array)


level(left_array)
