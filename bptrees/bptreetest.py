import bptree
b = bptree.Bptree(4)  # Each node contains 4 keys, which means 5 pointers
b.insert(12,"hello")
b.insert(24,"bye")
print("Value for 12 = " + b.getValue(12))
print("Value for 24 = " + b.getValue(24))
b.printTree()
