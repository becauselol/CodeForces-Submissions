from collections import Counter

n = int(input())

for _ in range(n):
	s, m = [int(i) for i in input().split()]

	arr = [int(i) for i in input().split()]

	c = Counter(arr)

	
