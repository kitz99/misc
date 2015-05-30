# merge sort implementation
import math
from heapq import merge

def merge_sort(a):
	if len(a) <= 1:
		return a 
	mid = len(a) // 2
	left = merge_sort(a[:mid])
	right = merge_sort(a[mid:])
	return list(merge(left, right))


if __name__ == '__main__':
	v = [1, 7, 9, 3, 2, -1, -19]
	v = merge_sort(v)
	print v