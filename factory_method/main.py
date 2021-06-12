from cheese_factory import CheeseFactory
from milk_factory import MilkFactory


def main():
    cheese_factory = CheeseFactory()
    cow_cheese = cheese_factory.produce_product("COW_CHEESE")

    milk_factory = MilkFactory()
    goat_milk = milk_factory.produce_product("GOAT_MILK")


if __name__ == "__main__":
    main()
