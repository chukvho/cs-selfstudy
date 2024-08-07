LAB_SOURCE_FILE = __file__



this_file = __file__

def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 0:
        return 0
    else:
        return n + skip_add(n-2)


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n-1, term)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 and n == 1:
        return 1
    elif m < 1 or n < 1:
        return 0
    else:
        return paths(m-1, n) + paths(m, n-1)


def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maxumum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    """
    Wrong code
    if t == 0:
        return 0
    else:
        def with_lastd(n, t):
            if t == 0:
                return 0
            return n % 10 + 10 * with_lastd(n//10, t-1)
        def without_lastd(n, t):
            if t == 0:
                return 0
            return with_lastd(n//10, t) 
            # 我的理解是：如果不采用最后一位，那么就使用前一位，前一位变成了这种情况下的最后一位。
              误区：写出来后，虽然改变了数据，不过文字上会显示在逻辑上“一直在使用最后一位”。
                   所以在排除了最后第一位后，排除不了最后第二位
    return max(with_lastd(n, t), without_lastd(n, t))
    """
    if t ==0 or n == 0:
        return 0
    use_last = max_subseq(n // 10, t - 1) * 10 + n % 10
    dont_use_last = max_subseq(n // 10, t)
    return max(use_last, dont_use_last)
"""recursion的时候选择分支之后，第二段代码是依次执行了use_last和dont_use_last。
   依次计算得出这两个值……直到到达base case的情况，得出具体的值，得到the depest case的max。
   返回到上一对应的use_last或者是dont_use_last……如此类推，最后得到最终max
"""

def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # ban iteration and sets
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp']) # Must use recursion
    True
    """
    "*** YOUR CODE HERE ***"
    """
    # Wrong code 
    在运行时一直报错 IndexError: string index out of range 所以我在中间过程中设置了很多if-else分支
    if w1[0]: # 报错问题主要是在这里，如果字符串是空，那么w1[0]是直接不存在的，所以访问出错
        if w1[0] == w2[0]:
            print(w1[0]) ## 理解错误点，输出的是w1中没有的，所以应该是w2[0]
            if w1[1]:
                return add_chars(w1[1:], w2[1:])
            else:
                print(w2)
                return None
        else:
            if w1[1]:
                return add_chars(w1,w2[1:])
            else:
                print(w2)
                return None # 在terminal中如果不是赋值语句，是会直接跳出结果的，不需要print，且print是会换行的
    else:
        print(w2)
        return None
    """
    #下面是Chatgpt修正版
    if not w1: #判断非空
        return w2
    if w1[0] == w2[0]:
        return add_chars(w1[1:], w2[1:])
    else:
        return w2[0] + add_chars(w1, w2[1:])