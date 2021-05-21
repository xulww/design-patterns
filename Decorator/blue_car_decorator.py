from car_decorator import CarDecorator


class BlueCarDecorator(CarDecorator):

    def __init__(self, decorated_car):
        super().__init__(decorated_car)

    def create(self):
        self._decorated_car.create()
        self.set_blue_color()

    def set_blue_color(self):
        print("Setting blue car color")
