n = int(input())

for _ in range(n):
	length = int(input())
	b = [int(i) for i in input().split()]

	odds = []
	evens = []

	min_o = float("inf")
	min_e = float("inf")

	for v in b:
		if v % 2 == 0:
			evens.append(v)
			min_e = min(min_e, v)
		else:
			odds.append(v)
			min_o = min(min_o, v)

	if not odds or not evens:
		print("YES")
		continue 

	if min_o < min_e:
		print("YES")
	else:
		print("NO")