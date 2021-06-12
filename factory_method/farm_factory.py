class FarmFactory:

    def create_product(self, product_name):
        pass

    def produce_product(self, product_name):
        product = self.create_product(product_name)
        product.prepare()
        return product
