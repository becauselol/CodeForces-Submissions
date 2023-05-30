def solve():
	n = int(input())
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	
	curr = None
	max_a = {}
	c = 0
	for i in a:
		if curr == None:
			curr = i 
			c += 1
			continue 
		if i == curr:
			c += 1
			continue 
		if i != curr:
			if curr not in max_a:
				max_a[curr] = c
			else:
				max_a[curr] = max(max_a[curr], c)

			curr = i 
			c = 1
	if curr not in max_a:
		max_a[curr] = c
	else:
		max_a[curr] = max(max_a[curr], c)

	curr = None
	max_b = {}
	c = 0
	for i in b:
		if curr == None:
			curr = i 
			c = 1
			continue 
		if i == curr:
			c += 1
			continue 
		if i != curr:
			if curr not in max_b:
				max_b[curr] = c
			else:
				max_b[curr] = max(max_b[curr], c)

			curr = i 
			c = 1
	if curr not in max_b:
		max_b[curr] = c
	else:
		max_b[curr] = max(max_b[curr], c)
	# print(max_a)
	# print(max_b)
	longest = 1
	for k, v in max_b.items():
		if k in max_a:
			longest = max(longest, v + max_a[k])
		else:
			longest = max(longest, v)
	for k, v in max_a.items():
		longest = max(longest, v)
		
	print(longest)
	


t = int(input())
for _ in range(t):
	solve()