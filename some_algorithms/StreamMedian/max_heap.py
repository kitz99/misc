class MaxHeap(object):
	"""implementation of a max heap"""
	
	def __init__(self, array):
		self.elem = []
		for i in array:
			self.elem.append(i)
		self.heap_size = len(array)
		self.build_max_heap()

	def max_heapify(self, i):
		l = 2 * i + 1
		r = 2 * i + 2
		largest = i
		if l < self.heap_size and self.elem[l] > self.elem[largest]:
				largest = l

		if r < self.heap_size and self.elem[r] > self.elem[largest]:
				largest = r 

		if largest != i:
			self.elem[i], self.elem[largest] = self.elem[largest], self.elem[i]
			self.max_heapify(largest)


	def build_max_heap(self):
		for i in range(self.heap_size-1 // 2, -1, -1):
			self.max_heapify(i)

	def insert(self, val):
		self.elem.append(val)
		self.heap_size += 1
		self.elem[self.heap_size - 1], self.elem[0] = self.elem[0], self.elem[self.heap_size - 1]
		self.max_heapify(0)

	def pop_max(self):
		value = self.max()
		self.elem[self.heap_size - 1], self.elem[0] = self.elem[0], self.elem[self.heap_size - 1]
		self.heap_size -= 1
		self.elem.pop()
		self.max_heapify(0)
		return value

	def max(self):
		return self.elem[0]