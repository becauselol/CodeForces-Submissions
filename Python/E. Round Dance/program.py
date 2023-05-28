## I gave up idk how to do

from collections import deque, defaultdict
n = int(input())

for _ in range(n):
	p = int(input())
	arr = [int(i) - 1 for i in input().split()]

	edge_map = defaultdict(list)
	for u, v in enumerate(arr):
		edge_map[u].append((v,1))
		edge_map[v].append((u,-1))

	parent = [None] * p 
	visited = [False] * p
	d = [None] * p

	cycles = 1
	components = 0

	for u in range(p):
		if not visited[u]:
			components += 1

			q = deque([u])
			visited[u] = True
			d[u] = 0
			while q:
				curr = q.popleft()

				for n, dist in edge_map[curr]:

					if not visited[n]:
						visited[n] = True
						q.append(n)
						parent[n] = curr
						d[n] = d[curr] + dist
					else:
						if d[curr] - d[n] > 1:
							cycles += 1
						# elif parent[n] == None:
						# 	parent[n] = curr 
						# 	components -= 1

	# print(arr)
	# print(parent)
	# print(d)
	# print(cycles)
	minimum = max(1, cycles)
	maximum = components
	print(str(minimum) + " " + str(maximum))