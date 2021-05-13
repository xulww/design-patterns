from shopping_cart_visitor import ShoppingCartVisitor
from fruit import Fruit
from book import Book


class PriceCalculator(ShoppingCartVisitor):
    def visit(self, obj):
        price = None

        if type(obj) == Book:
            price = obj.get_price()

            if (price > 50):
                price = price - 5

            print("Book: " + obj.get_title() + " costs: " + str(price))
        elif type(obj) == Fruit:
            price = obj.get_price_per_kilo() * obj.get_weight()

            print("Fruit: " + obj.get_name() + " costs: " + str(price))

        return price
