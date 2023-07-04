def solve():
	n, k, x = [int(i) for i in input().split()]
	if (k == 1 and x == 1) or (n % 2 == 1 and k == 2 and x == 1):
		print("NO")
		return

	if x != 1:
		print("YES")
		print(n)
		s = "1"
		for _ in range(n - 1):
			s += " 1"
		print(s)
		return

	if n % 2 == 0:
		print("YES")
		print(n // 2)
		s = "2"
		for _ in range(n // 2 - 1):
			s += " 2"
		print(s)
		return
	else:
		print("YES")
		print(n // 2)
		s = "3"
		for _ in range(n // 2 - 1):
			s += " 2"
		print(s)




t = int(input())
for _ in range(t):
	solve()