n = int(input())

for _ in range(n):
	length = input()
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]


	mod_a = [(v, i) for i, v in enumerate(a)]
	mod_a = sorted(mod_a)
	b = sorted(b)
	pack = [(mod_a[i][1], b[i]) for i in range(len(b))]
	pack = sorted(pack)

	res = [str(v) for idx, v in pack]
	print(" ".join(res))
