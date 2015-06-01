class Node(object):
	"""a node of the tree"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BST(object):
	"""Binary search tree"""
	def __init__(self, root_val):
		self.root = Node(root_val)

	def insert(self, root, node):
		if root is None:
			return node
		else:
			if node.value > root.value:
				root.right = self.insert(root.right, node)
			else:
				root.left = self.insert(root.left, node)
		return root

	def srd(self, node):
		if node is not None:
			self.srd(node.left)
			print node.value
			self.srd(node.right)



if __name__ == '__main__':
	T = BST(2)
	T.insert(T.root, Node(6))
	T.insert(T.root, Node(3))
	# # print T.root.left.value
	# # print T.root.right.value
	T.insert(T.root, Node(1))
	T.insert(T.root, Node(19))
	T.insert(T.root, Node(4))
	T.insert(T.root, Node(54))
	T.insert(T.root, Node(7))
	T.srd(T.root)
	print T.search(7, T.root)