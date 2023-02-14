class Employee:
    company = "googal"
    salary = 500

    def getsalary(self):
        print(f"the employee salary is {self.salary}")

class Freelancer:
    company = "youtube"
    level = 0

    def upgratelevel(self):
        self.level = self.level + 1
        print(f"the level is upgrated")

class Progarammer(Employee,Freelancer):
    name = "manish"

p = Progarammer()
p.upgratelevel()
print(p.level)
print(p.company)
print(p.name)
p.getsalary()

e = Employee()
e.getsalary()