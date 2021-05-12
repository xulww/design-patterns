from manager import Manager
from developer import Developer


def main():
    manager_one = Manager("Georgi", 4000)
    manager_two = Manager("Tsvetomir", 5000)
    manager_three = Manager("Spasimir The Boss", 7000)
    developer_one = Developer("Atanas", 2500)
    developer_two = Developer("Ivan", 3000)
    developer_three = Developer("Petar", 3500)
    developer_four = Developer("Anastas", 4000)
    developer_five = Developer("Evgeni", 4000)

    manager_one.add(developer_one)
    manager_one.add(developer_two)
    manager_two.add(developer_three)
    manager_two.add(developer_four)
    manager_three.add(developer_five)
    manager_three.add(manager_one)
    manager_three.add(manager_two)

    manager_three.print_data()


if __name__ == "__main__":
    main()
