import bptree
# b = bptree.Node(4)  # Each node contains 4 keys, which means 5 pointers

# b.addValue(12,"hello")
# b.addValue(24,"bye")
# b.addValue(14,"bye")
# b.addValue(11,"bye")
# #b.addValue(7, "cat")
# b.split()
# b.printMethod()


b = bptree.Bptree(4)  # Each node contains 4 keys, which means 5 pointers
b.insert(1,"hello")
b.insert(2,"bye")
b.insert(3,"hello")
b.insert(4,"bye")
b.insert(5,"hello")
b.insert(6,"hello")
b.insert(7,"hello")
b.insert(8,"hello")
b.insert(9,"hello")
b.insert(10,"hello")

# print("Value for 12 = " + b.getValue(12))
# print("Value for 24 = " + b.getValue(24))
#print("\n")
b.printTree()
