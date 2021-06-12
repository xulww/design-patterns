from car import Car


class CarDecorator(Car):

    _decorated_car = None

    def __init__(self, decorated_car):
        self._decorated_car = decorated_car

    def create(self):
        # here we can add functionality for the decorated car
        self._decorated_car.create()
