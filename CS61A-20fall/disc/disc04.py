# Tree Recursion
def count_stair_ways(n):
	if n == 0 or n == 1:
		return 1
	else:
		stepone = count_stair_ways(n-1)
		steptwo = count_stair_ways(n-2)
		return stepone + steptwo

def count_k(n, k):
	if k == 0 or n < 0: # 步数方案不对
		return 0  # 需要对于两个参数都进行base的限制
	elif n == 0: # base case
		return 1
	else:
		withk = count_k(n-k, k)
		withoutk = count_k(n, k-1)
		return withk + withoutk

#List
def max_products(s):
	if not s:
		return 1
	else:
		withfirst = s[0] * max_products(s[2:])
		withoutfirst = max_products(s[1:])
		return max(withfirst, withoutfirst)