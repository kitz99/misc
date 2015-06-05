import heapq

class StreamMedian(object):
	"""mediana unui sir de numere"""
	def __init__(self):
		self.minHeap, self.maxHeap = [], []
		self.N = 0

	def insert(self, num):
		if self.N % 2 == 0:
			heapq.heappush(self.maxHeap, -1*num)
			self.N += 1
			if len(self.minHeap) == 0:
				return
			if -1 * self.maxHeap[0] > self.minHeap[0]:
				toMin = -1 * heapq.heappop(self.maxHeap)
				toMax = heapq.heappop(self.minHeap)
				heapq.heappush(self.maxHeap, -1 * toMax)
				heapq.heappush(self.minHeap, toMin)		
		else:
			toMin = -1 * heapq.heappushpop(self.maxHeap, -1*num)
			heapq.heappush(self.minHeap, toMin)
			self.N += 1

	def getMedian(self):
		if self.N % 2 == 0:
			return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0
		else:
			return -1 * self.maxHeap[0]


if __name__ == '__main__':
	sm = StreamMedian()
	while True:
		x = input("numar: ")
		x = int(x)
		sm.insert(x)
		print sm.getMedian()



