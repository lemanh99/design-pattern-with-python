class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f"TreeType.draw: {self.name} {self.color} {self.texture} {x} {y}")


class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        if not TreeFactory.tree_types.get(name):
            TreeFactory.tree_types[name] = TreeType(name, color, texture)

        return TreeFactory.tree_types[name]


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(1, 2, "name", "color", "texture")
    forest.draw("canvas")