class Tree:

    def __init__(self, data):
        self.data = data
        self.Tree_list = []

    def add_child(self, child):
        self.Tree_list.append(child)

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"

        for child in self.Tree_list:
            ret += child.__str__(level + 1)

        return ret


# Create nodes
n1 = Tree("n1")
n2 = Tree("n2")
n3 = Tree("n3")
n4 = Tree("n4")
n5 = Tree("n5")
n6 = Tree("n6")
n7 = Tree("n7")
n9 = Tree("n9")
n10 = Tree("n10")


# Connect nodes
n1.add_child(n2)
n1.add_child(n3)

n2.add_child(n4)
n2.add_child(n5)

n3.add_child(n6)
n3.add_child(n7)

n4.add_child(n9)
n4.add_child(n10)


print(n1)