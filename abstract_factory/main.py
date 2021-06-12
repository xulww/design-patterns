from factory_producer import FactoryProducer


def main():
    shape_factory = FactoryProducer.get_factory("shape")
    color_factory = FactoryProducer.get_factory("color")

    circle = shape_factory.get_shape("circle")
    circle.draw()

    blue_color = color_factory.get_color("blue")
    blue_color.fill()


if __name__ == "__main__":
    main()
