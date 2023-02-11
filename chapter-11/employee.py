class Employee:
    def __init__(self, first, last, salary=0):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self):
        self.salary += 5000


# emp = Employee("Alzy", "Welzy")
# print(emp.salary)
