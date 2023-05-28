n = int(input())

for _ in range(n):
	length = int(input())
	b = input()

	arr = [0]
	m_arr = [0]
	x_arr = [0]
	mini = 0
	maxi = 0

	for i in range(length):
		if b[i] == ">":
			arr.append(arr[-1] - 1)
			x_arr.append(x_arr[-1] - 1)
			if m_arr[-1] == mini:
				m_arr.append(m_arr[-1] - 1)
				mini -= 1
			else:
				m_arr.append(mini)


		else:
			arr.append(arr[-1] + 1)
			m_arr.append(m_arr[-1] + 1)
			if x_arr[-1] == maxi:
				x_arr.append(x_arr[-1] + 1)
				maxi += 1
			else:
				x_arr.append(maxi)


	print(min(len(set(arr)), len(set(m_arr)), len(set(x_arr))))



