def solve():
	ax, ay = [int(i) for i in input().split()]
	bx, by = [int(i) for i in input().split()]
	cx, cy = [int(i) for i in input().split()]
	a = [bx - ax, by - ay, cx - ax, cy - ay]
	# print(by, cy)
	dot = (a[0] * a[2] + a[1] * a[3])

	if all([i < 0 for i in a]) or ( a[0] < 0 and a[1] < 0):
		a = [-i for i in a]
	elif a[0] >= 0 and a[1] < 0:
		a[0], a[1] = -a[1], a[0]
		a[2], a[3] = -a[3], a[2]
	elif a[0] < 0 and a[1] >= 0:
		a[0], a[1] = a[1], -a[0]
		a[2], a[3] = a[3], -a[2]

	if dot <= 0:
		print(max(min(a[0],a[2]), min(a[1], a[3])) + 1)
	else:
		print(min(a[0], a[2]) + min(a[1], a[3]) + 1)


t = int(input())
for _ in range(t):
	solve()