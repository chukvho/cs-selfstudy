"""Nonlocal"""
# Q 1.1
def memory(n):
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

"""Mutation"""
# Q 2.2
def mystery(p, q):
    p[1].extend(q[1][0])
    q[1][0].append(p[1:])
    
# p = [2, 3]
# q = [4, [p]]
# mystery(q[1][0], q)

# Q 2.3
def group_by(s, fn):
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped: # 直接使用in检查字典中是否有这个键
            grouped[key].append(e)
        else:
            grouped[key] = [e]
    return grouped

# Q 2.4
def add_this_many(x, el, s):
    # count = 0
    # for i in s:
    #     if i == x:
    #         count += 1
    # while count > 0:
    #     s.append(el)
    #     count -= 1
    count = s.count(x)
    s.extend([el] * count)
    
"""Generators"""
# 4.1
def filter(iterable, fn):
    for x in iterable:
        if fn(x):
            yield x
            
# 4.2
def merge(a, b):
    next_a = next(a)
    next_b = next(b)
    
    while True:
        if next_a < next_b:
            yield next_a
            next_a = next(a)
        elif next_a > next_b:
            yield next_b
            next_b = next(b)
        else:
            yield next_a
            next_a = next(a)
            next_b = next(b)