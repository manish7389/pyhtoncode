class Person:
    contary = "india"

    def takebreth(self):
        print("i am a person so i am brething")


class Employee(Person):
    company = "googal"
    salary = 500

    def getsalary(self):
        print(f"the emloyee salary is {self.salary}")

    def takebreth(self):
        print("i am a employee so i am  luckyly brething")


class Programmer(Employee):
        company = "youtube"
        def takebreth(self):
            super().takebreth()
            print("i am a programmer so i am brething++")

print("*************person class***************")
p = Person()
p.takebreth()

print("*************employee class***************")
e = Employee()
e.takebreth()


print("*************programmer class***************")
pr = Programmer()
pr.takebreth()
