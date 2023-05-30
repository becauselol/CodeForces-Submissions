from collections import defaultdict, deque

def solve():
	e = int(input())
	be = defaultdict(set)
	ee = defaultdict(set)

	for _ in range(e - 1):
		u, v = input().split()
		u, v = int(u), int(v)
		ee[u].add(v)
		ee[v].add(u)


		if v in ee:
			be[u] = be[u].union(ee[v])
			for k in be[v]:
				ee[k].add(u)
			
		if u in ee:
			be[v] = be[v].union(ee[u])
			for k in be[u]:
				ee[k].add(v)

	q = deque([1])
	visited = set([1])
	reads = 1
	while q:
		curr = q.popleft()
		add = False

		for nei in ee[curr]:
			if nei not in visited:
				q.append(nei)
				visited.add(nei)

		for nei in be[curr]:
			if nei not in visited:
				q.append(nei)
				visited.add(nei)
				add = True

		reads += int(add)

	print(reads)



t = int(input())

for _ in range(t):
	solve()