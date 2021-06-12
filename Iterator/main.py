from name_repository import NameRepository


def main():
    name_repository = NameRepository()
    iterator = name_repository.get_iterator()

    for _ in iterator.has_next():
        current_name = iterator.next()
        print("Name: " + current_name)


if __name__ == "__main__":
    main()
