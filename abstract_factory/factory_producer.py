from color_factory import ColorFactory
from shape_factory import ShapeFactory


class FactoryProducer:

    @staticmethod
    def get_factory(factory_name):
        if factory_name == "shape":
            return ShapeFactory()
        if factory_name == "color":
            return ColorFactory()

        print("Unknown factory")

        return None
