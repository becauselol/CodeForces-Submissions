def solve():
	s = input()
	arr = ""
	q = 0
	for c in s:
		if c == "?":
			q += 1
			continue 

		if q > 0:
			if arr == "":
				arr += "0" * q
			elif arr[-1] == "1" and c == "1":
				arr += ("1" * q)
			else:
				arr += ("0" * q)
			q = 0

		arr += c
		# print(c, arr)

	if q > 0:
		if arr[-1] == "0":
			arr += ("0" * q)
		else:
			arr += ("1" * q)
	print(arr)



t = int(input())
for _ in range(t):
	solve()