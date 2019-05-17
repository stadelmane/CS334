import bptree

b = bptree.Bptree(50)  # Each node contains 4 keys, which means 5 pointers
b.insert(1,"hello")
b.insert(2,"bye")
b.insert(3,"hello")
b.insert(4,"bye")
b.insert(5,"hello")
b.insert(6,"bye")
b.insert(7,"hello")
b.insert(8,"bye")
b.insert(9,"hello")
b.insert(10,"bye")
b.insert(11,"hello")
b.insert(12,"bye")
b.insert(13,"hello")
b.insert(14,"bye")
b.insert(15,"hello")
b.insert(16,"bye")
b.insert(17,"hello")
b.insert(18,"bye")
b.insert(19,"hello")
# b.insert(16,"bye")


# print("Value for 12 = " + b.getValue(12))
# print("Value for 24 = " + b.getValue(24))
b.printTree()
