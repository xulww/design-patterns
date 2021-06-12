from cake import Cake


def main():
    cocoa_cake = Cake.Builder().cocoa(15).eggs(3).milk(1).build()
    vanilla_cake = Cake.Builder().vanilla(3).sugar(2).eggs(3).milk(2).build()


if __name__ == "__main__":
    main()
