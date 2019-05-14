import bptree
b = bptree.Node(4)  # Each node contains 4 keys, which means 5 pointers

b.addValue(12,"hello")
b.addValue(24,"bye")
b.addValue(14,"bye")
# b.addValue(11,"bye")
b.split()
b.printMethod()
# print("Value for 12 = " + b.getValue(12))
# print("Value for 24 = " + b.getValue(24))
# b.printTree()
