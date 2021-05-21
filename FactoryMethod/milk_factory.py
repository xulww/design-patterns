from farm_factory import FarmFactory
from cow_milk import CowMilk
from goat_milk import GoatMilk


class MilkFactory(FarmFactory):

    def create_product(self, product_name):
        product = None
        if product_name == "COW_MILK":
            product = CowMilk()
            product.set_price(2.10)
        if product_name == "GOAT_MILK":
            product = GoatMilk()
            product.set_price(2.50)

        return product
