class Employee:
    def __init__(self, first, last, salary=0):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_salary=5000):
        self.salary += raise_salary


emp = Employee("Alzy", "Welzy")
print(emp.salary)
