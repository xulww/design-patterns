from employee import Employee


class Manager(Employee):
    _name = None
    _salary = None
    _employees = None

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self._employees = []

    def add(self, employee):
        self._employees.append(employee)

    def remove(self, employee):
        self._employees.remove(employee)

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def print_data(self):
        print("Manager name: " + self.get_name() +
              " with salary: " + str(self.get_salary()))

        for employee in self._employees:
            employee.print_data()
