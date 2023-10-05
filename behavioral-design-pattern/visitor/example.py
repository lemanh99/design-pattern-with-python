from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def draw(self):
        print(f"Draw circle at ({self._x}, {self._y}) with radius {self._radius}")

    def move(self, x, y):
        self._x = x
        self._y = y

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def draw(self):
        print(f"Draw rectangle at ({self._x}, {self._y}) with width {self._width} and height {self._height}")

    def move(self, x, y):
        self._x = x
        self._y = y

    def accept(self, visitor):
        visitor.visit_rectangle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


class XMLExportVisitor(Visitor):
    def visit_circle(self, circle):
        print(f"Export circle to XML at ({circle._x}, {circle._y}) with radius {circle._radius}")

    def visit_rectangle(self, rectangle):
        print(
            f"Export rectangle to XML at ({rectangle._x}, {rectangle._y}) with width {rectangle._width} and height {rectangle._height}")


class JSONExportVisitor(Visitor):
    def visit_circle(self, circle):
        print(f"Export circle to JSON at ({circle._x}, {circle._y}) with radius {circle._radius}")

    def visit_rectangle(self, rectangle):
        print(
            f"Export rectangle to JSON at ({rectangle._x}, {rectangle._y}) with width {rectangle._width} and height {rectangle._height}")


class ClientCode:
    def __init__(self, shapes: list, visitor: Visitor):
        self._shapes = shapes
        self._visitor = visitor

    def execute(self):
        for shape in self._shapes:
            shape.accept(self._visitor)


if __name__ == "__main__":
    shapes = [Circle(1, 2, 3), Rectangle(4, 5, 6, 7)]
    xml_export_visitor = XMLExportVisitor()
    json_export_visitor = JSONExportVisitor()

    client = ClientCode(shapes, xml_export_visitor)
    client.execute()

    client = ClientCode(shapes, json_export_visitor)
    client.execute()
