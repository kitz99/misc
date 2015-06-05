def partition(a, l, r):
	x = a[r-1]
	i = l - 1
	for j in range(l, r):
		if a[j] <= x:
			i += 1
			a[i], a[j] = a[j], a[i]

	a[i + 1], a[r-1] = a[r-1], a[i + 1]
	return i + 1
def hore(a, start, end):
	x = a[start]
	i = start - 1
	if end == len(a):
		j = end
	else:
		j = end + 1
	while True:
		while True:
			j -= 1
			if a[j] <= x:
				break

		while True:
			i += 1
			if a[i] >= x:
				break
		if i < j:
			a[i], a[j] = a[j], a[i]
		else:
			return j
def quicksort(a, l, r):
	if l < r:
		pivot = hore(a, l, r)
		print pivot
		quicksort(a, l, pivot - 1)
		quicksort(a, pivot + 1, r)


if __name__ == '__main__':
	v = [8, 3, 21, 1, 6, 18, 0, 22, 14]
	quicksort(v, 0, len(v))
	print v