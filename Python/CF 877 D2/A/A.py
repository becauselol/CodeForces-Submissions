def solve():
	n = int(input())
	arr = [int(i) for i in input().split()]
	mp, mn = float("-inf"), float("-inf")

	for i in arr:
		if i < 0:
			mn = max(mn, i)
		else:
			mp = max(mp, i)


	if mn > float("-inf"):
		print(mn)
	else:
		print(mp)


t = int(input())
for _ in range(t):
	solve()