class Node(object):
	"""a node of the tree"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parrent = None


class BST(object):
	"""Binary search tree"""
	def __init__(self, root_val):
		self.root = Node(root_val)

	def insert(self, root, node):
		if root is None:
			return Node(node)
		else:
			if node > root.value:
				root.right = self.insert(root.right, node)
				root.right.parrent = root
			else:
				root.left = self.insert(root.left, node)
				root.left.parrent =  root 
		return root

	def insert_bulk(self, values):
		for elem in values:
			self.insert(self.root, elem)


	def srd(self, node):
		if node is not None:
			self.srd(node.left)
			print node.value
			self.srd(node.right)

	def GetInorderSuccesor(self, node):
		# pas 1: Daca am subarbore drept, atunci sigur succesorul este minimul din subarborele drept
		if node.right is not None:
			return self.minValue(node.right)
		# pas 2: Sigur succesorul se gaseste printre fii
		parinte = node.parrent
		while parinte is not None and node == parinte.right:
			node = parinte
			parinte = parinte.parrent

		return parinte



	def minValue(self, node):
		current = node
		while current.left is not None:
			current = current.left
		return current



if __name__ == '__main__':
	T = BST(2)
	T.insert_bulk([7, 6, 3, 11])