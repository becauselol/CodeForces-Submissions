n = int(input())

for _ in range(n):
	length = int(input())
	string = input()

	s = set()
	for i in range(length - 1):
		s.add(string[i:i+2])

	print(len(s))
