from toyota import Toyota
from blue_car_decorator import BlueCarDecorator


def main():
    toyota = Toyota()
    toyota.create()

    another_toyota = Toyota()
    blue_toyota = BlueCarDecorator(another_toyota)
    blue_toyota.create()


if __name__ == "__main__":
    main()
