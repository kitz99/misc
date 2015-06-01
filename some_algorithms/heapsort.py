class Heap(object):
	"""implementation of a heap"""
	def __init__(self, array):
		self.elem = array
		self.heap_size = len(array)


	def max_heapify(self, i):
		l = 2 * i + 2
		r = 2 * i + 2
		largest = i
		if l < self.heap_size and self.elem[l] > self.elem[largest]:
				largest = l

		if r < self.heap_size and self.elem[r] > self.elem[largest]:
				largest = r 

		if largest != i:
			self.elem[i], self.elem[largest] = self.elem[largest], self.elem[i]
			self.max_heapify(largest)

	def min_heapify(self, i):
		l = 2 * i + 1
		r = 2 * i + 2
		smallest = i 
		if l < self.heap_size and self.elem[l] < self.elem[smallest]:
			smallest = l
		if r < self.heap_size and self.elem[r] < self.elem[smallest]:
			smallest = r 

		if smallest != i:
			self.elem[i], self.elem[smallest] = self.elem[smallest], self.elem[i]
			self.min_heapify(smallest)


	def build_max_heap(self):
		for i in range(self.heap_size-1 // 2, -1, -1):
			self.max_heapify(i)

	def heapsort_asc(self):
		self.build_max_heap()
		for i in range(len(self.elem)-1, -1, -1):
			self.elem[0], self.elem[i] = self.elem[i], self.elem[0]
			self.heap_size -= 1
			self.max_heapify(0)




if __name__ == '__main__':
	v = [8, 3, 21, 1, 6, 18, 0, 22, 14] 
	H = Heap(v)
	H.heapsort_asc()
	print H.elem

		