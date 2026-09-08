class Tree:
    def __init__(self, data):
        self.data = data
        self.Tree_list = []

    def add_child(self, child):
        self.Tree_list.append(child)

    def print_tree(self, level=0):
        print("  " * level + self.data)

        for child in self.Tree_list:
            child.print_tree(level + 1)


rootObj = Tree("Drink")

hot = Tree("hot")
cold = Tree("cold")

rootObj.add_child(hot)
rootObj.add_child(cold)

tea = Tree("tea")
coffee = Tree("coffee")

hot.add_child(tea)
hot.add_child(coffee)

nonAlchohalic = Tree("non Alchohalic")
alchohalic = Tree("alchohalic")

cold.add_child(nonAlchohalic)
cold.add_child(alchohalic)

# Print tree
rootObj.print_tree()