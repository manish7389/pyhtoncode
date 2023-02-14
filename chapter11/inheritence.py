class Person:
    contary = "india"

    def takebreth(self):
        print("i am a person so i am brething")


class Employee(Person):
    company = "googal"

    def getsalary(self):
        print(f"the emloyee salary is {self.salary}")


p = Person()
p.takebreth()

e = Employee()
e.takebreth()