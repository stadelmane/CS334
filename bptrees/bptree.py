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

	def printMethod(self, dic, level = 0):

		# print(level, str(self.keys))
		dic[level].append(str(self.keys))

		if self.leaf:
			for i in range(len(self.values)):
				dic[level].append(str(self.values[i]))
				# print(level, self.values[i])

		if not self.leaf:
			for item in self.values:
				#print(item.values)
				item.printMethod(dic, level+1)

		return dic


	def isFull(self):
		return (len(self.keys) == self.numKeys - 1)

	def rootSplit(self):
		left = Node(self.numKeys)
		right = Node(self.numKeys)
		middle = 0
		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2

			left.keys = self.keys[:middle]
			left.values = self.values[:middle]
			#print("left keys" , left.keys , "left values" , left.values)

			right.keys = self.keys[middle:]
			right.values = self.values[middle:]

			#print("right keys" , right.keys , "right values" , right.values)
		else:
			middle = (len(self.keys) - 1) // 2
			#print(middle)

			left.keys = self.keys[:middle]
			left.values = self.values[:middle]
			#print("left keys" , left.keys , "left values" , left.values)

			right.keys = self.keys[middle:]
			right.values = self.values[middle:]

			#print("right keys" , right.keys , "right values" , right.values)

		self.keys = [right.keys[0]]
		self.values = [left , right]
		self.leaf = False

	def leafSplit(self):
		right = Node(self.numKeys)
		left = Node(self.numKeys)
		middle = 0
		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2

			left.keys = self.keys[:middle]
			left.values = self.values[:middle]

			right.keys = self.keys[middle:]
			right.values = self.values[middle:]
		else:
			middle = (len(self.keys) - 1) // 2

			left.keys = self.keys[:middle]
			left.values = self.values[:middle]

			right.keys = self.keys[middle:]
			right.values = self.values[middle:]


		return (right.keys[0], left, right)

	def internalSplit(self):
		right = Node(self.numKeys)
		left = Node(self.numKeys)
		middle = 0

		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2

			left.keys = self.keys[:middle]
			left.values = self.values[:middle+1]

			right.keys = self.keys[middle+1:]
			right.values = self.values[middle+1:]
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


	def insert(self, key, value):
		if self.root.leaf:
			if self.root.isFull():
				self.root.addValue(key, value)
				self.root.rootSplit()
				return None
		return self.insertHelper(self.root, key, value)

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
			#print(child.printMethod)

			newEntry = self.insertHelper(child, key, value)

			if newEntry == None:
				return None

			elif not node.isFull():
				node.addValue(newEntry[0], newEntry[1])
				return None

			else:
				# print(newEntry, newEntry[1].printMethod(), newEntry[1])
				node.addValue(newEntry[0], newEntry[1])
				k, left, right = node.internalSplit()
				# print('impt', k, left.values[2].printMethod(), right.values[1].printMethod())
				node.keys = left.keys
				node.values = left.values
				newEntry = (k , right)
				right.leaf = False
				right.internal = True
				if node.isRoot:
					# print('hi:', k, right.keys, right.values[0].values[1])
					newRoot = Node(self.numKeys)
					left.leaf = False
					left.internal = True
					node.keys = [newEntry[0]]
					node.values = [left, right]
					# newRoot.isRoot = True
					# newRoot.leaf = False
					# newRoot.addValue(k, [node, right])
					return None
				return newEntry


	def findHelper(self, node, key):
		for i, item in enumerate(node.keys):
			if key < item:
				return node.values[i]
		return node.values[i + 1]



	def getValue(self, key):
		node = self.root
		while not node.leaf:
			node = self.findHelper(node, key)
		for i, item in enumerate(node.keys):
			if key == item:
				return node.values[i]
		return 'None'

	def printTree(self):
		d = defaultdict(list)
		objects = self.root.printMethod(d)
		for i in range(len(d)):
			print("Level: " , i , " " , d[i])		
		# print(objects)
