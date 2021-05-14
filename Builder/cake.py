class Cake:

    _SUGAR = None
    _EGGS = None
    _COCOA = None
    _VANILLA = None
    _MILK = None

    class Builder:

        _sugar = None
        _eggs = None
        _cocoa = None
        _vanilla = None
        _milk = None

        def sugar(self, cups):
            self._sugar = cups
            return self

        def eggs(self, count):
            self._eggs = count
            return self

        def cocoa(self, spoons):
            self._cocoa = spoons
            return self

        def vanilla(self, packets):
            self._vanilla = packets
            return self

        def milk(self, cups):
            self._milk = cups
            return self

        def build(self):
            return Cake(self)

    def __init__(self, builder):
        self._SUGAR = builder.sugar
        self._EGGS = builder.eggs
        self._COCOA = builder.cocoa
        self._VANILLA = builder.vanilla
        self._MILK = builder.milk
