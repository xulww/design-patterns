from product import Product


class Book(Product):

    _price = None
    _title = None
    _isbn_number = None

    def __init__(self, price, title, isbn_number):
        self._price = price
        self._title = title
        self._isbn_number = isbn_number

    def get_price(self):
        return self._price

    def get_title(self):
        return self._title

    def get_isbn_number(self):
        return self._isbn_number

    def accept(self, visitor):
        return visitor.visit(self)
