global x
global DIF
global n

def back(k, DIF, x, n):
	if k == n:
		print x
	else:
		x[k] = '('
		DIF += 1
		if DIF <= n - k:
			back(k + 1, DIF, x, n)
		DIF -= 1
		x[k] = ')'
		DIF -= 1
		if DIF >= 0:
			back(k + 1, DIF, x, n)
		DIF += 1


if __name__ == '__main__':
	n = 
	x = [0 for _ in range(0, n+1)]
	DIF = 0
	k = 0
	x[k] = "("
	DIF = 1
	back(1, DIF, x, n)