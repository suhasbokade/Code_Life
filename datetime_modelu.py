import datetime

class Employee:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def age(self):
        current_year = datetime.datetime.now().year
        current_age = current_year - self.birthyear
        print(f"Employee {self.name} current age is {current_age}")

emp1 = Employee("Suhas", 1991)
emp1.age()
emp2 = Employee("Ashwini", 1995)
emp2.age()