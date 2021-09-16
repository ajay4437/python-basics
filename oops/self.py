class Employee:
    company='Google'
    def getsalary(ajay):
        print(f"salary is {100000}")
ajay=Employee()
Employee.getsalary(ajay)
#or if self is not given as parameter in getsalary
class Employee:
    company='Google'
    def getsalary(self):
        print(f"salary is {100000}")
ajay=Employee()
ajay.getsalary()

# using self:
class Employee:
    company='Google'
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is  {self.salary}")
ajay=Employee()
ajay.salary=100000
ajay.getsalary()
