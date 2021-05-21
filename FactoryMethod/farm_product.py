class FarmProduct:

    _price = None

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def prepare(self):
        pass
