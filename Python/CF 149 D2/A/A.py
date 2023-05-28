n = int(input())

for _ in range(n):
	x, k = input().split()
	x, k = int(x), int(k)

	if x % k != 0:
		print(1)
		print(x)
		continue 
	else:
		print(2)
		num = k + 1 
		if num % k == 0:
			num = k - 1
		print(str(num) + " " + str(x - num))