import math
from collections import defaultdict

class Node(object):
	def __init__(self, numKeys):
		self.numKeys = numKeys
		self.keys = []
		self.values = []
		self.leaf = True
		self.internal = False
		self.isRoot = False

	'''Add value to node'''
	def addValue(self, key, value):
		if len(self.keys) == 0:
			self.keys.append(key)
			self.values.append(value)
			return
		if key in self.keys:
			raise Exception('Key is already present. No duplicates allowed!')
		for i, item in enumerate(self.keys):
			if key < item:
				self.keys.insert(i, key)
				self.values.insert(i, value)
				break
			elif i+1 == len(self.keys):
				self.keys.append(key)
				self.values.append(value)
				break

	'''print method that prints the tree and leaf data'''
	def printMethod(self, dic, level = 0):
		dic[level].append(str(self.keys))
		if self.leaf:
			for i in range(len(self.values)):
				dic[level].append(str(self.values[i]))
		if not self.leaf:
			for item in self.values:
				item.printMethod(dic, level+1)
		return dic

	'''retuns true if full'''
	def isFull(self):
		return (len(self.keys) == self.numKeys - 1)

	'''splits a root and pulls new key up'''
	def rootSplit(self):
		left = Node(self.numKeys)
		right = Node(self.numKeys)
		middle = 0
		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2
		else:
			middle = (len(self.keys) - 1) // 2
		left.keys = self.keys[:middle]
		left.values = self.values[:middle]
		right.keys = self.keys[middle:]
		right.values = self.values[middle:]

		self.keys = [right.keys[0]]
		self.values = [left , right]
		self.leaf = False

	'''splits a leaf node'''
	def leafSplit(self):
		right = Node(self.numKeys)
		left = Node(self.numKeys)
		middle = 0
		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2
		else:
			middle = (len(self.keys) - 1) // 2
		left.keys = self.keys[:middle]
		left.values = self.values[:middle]
		right.keys = self.keys[middle:]
		right.values = self.values[middle:]
		return (right.keys[0], left, right)

	'''splits an internal node'''
	def internalSplit(self):
		right = Node(self.numKeys)
		left = Node(self.numKeys)
		middle = 0
		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2
		else:
			middle = math.ceil(len(self.keys) / 2) - 1
		left.keys = self.keys[:middle]
		left.values = self.values[:middle+1]
		right.keys = self.keys[middle+1:]
		right.values = self.values[middle+1:]
		return (self.keys[middle], left, right)

class Bptree(object):
	def __init__(self, numKeys):
		self.numKeys = numKeys
		self.root = Node(self.numKeys)
		self.root.isRoot = True

	'''inserts values and calls root split the first time root fills up'''
	def insert(self, key, value):
		if self.root.leaf:
			if self.root.isFull():
				self.root.addValue(key, value)
				self.root.rootSplit()
				return None
		return self.insertHelper(self.root, key, value)

	'''actual algorithm for inserting nodes into tree'''
	def insertHelper(self, node, key, value):
		if node.leaf:
			if not node.isFull():
				node.addValue(key, value)
				return None
			else:
				node.addValue(key, value)
				newKey, left, right =  node.leafSplit()
				node.keys = left.keys
				node.values = left.values
				newEntry = (newKey, right)
				return newEntry
		else:
			child = node
			child = self.findHelper(node, key)
			newEntry = self.insertHelper(child, key, value)
			if newEntry == None:
				return None
			elif not node.isFull():
				node.addValue(newEntry[0], newEntry[1])
				return None
			else:
				node.addValue(newEntry[0], newEntry[1])
				k, left, right = node.internalSplit()
				node.keys = left.keys
				node.values = left.values
				newEntry = (k , right)
				right.leaf = False
				right.internal = True
				if node.isRoot:
					newRoot = Node(self.numKeys)
					left.leaf = False
					left.internal = True
					node.keys = [newEntry[0]]
					node.values = [left, right]
					return None
				return newEntry

	'''finds proper sub tree by comparing keys'''
	def findHelper(self, node, key):
		for i, item in enumerate(node.keys):
			if key < item:
				return node.values[i]
		return node.values[i + 1]

	'''recursively calls findHelper to follow proper subtree for value'''
	def getValue(self, key):
		node = self.root
		while not node.leaf:
			node = self.findHelper(node, key)
		for i, item in enumerate(node.keys):
			if key == item:
				return node.values[i]
		return 'None'

	'''prints entire tree'''
	def printTree(self):
		d = defaultdict(list)
		objects = self.root.printMethod(d)
		for i in range(len(d)):
			print("Level: " , i , " " , d[i])				
	
