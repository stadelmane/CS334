import bptree
# b = bptree.Node(4)  # Each node contains 4 keys, which means 5 pointers

# b.addValue(12,"hello")
# b.addValue(24,"bye")
# b.addValue(14,"bye")
# b.addValue(11,"bye")
# #b.addValue(7, "cat")
# b.split()
# b.printMethod()


b = bptree.Bptree(3)  # Each node contains 4 keys, which means 5 pointers
b.insert(1,"hello")
b.insert(2,"bye")
b.insert(3,"hello")
b.insert(4,"kate")
b.insert(5,"nate")
# b.insert(6,"fate")
# b.insert(7,"bate")
# b.insert(8,"late")
# b.insert(9,"ho")
# b.insert(10,"hell")
# b.insert(11, "date")
# b.insert(13, "date")

# print("Value for 12 = " + b.getValue(12))
# print("Value for 24 = " + b.getValue(24))
#print("\n")
b.printTree()
