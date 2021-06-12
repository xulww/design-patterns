from payment_strategy import PaymentStrategy


class PaypalPayment(PaymentStrategy):

    _email = None
    _password = None

    def __init__(self, email, password):
        self._email = email
        self._password = password

    def pay(self, amount):
        print("Paypal payment " + str(amount))
