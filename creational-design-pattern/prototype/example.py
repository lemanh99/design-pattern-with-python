import copy


class Shape:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.color = ""

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def clone(self):
        return copy.deepcopy(self)


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def clone(self):
        return copy.deepcopy(self)


class Application:
    def __init__(self):
        self.shapes = []

        circle = Circle()
        circle.X = 10
        circle.Y = 10
        circle.radius = 20
        self.shapes.append(circle)

        another_circle = circle.clone()
        self.shapes.append(another_circle)

        rectangle = Rectangle()
        rectangle.width = 10
        rectangle.height = 20
        self.shapes.append(rectangle)

    def business_logic(self):
        shapes_copy = []

        for shape in self.shapes:
            shapes_copy.append(shape.clone())

        for shape_copy in shapes_copy:
            print(f"Type: {type(shape_copy).__name__}, X: {shape_copy.X}, Y: {shape_copy.Y}, Color: {shape_copy.color}")


if __name__ == "__main__":
    app = Application()
    app.business_logic()
