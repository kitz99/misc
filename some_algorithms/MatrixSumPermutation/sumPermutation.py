def cont(x, k):
	for i in range(k):
		if x[i] == x[k]:
			return False
	return True

def main():
	f = file("input.txt", "r")
	(n, s) = [int(_) for _ in f.readline().split(" ")]
	a = [[0] * n for _ in range(n) ]


	for i in range(n):
		for j in range(n):
			num = f.read(1)
			if num == "\n" or num == " ":
				num = f.read(1)
			a[i][j] = int(num)

	f.close()

	"""
	vom genera permutari de cate k elemente,
	fiecare element al permutarii va fi considerat indice de coloana pentru o anumita linie i 
	daca se respecta conditia impusa de suma, printam rezultatul si oprim generarea permutarilor.
	"""

	x = [0 for _ in range(n)]
	k = 0
	x[k] = -1
	while k > -1:
		x[k] = x[k] + 1
		if x[k] > n - 1:
			k -= 1
		else:
			if cont(x, k):
				if k == n - 1:
					sum_part = 0
					numbers = []
					for elem in x:
						sum_part = sum_part + a[x.index(elem)][elem]
						numbers.append(a[x.index(elem)][elem])
					if sum_part == s:
						print numbers
						print x
						print "---------------------------"
				else:
					k += 1
					x[k] = -1



if __name__ == '__main__':
	main()