from employee import Employee


class Developer(Employee):
    _name = None
    _salary = None

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def add(self, employee):
        # leaf node cannot add employees
        pass

    def remove(self, employee):
        # leaf node cannot remove employees
        pass

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def print_data(self):
        print("Developer name: " + self.get_name() +
              " with salary: " + str(self.get_salary()))
