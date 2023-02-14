class Employee:
    company = "googal"
    salary = "400"
    def getsalary(self):
        print(f"the employee salary is {self.salary}")

    # def changesalary(self , sal):
        # self.salary = sal
        # print(f"the change salary is {sal}")

    # def changesalary(self , sal): # this is the first way to chnage the class atribute value
        # self.__class__.salary = sal
        # print(f"the change salary is {sal}")
    @classmethod
    def changesalary(cls , sal): # this is the second way to chnage the class atribute value
        cls.salary = sal
        print(f"the change salary is {sal}")

e = Employee()
print(e.salary)
e.changesalary(500)
print(Employee.salary)