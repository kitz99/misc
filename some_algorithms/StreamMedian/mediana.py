from max_heap import MaxHeap
from min_heap import MinHeap

if __name__ == '__main__':
	sup = MaxHeap([]) # MAX_HEAP
	inf = MinHeap([]) # MIN_HEAP
	n = 0
	while True:
		# citesc numarul pe care vreau sa il inserez
		x = input("Numar: ")
		x = int(x)
		sup.insert(x) # inseram in max-heap
		if n % 2 == 0:
			if inf.heap_size > 0: # daca am elemente in minheap
				if sup.max() > inf.min(): # daca radacina maxHeap-ului > radacina minHeapului
					# extrag radacinile si le inserez in cruce
					toMin = sup.pop_max()
					toMax = inf.pop_min()
					sup.insert(toMax)
					inf.insert(toMin)
		else: # daca numarul de numere e impar
			toMin = sup.pop_max() 
			inf.insert(toMin)
			# extrag radacina maxHeap-ului si o inserez in minHeap

		n += 1 # crestem numarul de elemente procesate
		
		# getting the median
		if n % 2 == 0:
			print (sup.max() + inf.min())/2.0
		else:
			print sup.max()






	




