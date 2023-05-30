def solve():
	l = int(input())
	arr = [str(l + 1 - int(i)) for i in input().split()]
	print(" ".join(arr))

t = int(input())
for _ in range(t):
	solve()