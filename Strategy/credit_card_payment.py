from payment_strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):

    _name = None
    _card_number = None
    _expiration_date = None
    _ccv = None

    def __init__(self, name, card_number, expiration_date, ccv):
        self._name = name
        self._card_number = card_number
        self._expiration_date = expiration_date
        self._ccv = ccv

    def pay(self, amount):
        print("Credit card payment " + str(amount))
