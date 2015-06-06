""" 
	Se da x < 1000000. Sa se gaseasca numarul minim de numere prime p1, p2 .. pk
	astfel incat p1 + p2 + p3 + .. + pk = x.
"""
def Goldbach(x, sive):
	if sive[x] is True:
		return [1]
	i = x - 1
	while True:
		while sive[i] is False:
			i -= 1
		if sive[x - i] is True:
			return[i, x - i]
		else:
			i -= 1


def main():
	x = int(input("Number: "))

	sive = [True for _ in range(0, 1000010)]

	sive[1] = False
	for i in range(1, x + 5):
		if sive[i] is True:
			j = 2 * i 
			while j <= x + 5:
				sive[j] = False
				j += i 

	if x == 0:
		print 0
	if x == 0:
		print 0
	if sive[x] is True:
		print 1
	else:
		if x % 2 == 0:
			print 2
		else:
			i = x - 1
			while sive[i] is False:
				i -= 1
			print 1 + len(Goldbach(x - i, sive))


if __name__ == '__main__':
	main()