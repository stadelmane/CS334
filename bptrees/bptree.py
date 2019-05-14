class Node(object):
	def __init__(self, numKeys):
		self.numKeys = numKeys
		self.keys = []
		self.values = []
		self.leaf = True


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
				print(item.values)
				item.printMethod(level+1)


	def isFull(self):
		return (len(self.keys) == self.numKeys)

	def split(self):
		left = Node(self.numKeys)
		right = Node(self.numKeys)
		middle = 0
		if self.numKeys % 2 == 0:
			middle = (self.numKeys) // 2
		else:
			middle = (self.numKeys + 1) // 2

		left.keys = self.keys[:middle]
		left.values = self.values[:middle]
		print("left keys" , left.keys , "left values" , left.values)

		right.keys = self.keys[middle:]
		right.values = self.values[middle:]

		print("right keys" , right.keys , "right values" , right.values)

		self.keys = [right.keys[0]]
		self.values = [left , right]
		self.leaf = False












class Bptree(object):
	def __init__(self, numKeys):
		self.numKeys = numKeys


	def insert(self, key, value):
		pass

	def getValue(self,key):
		pass

	def printTree(self):
		pass