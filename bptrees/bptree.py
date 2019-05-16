import math

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

	def printMethod(self, level = 0):

		print(level, str(self.keys))

		if not self.leaf:
			for item in self.values:
				#print(item.values)
				item.printMethod(level+1)


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
		# print(self.keys)
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
		print("keys" , right.keys , left.keys)
		print("lengths" , right.printMethod(), left.printMethod())
		if len(self.keys) % 2 == 0:
			middle = len(self.keys) // 2
		else:
			middle = math.ceil(len(self.keys) / 2) - 1
		# print("yeet" , middle , self.keys)
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
				return self.root.rootSplit()
		return self.insertHelper(self.root, key, value)

	def insertHelper(self, node, key, value):
		# print(node.printMethod())
		# print(node.leaf)
		# x = input("enter here")
		if node.leaf:
			if not node.isFull():
				#print('hh1')
				node.addValue(key, value)
				return None

			else:
				#print('hh2')
				node.addValue(key, value)
				newKey, left, right =  node.leafSplit()
				#print(newKey, left.printMethod(), right.printMethod())
				#print('1', node.printMethod())
				node.keys = left.keys
				node.values = left.values 
				#print('2', node.printMethod())
				newEntry = (newKey , right)		
				#print("keys" , len(right.keys) , len(left.keys))
				#print("lengths" , len(right.values) , len(left.values))
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
				k, left, right = node.internalSplit()
				node.keys = left.keys
				node.values = left.values
				newEntry = (k , right)
				if node.isRoot:
					node.isRoot = False 
					newRoot = Node(self.numKeys)
					newRoot.isRoot = True
					newRoot.leaf = False
					newRoot.keys.append(k)
					newRoot.values.append(left)
					newRoot.values.append(right)
					newRoot.keys
					newRoot.values



				return newEntry


	def findHelper(self, node, key):

		maximum = 0
		for i, item in enumerate(node.keys):
			maximum = i
			if key < item:
				# print("here" , i)
				return node.values[i]
		# print("here" , i)
		return node.values[i + 1]




	def getValue(self,key):
		pass

	def printTree(self):
		self.root.printMethod()