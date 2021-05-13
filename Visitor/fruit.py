from product import Product


class Fruit(Product):

    _name = None
    _price_per_kilo = None
    _weight = None

    def __init__(self, name, price_per_kilo, weight):
        self._name = name
        self._price_per_kilo = price_per_kilo
        self._weight = weight

    def get_name(self):
        return self._name

    def get_price_per_kilo(self):
        return self._price_per_kilo

    def get_weight(self):
        return self._weight

    def accept(self, visitor):
        return visitor.visit(self)
