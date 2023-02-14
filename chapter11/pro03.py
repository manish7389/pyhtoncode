class Employee:
    company = "googal"
    salary = 5500
    bonus = 500
    # totalsalary = 6000

    @property
    def salaryincriment(self):
        return self.salary + self.bonus

    @salaryincriment.setter
    def salaryincriment(self , val):
        self.salaryincriment = val + self.salary 

e = Employee()
Employee.bonus = 200
print(e.salaryincriment)