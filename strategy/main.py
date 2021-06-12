from shopping_cart import ShoppingCart
from item import Item
from paypal_payment import PaypalPayment
from credit_card_payment import CreditCardPayment


def main():
    shopping_cart = ShoppingCart()
    item_1 = Item("Banana", 2.5)
    item_2 = Item("Juice", 1.7)

    shopping_cart.add_item(item_1)
    shopping_cart.add_item(item_2)

    # shopping_cart.pay(PaypalPayment("test@gmail.com", "123456"))
    shopping_cart.pay(CreditCardPayment(
        "Ivan Ivanov", "1234 1234 1234 1234", "10/21", "123"))


if __name__ == "__main__":
    main()
