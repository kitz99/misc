def insertion_sort(a):
	for j in range(1, len(a)):
		key = a[j]
		# try to insert key in the correct position in the array
		i = j - 1
		while i >= 0 and a[i] > key:
			a[i + 1] = a[i]
			i = i - 1
		a[i + 1] = key



if __name__ == '__main__':
	v = [1, 7, 9, 3, 2, -1, -19]
	insertion_sort(v)
	print v