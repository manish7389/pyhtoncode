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
            print("i am a programmer so i am brething++")

print("*************person class***************")
p = Person()
print(p.contary)
p.takebreth()

print("*************employee class***************")
e = Employee()
print(e.company)
print(e.contary)
e.takebreth()
e.getsalary()

print("*************programmer class***************")
pr = Programmer()
print(pr.company)
print(pr.salary)
print(pr.contary)
pr.takebreth()
pr.getsalary()