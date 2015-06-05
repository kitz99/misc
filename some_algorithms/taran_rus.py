if __name__ == '__main__':
	x = 5
	y = 16
	p = 0
	while x > 0:
		if x % 2 == 1:
			p = p + y
		x = x / 2
		y = y + y

	print p