
class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('salary must be more than 1000')
        self.salary = salary

    def get_salary(self):
        return self.salary
