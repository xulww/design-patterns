from square import Square
from rectangle import Rectangle
from circle import Circle
from abstract_factory import AbstractFactory


class ShapeFactory(AbstractFactory):

    def get_color(self, color_name):
        # shape factory cannot return color instance
        return None

    def get_shape(self, shape_name):
        if shape_name == "square":
            return Square()
        if shape_name == "rectangle":
            return Rectangle()
        if shape_name == "circle":
            return Circle()

        print("Unknown shape")

        return None
