class Employee:
    company = "googal"
    salary = 5500
    bonus = 500
    # totalsalary = 6000

    @property
    def totalsalary(self):
        return self.salary + self.bonus

    @totalsalary.setter
    def totalsalary(self , val):
        self.bonus = val - self.salary 

e = Employee()
print(e.totalsalary)
e.totalsalary = 6100
print(e.bonus)