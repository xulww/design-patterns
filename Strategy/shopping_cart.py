class ShoppingCart:

    _items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def get_items_price(self):
        item_price = 0

        for item in self._items:
            item_price = item_price + item.get_price()

        return item_price

    def pay(self, payment_strategy):
        amount = self.get_items_price()
        payment_strategy.pay(amount)
