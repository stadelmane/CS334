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
				#print(item.values)
				item.printMethod(level+1)


	def isFull(self):
		return (len(self.keys) == self.numKeys - 1)

	def split(self):
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
			middle = (len(self.keys) + 1) // 2
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



class Bptree(object):
	def __init__(self, numKeys):
		self.numKeys = numKeys
		self.root = Node(self.numKeys)
		self.isRoot = True


	def insert(self, key, value):
		return self.insertHelper(self.root, key, value)

	def insertHelper(self, root, key, value):
		
		if self.root.leaf:
			if not self.root.isFull():
				print('hh1')
				self.root.addValue(key, value)
				return None

			else:
				print('hh2')
				self.root.addValue(key, value) #do we add value here?
				self.root.split()
				newEntry = (self.root.keys , self.root.values[1])
				return newEntry

		else:
			print('hh3')
			parent = None
			child = self.root

			
			child = self.findHelper(self.root, key)

			newEntry = self.insertHelper(child, key, value)

			if newEntry == None:
				return None

			elif not self.root.isFull():
				self.root.addValue(newEntry[0], newEntry[1])
				return None
			else:
				return None

	def findHelper(self, root, key):

		maximum = 0
		for i, item in enumerate(root.keys):
			maximum = i
			if key < item:
				print("here" , i)
				break
				return root.values[i]
		print("here")
		return root.values[maximum + 1]




	def getValue(self,key):
		pass

	def printTree(self):
		self.root.printMethod()