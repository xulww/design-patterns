from blue import Blue
from red import Red
from green import Green
from abstract_factory import AbstractFactory


class ColorFactory(AbstractFactory):

    def get_color(self, color_name):
        if color_name == "blue":
            return Blue()
        if color_name == "red":
            return Red()
        if color_name == "green":
            return Green()

        print("Unknown color")

        return None

    def get_shape(self, shape_name):
        # color factory cannot return shape instance
        return None
