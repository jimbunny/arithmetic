# 1、实现一个函数，对一个正整数n，算得到1需要的最少操作次数。操作规则为：如果n为偶数，将其除以2；如果n为奇数，可以加1或减1；一直处理下去。

# 例子：
# func(7) = 4，可以证明最少需要4次运算
# n = 7
# n-1 6
# n/2 3
# n-1 2
# n/2 1
# 要求：实现函数(实现尽可能高效) int func(unsign int n)；n为输入，返回最小的运算次数。给出思路(文字描述)，完成代码，并分析你算法的时间复杂度。


def func(value):
    count = 0
    if value % 2 == 0:
        count += 1
        func(value / 2)
    else:
        count += 1
        if value == 1:
            return count
        else:
            func((value - 1) / 2)
    return count

if __name__ == '__main__':
    print func(7)
