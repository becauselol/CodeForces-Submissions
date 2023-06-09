# idk how
def solve():
	n = int(input())
	arr = [int(i) for i in input().split()]

	one = arr.index(1)

	l = arr.index(n)

	if one < n and arr[one + 1] < arr[one - 1]:
		print(str(one + 2) + " " + str(l+1))
	elif one > 0 and arr[one - 1] > arr[one + 1]:
		print(str(one) + " " + str(l+1))
	else:
		print(str(one+1) + " " + str(one+1))

t = int(input())
for _ in range(t):
	solve()