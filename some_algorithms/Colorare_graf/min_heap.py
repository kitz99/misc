class MinHeap(object):
	"""implementation of a min heap"""

	def __init__(self, array):
		self.elem = array
		self.heap_size = len(array)
		self.build_min_heap()


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


	def build_min_heap(self):
		for i in range(self.heap_size-1 // 2, -1, -1):
			self.min_heapify(i)

	def insert(self, val):
		self.elem.append(val)
		self.heap_size += 1
		self.min_heapify(self.heap_size - 1)

	def min(self):
		return self.elem[0]

	def pop_min(self):
		value = self.min()
		self.elem[0] = self.elem[self.heap_size-1]
		self.elem.pop()
		self.heap_size -= 1
		self.min_heapify(0)
		return value

	def isEmpty(self):
		if self.elem:
			return False
		return True