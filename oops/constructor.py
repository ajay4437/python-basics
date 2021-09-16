class Employee:
    company='Google'
    
    def getsalary(self,signature):
        print(f"salary for this employee working in {self.company} is  {self.salary}\n{signature}")

    def __init__(self, name, salary, unit):
        self.name=name
        self.salary=salary
        self.unit=unit
        print('Employee is created')

    def getDetails(self):
        print(f"name of the Employee is {self.name}")
        print(f"salary of the Employee is {self.salary}")
        print(f"unit of the Employee is {self.unit}")


    @staticmethod # this method doesnot requried any  or parameter , such as 'self' in the above 
    def greet():
        print('good morning, sir!')

    @staticmethod
    def time():
        print(f"Time is {8}:{40}")

ajay=Employee('ajay','100k', 'computers')
#ajay=Employee()   #This throws an error and the error is (missing 3 required positional arguments: 'name', 'salary', and 'unit')
ajay.getDetails()
