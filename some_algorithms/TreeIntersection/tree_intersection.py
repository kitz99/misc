from binary_search_tree import BST


if __name__ == '__main__':
	T1 = BST(7)
	T1.insert_bulk([1, 8, 23, 12, 5])
	
	T2 = BST(54)
	T2.insert_bulk([1, 8, 23, 12, 5])

	n1 = T1.minValue(T1.root)
	n2 = T2.minValue(T2.root)

	while(n1 is not None and n2 is not None):
		if n1.value == n2.value:
			print n1.value
			n1 = T1.GetInorderSuccesor(n1)
			n2 = T2.GetInorderSuccesor(n2)
		else:
			if n1.value > n2.value:
				n2 = T2.GetInorderSuccesor(n2)
			else:
				n1 = T1.GetInorderSuccesor(n1)
	print "This is it"

	