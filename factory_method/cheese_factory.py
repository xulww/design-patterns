from farm_factory import FarmFactory
from cow_cheese import CowCheese
from goat_cheese import GoatCheese


class CheeseFactory(FarmFactory):

    def create_product(self, product_name):
        product = None
        if product_name == "COW_CHEESE":
            product = CowCheese()
            product.set_price(3.50)
        if product_name == "GOAT_CHEESE":
            product = GoatCheese()
            product.set_price(4.50)

        return product
