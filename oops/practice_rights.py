class Employee:
    company="Microsoft"

    def __init__(self,name,salary,product):
        self.name=name
        self.salary=salary
        self.product=product
    
    def getinfo(self):
        print(f"the employee name is {self.name} and his salary is {self.salary} He works with the product{self.product}")

ajay=Employee('ajay',100000, 'gethub')
manoj=Employee('manoj',1000,'skype')
ajay.getinfo()
manoj.getinfo()