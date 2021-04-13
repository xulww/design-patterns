from Singleton import Singleton


def main():
    connection_one = Singleton()
    connection_two = Singleton()

    print(connection_one is connection_two)  # true


if __name__ == "__main__":
    main()
