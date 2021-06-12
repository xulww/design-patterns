from fruit import Fruit
from book import Book
from price_calculator import PriceCalculator


def main():
    apple = Fruit("Apple", 1.50, 3)
    banana = Fruit("Banana", 2.50, 1)
    book = Book(70, "The Witcher", "SNNF343249A")
    price_calculator = PriceCalculator()

    price_for_apples = apple.accept(price_calculator)
    price_for_bananas = banana.accept(price_calculator)
    price_for_books = book.accept(price_calculator)


if __name__ == "__main__":
    main()
