"""Tree"""
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch) # Verifies the tree difinition
    return [label] + list(branches) # Creates a list from a sequence of branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
    # Verifies that tree is bound to a list
        return False
    for branch in branches(tree): # 对每一层的branches也进行判断
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_leaves(t):
    """Count the leaves of a tree."""
    if is_tree(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)

def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else: # sum a list of lists, get a list containing the elements of those lists
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

"""Below is for disc5"""
#1.1
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return 1 + max( height(branch) for branch in branches(t))


# t = tree(3, [tree(5, [tree(1)]), tree(2)])
# print("Tree hight:", height(t))

#1.2
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max(max_path_sum(branch) for branch in branches(t))

# t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
# print("Max path sum:", max_path_sum(t))

#1.3
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
               [tree(2,
                     [tree(3),
                      tree(4)]),
                tree(5,
                [tree(6,
                      [tree(7)]),
                 tree(8)])])
    >>>print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    newlabel = label(t)**2
    newbranches = [square_tree(branch) for branch in branches(t)] # 不用再额外判定branches是否存在了 调用branches的时候已经判定了
    return tree(newlabel, newbranches)

# numbers = tree(1,
#                [tree(2,
#                      [tree(3),
#                       tree(4)]),
#                 tree(5,
#                 [tree(6,
#                       [tree(7)]),
#                  tree(8)])])
# print_tree(square_tree(numbers))

#1.4
def find_path(tree, x):
    """
        >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
        >>> find_path(t, 5)
        [2, 7, 6, 5]
        >>> find_path(t, 10)  # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for branch in branches(tree):
        path = find_path(branch, x)
        if path:
            return [label(tree)] + path

# t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
# print(find_path(t, 5))

"""Binary Numbers"""
def prune_binary(t, nums):
    if is_leaf(t): # 已经遍历到leaves了
        if label(t) in nums:
        # 这里的代码疑问：label(t)是一个str，而nums是list，为什么可以直接调用
        # 解释：当递归到树的叶子结点时，nums很有可能被修剪到只剩下一个字符，所以如果恰好对应上那么就是这一条路径成立；否则回复None
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num and num[0] == label(t)] # 最后的if是检查num是否为真，为了确保num不是空字符串，后一个是为了检查num的第一个字符是否等于当前树节点的标签
        new_branches = []
        for branch in branches(t):
            pruned_branch = prune_binary(branch, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)

# t = tree("1", [tree("0", [tree("0"), tree("1")]), tree("1", [tree("0")])])
# print_tree(prune_binary(t, ["01", "110", "100"]))
# 1
#   0
#     0
#   1
#     0